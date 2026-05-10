# SPEC-010-B — `doview-image-retriever` skill (Mermaid-extended)

**Implements:** [ADR-009 — Faithful adaptation policy](../ADR-009-Faithful-Prompt-Adaptation.md), [ADR-010 — Two separate skills](../ADR-010-Two-Skills-Not-One.md)

Captures how Prompt B is transcribed into the skill SKILL.md, with the medium adaptation from PNG image retrieval to Mermaid block retrieval.

## Source

- **Source page**: https://www.doviewplanning.org/bookai
- **Source prompt**: Prompt B — Outcomes Theory Book Image Retriever Prompt
- **Version**: v1.1.9
- **Verbatim text**: `/tmp/bookai_text.txt` lines 345–480.

## Medium shift

The upstream prompt is designed to retrieve PNG images from doviewplanning.org pages (squarespace-cdn URLs). This repo's Markdown edition has the same diagrams as Mermaid blocks inside chapter `tool.md` files. Per ADR-009, we extend Prompt B's image-handling rules to cover Mermaid as the **primary representation** in this context, with the upstream PNG/image-file rules preserved as a **fallback** when a Mermaid block isn't available for the cited tool (e.g. handbook pages with poster-style diagrams that didn't translate cleanly to Mermaid — these are marked in their `tool.md` with the "does not translate cleanly to Mermaid" note).

## Skill layout

```
skills/doview-image-retriever/
├── SKILL.md
└── evals/
    └── evals.json
```

## SKILL.md structure

```markdown
---
name: doview-image-retriever
description: <triggering description — see below>
---

# DoView Diagram Retriever (Mermaid + PNG fallback)

> Faithful adaptation of *Prompt B — Outcomes Theory Book Image Retriever Prompt (v1.1.9)*
> from https://www.doviewplanning.org/bookai. Source content © Dr Paul W Duignan and
> DoViewPlanning.Org. Extended to retrieve **Mermaid blocks** as the primary representation
> (the source diagrams are available as Mermaid in the
> [doview-book](https://github.com/cgbarlow/doview-book) repo), with the upstream
> PNG/image-file rules preserved as a fallback.

## Medium adaptation note

Prompt B was originally written to retrieve and embed PNG images from doviewplanning.org pages. In this skill's context, the same diagrams are available as Mermaid code blocks inside chapter `tool.md` files at
https://github.com/cgbarlow/doview-book/tree/main/docs/md . When a relevant chapter has a Mermaid block, retrieve and reproduce the Mermaid block as the primary visual. When the chapter's `tool.md` notes "does not translate cleanly to Mermaid", fall back to the upstream PNG/image-file URL behaviour against the doviewplanning.org source page.

<verbatim Prompt B v1.1.9 text, lines 345–480 of /tmp/bookai_text.txt, with Mermaid-extension overlay>
```

## Verbatim-vs-extension diff

The body is the upstream Prompt B text verbatim, with **one** category of additions clearly delimited:

- A "**Mermaid-first rule**" subsection inserted under "MANDATORY IMAGE DISPLAY RULE" stating: if the cited chapter has a Mermaid block, reproduce the Mermaid block in a `mermaid` fenced code block; the upstream image-file/markdown-embed rules apply when no Mermaid is available.
- A note under "OUTPUT FORMAT" that each retrieved diagram entry now has an optional **Mermaid block** field, alongside the existing Page URL / Image file URL / Original image fields.
- "IMAGE FAITHFULNESS RULES" extended to apply equally to Mermaid: reproduce the Mermaid block exactly as it appears in `tool.md` — do not rewrite it, do not paraphrase node labels.

Everything else — the IMAGE PRIORITISATION RULE, the IMAGE DISPLAY LIMITATION WARNING (now reframed as also covering Mermaid rendering), the FINAL COMPLIANCE CHECK — is preserved.

## Frontmatter

### `name`

`doview-image-retriever`

### `description`

Draft:

> Retrieve and faithfully reproduce DoView Planning handbook diagrams to accompany an outcomes-theory answer. Use after a `doview-outcomes-answer` response when the user asks to see the diagrams, asks for the visual model, asks for "the picture", or whenever an outcomes-theory answer would land harder with the original tool diagrams visible. Reproduces **Mermaid blocks** from the local Markdown edition first (https://github.com/cgbarlow/doview-book), and falls back to the upstream PNG/image-file URLs from doviewplanning.org when a chapter's diagram doesn't translate cleanly to Mermaid. Faithful — never redraws, simplifies, paraphrases, or substitutes images or Mermaid blocks.

(Final wording finalised in Phase 4.)

## Faithfulness rules

Per ADR-009:

1. The frontmatter and the framing block above the verbatim prompt are the only structural additions other than the Mermaid-first overlay.
2. The Mermaid-first overlay is a **superset** of the upstream behaviour — it adds, it doesn't replace.
3. The upstream "IMAGE FAITHFULNESS RULES" — *do not redraw, simplify, improve, or approximate any missing image* — apply equally to Mermaid blocks.

## Eval prompts

3–4 prompts that follow a `doview-outcomes-answer`-style preceding response:

1. After a Prompt-A answer that cites Tool A1: *"Show me the original A1 diagram."* (expect Mermaid from `a1tool.md`).
2. After a Prompt-A answer that cites Tool C4 (which doesn't translate to Mermaid cleanly): *"Show me the original C4 image."* (expect PNG-fallback path with image-file URL from doviewplanning.org).
3. After a Prompt-A answer that cites multiple tools: *"Show me the diagrams for all of those."* (expect prioritisation per upstream rule, Mermaid-first per overlay).

Each eval expects the response to:
- Begin with the IMAGE DISPLAY LIMITATION WARNING.
- Reproduce the Mermaid block byte-identical to the chapter's `tool.md` when available.
- Use the upstream Page URL / Image file URL / Original image fields when Mermaid isn't available.
- End with the full handbook reference in raw visible URL form.

## Acceptance tests

- SKILL.md frontmatter parses cleanly.
- Body excluding frontmatter, framing, and the explicitly-delimited Mermaid-overlay subsections diffs cleanly against `/tmp/bookai_text.txt` lines 345–480.
- Skill loads in Claude Code.

## Files this spec governs

- `skills/doview-image-retriever/SKILL.md`
- `skills/doview-image-retriever/evals/evals.json`
