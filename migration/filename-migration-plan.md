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

Current result:

```text
Errors: 0
Warnings: 17
```

Warning groups:

- 1 unresolved documentation example link in `SCHEMA.md`
- 16 filename/frontmatter-ID mismatches

## Migration Principles

- Do not change frontmatter IDs.
- Do not change canonical research wording, evidence links, lifecycle state or review state.
- Prefer `ID_readable_slug.md` for Obsidian readability.
- For user needs, use the tested `short_name` as the filename slug source where available.
- Update wikilinks and relationship fields if any references use the old filename.
- Add aliases only where the old filename is likely to be searched or remembered.
- Record the migration in `CHANGELOG.md`.
- Do not add object-level changelog entries unless the migration changes research meaning, source references, validated/reviewed objects or relationship semantics.

## Proposed Rename Map

### User Needs

These should use the new `short_name` convention.

| Current path | ID | Proposed path | Risk | Notes |
|---|---|---|---|---|
| `003_User_needs/UN_002_begin_planning_before_choices_fixed.md` | `UN_012` | `003_User_needs/UN_012_need_to_plan_pathway_options_early.md` | Medium | Uses pilot `short_name`. Check links after rename. |
| `003_User_needs/UN_003_understand_realistic_options_for_child.md` | `UN_013` | `003_User_needs/UN_013_need_to_assess_realistic_options.md` | Medium | Uses pilot `short_name`. The old filename uses a cognitive verb; this is intentionally replaced by action-oriented wording. |
| `003_User_needs/UN_004_identify_viable_routes_if_grades_not_achieved.md` | `UN_014` | `003_User_needs/UN_014_need_to_identify_fallback_routes.md` | Medium | Uses pilot `short_name`. Check parent/child need links after rename. |

### Evidence

These are filename-only normalisations. Existing IDs already use `EVID_`.

| Current path | ID | Proposed path | Risk | Notes |
|---|---|---|---|---|
| `002_Evidence/Quote_001.md` | `EVID_001` | `002_Evidence/EVID_001_quote_001.md` | Medium | Consider alias `Quote_001` during transition. |
| `002_Evidence/Quote_002.md` | `EVID_002` | `002_Evidence/EVID_002_quote_002.md` | Medium | Consider alias `Quote_002` during transition. |
| `002_Evidence/Quote_003.md` | `EVID_003` | `002_Evidence/EVID_003_quote_003.md` | Medium | Consider alias `Quote_003` during transition. |
| `002_Evidence/EVID_DATA_001.md` | `EVID_004` | `002_Evidence/EVID_004_data_001.md` | Medium | Consider alias `EVID_DATA_001` during transition. |
| `002_Evidence/EVID_004_p3_parent_pathway_planning_need_signals.md` | `EVID_005` | `002_Evidence/EVID_005_p3_parent_pathway_planning_need_signals.md` | Medium | Important because many pathway-planning needs link to `EVID_005` by ID. Filename should catch up with the existing ID. |

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
| `005_Pain_point/Pain_point_template 1.md` | `PP_001` | `005_Pain_point/PP_001_pain_point_placeholder.md` | Medium | Filename suggests a template, but frontmatter says canonical `pain_point` with `PP_001`. Human review should confirm whether it is a real pain point or misplaced template before renaming. |

## Link Update Notes

Initial search found no current wikilinks to the listed filenames except documentation examples in `docs/ID_and_link_migration.md`.

The migration PR should still search for old basenames and update any new references before committing.

Recommended pre-migration check:

```bash
rg -n "\\[\\[(Quote_001|Quote_002|Quote_003|EVID_DATA_001|Pain_point_template 1|S001_survey|S002_parent_interviews|S003_case_studies|S004_professionals_interviews|S005_focus_groups|S006_in-school_workshops|S007_pathway_planning_guidance_level_test)"
```

## Proposed Migration Batches

### Batch 1: User need short-name filenames

- Rename `UN_012`, `UN_013` and `UN_014` files using pilot `short_name` slugs.
- Re-run validation and inspect Obsidian links.

### Batch 2: Evidence filenames

- Rename evidence notes to canonical `EVID_` filenames.
- Add aliases for old `Quote_*` and `EVID_DATA_001` names if useful.

### Batch 3: Research study filenames

- Rename `S001` to `S007` study filenames to `RS_001` to `RS_007`.
- Re-run link checks because studies are common source targets.

### Batch 4: Pain point decision

- Review `005_Pain_point/Pain_point_template 1.md`.
- Decide whether to rename it as `PP_001_pain_point_placeholder.md`, move it back to `Templates/`, or replace it with a properly named pain point.

## Human Review Questions

- Are the proposed user need filename slugs acceptable for Obsidian mapping?
- Should evidence quote files preserve old names as aliases?
- Should research study filename slugs stay short, or include fuller titles?
- Is `Pain_point_template 1.md` a real pain point or a misplaced template?
- Should the actual migration be one PR or several small PRs?

## Recommendation

Proceed with migration only after this plan is reviewed.

Preferred next step: a small migration PR for Batch 1, followed by validation and Obsidian link review.
