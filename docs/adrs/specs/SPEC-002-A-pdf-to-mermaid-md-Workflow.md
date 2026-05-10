# SPEC-002-A — `pdf-to-mermaid-md` skill workflow

**Implements:** [ADR-002 — Convert handbook PDFs to Markdown via Claude-native PDF reading](../ADR-002-PDF-to-Markdown-via-Claude-Native-Reading.md)

This spec captures the operational behaviour of the `pdf-to-mermaid-md` skill (`skills/pdf-to-mermaid-md/SKILL.md`). The skill itself is the canonical living document; this spec keeps a stable summary for cross-reference from ADRs and provides an at-a-glance overview without opening the SKILL.md file.

## Inputs and outputs

- **Input directory** — default `docs/pdf/`. Override allowed.
- **Output directory** — default `docs/md/`. Created if missing.
- **Pair detection** — group files by base prefix (everything before the trailing `question`/`tool`). Examples:
  - `a1question.pdf` + `a1tool.pdf` → pair `a1`.
  - `g2aquestion.pdf` + `g2atool.pdf` → pair `g2a` (the trailing letter is part of the prefix).
  - `conclusion.pdf` → standalone (no partner).

## Workflow

1. **Discover and pair.** List the input directory. Build a list of `(pdf_path, output_md_path, partner_md_or_null)` tuples. Filter out entries whose `output_md_path` already exists (per ADR-007).
2. **Per-PDF conversion.** For each remaining PDF:
   1. Read the PDF with the `Read` tool (Claude returns extracted text and rendered page image).
   2. Identify: title (often a question for `*question.pdf`, `DoView Tool [code] - [title]` for `*tool.pdf`), body prose, diagram regions, source/footer.
   3. Write the Markdown file using the [template](#markdown-output-template).
3. **Report.** Print `Converted: N · Skipped: M · Failed: K` plus failure filenames if any.

## Markdown output template

```markdown
---
source_pdf: docs/pdf/<basename>.pdf
pair: <prefix>           # omit for standalone files
kind: question | tool | standalone
---

# <Title from the PDF>

> **Pair:** <Question (this page) · [Tool](xxtool.md)>   <!-- omit for standalone; format per ADR-005 -->

<body prose, faithful to the PDF>

## Diagram                                                  <!-- only if a diagram exists -->

```mermaid
<mermaid code>
```

<any prose annotations that belong with the diagram>

---

*Source: <footer text from the PDF>*
```

## Diagram conversion rules

See [SPEC-003-A](SPEC-003-A-Mermaid-Pattern-Playbook.md) for the archetype playbook. Quick rules:

- Cyclic flow → `flowchart LR`.
- Hierarchy / linear progression → `flowchart TD`.
- Comparison matrix → Markdown table (not Mermaid).
- Two-column before/after → `flowchart LR` with `subgraph` per column.
- Visual that translates to neither → describe in prose under `## Diagram` and note it.

## Faithfulness rules

- Preserve paragraph breaks. Fix obvious OCR-like artefacts (split words across line wraps) but do not paraphrase.
- Do not add commentary or summaries.
- Do not bold or italicise inside paragraphs unless the source visibly emphasises.
- Strip `DoView Tool XX —` from titles when generating chapter folder names (per ADR-004), but keep it in the file's H1 because that's how the source labels the page.

## Idempotency

Per ADR-007: if the target `.md` exists, skip silently. Re-conversion requires deleting the existing file first. No flag.

## Edge cases

- **Standalone PDFs** (e.g. `conclusion.pdf`): omit pair line, `kind: standalone`.
- **PDFs with only a diagram, no prose**: title + `## Diagram` + footer. No body section.
- **PDFs with only prose, no diagram**: title + body. Omit `## Diagram`.

## Acceptance tests

- Running the skill on `docs/pdf/` produces 219 files under `docs/md/` (218 pairs + 1 standalone).
- Running it again converts 0 files and skips 219.
- Deleting one `.md` and re-running converts exactly that one.
- A spot-check on three sample chapters (a1, b1, c4) confirms: title preserved, prose faithful, Mermaid renders, pair links resolve, footer present.

## Files this spec governs

- `skills/pdf-to-mermaid-md/SKILL.md`
- `skills/pdf-to-mermaid-md/references/mermaid_patterns.md`
