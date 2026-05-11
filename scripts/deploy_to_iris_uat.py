"""Deploy the DoView Book corpus to an Iris instance (ADR-013).

Default target: https://iris-uat.chrisbarlow.nz (set via IRIS_UAT_URL env).

Two-pass strategy:

1. Walk docs/md/, build a manifest, POST every Text diagram with
   frontmatter-stripped content, capture relative_path → diagram_id.
2. For each diagram, rewrite markdown links to iris://diagram/<uuid>
   using the mapping, then PUT to update.

CLI:
    python deploy_to_iris_uat.py [--dry-run]
    python deploy_to_iris_uat.py --collection 'DoView Strategy Models' \\
                                  --set 'DoView Book'
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath
from typing import Any

import requests

from link_rewriter import rewrite_links, strip_frontmatter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("deploy")

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_ROOT = REPO_ROOT / "docs" / "md"

DEFAULT_API_URL = "https://iris-api-gtb3.onrender.com"
DEFAULT_WEB_URL = "https://iris-uat.chrisbarlow.nz"
DEFAULT_COLLECTION = "DoView Strategy Models"
DEFAULT_SET = "DoView Book"

# Iris UAT runs in Supabase deployment mode; /api/auth/login is disabled
# there ("Use Supabase Auth for authentication"). Rather than re-implement
# the Supabase password grant here, reuse the JWT that the Iris repo's
# Playwright `uat-setup` project persists to disk. Refresh it via:
#   cd ../../iris/frontend && npx playwright test --project=uat-setup
TESTER_JSON_PATH = Path(
    "/workspaces/workspace-basic/iris/frontend/tests/e2e/uat/.auth/tester.json"
)

H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


# ---------------------------------------------------------------------------
# Manifest + helpers
# ---------------------------------------------------------------------------

@dataclass
class FileEntry:
    rel_path: PurePosixPath          # corpus-relative posix path
    title: str                       # H1 or filename fallback
    description: str                 # joined frontmatter snippet
    body: str                        # markdown source (frontmatter stripped)
    package_chain: list[str]         # ['Part A - Foo', 'A01 - The Steps'] etc.
    diagram_id: str | None = None    # filled after pass 1


@dataclass
class Manifest:
    files: list[FileEntry] = field(default_factory=list)
    # rel_path → diagram_id, populated as pass 1 progresses
    id_by_path: dict[PurePosixPath, str] = field(default_factory=dict)
    introduction_id: str = ""


def filename_to_title_fallback(rel: PurePosixPath) -> str:
    return rel.stem.replace("-", " ").strip().title() or rel.name


def collect_files() -> Manifest:
    """Walk CORPUS_ROOT, build a FileEntry per .md file."""
    manifest = Manifest()
    for md_path in sorted(CORPUS_ROOT.rglob("*.md")):
        rel = PurePosixPath(md_path.relative_to(CORPUS_ROOT).as_posix())
        raw = md_path.read_text(encoding="utf-8")
        body, fm = strip_frontmatter(raw)
        h1 = H1_RE.search(body)
        title = h1.group(1).strip() if h1 else filename_to_title_fallback(rel)

        desc_parts: list[str] = []
        for key in ("kind", "pair", "part", "title", "source", "source_pdf"):
            if key in fm and fm[key] is not None:
                desc_parts.append(f"{key}: {fm[key]}")
        description = " · ".join(desc_parts)

        package_chain = list(rel.parts[:-1])

        manifest.files.append(
            FileEntry(
                rel_path=rel,
                title=title,
                description=description,
                body=body,
                package_chain=package_chain,
            )
        )
    return manifest


# ---------------------------------------------------------------------------
# Iris API client
# ---------------------------------------------------------------------------

def load_token_from_tester_storage(path: Path = TESTER_JSON_PATH) -> str:
    """Read the Supabase JWT from the Iris repo's playwright storage state.

    The token has a 1-hour lifetime. Refresh it before running this script
    by executing the uat-setup project in the iris frontend.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Run `cd /workspaces/workspace-basic/iris/frontend && "
            "npx playwright test --project=uat-setup` to sign in and persist the JWT."
        )
    data = json.loads(path.read_text())
    for origin in data.get("origins", []):
        for item in origin.get("localStorage", []):
            if item["name"].startswith("sb-") and item["name"].endswith("-auth-token"):
                parsed = json.loads(item["value"])
                exp = parsed.get("expires_at", 0)
                now = int(time.time())
                if exp and exp <= now + 60:
                    raise RuntimeError(
                        f"Stored JWT in {path} expires in {exp - now}s. Refresh by running "
                        "`npx playwright test --project=uat-setup` in iris/frontend."
                    )
                return parsed["access_token"]
    raise RuntimeError(f"No Supabase auth token found in {path}")


