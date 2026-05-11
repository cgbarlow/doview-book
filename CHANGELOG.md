# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **`scripts/deploy_to_iris_uat.py`** — publishes the corpus to an Iris instance as a Set of Text diagrams ([ADR-013](docs/adrs/ADR-013-Iris-Deployment-Script.md), [scripts/README.md](scripts/README.md)). Two-pass strategy: create the package hierarchy + diagrams, then rewrite every intra-corpus `.md` link to `iris://diagram/<uuid>` so navigation works inside Iris. Live deploy verified at https://iris-uat.chrisbarlow.nz under the "DoView Strategy Models" collection (230 diagrams, 119 packages).
- **`scripts/link_rewriter.py`** + tests — pure helpers (`strip_frontmatter`, `rewrite_links`) used by the deployment script. Handles plain `[label](file.md)`, angle-bracket `[label](<folder with spaces/file.md>)`, folder-only links (`<folder>` → `<folder>/index.md`), the out-of-corpus `../../README.md` back-link (rewritten to the introduction diagram), and skips links inside fenced code / inline code so Mermaid arrows (`A-->B`) are not mis-matched.
- **`docs/adrs/ADR-013-Iris-Deployment-Script.md`** — records the two-pass strategy, link-mapping rules, idempotency choice (fail-fast on duplicate set name), and rejected alternatives.

## [1.1.0] — 2026-05-10

### Added

- **`docs/adrs/`** — Architecture Decision Records, backfilling existing decisions and recording new decisions for the skill work. Bootstraps the WH(Y) format used in this repo:
  - ADR-001 — Enhanced ADR format for this repo
  - ADR-002 — Convert handbook PDFs to Markdown via Claude-native PDF reading
  - ADR-003 — Render visual models as Mermaid; Markdown tables for matrices
  - ADR-004 — Folder structure: `Part X - <title>/<XX> - <chapter title>/`
  - ADR-005 — Cross-link question/tool pairs in the same folder; do not merge
  - ADR-006 — Preserve original filenames inside chapter folders *(superseded by ADR-012)*
  - ADR-007 — Idempotent conversion: skip if `.md` already exists
  - ADR-008 — Licensing: free use with attribution; mirror DoView trademark policy
  - ADR-009 — Faithful adaptation policy for external prompts (Mermaid medium shift for Prompt B)
  - ADR-010 — Two separate skills mirroring Prompt A and Prompt B (not merged)
  - ADR-011 — Marketplace integration approach (local-source copy into cgbarlow/skills)
  - ADR-012 — Zero-padded chapter folder and file names (supersedes ADR-006)
- **`docs/adrs/specs/`** — implementation specs (SPEC-002-A, SPEC-003-A, SPEC-004-A, SPEC-010-A, SPEC-010-B, SPEC-011-A).
- **`skills/doview-outcomes-answer/`** — Claude Code skill, faithful adaptation of *Prompt A — Outcomes Theory Text Response Prompt v1.1.9* from https://www.doviewplanning.org/bookai. Answers outcomes-theory questions strictly from the handbook with the prompt's required Summary + Full standalone structure and raw-visible URL rules.
- **`skills/doview-image-retriever/`** — Claude Code skill, faithful adaptation of *Prompt B — Outcomes Theory Book Image Retriever Prompt v1.1.9* with a Mermaid-first overlay. Retrieves and reproduces relevant chapter `tool.md` Mermaid blocks as the primary visual, falling back to the upstream PNG/image-file URLs for diagrams that don't translate cleanly to Mermaid. Pairs with `doview-outcomes-answer`.
- **`docs/md/Part X - …/README.md`** (×10) — mini-TOC inside each Part folder, listing chapters in numerical order with links to each chapter's `xxquestion.md` entry point. Each README has YAML frontmatter (`part`, `title`, `kind: part-index`, `chapters`).
- **`BUILD.md`** — preserves the previous technical README content (file structure, viewing, conversion approach, ADR index).
- **`CHANGELOG.md`** — this file.
- **`tools/generate_part_readmes.py`** — helper that generates the per-Part READMEs.
- **`tools/zero_pad_chapter_names.py`** — one-shot helper that renamed chapter folders + Markdown files to the Xnn format.
- **`skills/doview-outcomes-answer/evals/RESULTS.md`** and `runs/` — Phase 5 evaluation outputs (8/8 + 7/7 assertion PASS).
- **`skills/doview-image-retriever/evals/RESULTS.md`** and `runs/` — Phase 5 evaluation outputs (6/6 assertion PASS on the primary Mermaid-first path).

### Changed

- **Chapter folder + file names zero-padded to Xnn format.** All 109 chapter folders renamed from `XN[suffix]` to `Xnn[suffix]` (`A1` → `A01`, `G2A` → `G02A`, etc.). All 218 chapter Markdown files renamed accordingly. Cross-links inside chapter files and YAML `pair:` frontmatter updated to match. Part-folder indexes regenerated. Source PDFs in `docs/pdf/` are unchanged — the `source_pdf:` frontmatter field still points at the as-published filename (e.g. `docs/pdf/a1question.pdf`).
- **`README.md`** — rewritten as a reader-friendly book front page with a Table of Contents linking to the introduction, every Part, and the conclusion. The previous technical content moved to `BUILD.md`.
- **Part folder indexes use `index.md`** so the GitHub Pages site (https://chrisbarlow.nz/doview-book/) serves them at the folder URL. (Initially shipped as `README.md` plus a `jekyll-readme-index` plugin attempt; the plugin built without error but didn't actually serve subdirectory READMEs, so the indexes are stored as `index.md` directly. `tools/generate_part_readmes.py` writes `index.md`.)

### Fixed

- GitHub Pages 404 on subdirectory URLs (e.g. `Part%20A%20-%20.../`). See the index.md rename above.

## [1.0.0] — 2026-05-10

### Added

- 219 Markdown files in `docs/md/`, mirroring the book's structure: Part A–J with chapter subfolders, plus introduction and conclusion at the root.
- Mermaid diagrams for every visual model that translates cleanly. Comparison matrices use Markdown tables; the few diagrams that don't fit either form are described in prose.
- Question / tool pairs cross-linked at the top of each chapter file.
- Source PDFs retained under `docs/pdf/`.
- D1 PowerPoint template under `docs/pptx/` — drill-down deck for the DoView Planning Framework.
- `skills/pdf-to-mermaid-md/` — Claude Code skill that produced the Markdown.
- `LICENSE.md` — attribution and trademark terms aligned with DoViewPlanning.Org.

[Unreleased]: https://github.com/cgbarlow/doview-book/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/cgbarlow/doview-book/compare/v1.0...v1.1.0
[1.0.0]: https://github.com/cgbarlow/doview-book/releases/tag/v1.0
