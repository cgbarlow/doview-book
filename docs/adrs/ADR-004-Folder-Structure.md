# ADR-004 — Folder structure under `docs/md/`

## Status

Accepted — 2026-05-10

## Why

The DoView Planning handbook is organised into 10 Parts (A through J), each containing 4–25 numbered chapters, plus an introduction and a conclusion. A flat list of 219 Markdown files (`a1question.md`, `a1tool.md`, …, `j7tool.md`) is greppable but unreadable: a reader can't see the book structure, and the tool's pair partner is visually buried among other unrelated files.

We need a layout that:
- mirrors the book's table of contents (Parts → Chapters → pair files) so a reader navigating the file tree sees the same structure they'd see flipping through the printed book;
- keeps each chapter's question/tool pair visibly co-located (depends on ADR-005);
- works both on the command line and in IDE tree views;
- doesn't break Markdown cross-links inside the files.

## What

`docs/md/` is laid out as `Part X - <Part Title>/<XX> - <Chapter Title>/{xxquestion.md, xxtool.md}`. The introduction and conclusion sit at the root of `docs/md/`. Part folder names use the Part letter capitalised; chapter folder names use the chapter code in caps followed by the chapter's full title (extracted from the chapter's `tool.md` H1).

## How

- Example: `docs/md/Part A - DoView Planning Fundamentals/A1 - The Five Steps in DoView Planning/a1question.md`.
- Standalone files (introduction, conclusion) live at `docs/md/`.
- Part titles come from doviewplanning.org/bookai. Chapter titles come from each chapter's tool.md H1 (stripping the `DoView Tool XX —` prefix).
- Filesystem-unsafe characters (`/`, `:`, `?`, `|`, `*`, `<`, `>`, `"`, `\`) in titles are sanitised — `/` becomes ` or `, `:` becomes ` -`, etc.
- The build script that performed this restructure is captured in [SPEC-004-A](specs/SPEC-004-A-Restructure-Mapping.md).
- Files this decision touches: every file under `docs/md/`, plus the `Pair:` cross-link line at the top of each chapter file (which expects siblings, not flat-namespace lookups).

## Rejected alternatives

### Flat — all 219 files in `docs/md/`

Lowest friction to implement. Rejected because the book structure is invisible; readers can't browse by Part; introducing chapter renames or insertions in the future is awkward.

### Two-level: `docs/md/<Part>/<file>`

E.g. `docs/md/A/a1question.md`, `docs/md/A/a1tool.md`. Better than flat but still doesn't surface chapter titles in the tree, and the question/tool pair shares a folder with every other chapter in the part — visual noise when a reader opens the Part folder.

### Three-level by file type: `docs/md/Part A/A1/question.md` and `tool.md`

We considered renaming the files to bare `question.md` / `tool.md`. Rejected because:
- Cross-links inside the files use the original filenames (`[Tool](a1tool.md)`); renaming would require rewriting every cross-link in 219 files.
- A bare `question.md` is meaningless when opened standalone (e.g. via "Open Recent" or a shared link).
- See ADR-006 for the filename decision.

### Merge each pair into one file: `docs/md/Part A/A1.md`

Cleaner tree but loses the question/tool separation that the source book uses to structure its content. Rejected by the user during initial discussion.

### Use numeric ordinals (`01-introduction.md`, `02-...`)

Numbering imposes a global order that the book doesn't really have at the chapter level. The book's Parts are ordered A–J; chapters are numbered within parts; the existing `Part X - …` and `XX - …` naming gives ordering naturally without inventing a new sequence.

## Dependencies

- Depends on ADR-002, ADR-005, ADR-006.
