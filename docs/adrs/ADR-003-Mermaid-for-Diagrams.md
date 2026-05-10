# ADR-003 — Render visual models as Mermaid; use Markdown tables for matrices

## Status

Accepted — 2026-05-10

## Why

Many of the handbook's tool pages carry a *visual model* — a flow, a hierarchy, a comparison matrix, a before/after pair — that is the point of the page. A Markdown copy that drops the visual loses the page's meaning.

We need a representation that:
- lives in plain text (so the Markdown is searchable, diffable, and version-controllable);
- renders in mainstream tools where the user is already reading: VS Code preview, GitHub web UI, Obsidian, Logseq, Typora;
- can be edited as code (so a future change to a diagram is a trivial PR, not a graphics-editor round-trip);
- is *good enough* for the kinds of diagrams the handbook contains — flows, trees, simple cycles, comparison columns — without forcing the converter to fight the tooling for fancy layouts.

## What

Render each handbook diagram as a [Mermaid](https://mermaid.js.org/) fenced code block under a `## Diagram` heading. For diagrams that are fundamentally tabular (rows × columns of values), use a Markdown table instead of Mermaid. For diagrams that translate cleanly to neither (poster-style infographics, freehand sketches, dense visual alignment posters), describe the visual in prose under `## Diagram` and note that the original does not translate cleanly.

## How

- The skill picks the Mermaid pattern (`flowchart LR`, `flowchart TD`, subgraphs for before/after, etc.) based on the diagram archetype. A playbook of these patterns lives at `skills/pdf-to-mermaid-md/references/mermaid_patterns.md`.
- Quote node labels containing spaces or punctuation: `A["A — label here"]`.
- Keep node labels short. If the source box has multiple lines, put the first line in the node and the rest in prose under the diagram.
- Comparison matrices (rows of categories with columns of letter-chips, e.g. A1's "where steps used") render as Markdown tables — clearer to read and easier to edit than fighting Mermaid into a grid.
- Pages with no visual model omit the `## Diagram` section entirely.

The full archetype playbook is captured in [SPEC-003-A](specs/SPEC-003-A-Mermaid-Pattern-Playbook.md) and lives in the skill at `skills/pdf-to-mermaid-md/references/mermaid_patterns.md`.

## Rejected alternatives

### Embed page images as PNG

Faithful to the original but kills searchability and diffability — every diagram becomes opaque to grep, AI tooling, and PR review. Also bloats the repo with binary blobs.

### SVG inline

Mainstream Markdown renderers (GitHub, VS Code default preview) don't render arbitrary inline SVG inside fenced blocks the way they render Mermaid. SVG would also require either hand-authoring (slow) or PDF-to-SVG conversion (lossy on text positioning), with no real readability win over Mermaid for the simple flows the handbook contains.

### draw.io XML / Excalidraw JSON

The cgbarlow/doview-skill repo uses these formats for *authored* DoView diagrams. They're great when you want post-generation interactive editing. For our use case — converting an existing book to read-only Markdown — they add tooling friction (need a viewer extension to render) and aren't supported by GitHub web UI without effort. Mermaid wins on "renders everywhere readers will look".

### ASCII art

Cute but unreadable for anything more than a 3-node flow. Editing burden is also brutal.

### Drop diagrams entirely; rely on the source PDFs

Loses half the handbook's value in the Markdown layer. Defeats the whole point of conversion.

## Dependencies

- Depends on ADR-002.
