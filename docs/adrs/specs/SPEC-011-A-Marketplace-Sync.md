# SPEC-011-A — Marketplace sync workflow

**Implements:** [ADR-011 — Marketplace integration approach](../ADR-011-Marketplace-Integration.md)

Captures the workflow for keeping `cgbarlow/skills` in sync with skills authored in this repo.

## Source of truth

- **Editorial:** `cgbarlow/doview-book/skills/<name>/` is where the skill is authored, reviewed, and tested.
- **Published:** `cgbarlow/skills/skills/<name>/` is what end-users install via the marketplace. It must be a byte-identical copy of the editorial version at the time of publication.

## Publishing a skill (first time)

1. In `cgbarlow/skills`, create a branch `feature/add-<skill-name>`.
2. Copy `cgbarlow/doview-book/skills/<name>/` recursively into `cgbarlow/skills/skills/<name>/`.
3. Add a new plugin entry to `cgbarlow/skills/.claude-plugin/marketplace.json`:
   ```json
   {
     "name": "<skill-name>",
     "description": "<the skill's frontmatter description, condensed if needed>",
     "source": "./",
     "strict": false,
     "skills": ["./skills/<skill-name>"],
     "author": { "name": "Chris Barlow" },
     "license": "CC-BY-SA-4.0",
     "keywords": [ /* relevant tags */ ]
   }
   ```
4. Bump `metadata.version` in marketplace.json (semver patch for additions). Per the marketplace-version-sync rule, this is required for Cowork to detect the new plugin.
5. Update `cgbarlow/skills/README.md` to mention the new plugin in the skills table.
6. Open a PR in `cgbarlow/skills`; merge once tests pass.

## Updating a skill

1. Make the change in `cgbarlow/doview-book/skills/<name>/` first; merge to `main` (with whatever ADR/spec updates apply).
2. Copy the updated folder into `cgbarlow/skills/skills/<name>/`.
3. Bump `metadata.version` in `cgbarlow/skills/.claude-plugin/marketplace.json`.
4. PR in `cgbarlow/skills`.

## Verification

After merging a `cgbarlow/skills` PR:

- `diff -r cgbarlow/doview-book/skills/<name>/ cgbarlow/skills/skills/<name>/` is empty.
- `cgbarlow/skills/.claude-plugin/marketplace.json` is valid JSON and the new plugin entry is well-formed.
- `cgbarlow/skills/README.md` lists the plugin in its skills table.
- A fresh Claude Code install via the marketplace lists the plugin with the correct description.

## Out of scope

- Automated sync (CI that mirrors the folder on commit). The skill set is small and per-release synchronisation is cheap enough manually. Could be revisited if we end up with > 5 doview-book skills.

## Files this spec governs

- `cgbarlow/skills/.claude-plugin/marketplace.json`
- `cgbarlow/skills/skills/<name>/` (for each doview-book-authored skill)
- `cgbarlow/skills/README.md`