class IrisClient:
    def __init__(self, api_url: str, web_url: str, token: str) -> None:
        self.api_url = api_url.rstrip("/")
        self.web_url = web_url.rstrip("/")
        self.token = token
        self.session = requests.Session()

    def _headers(self, extra: dict[str, str] | None = None) -> dict[str, str]:
        h = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
        if extra:
            h.update(extra)
        return h

    def _request(
        self,
        method: str,
        path: str,
        *,
        json_body: Any = None,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        retry_on_429: bool = True,
    ) -> requests.Response:
        url = f"{self.api_url}{path}"
        for attempt in range(6):
            r = self.session.request(
                method,
                url,
                json=json_body,
                headers=self._headers(headers),
                params=params,
                timeout=30,
            )
            if r.status_code == 401:
                raise RuntimeError(
                    "Supabase JWT rejected (401). Refresh it by running "
                    "`npx playwright test --project=uat-setup` in iris/frontend, "
                    "then retry."
                )
            if r.status_code == 429 and retry_on_429:
                wait = min(2 ** attempt, 15)
                log.warning("Rate limited; sleeping %ds (attempt %d)", wait, attempt + 1)
                time.sleep(wait)
                continue
            return r
        return r

    def list_collections(self) -> list[dict[str, Any]]:
        r = self._request("GET", "/api/collections")
        r.raise_for_status()
        return r.json().get("items", [])

    def create_collection(self, name: str, description: str = "") -> dict[str, Any]:
        r = self._request(
            "POST",
            "/api/collections",
            json_body={"name": name, "description": description},
        )
        r.raise_for_status()
        return r.json()

    def find_or_create_collection(self, name: str) -> dict[str, Any]:
        for c in self.list_collections():
            if c["name"] == name:
                return c
        log.info("Collection %r not found; creating", name)
        return self.create_collection(name)

    def find_set_by_name_in_collection(
        self, collection_id: str, set_name: str
    ) -> dict[str, Any] | None:
        r = self._request("GET", "/api/sets", params={"collection_id": collection_id})
        r.raise_for_status()
        for s in r.json().get("items", []):
            if s["name"] == set_name:
                return s
        return None

    def create_set(self, name: str, collection_id: str, description: str = "") -> dict[str, Any]:
        r = self._request(
            "POST",
            "/api/sets",
            json_body={
                "name": name,
                "description": description,
                "collection_id": collection_id,
            },
        )
        if r.status_code == 409:
            r.raise_for_status()
        r.raise_for_status()
        return r.json()

    def create_package(
        self,
        name: str,
        set_id: str,
        parent_package_id: str | None,
    ) -> dict[str, Any]:
        r = self._request(
            "POST",
            "/api/packages",
            json_body={
                "name": name,
                "set_id": set_id,
                "parent_package_id": parent_package_id,
            },
        )
        r.raise_for_status()
        return r.json()

    def create_diagram(
        self,
        name: str,
        description: str,
        content: str,
        set_id: str,
        parent_package_id: str | None,
    ) -> dict[str, Any]:
        r = self._request(
            "POST",
            "/api/diagrams",
            json_body={
                "diagram_type": "text",
                "name": name[:255],
                "notation": "markdown",
                "description": description[:1000] if description else "",
                "data": {"content": content},
                "set_id": set_id,
                "parent_package_id": parent_package_id,
            },
        )
        r.raise_for_status()
        return r.json()

    def update_diagram_content(
        self,
        diagram_id: str,
        name: str,
        description: str,
        content: str,
        version: int = 1,
    ) -> dict[str, Any]:
        r = self._request(
            "PUT",
            f"/api/diagrams/{diagram_id}",
            json_body={
                "name": name[:255],
                "description": (description or "")[:1000],
                "data": {"content": content},
                "change_summary": "iris-deploy: rewrite intra-corpus links to iris://diagram/<id>",
            },
            headers={"If-Match": str(version)},
        )
        if r.status_code == 409:
            # Optimistic-concurrency mismatch — fetch latest version and retry.
            log.warning("Version conflict on %s; refetching", diagram_id)
            cur = self._request("GET", f"/api/diagrams/{diagram_id}")
            cur.raise_for_status()
            return self.update_diagram_content(
                diagram_id, name, description, content,
                version=cur.json()["current_version"],
            )
        r.raise_for_status()
        return r.json()


# ---------------------------------------------------------------------------
# Deployment passes
# ---------------------------------------------------------------------------

def plan_packages(manifest: Manifest) -> list[tuple[list[str], str]]:
    """Return the unique package chains in depth-first order.

    Each chain is a list of part names (e.g. ['Part A - Foo', 'A01 - Steps']).
    Returned with parent-first ordering so packages are created before
    their children.
    """
    chains: set[tuple[str, ...]] = set()
    for f in manifest.files:
        for i in range(1, len(f.package_chain) + 1):
            chains.add(tuple(f.package_chain[:i]))
    # Sort by depth so parents come before children, then by name for
    # determinism.
    ordered = sorted(chains, key=lambda c: (len(c), c))
    return [(list(c), c[-1]) for c in ordered]


