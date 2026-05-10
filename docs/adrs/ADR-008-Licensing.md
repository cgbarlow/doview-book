# ADR-008 — Licensing: free use with attribution; mirror DoView trademark policy

## Status

Accepted — 2026-05-10

## Why

This repository contains a markdown adaptation of *DoView Planning and Practical Outcomes Theory Handbook (2025)* by Dr Paul W Duignan, plus diagrams converted to Mermaid and supporting tooling. The handbook itself is the primary source — we are not the copyright holder of its content.

We needed a license posture that:

- Honours Dr Duignan's stated terms on the source page ("Free to use, copy, share, and adapt for any purpose with attribution; DoView® is a registered trademark; trademark use must comply with the policy on doviewplanning.org/trademarkuse").
- Is consistent with the existing [cgbarlow/doview-skill](https://github.com/cgbarlow/doview-skill) repo, which uses the same wording. Two repos with the same author and same source content should not invent inconsistent licenses.
- Disclaims warranty for the conversion (Mermaid renderings, folder restructuring, eval-driven content selection — these are derived works that may have subtle errors the original PDFs don't).

## What

The repo's `LICENSE.md` says: *Free to use, copy, share, and adapt for any purpose (including commercial) with attribution.* Attribution requires (1) acknowledging use of DoView Planning, (2) citing Duignan, P. (2025) and DoViewPlanning.Org, and (3) linking back to https://www.doviewplanning.org. The DoView® trademark notice and policy link are reproduced. A no-warranty clause closes the file.

## How

- `LICENSE.md` lives at the repo root and is linked from `README.md` and `BUILD.md`.
- The same terms are reproduced on every output page where appropriate (handbook citation footers in each `.md` file already include the original copyright line — we don't strip those).
- Files this decision touches: `LICENSE.md`, `README.md` (link to license), `BUILD.md` (link to license).

## Rejected alternatives

### MIT / Apache-2.0 / BSD

Standard OSS licenses are designed for code, not for derivative works of someone else's book. Slapping MIT on a handbook adaptation would misrepresent the rights situation — Dr Duignan owns the underlying content, and we cannot grant MIT rights to it.

### CC-BY 4.0

Closer to right (attribution-only), but Dr Duignan's stated terms include an explicit trademark clause that CC-BY doesn't carry. Mirroring his exact wording is more honest than overlaying a Creative Commons label.

### "All rights reserved"

Wrong direction — Dr Duignan explicitly grants liberal use rights, and this repo is meant to make the handbook more accessible, not lock it down further.

### Dual-license: CC-BY for content, MIT for code (skill, scripts)

Defensible but adds confusion. The skill in `skills/pdf-to-mermaid-md/` is small enough that the same attribution-with-trademark license covers it without harm. If the skill ever grows into something with significant standalone value, this decision can be revisited.

## Dependencies

- —
