# SPEC-004-A — Restructure mapping (flat → Part/Chapter folders)

**Implements:** [ADR-004 — Folder structure under `docs/md/`](../ADR-004-Folder-Structure.md)

Captures the algorithm that mapped the initial flat output (`docs/md/<basename>.md` × 219) into the Part/Chapter folder structure now in place.

## Inputs

- `docs/md/*.md` (flat output produced by the `pdf-to-mermaid-md` skill).
- A Part-letter → Part-title mapping (sourced from doviewplanning.org/bookai):

  | Letter | Part title |
  |---|---|
  | A | DoView Planning Fundamentals |
  | B | DoView Drawing and Strategy Principles |
  | C | Alignment and Prioritization |
  | D | Indicators and Frameworks |
  | E | Contracting and Delegation |
  | F | Performance Improvement |
  | G | Evaluation and Research |
  | H | Reporting |
  | I | Implementation and Integration |
  | J | AI Applications |

## Algorithm

For each `*tool.md` in `docs/md/`:

1. Extract the chapter code from the filename: `^([a-z]+\d+[a-z]?)tool\.md$` — produces `a1`, `g2a`, etc.
2. Read the file's H1 and strip the `DoView Tool XX —` prefix to derive the chapter title.
3. Sanitise the title for filesystem use: `/` → ` or `, `:` → ` -`, drop `?`, etc.
4. Compute the destination: `docs/md/Part <CODE-LETTER-UPPER> - <Part Title>/<CODE-UPPER> - <Chapter Title>/`.
5. Move both `<code>question.md` and `<code>tool.md` into the destination folder.

Standalone files (e.g. `conclusion.md`, `1 - introduction.md`, `2 - conclusion.md`) stay at `docs/md/`.

## Reference implementation

The original implementation script is preserved as `restructure.py` in the repo root. It is one-shot: running it against an already-restructured tree is a no-op (because the flat-name patterns no longer match anything at the top level).

## Idempotency

The restructure is idempotent in practice — once moved, files don't get moved again. But it's not designed to be re-run as part of a pipeline; if the conversion is regenerated from scratch, run the conversion to a fresh empty `docs/md/`, then restructure once.

## Acceptance tests

- After the run, `docs/md/` has exactly 10 Part folders, 109 chapter folders, and 3 root files (`1 - introduction.md`, `2 - conclusion.md`, plus any standalone original).
- All 219 chapter `.md` files are present and reachable under their part folder.
- Cross-link `[Tool](xxtool.md)` and `[Question](xxquestion.md)` lines inside the files still resolve (siblings in the same folder).
- The introduction's TOC (`1 - introduction.md`) links to each Part folder name and resolves on GitHub web UI.

## Files this spec governs

- The folder layout under `docs/md/`.
- `restructure.py` (the as-built script, retained for posterity, can be removed once stability is proven).
