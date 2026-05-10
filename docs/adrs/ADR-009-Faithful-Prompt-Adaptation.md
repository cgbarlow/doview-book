# ADR-009 — Faithful adaptation policy for external prompts

## Status

Accepted — 2026-05-10

## Why

DoViewPlanning.org publishes two carefully-crafted system prompts at https://www.doviewplanning.org/bookai for AI systems answering questions about Dr Paul Duignan's outcomes theory:

- **Prompt A — Outcomes Theory Text Response Prompt (v1.1.9)** — formal style rules, required response structure (Summary + Full), strict raw-visible-URL rules, an "outcomes system" definition rule, and a final compliance check.
- **Prompt B — Outcomes Theory Book Image Retriever Prompt (v1.1.9)** — image-display warning, image faithfulness rules, image-file URL handling, all designed for retrieving and embedding PNG diagrams from the doviewplanning.org pages.

The author has invested deliberate effort in the exact wording. Style rules like "no first-person", "outcomes theory as the primary frame", the "outcomes system" definition, and the "no markdown links — raw visible URLs only" rule are non-negotiable from the source's perspective. Any paraphrase risks degrading those constraints.

But our adaptation has to live as Claude Code skills, which adds a YAML frontmatter and a triggering description. And our medium has shifted: the diagrams that Prompt B fetches from doviewplanning.org as PNG images are *also available* in this repo as Mermaid blocks inside chapter `tool.md` files (ADR-002, ADR-003). Treating the upstream prompts as immutable text loses an opportunity for the skills to reference the local Markdown when it's available.

We need an explicit policy on what we may change and what we may not.

## What

The two skills derived from Prompt A and Prompt B are **substantially verbatim** copies of the upstream prompt text, with three categories of permitted edit:

1. **Skill frontmatter wrap** — a YAML frontmatter block with `name`, `description`, and (optionally) `argument-hint` is added at the top. The frontmatter does not paraphrase the prompt — it provides Claude Code's triggering metadata.
2. **Minimal contextual framing** — a short paragraph at the top of the SKILL.md body may identify the source page, the version number, and (in Prompt B's case) note the medium adaptation. Total framing is ≤ 5 lines.
3. **Medium adaptation** — Prompt B's image-handling rules are explicitly extended to cover **Mermaid blocks** as the primary representation, with the upstream PNG/image-file rules preserved as a fallback. This is the only structural change. Prompt A's text passes through unchanged.

Version numbers stay byte-identical (e.g. "v1.1.9" appears exactly as it does on the source page). If DoViewPlanning.org publishes a new version of either prompt, we produce a new version of the corresponding skill that mirrors the new version number.

## How

- The verbatim source is captured at `/tmp/bookai_text.txt` lines 103–344 (Prompt A) and 345–480 (Prompt B). The skill files reproduce these byte-for-byte except for the permitted edits above.
- Diff is reviewable: a future maintainer can compare the skill body to the source page and see exactly what changed. The frontmatter, framing paragraph, and (for skill B only) the Mermaid-extension language are clearly delineated.
- ADR-010 captures the two-skill structure decision.
- SPEC-010-A and SPEC-010-B (Phase 2) spell out the per-skill mapping.
- Files this decision touches: `skills/doview-outcomes-answer/SKILL.md`, `skills/doview-image-retriever/SKILL.md`.

## Rejected alternatives

### Verbatim with zero edits

Faithful but unworkable — Claude Code skills require frontmatter to be discovered and triggered. Without it the skills wouldn't load. And without the medium-shift note on Prompt B, the skill would chase squarespace-cdn image URLs and miss the Mermaid that's right next to it in the repo.

### Heavy paraphrase / "rewrite in our own words"

Tempting for tone consistency with other cgbarlow skills, but destroys the upstream value. The author's style rules are deliberately specific (e.g. "do not write 'I would', 'you could'", "outcomes theory as the primary frame, DoView as applied form") and a rewrite would silently drop them.

### Two versions of each skill — verbatim + ours-style

Doubles maintenance with no clear benefit. The verbatim copy is the canonical artefact; "our style" doesn't add value.

### Merge Prompt A and Prompt B into a single skill

Considered and rejected in ADR-010. A summary: the upstream split has structural value — Prompt B explicitly references Prompt A's output and runs after. Merging would either lose Prompt B's image/Mermaid handling or force its rules into Prompt A's response, conflicting with Prompt A's compliance check.

## Dependencies

- Depends on ADR-001 (format).
- Drives ADR-010 (skill structure), SPEC-010-A, SPEC-010-B.
