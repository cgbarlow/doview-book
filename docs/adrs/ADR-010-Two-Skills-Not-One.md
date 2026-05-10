# ADR-010 — Two separate skills mirroring Prompt A and Prompt B

## Status

Accepted — 2026-05-10

## Why

DoViewPlanning.org publishes two prompts (Prompt A and Prompt B) that operate in sequence: Prompt A produces an outcomes-theory text answer; Prompt B runs after, reading the previous response and retrieving relevant diagrams. We had to decide whether to ship this as one skill or two.

## What

Ship **two distinct skills**:

- `doview-outcomes-answer` — adapts Prompt A. Triggers on outcomes-theory questions.
- `doview-image-retriever` — adapts Prompt B. Triggers after a `doview-outcomes-answer` response when the user asks for the diagrams (or proactively when the answer would benefit from them).

Both can live independently — a user who wants just the textual answer never has to invoke the retriever. A user who wants visuals invokes both in sequence (or the retriever picks up the previous answer in the conversation, exactly as Prompt B is designed to do).

## How

- Each skill is its own folder under `skills/`, with its own `SKILL.md` and (Phase 5) `evals/`.
- The `description` field on `doview-outcomes-answer`'s frontmatter focuses on triggering — outcomes-theory questions, "from a DoView perspective", "analyse this proposal/document using outcomes theory", etc.
- The `description` field on `doview-image-retriever` focuses on its sequencing role — runs after `doview-outcomes-answer`, retrieves and faithfully reproduces relevant Mermaid blocks from this repo's chapter `tool.md` files (with doviewplanning.org image URLs as fallback per the upstream prompt).
- Files this decision touches: the two new skill folders, and the marketplace.json entries (ADR-011).

## Rejected alternatives

### Merge into one skill that produces text + Mermaid inline

Conceptually appealing because Mermaid is text — there's no rendering bottleneck the way there is with PNG retrieval. Rejected because:

- **Prompt A's compliance check** is explicit: the response ends with the Image-retrieval seed list. Inlining the diagrams *within* Prompt A's response would violate the upstream structure and require rewriting Prompt A — which ADR-009 forbids.
- Splitting keeps the **two compliance contracts independent**. If Prompt A is updated upstream, we update one skill; same for Prompt B. Merging would make every upstream change a coordinated edit.
- A user who only wants the text answer (e.g. piping into a document) gets a clean response without inline `mermaid` blocks that they'd have to strip.

### One skill that calls the other as a sub-skill

Adds orchestration complexity for no real benefit. Claude Code's skill system supports the two-step pattern naturally — user invokes skill A, optionally invokes skill B, both have clear triggering signals.

### Drop Prompt B; only ship Prompt A

Rejected by user in Phase 1 clarification. Prompt B's "show me the diagrams" capability has standalone value, even if the medium has shifted from PNG to Mermaid.

### Keep PNG-retrieval semantics; don't extend to Mermaid

Faithful to upstream but ignores that this repo carries the Mermaid for every chapter. A user in this repo's context would rather see the Mermaid (which they can copy, edit, or render) than a PNG. The extension is captured in ADR-009 as the only structural change to either prompt.

## Dependencies

- Depends on ADR-009.
- Drives ADR-011, SPEC-010-A, SPEC-010-B.
