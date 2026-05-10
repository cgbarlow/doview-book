# SPEC-010-A — `doview-outcomes-answer` skill

**Implements:** [ADR-009 — Faithful adaptation policy](../ADR-009-Faithful-Prompt-Adaptation.md), [ADR-010 — Two separate skills](../ADR-010-Two-Skills-Not-One.md)

Captures how Prompt A is transcribed into the skill SKILL.md.

## Source

- **Source page**: https://www.doviewplanning.org/bookai
- **Source prompt**: Prompt A — Outcomes Theory Text Response Prompt
- **Version**: v1.1.9
- **Verbatim text**: `/tmp/bookai_text.txt` lines 103–344 (captured at the time of this work).

## Skill layout

```
skills/doview-outcomes-answer/
├── SKILL.md
└── evals/
    └── evals.json
```

## SKILL.md structure

```markdown
---
name: doview-outcomes-answer
description: <triggering description — see below>
---

# Outcomes Theory Text Response (DoView Planning Handbook)

> Faithful adaptation of *Prompt A — Outcomes Theory Text Response Prompt (v1.1.9)*
> from https://www.doviewplanning.org/bookai. Source content © Dr Paul W Duignan and
> DoViewPlanning.Org. This skill is included with the
> [doview-book](https://github.com/cgbarlow/doview-book) Markdown edition.

<verbatim Prompt A v1.1.9 text, lines 103–344 of /tmp/bookai_text.txt>
```

## Frontmatter

### `name`

`doview-outcomes-answer`

### `description`

Pushy, concrete triggering language. Draft:

> Answer outcomes-theory questions strictly from Dr Paul Duignan's *DoView Planning and Outcomes Theory Handbook* (2025). Use whenever the user asks for an outcomes-theory perspective, requests a DoView analysis, asks "what does outcomes theory say about…", asks to analyse a strategy/proposal/plan/policy from an outcomes perspective, mentions outcomes theory/outcomes systems/DoView Boards/strategy-outcomes diagrams, or shares a document and wants it critiqued through an outcomes-theory lens. Also use when the user wants a formal, standalone, copy-safe response with the required Summary + Full structure and raw-visible URLs that the handbook's Prompt A v1.1.9 demands. Strictly avoids first-person advice; uses outcomes theory as the primary frame and DoView as its applied form.

(Final wording finalised in Phase 3 after the description-optimisation step.)

## Faithfulness rules

Per ADR-009:

1. **Frontmatter wrap is the only structural addition.**
2. **Framing block** above the verbatim prompt is ≤ 5 lines and states only: source, version, attribution.
3. **Verbatim body**: every "STYLE RULES", "RAW VISIBLE URL RULE", "OUTCOMES SYSTEM DEFINITION RULE", "REQUIRED STRUCTURE", "IMAGE-RETRIEVAL SEED LIST FOR PROMPT B", and "FINAL COMPLIANCE CHECK BEFORE ANSWERING" section is byte-identical to the source.
4. **No paraphrase** of style rules, no condensation of the URL rule, no reordering of the compliance check.

## Eval prompts

A starting set of 3–4 prompts (final assertions in Phase 5):

1. *"From an outcomes-theory perspective, why does this strategy doc lack a clear theory of change?"* (paste a short fictional strategy snippet)
2. *"Analyse this council programme proposal using DoView Planning principles — what outcomes-system gaps stand out?"*
3. *"What does outcomes theory say about choosing KPIs for a homelessness reduction initiative?"*
4. *"Critique this 'we measured X, results improved' attribution claim through an outcomes lens."*

Each eval expects the response to:
- Begin with the required preliminary sentence (`I have prepared a summary response and a full response…`).
- Contain exactly two main sections starting `1. Summary response to …` and `2. Full response to …`.
- Cite at least one DoView tool by name and include its full raw-visible-URL.
- End the Full response with the full handbook reference + raw-visible URL + "Image-retrieval seed list for Prompt B" block.
- Contain zero hidden links, zero markdown link syntax for URLs, zero "see above" wording.

## Acceptance tests

- SKILL.md frontmatter parses cleanly (YAML loader produces `{name, description}`).
- Body length ≈ source prompt length (allow ±50 lines for framing).
- Diff between SKILL.md body (excluding frontmatter and framing) and `/tmp/bookai_text.txt` lines 103–344 is **empty**.
- Skill loads in Claude Code (verified manually in Phase 3 PR).

## Files this spec governs

- `skills/doview-outcomes-answer/SKILL.md`
- `skills/doview-outcomes-answer/evals/evals.json`
