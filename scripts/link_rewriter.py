"""Pure helpers for the Iris deployment script (ADR-013).

Two functions:

- `strip_frontmatter(content)` — removes a leading `---\\n...---\\n`
  YAML block and returns `(body, parsed_frontmatter_dict)`.
- `rewrite_links(content, source_path, mapping, introduction_id)` —
  rewrites every `.md`-relative or folder-relative markdown link to
  `iris://diagram/<uuid>` using `mapping`. Code fences and inline code
  are skipped. Returns `(rewritten_content, unknown_link_targets)`.

No I/O, no HTTP. Tested in `tests/test_link_rewriter.py`.
"""

from __future__ import annotations

import re
from pathlib import PurePosixPath
from typing import Any

import yaml

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)

# Markdown link `[label](url)` and `[label](<url with spaces>)`.
# Group 1: label. Group 2: angle-bracketed url. Group 3: plain url.
LINK_RE = re.compile(
    r"\[([^\]]+)\]\((?:<([^>]+)>|([^)\s]+))\)"
)

# A fenced code block: starts at ``` (optionally with a lang tag), ends at
# matching ```. Multi-line, DOTALL.
FENCE_RE = re.compile(r"```[^\n]*\n.*?\n```", re.DOTALL)

# Inline code: backtick-delimited. Non-greedy so adjacent backticks pair.
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")

# URL schemes / forms the rewriter must NOT touch.
_PASS_THROUGH_PREFIXES = ("http://", "https://", "mailto:", "iris://", "#", "/")


def strip_frontmatter(content: str) -> tuple[str, dict[str, Any]]:
    """Strip a leading YAML frontmatter block. Returns `(body, frontmatter_dict)`.

    Frontmatter must start at byte zero (`---` on the first line).
    Trailing `---` lines inside the document body are left alone.
    """
    m = FRONTMATTER_RE.match(content)
    if not m:
        return content, {}
    fm_text = m.group(1)
    try:
        fm = yaml.safe_load(fm_text) or {}
        if not isinstance(fm, dict):
            fm = {}
    except yaml.YAMLError:
        fm = {}
    return content[m.end():].lstrip("\n"), fm


def _resolve_target(
    href: str,
    source_path: PurePosixPath,
    mapping: dict[PurePosixPath, str],
    introduction_id: str,
) -> tuple[str | None, bool]:
    """Resolve a markdown link target to an iris://diagram id.

    Returns `(new_href, was_unknown)`:
    - `(new_href, False)` if successfully rewritten.
    - `(None, False)` if the link should be passed through unchanged
      (external URL, anchor, absolute path, already-iris://).
    - `(None, True)` if it looks like a corpus-internal link but
      doesn't resolve in the mapping. Caller logs and leaves the link
      as-is.

    Special case: any path resolving to `../../README.md` (the
    out-of-corpus book root README) routes to `introduction_id`.
    """
    if href.startswith(_PASS_THROUGH_PREFIXES):
        return None, False

    # Resolve relative to the source file's parent directory.
    src_parent = PurePosixPath(*source_path.parts[:-1]) if source_path.parts else PurePosixPath("")
    # PurePosixPath does not implement `.resolve()` for relative refs; we
    # join + normalise manually.
    parts = list(src_parent.parts) + href.split("/")
    norm: list[str] = []
    for p in parts:
        if p == "" or p == ".":
            continue
        if p == "..":
            if norm:
                norm.pop()
            else:
                # Walking above the corpus root — the only legitimate
                # case is `../../README.md` to the book root.
                norm.append("..")
        else:
            norm.append(p)

    if norm and norm[0] == ".." and norm[-1].lower() == "readme.md":
        # `../../README.md` style back-link → introduction diagram.
        return f"iris://diagram/{introduction_id}", False

    candidate = PurePosixPath("/".join(norm))

    # Folder-only link (e.g. `<Part A - Foo>`) → look for `<folder>/index.md`.
    if not candidate.suffix:
        candidate = candidate / "index.md"

    if candidate in mapping:
        return f"iris://diagram/{mapping[candidate]}", False

    return None, True


def rewrite_links(
    content: str,
    source_path: PurePosixPath,
    mapping: dict[PurePosixPath, str],
    introduction_id: str,
) -> tuple[str, list[str]]:
    """Rewrite markdown links in `content`. See module docstring.

    Returns `(new_content, unknown_targets)`. `unknown_targets` lists
    the verbatim hrefs that looked corpus-internal but did not resolve.
    """
    # Mask code spans (fenced + inline) so links inside them are left alone.
    masks: list[str] = []

    def _mask(m: re.Match[str]) -> str:
        masks.append(m.group(0))
        return f"\x00MASK{len(masks) - 1}\x00"

    masked = FENCE_RE.sub(_mask, content)
    masked = INLINE_CODE_RE.sub(_mask, masked)

    unknown: list[str] = []

    def _replace(m: re.Match[str]) -> str:
        label = m.group(1)
        href = m.group(2) if m.group(2) is not None else m.group(3)
        new_href, was_unknown = _resolve_target(href, source_path, mapping, introduction_id)
        if was_unknown:
            unknown.append(href)
        if new_href is None:
            return m.group(0)
        return f"[{label}]({new_href})"

    rewritten = LINK_RE.sub(_replace, masked)

    # Restore code spans.
    def _unmask(m: re.Match[str]) -> str:
        idx = int(m.group(1))
        return masks[idx]

    rewritten = re.sub(r"\x00MASK(\d+)\x00", _unmask, rewritten)
    return rewritten, unknown
