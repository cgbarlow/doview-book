# DoView Planning Handbook — Markdown edition

A markdown conversion of *DoView Planning and Practical Outcomes Theory Handbook (2025)* by Dr Paul W Duignan, with all diagrams and visual models rendered as Mermaid where they translate cleanly. Source PDFs are kept alongside.

For the canonical original, see [DoViewPlanning.org](https://www.doviewplanning.org).

## What's in here

```
docs/
  pdf/    — original handbook PDFs (the source of truth)
  pptx/   — drill-down PowerPoint template for Tool D1 (overview slide + one slide per framework component, ready for a strategist to fill in)
  md/     — markdown conversion, organised by Part > Chapter
skills/
  pdf-to-mermaid-md/  — Claude Code skill that produced the markdown
LICENSE.md
README.md
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

## Attribution

This work is adapted from the *DoView Planning and Practical Outcomes Theory Handbook (2025)* by Dr Paul W Duignan, published at [DoViewPlanning.org](https://www.doviewplanning.org). All methodology, tool content, diagrams, and accompanying text are © Dr Paul W Duignan and DoViewPlanning.Org.

DoView® is a registered trademark. Use of DoView® Marks must comply with the [Attribution & Trademark Use Policy](https://www.doviewplanning.org/trademarkuse).

## License

Free to use, copy, share, and adapt for any purpose (including commercial) with attribution. See [LICENSE.md](LICENSE.md) for full terms.
