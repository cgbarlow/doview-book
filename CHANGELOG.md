# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `docs/adrs/` — Architecture Decision Records, backfilling existing decisions and recording new decisions for the skill work. Bootstraps the WH(Y) format used in this repo:
  - ADR-001 — Enhanced ADR format for this repo
  - ADR-002 — Convert handbook PDFs to Markdown via Claude-native PDF reading
  - ADR-003 — Render visual models as Mermaid; Markdown tables for matrices
  - ADR-004 — Folder structure: `Part X - <title>/<XX> - <chapter title>/`
  - ADR-005 — Cross-link question/tool pairs in the same folder; do not merge
  - ADR-006 — Preserve original filenames inside chapter folders
  - ADR-007 — Idempotent conversion: skip if `.md` already exists
  - ADR-008 — Licensing: free use with attribution; mirror DoView trademark policy
  - ADR-009 — Faithful adaptation policy for external prompts (Mermaid medium shift for Prompt B)
  - ADR-010 — Two separate skills mirroring Prompt A and Prompt B (not merged)
  - ADR-011 — Marketplace integration approach (local-source copy into cgbarlow/skills)
- `docs/adrs/specs/` — implementation specs:
  - SPEC-002-A — `pdf-to-mermaid-md` skill workflow
  - SPEC-003-A — Mermaid pattern playbook
  - SPEC-004-A — Restructure mapping
  - SPEC-010-A — `doview-outcomes-answer` skill (Prompt A adaptation)
  - SPEC-010-B — `doview-image-retriever` skill (Prompt B adaptation with Mermaid extension)
  - SPEC-011-A — Marketplace sync workflow
- `BUILD.md` — preserves the previous technical README content (file structure, viewing, conversion approach, ADR index).
- `CHANGELOG.md` — this file.

- `skills/doview-outcomes-answer/` — Claude Code skill, faithful adaptation of *Prompt A — Outcomes Theory Text Response Prompt v1.1.9* from https://www.doviewplanning.org/bookai. Answers outcomes-theory questions strictly from the handbook with the prompt's required Summary + Full standalone structure and raw-visible URL rules.
- `skills/doview-image-retriever/` — Claude Code skill, faithful adaptation of *Prompt B — Outcomes Theory Book Image Retriever Prompt v1.1.9* with a Mermaid-first overlay. Retrieves and reproduces relevant chapter `tool.md` Mermaid blocks as the primary visual, falling back to the upstream PNG/image-file URLs for diagrams that don't translate cleanly to Mermaid. Pairs with `doview-outcomes-answer`.
- `docs/md/Part X - …/README.md` (×10) — mini-TOC inside each Part folder, listing chapters in numerical order with links to each chapter's `xxquestion.md` entry point.
- `tools/generate_part_readmes.py` — helper that generates the per-Part READMEs.
- `tools/zero_pad_chapter_names.py` — one-shot helper that renamed chapter folders + Markdown files to the Xnn format.
- ADR-012 — Zero-padded chapter folder and file names (supersedes ADR-006).

### Changed

- All 109 chapter folders renamed from `XN[suffix]` to `Xnn[suffix]` format (`A1` → `A01`, `G2A` → `G02A`, etc.). All 218 chapter Markdown files renamed accordingly. Cross-links inside chapter files and YAML `pair:` frontmatter updated to match. Part-folder READMEs regenerated. Source PDFs in `docs/pdf/` are unchanged — the `source_pdf:` frontmatter field still points at the as-published filename (e.g. `docs/pdf/a1question.pdf`).

- `README.md` — rewritten as a reader-friendly book front page with a Table of Contents linking to the introduction, every Part, and the conclusion. The previous technical content moved to `BUILD.md`.

## [1.0.0] — 2026-05-10

### Added

- 219 Markdown files in `docs/md/`, mirroring the book's structure: Part A–J with chapter subfolders, plus introduction and conclusion at the root.
- Mermaid diagrams for every visual model that translates cleanly. Comparison matrices use Markdown tables; the few diagrams that don't fit either form are described in prose.
- Question / tool pairs cross-linked at the top of each chapter file.
- Source PDFs retained under `docs/pdf/`.
- D1 PowerPoint template under `docs/pptx/` — drill-down deck for the DoView Planning Framework.
- `skills/pdf-to-mermaid-md/` — Claude Code skill that produced the Markdown.
- `LICENSE.md` — attribution and trademark terms aligned with DoViewPlanning.Org.

[Unreleased]: https://github.com/cgbarlow/doview-book/compare/v1.0...HEAD
[1.0.0]: https://github.com/cgbarlow/doview-book/releases/tag/v1.0
