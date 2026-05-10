# SPEC-003-A — Mermaid pattern playbook

**Implements:** [ADR-003 — Render visual models as Mermaid; use Markdown tables for matrices](../ADR-003-Mermaid-for-Diagrams.md)

The canonical playbook is the file the skill actually consumes: `skills/pdf-to-mermaid-md/references/mermaid_patterns.md`. This spec is a stable summary for ADR cross-reference. When the playbook evolves, update both.

## Diagram archetypes

### 1. Cyclic step flow (A → B → C → … → A)

`flowchart LR` with arrows. Label each node with its letter and a short description.

### 2. Linear pipeline / progression

`flowchart TD` with stacked boxes. Side annotations like NOW/FUTURE go in prose under the diagram, not forced into Mermaid.

### 3. Comparison matrix (rows × columns)

**Markdown table**, not Mermaid. Use Mermaid only when the matrix has visual structure (linking arrows between cells, grouped subgraphs) that a table can't carry.

### 4. Drill-down / outcomes tree

`flowchart TD`. Keep node labels short; long descriptions go in prose afterwards.

### 5. Two-column comparison (NOW vs FUTURE, etc.)

`flowchart LR` with two `subgraph` blocks and a connecting arrow.

### 6. Process with feedback loop

`flowchart LR` with forward chain plus a labelled arrow looping back from a later step to an earlier one.

### 7. Single concept with annotations

Often clearer as prose plus a small radial diagram (`flowchart TD` with `core --- a`, `core --- b`, etc.).

## When NOT to use Mermaid

- Decorative visuals (logos, icons, stock photos).
- Diagrams whose layout carries meaning Mermaid can't reproduce (hand-drawn sketches with positional semantics).
- "Diagrams" that are really styled bullet lists — use a Markdown list.

For these cases: describe the visual in one sentence under `## Diagram` and add `_This page contains a visual that does not translate cleanly to Mermaid; described above._`

## Authoring rules

- **Quote node labels** with `"..."` whenever they contain spaces, punctuation, or parentheses.
- Use `flowchart` (not the older `graph`) — better layout and label support.
- Keep node labels short (one line of source text, max). Move the rest to prose.
- Don't try to pixel-match the source. Capture the *connections*, not the colours.

## Acceptance tests

- Each Mermaid block in `docs/md/` parses cleanly when opened in VS Code with `bierner.markdown-mermaid` or rendered on GitHub.
- For each archetype above, at least one chapter under `docs/md/` is a worked example. (Existing examples: A1 cyclic flow, B1 linear progression, A1 comparison matrix as table, J2 cyclic flow, G22 process with feedback loop.)

## Files this spec governs

- `skills/pdf-to-mermaid-md/references/mermaid_patterns.md` (the canonical, skill-consumed playbook).
