# ADR-006 — Preserve original filenames inside chapter folders

## Status

Superseded by [ADR-012](ADR-012-Zero-Padded-Chapter-Names.md) — 2026-05-10

(Originally accepted earlier on 2026-05-10. The 1:1 filename mapping between `docs/md/` and `docs/pdf/` is no longer maintained; see ADR-012 for the new rule and the trade-off.)

## Why

Once the chapter folder structure was in place (ADR-004), we had to choose what the two pair files inside each folder would be named. Two natural options:

- **Bare names** — `question.md` and `tool.md`, with the chapter context coming from the folder.
- **Prefixed names** — `a1question.md` and `a1tool.md`, the same names that live in `docs/pdf/`.

The choice has consequences for cross-link rewriting, file portability, and whether a file is meaningful when opened standalone.

## What

Inside each chapter folder, the pair files keep their **original prefixed names** (`a1question.md`, `a1tool.md`, `g2aquestion.md`, etc.) — a 1:1 mapping with `docs/pdf/`.

## How

- Each chapter folder contains exactly two files (or one for standalone chapters): `<code>question.md` and `<code>tool.md`, where `<code>` is the chapter prefix from the source PDF (lowercase letter + number, occasionally with a trailing letter like `g2a`).
- Cross-links inside files (`[Tool](a1tool.md)`) work as bare relative filenames because the partner is a sibling in the same folder.
- Files this decision touches: every file under `docs/md/Part X - …/XX - …/`. Already in place after the restructure.

## Rejected alternatives

### Rename to bare `question.md` / `tool.md`

Cleaner names, but:
- Every Pair-line cross-link in 219 files would need rewriting. Mass rewriting is risky on first restructure when the verification cost is highest.
- A bare `question.md` shared via "Open Recent" or copy-paste loses its chapter context — you'd have to look at the folder name to know which chapter you're reading. Prefixed names are self-identifying.
- The 1:1 with `docs/pdf/` (where source PDFs use the prefixed names) makes auditing easier — `diff -q` between the two trees has clean filename correspondence.

### Add an explicit chapter-code suffix to the folder + bare names inside

Hybrid: `Part A - …/A1 - …/question.md` plus the folder name carrying the code. Loses standalone identifiability of the file (same drawback as above) without much gain.

### Keep flat, no chapter folders, prefixed names only

Subsumed under ADR-004's "flat" rejection.

## Dependencies

- Depends on ADR-004, ADR-005.
