# ADR-007 — Idempotent conversion: skip if `.md` already exists

## Status

Accepted — 2026-05-10

## Why

Converting 219 PDFs is non-trivial work — token-expensive (each PDF is read with vision) and slow enough that it had to be parallelised across multiple subagents. We needed re-run behaviour that was:

- Safe by default (a re-run shouldn't silently re-do completed work, wasting tokens and risking quality drift on already-good outputs).
- Resumable across sessions (if a run is interrupted, the next run continues where it stopped).
- Predictable (no flag combinations to remember).
- Reversible by the user, intentionally — re-conversion of a specific file should require an explicit action, not an accidental flag.

## What

The skill checks for the existence of the target `.md` file before processing each PDF. If the target exists, the skill **skips** that file silently and increments a "skipped" counter. To force re-conversion of any file, the user **deletes** the existing `.md` first. There is no `--force` or `--overwrite` flag.

## How

- The skill reports at the end: `Converted: N · Skipped: M · Failed: K`.
- Re-conversion is explicit and per-file: `rm docs/md/.../a1tool.md && rerun`.
- This makes parallel subagents safe — they can be assigned overlapping ranges with no risk of stepping on each other's outputs (later one sees the file exists and skips).
- Files this decision touches: `skills/pdf-to-mermaid-md/SKILL.md` (the rule is stated explicitly there).

## Rejected alternatives

### Default overwrite

Re-runs would re-do everything. Token-expensive and risks quality drift if the LLM produces a slightly different rendering on the second pass. Rejected.

### `--force` / `--overwrite` flag, default skip

Functionally identical to skip-default-no-flag for almost every workflow, but introduces a flag the user has to remember. The deletion-as-explicit-intent pattern is simpler and has zero ambiguity.

### Hash-based "re-convert if source PDF changed"

Tempting for a long-lived corpus that gets new editions. Rejected as overengineering for a one-time conversion of a static handbook (2025 edition). Can be revisited if the handbook gets updated annually.

### Append a counter on the new output (`a1tool.md`, `a1tool.1.md`, …)

Silent multiplication of files. Rejected as confusing for downstream consumers.

## Dependencies

- Depends on ADR-002.
