# User need file renaming plan

Date: 2026-06-16

## Purpose

This plan describes how to rename early user need files so filenames align with the current repository convention:

```text
UN_###_need_to_action_object_context.md
```

The immediate focus is `UN_001` to `UN_004`, which were created before the current `short_name` convention was applied.

This is a planning document only. It does not rename files.

## Scope

In scope:

- propose target filenames for `UN_001` to `UN_004`
- identify likely backlink and wikilink updates
- define a safe migration sequence
- define checks before and after the rename PR

Out of scope:

- changing user need IDs
- changing canonical need meaning
- promoting review or validation status
- rewriting user needs beyond any already-reviewed frontmatter clean-up
- renaming later user needs outside `UN_001` to `UN_004`
- recreating Git history in Markdown

## Dependency

This plan assumes PR #28, `Clean up user needs 001 to 004`, is reviewed and merged first.

That PR adds or normalises `short_name` values for the first four user needs. The filenames below are based on those proposed `short_name` values.

If PR #28 changes before merge, update this plan before carrying out the rename.

## Proposed filename changes

| Current file | Proposed file | Basis |
|---|---|---|
| `003_User_needs/UN_001.md` | `003_User_needs/UN_001_need_to_identify_matching_options.md` | Proposed `short_name`: `Need to identify matching options` |
| `003_User_needs/UN_002.md` | `003_User_needs/UN_002_need_to_access_trusted_service_information.md` | Proposed `short_name`: `Need to access trusted service information` |
| `003_User_needs/UN_003.md` | `003_User_needs/UN_003_need_to_find_relevant_information_quickly.md` | Proposed `short_name`: `Need to find relevant information quickly` |
| `003_User_needs/UN_004.md` | `003_User_needs/UN_004_need_to_stay_connected_to_pathway.md` | Proposed `short_name`: `Need to stay connected to pathway` |

## Link impact found during planning

Repository search suggests the following files may contain wikilinks or references that need checking during the rename PR.

### `UN_001`

Likely references:

- `003_User_needs/UN_001.md`
- `007_Themes/TH_001.md`
- `docs/ID_and_link_migration.md`
- `docs/Repository_validation.md`
- `SCHEMA.md`
- `docs/LLM_intervention_logging.md`
- `002_Evidence/EVID_003_quote_003.md`
- `004_Behaviours/BEH_001.md`
- `docs/Change_events_structure.md`
- `migration/validation-baseline-report.md`
- `002_Evidence/EVID_002_quote_002.md`
- `CONTRIBUTING.md`
- `migration/id-normalisation-audit.md`
- `004_Behaviours/BEH_002.md`
- `002_Evidence/EVID_001_quote_001.md`

### `UN_002`

Likely references:

- `003_User_needs/UN_002.md`
- `003_User_needs/UN_012_need_to_plan_pathway_options_early.md`
- `migration/validation-baseline-report.md`
- `001_Research_studies/RS_007_pathway_planning_guidance_level_test.md`

### `UN_003`

Likely references:

- `003_User_needs/UN_003.md`
- `docs/Change_events_structure.md`
- `003_User_needs/UN_013_need_to_assess_realistic_options.md`
- `docs/User_need_persistence_and_deprecation.md`
- `docs/Evidence_standards.md`
- `migration/validation-baseline-report.md`

### `UN_004`

Likely references:

- `003_User_needs/UN_004.md`
- `007_Themes/TH_001.md`
- `003_User_needs/UN_014_need_to_identify_fallback_routes.md`
- `migration/validation-baseline-report.md`
- `SCHEMA.md`

Not all search hits necessarily require updates. Some may be historical examples, migration reports or schema documentation. The rename PR should inspect each hit and only update live links where doing so improves navigation without rewriting historical audit material.

## Migration approach

Use a dedicated rename PR after PR #28 is merged.

Recommended sequence:

1. Create a branch from current `main` after PR #28 is merged.
2. Rename one file at a time using Git so history is preserved as a rename where possible.
3. Update live wikilinks from `[[UN_###]]` or old path references to the new note names where needed.
4. Preserve stable IDs in frontmatter.
5. Do not change `need`, `short_name`, evidence links, maturity, review status or confidence unless explicitly required by review.
6. Run the repository validation script if available.
7. Review Obsidian graph/navigation manually if possible.
8. Open a small PR containing only the renames and required link updates.

## Link update rules

Use these rules during the rename PR:

- Preserve `id: UN_###` exactly.
- Prefer updating active wikilinks to the renamed note where the link is intended to navigate to the note.
- Do not rewrite historical migration reports unless they are used as active navigation documents.
- Do not update examples in schema or documentation if the old ID-only form is intentionally demonstrating stable IDs.
- Do not introduce aliases unless there is a clear Obsidian navigation need.
- If aliases are added, use them only to preserve navigation from existing ID-only links, for example:

```yaml
aliases:
  - UN_001
```

Aliases should be considered optional. The preferred repository convention is still stable IDs in frontmatter and meaningful filenames.

## Proposed rename PR acceptance criteria

- `UN_001` to `UN_004` have meaningful filenames based on their `short_name` values.
- Frontmatter `id` values remain unchanged.
- No user need wording is materially changed.
- No item is promoted to reviewed or validated.
- Live wikilinks continue to resolve.
- Repository validation passes, or any known validation warnings are documented in the PR.
- PR summary lists renamed files and updated references.

## Review risks

- Some references may be historical and should not be updated automatically.
- Some Obsidian links may rely on ID-only note names. If that proves true, aliases may be needed.
- PR #28 may change the proposed `short_name` values before merge, which would change the target filenames.
- GitHub web edits may not always show file renames as cleanly as local `git mv`; if preserving rename detection matters, perform the rename locally.

## Recommendation

Do not perform the rename until PR #28 is merged.

After that, use one focused rename PR for `UN_001` to `UN_004`. Keep it administrative: filenames and necessary link updates only.
