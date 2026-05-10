# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `docs/adrs/` — Architecture Decision Records, backfilling existing decisions and bootstrapping the WH(Y) format used in this repo:
  - ADR-001 — Enhanced ADR format for this repo
  - ADR-002 — Convert handbook PDFs to Markdown via Claude-native PDF reading
  - ADR-003 — Render visual models as Mermaid; Markdown tables for matrices
  - ADR-004 — Folder structure: `Part X - <title>/<XX> - <chapter title>/`
  - ADR-005 — Cross-link question/tool pairs in the same folder; do not merge
  - ADR-006 — Preserve original filenames inside chapter folders
  - ADR-007 — Idempotent conversion: skip if `.md` already exists
  - ADR-008 — Licensing: free use with attribution; mirror DoView trademark policy
- `docs/adrs/specs/` — implementation specs:
  - SPEC-002-A — `pdf-to-mermaid-md` skill workflow
  - SPEC-003-A — Mermaid pattern playbook
  - SPEC-004-A — Restructure mapping
- `BUILD.md` — preserves the previous technical README content (file structure, viewing, conversion approach, ADR index).
- `CHANGELOG.md` — this file.

### Changed

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
