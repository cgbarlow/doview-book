# ADR-005 — Cross-link question/tool pairs in the same folder; do not merge

## Status

Accepted — 2026-05-10

## Why

The handbook publishes each chapter as a *pair* of PDFs — one "question" PDF (a question framed in the user's language plus a few paragraphs of explanatory prose) and one "tool" PDF (the visual model and its tabular accompaniments). The pair carries meaning together: the question motivates the tool, and the tool answers the question.

When converting to Markdown we had to decide:

- Are these one Markdown file or two?
- If two, how do they signal they belong together?
- What about the existing inline cross-references (each chapter file references its partner)?

## What

Keep the pair as **two separate Markdown files** sharing a chapter folder. At the top of each file, immediately after the H1, render a **Pair line** linking to the partner file. The current page is shown in plain text (not a link); the partner is shown as a Markdown link.

Format:

```markdown
> **Pair:** Question (this page) · [Tool](xxtool.md)
```

```markdown
> **Pair:** [Question](xxquestion.md) · Tool (this page)
```

## How

- Both files of a pair live in the same chapter folder (ADR-004), so the cross-link can be a bare relative filename.
- The Pair line goes **after** the H1 and **before** the body prose. It uses Markdown blockquote syntax for visual separation.
- The current page uses plain text so the reader can see at a glance which side they're on without needing to look at the URL bar.
- Standalone files (introduction, conclusion) omit the Pair line.
- Files this decision touches: every chapter `.md` file under `docs/md/Part X - …/XX - …/`.

## Rejected alternatives

### Merge each pair into one file (`a1.md` containing both)

Cleaner file tree (109 files instead of 218). Rejected because:
- Every cross-reference in the source PDFs is to a specific side of the pair ("see the question for context", "see the tool"), and merging would require rewriting those references or leaving them ambiguous.
- The question and tool have different reading affordances: a reader skimming the book may want to land on tools to scan models, or on questions to read prose. Two files honour that distinction.
- The user explicitly chose this option during initial setup.

### Two files, no cross-link

Lowest friction but a reader landing on the question file has no in-document way to reach the matching tool. Rejected because the Pair line costs almost nothing and is visibly the *only* navigation a reader needs at chapter level.

### Cross-link via frontmatter only (`pair: a1`)

The frontmatter's `pair` field is useful for tooling (search, group-by-pair queries), but it's invisible in rendered Markdown. Rejected on its own; we keep the `pair: a1` frontmatter field *as well as* the visible Pair line — frontmatter is for tools, the line is for humans.

### Symbolic links between paired files

Filesystem-level link, transparent in tools that follow them, opaque in tools that don't. Rejected as fragile (Windows / web rendering breaks links) and surprising.

## Dependencies

- Depends on ADR-002, ADR-004, ADR-006.
