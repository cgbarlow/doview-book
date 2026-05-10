# Plan: Faithfully adapt the doviewplanning.org/bookai prompts as Claude Code skills, backfill ADRs, and publish via cgbarlow/skills marketplace

## Context

**What we're doing.** Two prompts are published at https://www.doviewplanning.org/bookai for AI systems to use when answering questions about Dr Paul Duignan's outcomes theory and the DoView Planning handbook:

- **Prompt A — Outcomes Theory Text Response Prompt (v1.1.9)** — answers user questions strictly from the handbook with a defined Summary + Full structure, strict URL/style rules, and an image-retrieval seed list.
- **Prompt B — Outcomes Theory Book Image Retriever Prompt (v1.1.9)** — runs after Prompt A to retrieve and faithfully embed relevant images from the handbook.

The verbatim text of both prompts is captured at `/tmp/bookai_text.txt` lines 103–480.

We will:

1. **Faithfully adapt** these into two Claude Code skills (verbatim prompt text preserved, version numbers preserved, only minimal edits for skill-frontmatter integration).
2. **Add them to the doview-book repo** under `skills/` (alongside the existing `pdf-to-mermaid-md` skill).
3. **Publish them via the cgbarlow/skills marketplace.**
4. **Backfill ADRs** for design decisions made earlier in the doview-book repo (markdown conversion, mermaid choice, folder structure, etc.) AND record new decisions for the skill work.
5. **Follow `cgbarlow/protocols`** throughout: ADRs, specs, feature branches, CHANGELOG, releases, README accuracy, DRY.
6. **Open one GitHub issue per phase** on the doview-book repo (per the user's saved preference) and link them all to the master plan issue.

## Decisions and how they're captured

The protocol says ADRs follow the "enhanced WH(Y) format" defined in the (currently missing) ADR-001. We'll bootstrap by writing ADR-001 in the doview-book repo as the canonical format reference for this repo. Each ADR will use these sections:

- **Status** (Proposed / Accepted / Superseded)
- **Why** — context: the problem or pressure that prompted the decision
- **What** — the decision itself in one or two sentences
- **How** — implementation consequences and follow-on steps
- **Rejected alternatives** — each option considered, plus why it lost
- **Dependencies** — other ADRs this depends on or supersedes

Implementation-focused ADRs get a corresponding `SPEC-{ADR-number}-{letter}-{Title}.md`.

## ADRs to write

### Backfill — existing repo decisions

| # | Title | Spec? |
|---|---|---|
| 001 | Enhanced ADR format for this repo | — |
| 002 | Convert handbook PDFs to markdown via Claude-native PDF reading | SPEC-002-A — pdf-to-mermaid-md skill workflow |
| 003 | Render visual models as Mermaid; markdown tables for matrices | SPEC-003-A — mermaid pattern playbook |
| 004 | Folder structure: `Part X - <title>/XX - <chapter title>/` | SPEC-004-A — restructure mapping |
| 005 | Cross-link question/tool pairs in same folder; do not merge | — |
| 006 | Preserve original filenames (`xxquestion.md` / `xxtool.md`) | — |
| 007 | Idempotent conversion: skip if `.md` already exists | — |
| 008 | Licensing — free use with attribution; mirror DoView trademark policy | — |

### New — skill work decisions

| # | Title | Spec? |
|---|---|---|
| 009 | Faithful adaptation policy for external prompts (verbatim text + version preserved) | — |
| 010 | Two separate skills mirroring Prompt A and Prompt B (rather than one combined skill) | SPEC-010-A — skill A (`doview-outcomes-answer`); SPEC-010-B — skill B (`doview-image-retriever`) |
| 011 | Marketplace integration — copy skills into `cgbarlow/skills/skills/` and register as local plugins (URL-source pattern requires SKILL.md at repo root, which doview-book doesn't have) | SPEC-011-A — sync workflow between doview-book and cgbarlow/skills |

## Skills to build

### Skill 1: `doview-outcomes-answer` (Prompt A)

- **Path in doview-book**: `skills/doview-outcomes-answer/SKILL.md`
- **Frontmatter**: `name: doview-outcomes-answer`, `description:` covering "answer outcomes-theory questions strictly from Dr Paul Duignan's DoView Planning handbook" with explicit triggering language for user phrases like "from an outcomes theory perspective", "DoView analysis of", "what does outcomes theory say about…".
- **Body**: the verbatim Prompt A text (v1.1.9), wrapped only with skill-flavoured framing at the top (one short paragraph noting source and version) and a closing note about the Image-retrieval seed list pointing to the partner skill.
- **No paraphrasing.** The "STYLE RULES", "RAW VISIBLE URL RULE", "OUTCOMES SYSTEM DEFINITION RULE", "REQUIRED STRUCTURE", and "FINAL COMPLIANCE CHECK" sections stay byte-identical.

### Skill 2: `doview-image-retriever` (Prompt B)

- **Path in doview-book**: `skills/doview-image-retriever/SKILL.md`
- **Frontmatter**: `name: doview-image-retriever`, `description:` covering "after a doview-outcomes-answer response, retrieve and faithfully embed relevant images/diagrams from the DoView handbook" with triggering language like "show me the diagrams", "include the original images".
- **Body**: the verbatim Prompt B text (v1.1.9), with the same minimal framing approach as Skill 1.

## Locations and synchronisation

- **doview-book** is the source-of-truth for skill content (the user's stated home).
- **cgbarlow/skills** marketplace gets a copy under `skills/doview-outcomes-answer/` and `skills/doview-image-retriever/`, registered in `.claude-plugin/marketplace.json` as local plugins (`source: "./"`, `skills: ["./skills/<name>"]`).
- Per the user's saved memory: when these skills hit v1.0, bump the marketplace `metadata.version` to match (Cowork uses the marketplace-declared version for update detection).

## File layout (after this work)

```
doview-book/
├── .claude-plugin/
│   └── plugin.json                       # only if URL-source ever needed; out of scope here
├── docs/
│   ├── adrs/
│   │   ├── ADR-001-Enhanced-ADR-Format.md
│   │   ├── ADR-002-PDF-to-Markdown-via-Claude-Native-Reading.md
│   │   ├── ADR-003-Mermaid-for-Diagrams.md
│   │   ├── ADR-004-Folder-Structure.md
│   │   ├── ADR-005-Cross-Linked-Pairs.md
│   │   ├── ADR-006-Preserve-Original-Filenames.md
│   │   ├── ADR-007-Idempotent-Conversion.md
│   │   ├── ADR-008-Licensing.md
│   │   ├── ADR-009-Faithful-Prompt-Adaptation.md
│   │   ├── ADR-010-Two-Skills-Not-One.md
│   │   ├── ADR-011-Marketplace-Integration.md
│   │   └── specs/
│   │       ├── SPEC-002-A-pdf-to-mermaid-md-Workflow.md
│   │       ├── SPEC-003-A-Mermaid-Pattern-Playbook.md
│   │       ├── SPEC-004-A-Restructure-Mapping.md
│   │       ├── SPEC-010-A-Skill-doview-outcomes-answer.md
│   │       ├── SPEC-010-B-Skill-doview-image-retriever.md
│   │       └── SPEC-011-A-Marketplace-Sync.md
│   ├── md/                              # existing
│   ├── pdf/                             # existing
│   └── pptx/                            # existing
├── skills/
│   ├── pdf-to-mermaid-md/               # existing
│   ├── doview-outcomes-answer/          # NEW
│   │   └── SKILL.md
│   └── doview-image-retriever/          # NEW
│       └── SKILL.md
├── BUILD.md                             # NEW — current README content moved here (build/ADR/skill info)
├── CHANGELOG.md                         # NEW (Keep a Changelog format)
├── LICENSE.md                           # existing
└── README.md                            # REWRITTEN — friendly book front page with TOC for readers
```

## Phases (one GitHub issue per phase, per user preference)

Each phase: branch from `main`, work, open phase issue with description + acceptance criteria, post progress to that issue, PR back to `main`, merge.

### Phase 1 — Foundations, ADR backfill, and reader-friendly README
**Branch:** `feature/adrs-and-foundations`
**Tasks:**
- Create `docs/adrs/` and `docs/adrs/specs/` directories.
- Write ADR-001 through ADR-008 (backfill).
- Write SPEC-002-A, SPEC-003-A, SPEC-004-A (lifted/adapted from existing SKILL.md and references).
- Add `CHANGELOG.md` with `[Unreleased]` section listing the backfill.
- **README split** — the current `README.md` is technical (file structure, conversion process, how to view, attribution). Move it to `BUILD.md` (or similar) and replace `README.md` with a reader-friendly front page:
  - One-paragraph welcome introducing Dr Paul Duignan's *DoView Planning and Practical Outcomes Theory Handbook* and what's in this repo.
  - **Table of contents** with links to:
    - `docs/md/1 - introduction.md`
    - Each Part folder (`Part A` through `Part J`)
    - `docs/md/2 - conclusion.md`
  - "How to read" — short note that each chapter is a question/tool pair, kept in the same folder, cross-linked at the top.
  - Pointer to `BUILD.md` for anyone wanting to know how the markdown was generated, the bundled skill, or the ADRs.
  - Brief attribution + link to LICENSE.md.
- **Acceptance:** all ADR/spec files render cleanly; new README opens to TOC for a reader; BUILD.md preserves all current technical content; CHANGELOG follows Keep a Changelog format.

### Phase 2 — New ADRs and skill specs
**Branch:** `feature/skill-adrs`
**Tasks:**
- Write ADR-009 (faithfulness), ADR-010 (two skills), ADR-011 (marketplace integration).
- Write SPEC-010-A, SPEC-010-B (skill specs covering frontmatter description, body source mapping, eval prompts), SPEC-011-A.
- **Acceptance:** specs unambiguous enough for the implementation phases to be mechanical.

### Phase 3 — Build `doview-outcomes-answer`
**Branch:** `feature/skill-outcomes-answer`
**Tasks:**
- Create `skills/doview-outcomes-answer/SKILL.md` per SPEC-010-A. Body = verbatim Prompt A v1.1.9 with minimal framing.
- Add `evals/evals.json` with 3–4 realistic test prompts.
- Update CHANGELOG.
- **Acceptance:** SKILL.md frontmatter validates; verbatim text matches the source page; eval prompts are concrete and substantive.

### Phase 4 — Build `doview-image-retriever`
**Branch:** `feature/skill-image-retriever`
**Tasks:** As Phase 3, for Prompt B per SPEC-010-B.

### Phase 5 — Skill evaluation
**Branch:** `feature/skill-evals`
**Tasks:**
- Run skill-creator's eval loop on both skills (with-skill vs baseline; iterate up to 2 rounds). Skill-creator path: `/home/vscode/.claude/plugins/cache/claude-plugins-official/skill-creator/...`
- Save results under `skills/<name>/evals/`.
- Document outcomes in the phase issue.
- **Acceptance:** with-skill outcomes are demonstrably better than baseline on the assertions defined in `evals/evals.json`. No regressions in the existing skill (`pdf-to-mermaid-md`).

### Phase 6 — Publish to doview-book repo (release v1.1)
**Branch:** `feature/release-v1.1`
**Tasks:**
- Move `[Unreleased]` CHANGELOG entries to `[1.1.0]` heading.
- README updated to advertise the two new skills.
- Tag `v1.1.0` and create GitHub release with notes referencing all ADRs added in this work.
- **Acceptance:** release is live on GitHub; README accurately reflects all bundled skills.

### Phase 7 — Publish to cgbarlow/skills marketplace
**Branch in cgbarlow/skills:** `feature/add-doview-skills`
**Tasks:**
- Copy `skills/doview-outcomes-answer/` and `skills/doview-image-retriever/` into `cgbarlow/skills/skills/`.
- Add two plugin entries to `.claude-plugin/marketplace.json` (local source, with proper description, keywords, license).
- Bump `metadata.version` in marketplace.json (per user's saved memory about marketplace version sync).
- Update cgbarlow/skills README to list the new plugins.
- Open PR. Tag a marketplace release once merged.
- **Acceptance:** marketplace.json validates; plugin entries discoverable; metadata version bumped.

## Issue strategy on doview-book

- **Master plan issue** (created first): describes the goal, links to this plan file (or its committed form once Phase 1 lands), and lists the 7 phase issues as a checklist.
- **Per-phase issues** (created at the start of each phase per the user's saved preference): describe the phase's tasks, acceptance criteria, and link back to the master issue. Progress is posted as comments on the phase issue, not on the master.

## Critical files referenced or reused

- `/tmp/bookai_text.txt` lines 103–344 (Prompt A v1.1.9), 345–480 (Prompt B v1.1.9) — source for Phases 3 and 4.
- `/tmp/protocols.md` — protocol authority.
- `/workspaces/workspace-basic/doview-book/skills/pdf-to-mermaid-md/SKILL.md` — pattern for SKILL.md frontmatter & description style.
- `/workspaces/workspace-basic/skills/skills/iris/SKILL.md` and `math-coach/SKILL.md` — marketplace skill patterns.
- `cgbarlow/skills/.claude-plugin/marketplace.json` — Phase 7 target.
- Existing doview-book artefacts that ADRs/specs document retrospectively: `skills/pdf-to-mermaid-md/SKILL.md`, `skills/pdf-to-mermaid-md/references/mermaid_patterns.md`, `restructure.py` (history), `README.md`, `LICENSE.md`.

## Verification

- **Per phase:** push branch, open PR, run any tests defined in the spec, merge.
- **End to end:**
  1. Clone doview-book fresh, verify ADR index is browsable from README.
  2. Install cgbarlow-skills marketplace; verify both new plugins appear with correct descriptions.
  3. From a fresh Claude Code session: invoke a query that should trigger `doview-outcomes-answer` (e.g. "from an outcomes-theory perspective, why does this strategy doc lack a clear theory of change?") and confirm the response begins with the required preliminary sentence and contains the Summary + Full sections per Prompt A's compliance checklist.
  4. After (3), invoke `doview-image-retriever` and confirm it produces the required image-retrieval response format per Prompt B's checklist.
  5. CHANGELOG.md entries match the work performed; v1.1.0 release tag points to the merged main.

## Out of scope

- Hosting the skills as a separate URL-sourced repo (would require restructuring doview-book; not needed now).
- Implementing automation that keeps doview-book and cgbarlow/skills copies in sync (manual sync acknowledged in SPEC-011-A; user's saved memory covers the version-bump rule).
- Adding skill telemetry or trigger-rate optimisation (the description-optimization step is a follow-on; can be a v1.2.0).
