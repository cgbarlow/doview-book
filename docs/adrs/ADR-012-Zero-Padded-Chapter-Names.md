# ADR-012 — Zero-padded chapter folder and file names (Xnn format)

## Status

Accepted — 2026-05-10

Supersedes [ADR-006 — Preserve original filenames inside chapter folders](ADR-006-Preserve-Original-Filenames.md).

## Why

After ADR-006 settled on preserving the as-published chapter prefixes (`a1`, `b25`, `g2a`, …) for `docs/md/` filenames — keeping a 1:1 mapping with `docs/pdf/` — readers and downstream tools kept running into the **lexicographic sort** problem:

- A flat `ls` of Part B's chapters returns `B1, B10, B11, B12, …, B19, B2, B20, B21, …` — alphabetical, not numerical.
- Any GitHub folder view, IDE tree view, or shell glob walks the chapters in the wrong order.
- Anyone reading the book by clicking through the chapter folders has to mentally re-sort.

The Part-folder READMEs added in Phase 1.5 mitigated this by re-sorting numerically in code, but that's per-view rather than at the source. Zero-padding the chapter ordinals (`A01`, `B25`, `G02A`) makes lexicographic sort agree with numerical sort everywhere, by construction — no helper sort code required.

The trade-off is the 1:1 mapping with `docs/pdf/` (which keeps the as-published `a1question.pdf` filenames): we lose the property that `diff -q docs/md/.../a1question.md docs/pdf/a1question.pdf` correspond by filename. The source PDFs cannot reasonably be renamed (they're the published artefacts; changing their basenames would invalidate external citations and confuse anyone bouncing between this repo and DoViewPlanning.Org).

## What

Chapter folder names and the Markdown filenames inside them are zero-padded to **Xnn** format (letter prefix + two digits, with optional uppercase subletter for cases like `G2A`):

- Folders: `A01`, `B01`, `B25`, `C01`, `G01`, `G02`, `G02A`, `G25`, …
- Files: `a01question.md`, `a01tool.md`, `b25question.md`, `g02aquestion.md`, `g02atool.md`, …

`docs/pdf/` filenames remain unchanged (`a1question.pdf`, `g2aquestion.pdf`). The mapping between the two is now lookup-by-frontmatter (`source_pdf:` field in each `.md`) rather than filename-equality.

## How

- Cross-links inside chapter files use the new padded filenames (`[Tool](a01tool.md)`).
- The `pair:` frontmatter field uses the padded code (`pair: a01`).
- The `source_pdf:` frontmatter field continues to point at the un-padded source filename (`docs/pdf/a1question.pdf`), so the audit trail back to the original publication is preserved.
- Part-folder READMEs (`docs/md/Part X - …/README.md`) link to padded folder and file paths.
- A one-shot helper at `tools/zero_pad_chapter_names.py` performed the conversion; `tools/generate_part_readmes.py` regenerates the Part READMEs from the new tree.
- Files this decision touches: every folder and `.md` file under `docs/md/Part X - …/`, plus the 10 Part READMEs.

## Rejected alternatives

### Stay with `A1, B25, G2A` (the ADR-006 status quo)

The 1:1 mapping with `docs/pdf/` is a real audit-trail benefit, but the readability cost compounded as more views and tools were added (Part READMEs needed custom sort; any future "list all chapters" view would need the same). Zero-padding is paid once and harvests everywhere.

### Pad to three digits (`A001, B025`)

Overkill — no Part has more than 25 chapters in the published edition, and three-digit padding signals "this corpus has hundreds of items per part" which it doesn't. Two digits matches the actual range.

### Rename PDFs too (full consistency)

Considered and rejected by the user in the scope question. The PDFs are the as-published artefacts; renaming them would silently break external references to `doviewplanning.org/a1doviewtool` etc. (those tool page URLs use the un-padded form). Keeping PDFs un-padded preserves the link back to the canonical publication.

### Different padding for the G2A case (`G02-A`, `G2A → G2_A`, etc.)

Considered `G02-A` (clearer separation) but it breaks `[A-Z]+\d+[A-Z]*` style code parsers and looks odd alongside `G02`. Considered lowercase `G02a` and rejected as inconsistent with the rest of the codes which use uppercase letters. `G02A` keeps the existing case scheme and parses cleanly.

## Dependencies

- Supersedes ADR-006.
- Depends on ADR-004 (folder structure), ADR-005 (cross-linked pairs).
