# User need file renaming plan

Date: 2026-06-16

Status: completed by PR #30, `Rename user need files 001 to 004`.

## Purpose

This plan recorded how to rename early user need files so filenames align with the current repository convention:

```text
UN_###_need_to_action_object_context.md
```

The immediate focus was `UN_001` to `UN_004`, which were created before the current `short_name` convention was applied.

This document is now retained as a completed migration record. PR #30 performed the rename.

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

## Resolved dependency

This plan assumed PR #28, `Clean up user needs 001 to 004`, was reviewed and merged first.

That PR added or normalised `short_name` values for the first four user needs. The filenames below were based on those `short_name` values.

PR #28 merged before the rename PR.

## Completed filename changes

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
- removed source-specific research-study records

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

## Completed migration approach

PR #30 used a dedicated rename PR after PR #28 merged.

Completed sequence:

1. Created a branch from current `main` after PR #28 merged.
2. Renamed one file at a time using Git so history was preserved as a rename where possible.
3. Preserved stable IDs in frontmatter.
4. Added aliases for ID-only Obsidian navigation.
5. Did not change `need`, `short_name`, evidence links, maturity, review status or confidence.
6. Ran the repository validation script.
7. Opened a small PR containing only the renames and required aliases.

## Link update rules

These rules were used during the rename PR:

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

## Rename PR acceptance criteria

- `UN_001` to `UN_004` have meaningful filenames based on their `short_name` values.
- Frontmatter `id` values remain unchanged.
- No user need wording is materially changed.
- No item is promoted to reviewed or validated.
- Live wikilinks continue to resolve.
- Repository validation passes, or any known validation warnings are documented in the PR.
- PR summary lists renamed files and updated references.

## Review risks

- Some references may be historical and should not be updated automatically.
- Some Obsidian links may rely on ID-only note names, so aliases were added.
- GitHub web edits may not always show file renames as cleanly as local `git mv`; the completed PR used Git renames.

## Recommendation

No further action is required for this migration plan. Future work should use the naming and linking contract at creation time rather than repeating broad filename cleanups.
