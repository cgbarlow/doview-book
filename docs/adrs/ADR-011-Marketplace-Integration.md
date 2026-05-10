# ADR-011 — Marketplace integration approach

## Status

Accepted — 2026-05-10

## Why

The two new skills (`doview-outcomes-answer`, `doview-image-retriever`) need to be installable via the [cgbarlow-skills](https://github.com/cgbarlow/skills) Claude plugin marketplace, alongside the existing skills there (iris, math-coach, pdf-to-ebook, etc.). The marketplace supports two integration patterns:

1. **Local source** — the plugin entry has `source: "./"` and `skills: ["./skills/<name>"]`. The skill lives in the marketplace repo itself. This is how `iris`, `math-coach`, `pdf-to-ebook` etc. are wired.
2. **URL source** — the plugin entry has `source: { source: "url", url: "..." }` pointing at an external repo. The marketplace expects that external repo to follow a specific layout: a `.claude-plugin/marketplace.json` (or `plugin.json`) and a `skills/` directory at the repo root. This is how `six-animals` and `campaign-mode` are wired.

The doview-book repo currently has `skills/pdf-to-mermaid-md/` plus the two new skills, but **no `.claude-plugin/` config**. Adding one — to make doview-book eligible as a URL source — would change doview-book's primary purpose (it's the book, not a plugin home) and pull in marketplace concerns to a content-focused repo.

We need a decision on which pattern to use for the new skills.

## What

Use the **local source pattern**. Copy `skills/doview-outcomes-answer/` and `skills/doview-image-retriever/` into `cgbarlow/skills/skills/` and register them in the marketplace's `.claude-plugin/marketplace.json` with `source: "./"` and `skills: ["./skills/<name>"]`. The doview-book repo remains the *editorial* source of truth; the marketplace holds the *published* copy.

## How

- Each skill exists in two places: `cgbarlow/doview-book/skills/<name>/` (source of truth) and `cgbarlow/skills/skills/<name>/` (published copy). Both folders contain the same files.
- Updates flow editorially: edit in doview-book, then propagate to cgbarlow/skills as part of the same release cycle.
- The user's saved preference is to bump `cgbarlow/skills/.claude-plugin/marketplace.json` → `metadata.version` whenever a plugin in the marketplace gets a new version (Cowork uses the marketplace-declared version for update detection). We follow this.
- A short sync workflow is captured in [SPEC-011-A](specs/SPEC-011-A-Marketplace-Sync.md).
- Files this decision touches: `cgbarlow/skills/.claude-plugin/marketplace.json`, `cgbarlow/skills/skills/doview-outcomes-answer/`, `cgbarlow/skills/skills/doview-image-retriever/`, `cgbarlow/skills/README.md`.

## Rejected alternatives

### URL-source pointing at doview-book

Cleanest in theory — one canonical copy, no duplication. Rejected because:

- doview-book doesn't have `.claude-plugin/` config, and adding it would mix marketplace plumbing into a content repo. The repo's primary readers are people reading the handbook, not plugin maintainers.
- The URL-source pattern in the marketplace expects skills at `./skills/`. We could match that layout, but the doview-book repo already has other things at that path (the `pdf-to-mermaid-md` skill), and not every skill in `doview-book/skills/` is destined for the marketplace.
- Pinning a URL source to a tag means re-tagging doview-book whenever a skill changes, even for skill-only edits.

### Both: URL-source for production + a local mirror for development

Triples the surface area for no concrete benefit. The marketplace doesn't care where the canonical copy lives; the cgbarlow/skills copy *is* the marketplace's view of the skill.

### Move skills out of doview-book entirely; live only in cgbarlow/skills

Possible, but: the skills are *about the handbook*. Co-locating them in the book repo means a reader of the book can also see the skills built on it. They're documented in the book's BUILD.md/README. Removing them would weaken that link.

### Make doview-book itself a marketplace plugin (its own `.claude-plugin/`)

Out of scope for this work and weakens the editorial focus of the book repo. Could be reconsidered if the doview-book skills grow into a coherent suite worth advertising as a standalone product.

## Dependencies

- Depends on ADR-009, ADR-010.
