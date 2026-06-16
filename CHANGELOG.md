# Changelog

This changelog records repository-level changes.

Use entry-level changelogs inside individual notes for changes to specific evidence, needs, behaviours, pain points, insights or review notes.

## 2026-06-16

### Added

- Added a project-scoped Codex permission profile to support shared repository workflow, GitHub access and safer local automation.

### Changed

- Renamed low-risk insight files to ID-prefixed readable filenames and updated the filename migration plan to remove completed insight migrations.
- Renamed the three pilot user need files to ID-prefixed `short_name` slugs and updated the filename migration plan to remove completed user need migrations.
- Renamed evidence files to canonical ID-prefixed filenames and updated the filename migration plan to remove completed evidence migrations.

## 2026-06-15

### Added

- Added a shared `Bases/` folder with starter Obsidian Bases for user needs, evidence, review queue and LLM-assisted objects.
- Added `AGENTS.md` to define repository-specific Codex operating rules for branch use, changelogs, research safety and validation.
- Added `.github/pull_request_template.md` with the repository compliance and review checklist.
- Added `migration/filename-migration-plan.md` to map filename/frontmatter-ID mismatches before any rename migration.

### Changed

- Consolidated the root README guidance, removed the duplicate `Readme.md` entry and documented persona or segment models as deferred during the current MVP.
- Updated `.gitignore` to keep personal Obsidian workspace state, local plugin state, local-only notes and accidental untitled Bases out of shared history.
- Stopped tracking personal Obsidian workspace files and root-level untitled Base files while preserving them locally for individual contributors.
- Normalised research study and review note templates to include current lifecycle, review, evidence strength, confidence and change-level fields.
- Replaced the legacy `Study_template.md` example that used a live `RS_001` ID with a generic non-colliding study template.
- Clarified that filenames may either match the stable object ID exactly or use an ID-prefixed readable slug, and updated repository validation to match that convention.
- Added a `short_name` convention for user needs so Obsidian Bases, mapping and design artefacts can use compact `Need to + verb + object/context` labels while preserving the full canonical need.
- Piloted `short_name` on three pathway-planning user needs without changing canonical need wording, evidence links or review state.
- Updated `docs/Codex_repository_automation.md` to point Codex and similar agents to the required branch, pull request, changelog and validation workflow.

### Notes

- This includes Obsidian workflow, template, repository hygiene and Codex workflow governance changes.
- Shared Obsidian configuration remains tracked where it supports common repository behaviour.
- No existing research objects were semantically changed, promoted, validated, deprecated or marked as reviewed.
- Object-level changelog entries were not added because these changes do not affect the interpretation of existing research objects.

## 2026-06-09

### Added

- Added `docs/index.html` as a GOV.UK-style GitHub Pages overview for the civic design intelligence system.
- Added `scripts/build-stats.mjs` to generate repository object counts from numbered markdown object folders and available frontmatter.
- Added `.github/workflows/build-pages-stats.yml` to rebuild `docs/stats.json` on pushes to `main` and on manual workflow dispatch.
- Added `docs/Safe_research_ingestion_MVP.md` to define the minimum conventions for breaking a small SEND pathway-planning research sample into structured objects.
- Added `docs/Object_change_logs.md` to define when object-level changelogs are required and when Git and pull request summaries are enough.
- Added `Templates/Civic_need_template.md` so civic needs can be created as first-class analysis objects during the MVP.

### Changed

- Updated `README.md` to reference civic needs, the safe-ingestion MVP and the object changelog convention.
- Updated `CONTRIBUTING.md` to clarify safe ingestion, civic needs and object-level changelog rules.

### Notes

- This includes an administrative platform change for stakeholder visibility through GitHub Pages and generated repository statistics.
- Generated stats count missing metadata explicitly and do not infer review, validation, lifecycle state or evidence strength.
- No existing research objects were migrated or semantically changed.
- No existing object was promoted, validated, deprecated or marked as reviewed.
- Object-level changelog entries were not added because the change does not alter the interpretation of existing research objects.

## 2026-06-08

### Added

- Added repository documentation entry point in `README.md`.
- Added repository schema in `SCHEMA.md`.
- Added LLM operating rules in `llm-instructions.md`.
- Added practical governance rules in `GOVERNANCE.md`.
- Added contribution workflow in `CONTRIBUTING.md`.
- Added global changelog.
- Added supporting documentation for review process, Obsidian workflow, evidence standards and LLM safety model.

### Notes

- This is a documentation-only change.
- Existing research notes, evidence notes, insights and templates have not been migrated to the new schema yet.
- A follow-up migration should normalise IDs, statuses, evidence strength and review metadata across existing notes.
