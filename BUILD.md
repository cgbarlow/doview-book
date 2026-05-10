# Build & development guide

> **Looking for the book?** Start at [README.md](README.md) — that's the reader-facing front page with the table of contents.
>
> This file is the technical/maintainer view: how the repo is laid out, how the Markdown was generated, and where the design decisions live.

A Markdown conversion of *DoView Planning and Practical Outcomes Theory Handbook (2025)* by Dr Paul W Duignan, with all diagrams and visual models rendered as Mermaid where they translate cleanly. Source PDFs are kept alongside.

For the canonical original, see [DoViewPlanning.org](https://www.doviewplanning.org).

## What's in here

```
docs/
  adrs/                — Architecture Decision Records (decisions, rejected alternatives, dependencies)
    specs/             — implementation specs accompanying ADRs
  pdf/                 — original handbook PDFs (the source of truth)
  pptx/                — drill-down PowerPoint template for Tool D1
  md/                  — Markdown conversion, organised by Part > Chapter
skills/
  pdf-to-mermaid-md/   — Claude Code skill that produced the Markdown
BUILD.md               — this file
CHANGELOG.md           — Keep a Changelog format, semver
LICENSE.md             — attribution and trademark terms
README.md              — reader-facing front page with TOC
```

## The markdown structure

`docs/md/` mirrors the book's table of contents:

- `1 - introduction.md` — title, attribution and a TOC linking to each Part
- `2 - conclusion.md` — closing chapter
- `Part A - DoView Planning Fundamentals/` … `Part J - AI Applications/` — one folder per part
  - Inside each Part: chapter folders named `XX - <chapter title>` (e.g. `A1 - The Five Steps in DoView Planning/`)
  - Each chapter folder contains the question/tool pair as two files: `xxquestion.md` and `xxtool.md`, cross-linked at the top

There are 109 chapter pairs across Parts A–J plus the introduction and conclusion — 219 markdown files total, one per source PDF.

## Viewing the diagrams

Each `*tool.md` whose source contained a visual model has a `## Diagram` section with a fenced ```mermaid block. To render these:

- **VS Code** — install the [`bierner.markdown-mermaid`](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) extension, then open any `.md` file and press `Ctrl+Shift+V` (or `Cmd+Shift+V` on Mac) for the rendered preview.
- **GitHub** — Mermaid blocks render natively in the web UI when browsing the repo.
- **Obsidian / Logseq / Typora** — Mermaid is supported natively.

A handful of source diagrams (e.g. C4's large real-world visual alignment poster) cannot be expressed cleanly in Mermaid; those pages note this and describe the visual in prose.

## How the conversion was done

PDFs were processed through a Claude Code skill — [`skills/pdf-to-mermaid-md/`](skills/pdf-to-mermaid-md/SKILL.md) — that:

1. Reads each PDF natively (text + page render),
2. Identifies prose, diagrams, and matrices,
3. Writes a markdown file with YAML frontmatter, an H1 title, a pair-link line, body prose, and a `## Diagram` section using the most appropriate Mermaid pattern (or a markdown table for matrices),
4. Cross-links each `xxquestion.md` ↔ `xxtool.md` pair,
5. Skips re-conversion if the target `.md` already exists.

Pair files for each chapter share the same folder, so the relative cross-links resolve without rewriting.

The skill is generic — point it at any directory of paired question/tool PDFs and it'll do the same. See [`skills/pdf-to-mermaid-md/SKILL.md`](skills/pdf-to-mermaid-md/SKILL.md) for the workflow and [`skills/pdf-to-mermaid-md/references/mermaid_patterns.md`](skills/pdf-to-mermaid-md/references/mermaid_patterns.md) for the diagram-archetype playbook (cyclic flows, drill-down trees, evolution timelines, etc.).

## Bundled Claude Code skills

The repo bundles three Claude Code skills:

- **[`pdf-to-mermaid-md`](skills/pdf-to-mermaid-md/SKILL.md)** — the conversion skill above. Generic across paired question/tool PDFs.
- **[`doview-outcomes-answer`](skills/doview-outcomes-answer/SKILL.md)** — faithful adaptation of *Prompt A — Outcomes Theory Text Response Prompt v1.1.9* from [doviewplanning.org/bookai](https://www.doviewplanning.org/bookai). Answers outcomes-theory questions strictly from Dr Paul Duignan's handbook with the prompt's required Summary + Full structure and raw-visible URL rules.
- **[`doview-image-retriever`](skills/doview-image-retriever/SKILL.md)** — faithful adaptation of *Prompt B — Outcomes Theory Book Image Retriever Prompt v1.1.9*, with a Mermaid-first overlay that retrieves Mermaid blocks from this repo's chapter `tool.md` files (falling back to upstream PNG/image-file URLs for diagrams that don't translate cleanly to Mermaid). Pairs with `doview-outcomes-answer`.

The two `doview-*` skills are also published in the [cgbarlow-skills](https://github.com/cgbarlow/skills) Claude plugin marketplace.

## Architecture decisions

The *why* behind the structure above is captured as ADRs — short, immutable records of each technical decision plus the rejected alternatives. Browse them in [`docs/adrs/`](docs/adrs/):

- [ADR-001 — Enhanced ADR format for this repo](docs/adrs/ADR-001-Enhanced-ADR-Format.md)
- [ADR-002 — Convert handbook PDFs to Markdown via Claude-native PDF reading](docs/adrs/ADR-002-PDF-to-Markdown-via-Claude-Native-Reading.md) (spec: [SPEC-002-A](docs/adrs/specs/SPEC-002-A-pdf-to-mermaid-md-Workflow.md))
- [ADR-003 — Render visual models as Mermaid; Markdown tables for matrices](docs/adrs/ADR-003-Mermaid-for-Diagrams.md) (spec: [SPEC-003-A](docs/adrs/specs/SPEC-003-A-Mermaid-Pattern-Playbook.md))
- [ADR-004 — Folder structure: `Part X - <title>/<XX> - <chapter title>/`](docs/adrs/ADR-004-Folder-Structure.md) (spec: [SPEC-004-A](docs/adrs/specs/SPEC-004-A-Restructure-Mapping.md))
- [ADR-005 — Cross-link question/tool pairs in the same folder; do not merge](docs/adrs/ADR-005-Cross-Linked-Pairs.md)
- [ADR-006 — Preserve original filenames inside chapter folders](docs/adrs/ADR-006-Preserve-Original-Filenames.md) *(superseded by ADR-012)*
- [ADR-007 — Idempotent conversion: skip if `.md` already exists](docs/adrs/ADR-007-Idempotent-Conversion.md)
- [ADR-008 — Licensing: free use with attribution; mirror DoView trademark policy](docs/adrs/ADR-008-Licensing.md)
- [ADR-009 — Faithful adaptation policy for external prompts](docs/adrs/ADR-009-Faithful-Prompt-Adaptation.md)
- [ADR-010 — Two separate skills mirroring Prompt A and Prompt B](docs/adrs/ADR-010-Two-Skills-Not-One.md) (specs: [SPEC-010-A](docs/adrs/specs/SPEC-010-A-Skill-doview-outcomes-answer.md), [SPEC-010-B](docs/adrs/specs/SPEC-010-B-Skill-doview-image-retriever.md))
- [ADR-011 — Marketplace integration approach](docs/adrs/ADR-011-Marketplace-Integration.md) (spec: [SPEC-011-A](docs/adrs/specs/SPEC-011-A-Marketplace-Sync.md))
- [ADR-012 — Zero-padded chapter folder and file names (Xnn format)](docs/adrs/ADR-012-Zero-Padded-Chapter-Names.md) — supersedes ADR-006

This repo follows the workflow described in [cgbarlow/protocols](https://github.com/cgbarlow/protocols/blob/main/protocols.md): ADRs in `docs/adrs/`, specs in `docs/adrs/specs/`, feature branches off `main`, semver via `CHANGELOG.md`.

## Attribution

This work is adapted from the *DoView Planning and Practical Outcomes Theory Handbook (2025)* by Dr Paul W Duignan, published at [DoViewPlanning.org](https://www.doviewplanning.org). All methodology, tool content, diagrams, and accompanying text are © Dr Paul W Duignan and DoViewPlanning.Org.

DoView® is a registered trademark. Use of DoView® Marks must comply with the [Attribution & Trademark Use Policy](https://www.doviewplanning.org/trademarkuse).

## License

Free to use, copy, share, and adapt for any purpose (including commercial) with attribution. See [LICENSE.md](LICENSE.md) for full terms.
