# ADR-001 — Enhanced ADR Format for this repo

## Status

Accepted — 2026-05-10

## Why

[cgbarlow/protocols](https://github.com/cgbarlow/protocols/blob/main/protocols.md) requires every architectural, technical, or significant design decision to be captured as an ADR following the "enhanced WH(Y) format". The canonical ADR-001 referenced by the protocol does not yet exist in `cgbarlow/protocols/adrs/`, so each project that adopts the protocol must bootstrap its own ADR-001 to define the format used locally.

Without a written format we'd end up with inconsistent ADRs across the repo and ambiguous status of past decisions. With one, ADRs become quick to write and quick to read — a one-page record of *why we did it this way and what we ruled out*.

## What

ADRs in this repo use the **WH(Y)** sections below, in this exact order:

1. **Status** — `Proposed` / `Accepted` / `Superseded by ADR-NNN` plus the date of the most recent transition.
2. **Why** — context: the problem, pressure, or constraint that prompted the decision. Plain prose. No bullet list of generic considerations — describe the actual situation.
3. **What** — the decision itself in one or two sentences. Imperative present tense ("Use Mermaid for diagrams", not "We should use Mermaid").
4. **How** — implementation consequences, follow-on steps, and any non-obvious downstream effects. Where useful, list the files this decision will touch.
5. **Rejected alternatives** — every option considered, plus the specific reason it lost. One sub-section per alternative. The rationale must be honest, not retrofitted.
6. **Dependencies** — other ADRs this depends on, supersedes, or is superseded by. Dash if none.

## How

- ADRs live in `docs/adrs/`, filename `ADR-NNN-Title-In-Title-Case.md`.
- ADRs are immutable once accepted. To change a decision, write a new ADR that supersedes the old one (update both `Status` lines).
- Implementation-focused ADRs have a corresponding `docs/adrs/specs/SPEC-NNN-X-Title.md` that captures the *how* in detail. Specs are living documents; ADRs stay stable.
- Decisions about content (e.g. what's in the markdown) are not ADRs — they're editorial choices. ADRs are for technical and architectural shape.
- Every PR that introduces a non-trivial decision must add or supersede an ADR. The PR description names the ADR.

## Rejected alternatives

### Nygard-style ADR (Status / Context / Decision / Consequences)

The classic Michael Nygard format is shorter but conflates "Why" and "How" into a single Consequences section. The WH(Y) split is more legible when scanning, especially when explicit "Rejected alternatives" are required by the protocol. Nygard format also doesn't enforce a Dependencies field, which we want for graph navigation between ADRs.

### MADR (Markdown ADR template)

MADR has more structure (Decision Drivers, Considered Options with detailed pros/cons, Decision Outcome, Confirmation, Pros and Cons of the Options). Useful at scale but overweight for a personal-use repo with one author. The protocol's Rejected Alternatives requirement gives us 80% of MADR's value with less ceremony.

### Free-form decision log entries

A single chronological `DECISIONS.md` file would be lower friction but loses the discoverability of named ADR files (you can grep for `ADR-004` and land on exactly the right page). The Dependencies field also gets unwieldy in a single-file log.

## Dependencies

—
