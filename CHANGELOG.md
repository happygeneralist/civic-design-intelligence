# Changelog

This changelog records repository-level changes.

Use entry-level changelogs inside individual notes for changes to specific evidence, needs, behaviours, pain points, insights or review notes.

## 2026-11-06

### Changed

- Reconciled PR #100's full scope: a public needs semantic contract, aligned agent/writing/quality/hierarchy/relationship/value guidance, current roadmap, documentation entry points, schema explanations and optional user-need template sections. The earlier four-file description no longer represented the change.
- Made stable, revisable candidate knowledge and human judgement the governing aim. Discovery has no fixed needs-per-source quota; meaningful constituent needs can coexist with broader parents, and contexts, tensions and many-to-many civic/capability/rights relationships remain inspectable.
- Distinguished the persisted canonical formulation, short mapping label, authentic language and revision-bound role-specific views. Separated need, pain, expected value, fulfilment conditions, indicators and realised value without requiring every candidate to complete every component.
- Made empirical, normative and legal bases explicit. Rights and civic obligations must not automatically be offset by an efficiency preference score.
- Reconciled documented need levels with the existing allowed values: solution requirements are separate responses, not a user-need level. No new mandatory research fields or object migration were introduced.
- Extended stable IDs to at least three numeric digits, supporting IDs beyond 999 without renumbering existing objects. Added declared human-review consistency checks and an advisory warning for direct evidence fit with no evidence basis.
- Added 16 deterministic regression tests and template validation to CI. The tests check structure and state consistency, not model reliability or research truth.

### Handover and boundaries

- Existing research objects, quotations, source links, evidence strength, confidence and review states remain unchanged. The 12 existing direct-fit/no-basis inconsistencies and the pre-existing cognitive-wording warning remain visible for source-aware review, not automatic correction.
- The operating audit records the inspected scope and limits; this is not a fresh semantic validation of every historical file or source.
- User-authorised cleanup and merge is distinct from research validation. AI Capability Layer owns the experimental skill and reusable reviewer capability. Its next skill alignment/release remains separate work, followed by pilot setup; this PR does not deploy a skill, implement the reviewer application or execute the 15-source pilot.
- Whole-repository and template checks, actual head revisions and merge outcomes are recorded in the PR rather than copied into object change logs.

## 2026-11-05

### Added

- Issue #97: four source records and eight captured evidence records from verified Bexley, Blackburn with Darwen, Blackpool and DfE originals, reusing existing Essex evidence.
- A provisional five-source SEND waiting/support/navigation research view, with claim-level reconciliation, positive cases, limits and an LLM intervention record. Existing research objects and maturity remain unchanged; human review is outstanding.

### Changed

- Clarified that evidence-grounded candidate user needs can support exploratory research, policy/service gap hypotheses and provisional solution assessment before human validation, with use-specific limits and checks.
- Added a provisional bronze/source, silver/evidence and gold/needs-intelligence description without changing object status, evidence-basis or review schemas.
- Replaced the outdated blanket deferral of source-inventory synchronisation with a bounded, deterministic source-manifest trial following the completed Essex and five-source research examples.
- Defined pilot #99 as the next evaluation step before scaling agent extraction or choosing a broad versus specialised skill architecture.

## 2026-07-04

### Changed

- Added lightweight issue-first workflow guidance to `AGENTS.md` and `CONTRIBUTING.md` for non-trivial scoped work, while keeping tiny obvious edits issue-optional.

## 2026-06-16

### Added

- Added a project-scoped Codex permission profile to support shared repository workflow, GitHub access and safer local automation.
- Added documentation for the companion public secondary-research source archive, `happygeneralist/civic-design-secondary-research`, including the first source example `SRC_001_ofsted_essex_area_send_inspection_jan_2026`.
- Added the first bounded primary-research safe-ingestion objects. These have since been reset to unsupported candidate objects pending public or explicitly authorised evidence.
- Added an MVP public roadmap and changelog page, linked from the public homepage footer, to communicate progress and next steps in chunks.

### Changed

- Updated secondary-research ingestion guidance to name the companion source archive, describe a public-source inspection-report example and define future cross-repository evidence-map checks as deferred workflow automation.
- Updated the roadmap and roadmap cursor to reflect the new companion secondary-research repository, the manual source-record/evidence-map workflow and the future possibility of cross-repository sync.
- Added naming-contract pointers to the Obsidian workflow and repository validation docs, and advanced the roadmap cursor toward bounded research ingestion.
- Updated template validation so template filenames and controlled-value option lists are handled as scaffolding, while real content notes still require selected values.
- Aligned recent PR follow-up metadata by reclassifying early user-need cleanup changes as material, narrowing `need_shape` to the MVP value and marking the completed user-need rename plan as historical.
- Renamed research study files and the `PP_001` pain point file to ID-prefixed readable filenames, and fixed a broken schema example wikilink.
- Renamed low-risk insight files to ID-prefixed readable filenames and updated the filename migration plan to remove completed insight migrations.
- Renamed the three pilot user need files to ID-prefixed `short_name` slugs and updated the user-need filename migration plan.
- Renamed evidence files to canonical ID-prefixed filenames and updated the filename migration plan accordingly.

### Notes

- The companion secondary-research repository is a source archive, not a competing intelligence repository.
- No research objects were changed, promoted, reviewed or validated by documenting the companion repository.
- Cross-repository sync was deferred until the manual source archive to source record to evidence map workflow had been tested; see the later dated entries for the current position.

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
- Replaced the legacy `Study_template.md` example that used a live source ID with a generic non-colliding study template.
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
