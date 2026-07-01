# Naming and linking contract

This document defines the repository contract for filenames, IDs, aliases and internal links.

It exists to prevent repeated filename migrations and to keep the repository usable in Obsidian, machine-readable for future data layers, and safe for LLM-assisted handling.

## Operating principle

Use stable IDs for traceability. Use readable filenames for humans. Use frontmatter for data.

```text
stable ID + readable filename + queryable frontmatter + resolvable links
```

The repository must support four modes at the same time:

- Obsidian use, including graph, backlinks, aliases, Bases and search
- GitHub review, including readable diffs and clear PR scopes
- future database or API ingestion, where frontmatter is the source of structured data
- LLM and AI-assisted handling, where naming patterns reduce ambiguity and accidental rewrites

## Naming contract

Every structured knowledge object must have:

- one stable frontmatter `id`
- a filename that starts with the same ID
- a readable slug where the object has a stable short label
- frontmatter fields that carry the canonical meaning
- links that resolve by ID, filename or alias

Do not rely on filename wording as the canonical meaning of an object.

The canonical meaning belongs in frontmatter and body content, for example:

- `need` for user needs
- `short_name` for compact user-need labels
- `pain_point` for pain points
- `behaviour` for behaviours
- `title` for evidence, studies, insights and themes where applicable

## Filename pattern

Use this pattern for structured notes:

```text
<ID>_<readable_slug>.md
```

Examples:

```text
UN_001_need_to_identify_matching_options.md
EVID_000_public_source_extract.md
RS_000_public_source_record.md
BEH_001_parent_searches_for_guidance.md
PP_001_fragmented_university_send_information.md
INS_001_level_of_aspiration_changes_with_age.md
TH_001_pathway_planning_confidence.md
```

Bare ID filenames such as `UN_001.md` are valid only as temporary or transitional files. Prefer the readable filename once a stable `short_name` or title exists.

## Stable IDs

The ID must not change casually.

IDs are durable handles for:

- Obsidian links
- relationship fields
- generated views
- future data ingestion
- audit trails
- LLM lookup and retrieval

Use the existing prefix convention:

| Object type | Prefix | Example |
|---|---|---|
| Research study | `RS_` | `RS_001` |
| Evidence | `EVID_` | `EVID_001` |
| User need | `UN_` | `UN_001` |
| Behaviour | `BEH_` | `BEH_001` |
| Pain point | `PP_` | `PP_001` |
| Insight | `INS_` | `INS_001` |
| Theme | `TH_` | `TH_001` |
| Journey | `JNY_` | `JNY_001` |
| Opportunity | `OPP_` | `OPP_001` |
| Claim | `CLM_` | `CLM_001` |
| Value dimension | `VAL_` | `VAL_001` |

## Slug rules

Readable slugs should be short, stable and derived from the object’s compact label.

Use:

- lower case
- underscores between words
- plain ASCII characters
- meaningful action words
- no punctuation
- no apostrophes
- no dates unless the date is part of the object identity

Avoid:

- full sentences
- vague slugs such as `new_note`, `misc`, `draft`, `template`, `final`
- slugs based on temporary workshop wording
- slugs that overclaim review or validation
- slugs that change every time wording is refined

For user needs, derive the slug from `short_name`, not the full canonical `need` statement.

Example:

```yaml
id: UN_001
short_name: Need to identify matching options
need: A parent/carer needs to identify which pathway options match the young person's needs and aspirations, so they can help them decide their next steps.
```

Filename:

```text
UN_001_need_to_identify_matching_options.md
```

## Frontmatter is the data contract

Future API or database ingestion should read frontmatter, not infer meaning from filenames.

Filenames are for:

- human readability
- Obsidian navigation
- GitHub review
- search affordance
- LLM retrieval hints

Frontmatter is for:

- object type
- stable ID
- canonical wording
- short labels
- lifecycle state
- evidence maturity
- confidence
- review state
- relationships
- generated views
- future data ingestion

