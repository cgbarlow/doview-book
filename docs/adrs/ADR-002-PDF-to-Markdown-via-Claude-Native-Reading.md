# ADR-002 — Convert handbook PDFs to Markdown via Claude-native PDF reading

## Status

Accepted — 2026-05-10

## Why

The DoView Planning handbook is published as a directory of paired PDFs (one "question" PDF and one "tool" PDF per chapter, ~219 PDFs in total). Each PDF carries meaning in two layers: prose and a visual model. To make the handbook searchable, version-controllable, and re-mixable, we need a Markdown copy that preserves both layers — text faithfully, and diagrams in a code-renderable form (see ADR-003 for the diagram choice).

We needed a conversion approach that:
- handles single-page PDFs containing both prose and a diagram;
- preserves the handbook's exact wording (a Duignan handbook is a primary source — paraphrase corrupts it);
- can run incrementally across hundreds of files and resume cleanly;
- doesn't require setting up a custom OCR/extraction toolchain we'd have to maintain.

## What

Use Claude's native PDF reading (the `Read` tool's PDF support, which returns both extracted text and a rendered page image) to convert each PDF in `docs/pdf/` into a corresponding Markdown file under `docs/md/`. The conversion is driven by a Claude Code skill (`skills/pdf-to-mermaid-md/`) that orchestrates discovery, pair detection, idempotency, and per-file output following a fixed Markdown template.

## How

- The skill reads each PDF once and produces one `.md` per `.pdf`, preserving the basename (see ADR-006).
- Where a PDF contains a diagram, the skill renders it as Mermaid (ADR-003) or, for matrices, as a Markdown table.
- Pairs (e.g. `a1question.pdf` + `a1tool.pdf`) are co-located in the same chapter folder and cross-linked at the top (ADR-005).
- Re-runs are idempotent — see ADR-007.
- Files this decision touches: `skills/pdf-to-mermaid-md/SKILL.md`, `skills/pdf-to-mermaid-md/references/mermaid_patterns.md`, every file under `docs/md/`.

The detailed workflow is captured in [SPEC-002-A](specs/SPEC-002-A-pdf-to-mermaid-md-Workflow.md).

## Rejected alternatives

### `pdfplumber` / `PyMuPDF` Python pipeline

A standalone Python pipeline using `pdfplumber` or `PyMuPDF` would be reproducible and CI-able without an LLM in the loop. We rejected it because:
- Diagram-to-Mermaid translation requires *understanding* the visual, which is an LLM task. A Python pipeline would have to either skip diagrams (losing the model layer) or invoke an LLM anyway, at which point the orchestration value of pure-Python collapses.
- The handbook's prose is already cleanly extractable; the hard part is the visual interpretation, which Claude does natively in a single round-trip.
- One-time conversion of a fixed corpus doesn't justify a separate code surface to maintain.

### `marker` or `unstructured` (ML PDF extractors)

Tools like `marker-pdf` or `unstructured.io` produce decent Markdown from PDFs and handle layout. Rejected because they would still emit images for the diagrams (we'd need a second pass to translate to Mermaid), and they're overkill for single-page PDFs with mostly clean text. Adding them as dependencies for ~219 small PDFs is a poor trade.

### OCR (Tesseract/ocrmypdf)

OCR is for scanned/image PDFs. The handbook PDFs have a real text layer, so OCR would degrade quality.

### Manual transcription

Faithful but unrealistic at scale and prone to drift.

## Dependencies

- Depends on ADR-001 (format).
- Followed by ADR-003 (diagram strategy), ADR-004 (folder structure), ADR-005 (pair handling), ADR-006 (filename convention), ADR-007 (idempotency).