def deploy(
    client: IrisClient,
    collection_name: str,
    set_name: str,
    *,
    dry_run: bool,
) -> None:
    manifest = collect_files()
    log.info("Found %d markdown files", len(manifest.files))

    chains = plan_packages(manifest)
    log.info("Planned %d packages, %d diagrams", len(chains), len(manifest.files))

    if dry_run:
        log.info("DRY RUN — printing plan and exiting (no writes).")
        _print_plan(manifest, chains)
        return

    # Collection
    collection = client.find_or_create_collection(collection_name)
    collection_id = collection["id"]
    log.info("Collection %r id=%s", collection_name, collection_id)

    # Set (fail-fast on duplicate)
    existing = client.find_set_by_name_in_collection(collection_id, set_name)
    if existing is not None:
        log.error(
            "Set %r already exists in collection %r (id=%s).\n"
            "Open %s/sets/%s to delete it, "
            "or pass --set <new-name> to publish alongside.",
            set_name, collection_name, existing["id"], client.web_url, existing["id"],
        )
        sys.exit(2)
    new_set = client.create_set(set_name, collection_id, description="DoView Book — published from doview-book repo")
    set_id = new_set["id"]
    log.info("Set %r id=%s", set_name, set_id)

    # Packages
    package_id_by_chain: dict[tuple[str, ...], str] = {}
    for chain, name in chains:
        parent_chain = tuple(chain[:-1])
        parent_id = package_id_by_chain.get(parent_chain)
        pkg = client.create_package(name=name, set_id=set_id, parent_package_id=parent_id)
        package_id_by_chain[tuple(chain)] = pkg["id"]
        log.info("Package %s/ id=%s", "/".join(chain), pkg["id"])

    # Pass 1: POST diagrams with original (frontmatter-stripped) content.
    log.info("Pass 1: creating %d diagrams", len(manifest.files))
    for i, f in enumerate(manifest.files, start=1):
        parent_id = package_id_by_chain.get(tuple(f.package_chain))
        d = client.create_diagram(
            name=f.title,
            description=f.description,
            content=f.body,
            set_id=set_id,
            parent_package_id=parent_id,
        )
        f.diagram_id = d["id"]
        manifest.id_by_path[f.rel_path] = d["id"]
        if i % 20 == 0:
            log.info("  ... created %d/%d", i, len(manifest.files))

    intro = manifest.id_by_path.get(PurePosixPath("1 - introduction.md"))
    if intro is None:
        log.warning("introduction file not in mapping; back-links will be left as-is")
        intro = ""
    manifest.introduction_id = intro

    # Pass 2: rewrite links and PUT.
    log.info("Pass 2: rewriting links + updating diagrams")
    unknown_by_file: dict[str, list[str]] = {}
    rewritten_count = 0
    for i, f in enumerate(manifest.files, start=1):
        new_body, unknown = rewrite_links(
            f.body, f.rel_path, manifest.id_by_path, manifest.introduction_id
        )
        if unknown:
            unknown_by_file[str(f.rel_path)] = unknown
        if new_body != f.body:
            assert f.diagram_id is not None
            client.update_diagram_content(
                f.diagram_id, f.title, f.description, new_body
            )
            rewritten_count += 1
        if i % 20 == 0:
            log.info("  ... processed %d/%d (rewrote %d)", i, len(manifest.files), rewritten_count)

    log.info("Done. Diagrams created: %d. Diagrams rewritten: %d.",
             len(manifest.files), rewritten_count)
    if unknown_by_file:
        log.warning("Unknown links (left as-is): %d files affected", len(unknown_by_file))
        for path, links in sorted(unknown_by_file.items())[:20]:
            log.warning("  %s → %s", path, ", ".join(links))
        if len(unknown_by_file) > 20:
            log.warning("  ... and %d more (full list in JSON below)", len(unknown_by_file) - 20)
        log.warning("Full unknown-link report:\n%s",
                    json.dumps(unknown_by_file, indent=2, sort_keys=True))
    log.info("Live set URL: %s/sets/%s", client.web_url, set_id)


def _print_plan(manifest: Manifest, chains: list[tuple[list[str], str]]) -> None:
    by_chain: dict[tuple[str, ...], int] = {}
    for f in manifest.files:
        by_chain[tuple(f.package_chain)] = by_chain.get(tuple(f.package_chain), 0) + 1
    log.info("--- Plan ---")
    log.info("Root-level diagrams: %d", by_chain.get((), 0))
    for chain, _ in chains:
        count = by_chain.get(tuple(chain), 0)
        log.info("  %s  (%d direct diagrams)", "/".join(chain) + "/", count)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Print plan, do not write.")
    parser.add_argument("--collection", default=DEFAULT_COLLECTION)
    parser.add_argument("--set", dest="set_name", default=DEFAULT_SET)
    args = parser.parse_args()

    api_url = os.environ.get("IRIS_UAT_API_URL", DEFAULT_API_URL)
    web_url = os.environ.get("IRIS_UAT_URL", DEFAULT_WEB_URL)

    token = os.environ.get("IRIS_UAT_TOKEN")
    if not token:
        log.info("IRIS_UAT_TOKEN env var not set; reading JWT from %s", TESTER_JSON_PATH)
        token = load_token_from_tester_storage()
        log.info("Loaded Supabase JWT (%d chars)", len(token))

    client = IrisClient(api_url, web_url, token)
    deploy(client, args.collection, args.set_name, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