A filename may be useful, but it must never be the only place where meaning exists.

## Obsidian linking rules

Prefer links that remain readable and resilient.

Acceptable link styles:

```markdown
[[UN_001_need_to_identify_matching_options]]
[[UN_001_need_to_identify_matching_options|Need to identify matching options]]
[[UN_001]]
```

Use ID-only links where stability matters more than display wording. Use aliases to keep these links resolvable after filename migrations.

Use display text where the link appears in prose or user-facing synthesis.

Example:

```markdown
This relates to [[UN_001_need_to_identify_matching_options|Need to identify matching options]].
```

## Aliases

Use aliases to preserve navigation from old note names, ID-only links or recently migrated filenames.

Example:

```yaml
aliases:
  - UN_001
```

Aliases should support continuity. They should not become a substitute for a stable filename and frontmatter ID.

Keep aliases when:

- old ID-only links are likely to exist
- a file has recently been renamed
- Obsidian users may still search by the old name
- a migration has not yet updated all live links

Remove aliases only after the repository has stabilised and a link check shows they are no longer needed.

## Creation-time checklist

Before adding a new structured note, check:

- Does the file live in the correct numbered object folder?
- Does the filename begin with the frontmatter `id`?
- Does the ID prefix match the object type?
- Is the readable slug derived from the compact label, not an unstable sentence?
- For user needs, is `short_name` present once the need is stable enough to name?
- Are links written as wikilinks where Obsidian navigation is useful?
- Are relationship fields using resolvable links?
- Are lifecycle, evidence and review fields honest and conservative?
- If this is LLM-assisted, is `llm_generated` and `creation_mode` accurate?

## Rename checklist

Before renaming an existing structured note, check:

- Is the rename purely administrative, or does it change interpretation?
- Does the frontmatter `id` stay the same?
- Does the filename still begin with the same ID?
- Does the new slug come from a stable compact label?
- Should the old filename or ID be added to `aliases`?
- Are live wikilinks still resolvable?
- Are relationship fields still resolvable?
- Does the PR state that no research meaning changed?
- Does the PR avoid promoting review status, confidence or evidence strength?

Administrative filename migrations usually do not need object-level changelog entries if they do not change research meaning. Use the PR summary and Git history as the audit trail.

## LLM handling rules

When an LLM creates or edits repository objects, it must:

- inspect existing naming conventions before creating new files
- use the correct ID prefix for the object type
- make filenames begin with the frontmatter ID
- derive user-need slugs from `short_name`
- avoid inventing polished filenames that change the meaning of the object
- preserve aliases during migration unless explicitly told to remove them
- avoid broad link rewrites unless the task is specifically a link migration
- state whether a filename change is administrative or semantic
- avoid marking objects as reviewed or validated during naming work

If unsure, create the note in `000_Inbox/` or keep it as a draft/candidate rather than forcing it into a canonical structured object too early.

## PR expectations for naming work

A naming or linking PR should state:

- which files were renamed
- whether IDs changed
- whether canonical wording changed
- whether aliases were added or removed
- whether live links were updated
- whether any object-level meaning changed
- whether review state, confidence, evidence strength or lifecycle state changed
- what validation was run, or why it was not run

Naming-only PRs should be small and mechanical.

## What not to do

Do not:

- create structured notes with missing or mismatched IDs
- use filename wording as the only source of meaning
- rename files and rewrite object meaning in the same PR
- remove aliases during the same PR that introduces a rename
- use `title` as a substitute for `short_name` on user needs
- create filenames from vague cognitive verbs if the object has a more direct action label
- make LLM-assisted objects look human-reviewed
- force immature notes into canonical object folders when `000_Inbox/` is safer

## Current repository position

The recent migration work has moved the repository close to a stable naming baseline.

The remaining guardrail is procedural: all future structured notes should follow this contract at creation time, so the repository does not need repeated filename clean-up migrations.
