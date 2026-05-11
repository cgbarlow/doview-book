# ADR-013 — Deploy DoView Book to Iris via a two-pass Python script

## Status

Accepted — 2026-05-11

## Why

The DoView Book corpus at `docs/md/` is designed to be read on disk
(GitHub, VS Code, Obsidian) but the author also wants it published on
the Iris UAT instance at https://iris-uat.chrisbarlow.nz under a new
"DoView Book" set inside the existing "DoView Strategy Models"
collection. Iris natively renders markdown — including Mermaid as of
v5.7.0 / ADR-149 — so the corpus can land as ~230 Text diagrams with
no content transformation other than rewriting links.

The hard constraint is link rewriting. Iris uses an `iris://diagram/<uuid>`
URL scheme to navigate between diagrams. The corpus uses ordinary
relative markdown links (`[label](file.md)`,
`[label](<folder with spaces/file.md>)`, `[label](<folder>)` resolving
to `folder/index.md` per Jekyll readme-index). Those links must be
rewritten to point at Iris-generated UUIDs after every diagram is
created.

Iris's POST endpoint generates UUIDs server-side — we cannot
pre-allocate them. So a single-pass deploy that writes rewritten
content from the start is not possible.

## What

Deploy the corpus to Iris via a two-pass Python script
`scripts/deploy_to_iris_uat.py`:

1. **Pass 1** — authenticate, ensure the collection exists, create
   the set (fail-fast on duplicate), walk the disk tree, create the
   package hierarchy, then `POST /api/diagrams` for every `.md` file
   with frontmatter-stripped content. Collect a
   `relative_path → diagram_id` mapping as each diagram is created.
2. **Pass 2** — for each diagram, run a pure
   `rewrite_links(content, source_path, mapping, introduction_id)`
   helper, then `PUT /api/diagrams/{id}` (with `If-Match: 1`) to push
   the rewritten content.

The hierarchy is **deep** — mirror the disk layout: one package per
Part, one nested package per chapter, two diagrams per chapter
(question + tool), root pages (introduction, conclusion) at set
root.

## How

- Files added under `scripts/`:
  - `link_rewriter.py` — pure module with `strip_frontmatter` and
    `rewrite_links` functions. No I/O. Fully unit-tested.
  - `deploy_to_iris_uat.py` — driver. Reads `IRIS_UAT_URL`,
    `IRIS_UAT_USER`, `IRIS_UAT_PASSWORD` from env (defaults to UAT
    sandbox). Supports `--dry-run` to print the planned hierarchy
    without writing.
  - `tests/test_link_rewriter.py` — pytest unit tests covering: plain
    relative links, angle-bracket links with spaces, folder-only
    links → `<folder>/index.md`, `../../README.md` → introduction id,
    external URLs untouched, frontmatter stripping, code-fence
    skipping (mermaid arrows like `A-->B` must not be mis-matched),
    unknown links left in place with a warning.
  - `requirements.txt` — `requests`, `pyyaml`, `pytest`.
  - `README.md` — usage instructions.
- The script implements exponential backoff on `429` and
  re-authenticates on `401` so a long run survives token expiry.
- Idempotency is **fail-fast on duplicate set name**. Re-running the
  script after a partial failure requires the user to delete the
  partial set via the Iris UI first.
- The script logs every operation and writes a summary at the end
  (count of diagrams created, count of links rewritten, count of
  unknown links with a per-file breakdown for spot-checking).

## Rejected alternatives

### Pre-allocate UUIDs client-side and POST with custom ids

Would let the script run in a single pass. Rejected: the Iris POST
contract does not accept a client-supplied id —
`backend/app/diagrams/service.py:39` generates the UUID server-side.
Changing the Iris contract is out of scope for a content-deployment
task.

### Render mermaid + iris://-rewritten markdown ahead of time and import as HTML

Would skip the second pass. Rejected: Iris's Text diagram contract
expects markdown source in `data.content` (SPEC-137-A), not HTML.
Iris's renderer + sanitiser pipeline is the canonical render path;
pre-rendering would bypass it and lose the editing affordance.

### Bash + curl + jq

Faster to bootstrap for HTTP but fragile for link rewriting
(markdown parsing in bash is painful — angle-bracket forms, code
fences, frontmatter all need stateful handling). Python with
`pathlib` + a small regex set is the cleaner fit. Tests are also
trivial in pytest.

### Write the deployment script inside the iris repo

Considered putting it in `iris/scripts/`. Rejected: the script
deploys *content* that lives in this repo; coupling it to iris
would split ownership and make future content updates require a
cross-repo PR. The script consumes the Iris public API (a stable
contract via ADR-137 / ADR-149 / SPEC-137-A) so dependency is
one-way.

## Dependencies

— (this is the first deployment-tooling decision in this repo;
ADR-001 defines the format).
