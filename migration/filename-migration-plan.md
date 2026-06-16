# Filename migration plan

This plan records the proposed filename-only migration for structured repository objects whose filenames do not begin with their canonical frontmatter IDs.

No research notes are renamed by this plan.

## Purpose

The repository now allows two filename patterns for structured objects:

```text
ID.md
ID_readable_slug.md
```

For user needs, the readable slug should normally derive from `short_name`. For other objects, the slug may derive from title, evidence source, behaviour, pain point, insight or study title.

The current validator reports filename warnings where the filename does not begin with the frontmatter `id`. This plan maps those warnings before any migration PR changes file paths.

## Validation Baseline

Command:

```bash
python3 tools/validate_repository.py
```

Pre-migration result:

```text
Errors: 0
Warnings: 9
```

Warning groups:

- 1 unresolved documentation example link in `SCHEMA.md`
- 8 filename/frontmatter-ID mismatches

The 2026-06-16 validation warning cleanup resolved these default validation
warnings by renaming the remaining study and pain point files and replacing the
broken `SCHEMA.md` example link with an existing user need ID.

## Migration Principles

- Do not change frontmatter IDs.
- Do not change canonical research wording, evidence links, lifecycle state or review state.
- Prefer `ID_readable_slug.md` for Obsidian readability.
- For user needs, use the tested `short_name` as the filename slug source where available.
- Update wikilinks and relationship fields if any references use the old filename.
- Add aliases only where the old filename is likely to be searched or remembered.
- Record the migration in `CHANGELOG.md`.
- Do not add object-level changelog entries unless the migration changes research meaning, source references, validated/reviewed objects or relationship semantics.

## Completed Rename Map

### Research Studies

| Current path | ID | Proposed path | Risk | Notes |
|---|---|---|---|---|
| `001_Research_studies/S001_survey.md` | `RS_001` | `001_Research_studies/RS_001_send_survey.md` | Medium | Replaces legacy `S001` prefix with canonical `RS_001`. |
| `001_Research_studies/S002_parent_interviews.md` | `RS_002` | `001_Research_studies/RS_002_parent_interviews.md` | Medium | Replaces legacy `S002` prefix with canonical `RS_002`. |
| `001_Research_studies/S003_case_studies.md` | `RS_003` | `001_Research_studies/RS_003_case_studies.md` | Medium | Replaces legacy `S003` prefix with canonical `RS_003`. |
| `001_Research_studies/S004_professionals_interviews.md` | `RS_004` | `001_Research_studies/RS_004_professionals_interviews.md` | Medium | Replaces legacy `S004` prefix with canonical `RS_004`. |
| `001_Research_studies/S005_focus_groups.md` | `RS_005` | `001_Research_studies/RS_005_focus_groups.md` | Medium | Replaces legacy `S005` prefix with canonical `RS_005`. |
| `001_Research_studies/S006_in-school_workshops.md` | `RS_006` | `001_Research_studies/RS_006_in_school_workshops.md` | Medium | Replaces legacy `S006` prefix with canonical `RS_006`; normalises hyphen to underscore in slug. |
| `001_Research_studies/S007_pathway_planning_guidance_level_test.md` | `RS_007` | `001_Research_studies/RS_007_pathway_planning_guidance_level_test.md` | Medium | Replaces legacy `S007` prefix with canonical `RS_007`. |

### Pain Point

| Current path | ID | Proposed path | Risk | Notes |
|---|---|---|---|---|
| `005_Pain_point/Pain_point_template 1.md` | `PP_001` | `005_Pain_point/PP_001_fragmented_university_send_information.md` | Medium | Filename suggested a template, but frontmatter and body describe a concrete pain point. Renamed without changing the pain point wording, status or review state. |

## Link Update Notes

Initial search found no current wikilinks to the listed filenames except documentation examples in `docs/ID_and_link_migration.md`.

The migration PR should still search for old basenames and update any new references before committing.

Recommended pre-migration check:

```bash
rg -n "\\[\\[(Pain_point_template 1|S001_survey|S002_parent_interviews|S003_case_studies|S004_professionals_interviews|S005_focus_groups|S006_in-school_workshops|S007_pathway_planning_guidance_level_test)"
```

## Completed Migration Batches

### Batch 1: Research study filenames

- Completed 2026-06-16.
- Renamed `S001` to `S007` study filenames to `RS_001` to `RS_007`.
- Re-ran link checks because studies are common source targets.

### Batch 2: Pain point decision

- Completed 2026-06-16.
- Reviewed `005_Pain_point/Pain_point_template 1.md`.
- Treated it as a real `PP_001` pain point because frontmatter and body contain a concrete pain point statement.
- Renamed it to `005_Pain_point/PP_001_fragmented_university_send_information.md`.

## Human Review Questions

- Should research study filename slugs stay short, or include fuller titles?
- Should the actual migration be one PR or several small PRs?

## Recommendation

No default-scope filename migration warnings remain after the 2026-06-16
validation warning cleanup. Future filename migrations should continue to use
small PRs with validation and Obsidian link review.
