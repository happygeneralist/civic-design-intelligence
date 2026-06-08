# ID and link migration

This file defines the safe process for normalising IDs, filenames and internal links in the research repository.

## Purpose

IDs are not just labels. They appear in filenames, YAML frontmatter, wikilinks and relationship fields such as `source_study`, `related_evidence`, `related_needs`, `related_behaviours`, `related_pain_points` and `related_insights`.

Normalising IDs should therefore be treated as a migration, not a casual tidy-up.

## Core rule

Do not rename files or change IDs until the current links and references have been audited.

Use this sequence:

```text
audit -> proposed mapping -> review -> migration PR -> validation
```

## Canonical ID prefixes

Use these prefixes for structured entity notes.

| Object type | Prefix | Example |
|---|---|---|
| Research study | `RS_` | `RS_001` |
| Evidence | `EVID_` | `EVID_001` |
| User need | `UN_` | `UN_001` |
| Behaviour | `BEH_` | `BEH_001` |
| Pain point | `PP_` | `PP_001` |
| Insight | `INS_` | `INS_001` |
| Theme | `TH_` | `TH_001` |
| Persona | `PER_` | `PER_001` |
| Journey | `JNY_` | `JNY_001` |
| Opportunity | `OPP_` | `OPP_001` |
| Review note | `REV_` | `REV_001` |
| Claim | `CLM_` | `CLM_001` |

## What gets a canonical ID

Canonical IDs should be used for structured entity notes, such as evidence, user needs, behaviours, pain points and insights.

Indexes, dashboards, loose notes, anchor summaries and working notes do not need canonical IDs unless they become structured research objects.

## Audit requirements

Before migrating, create an audit table with:

```text
current_path
current_filename
frontmatter_type
frontmatter_id
expected_prefix
proposed_id
proposed_path
source_study
related_evidence
related_needs
related_behaviours
related_pain_points
related_insights
outbound_wikilinks
inbound_wikilinks
risk_level
notes
```

## Risk levels

Use these levels to decide how carefully to review the change.

### Low risk

Use for notes where:

- the current ID already matches the expected prefix
- the filename is consistent
- few or no other notes link to it
- no relationship fields need updating

### Medium risk

Use for notes where:

- the ID or filename needs normalising
- there are wikilinks to update
- relationship fields point to an old name
- aliases may be useful during transition

### High risk

Use for notes where:

- many notes link to it
- the object type is unclear
- multiple IDs or aliases appear to refer to the same item
- the note may be a duplicate
- the evidence source is ambiguous
- the change could affect validated or reviewed findings

## Proposed mapping file

Create a mapping file before making changes.

Suggested location:

```text
migration/id-normalisation-map.csv
```

Suggested columns:

```text
old_path,new_path,old_id,new_id,object_type,old_aliases,links_to_update,risk_level,notes
```

Example:

```csv
old_path,new_path,old_id,new_id,object_type,old_aliases,links_to_update,risk_level,notes
002_Evidence/Quote_001.md,002_Evidence/EVID_001.md,Quote_001,EVID_001,evidence,"Quote_001",true,medium,"Update links from [[Quote_001]] to [[EVID_001]]"
```

## Link update rules

When renaming an object, update:

- filename
- frontmatter `id`
- wikilinks in all Markdown files
- relationship fields such as `source_study` and `related_evidence`
- entry-level changelog if the change is material
- aliases where useful

## Aliases

Use aliases during migration when old names are likely to be searched or remembered.

Example:

```yaml
aliases:
  - Quote_001
  - Study_001
```

Aliases should support transition but not become a substitute for canonical IDs.

## Changelog guidance

ID-only migrations usually do not require detailed changelog entries inside every note if no research meaning changes.

Use entry-level changelogs when:

- the object type changes
- the note is split, merged or deprecated
- evidence links change meaningfully
- a source reference is corrected
- a validated or reviewed item is affected

Record the overall migration in `CHANGELOG.md`.

## Validation after migration

After migration, check for:

- duplicate IDs
- missing IDs on structured notes
- invalid ID prefixes
- broken wikilinks
- unresolved `source_study` references
- unresolved `related_*` references
- notes whose type and ID prefix do not match
- notes whose filename and ID do not match, where matching is expected

## What not to do

Do not blindly rename every file based on its folder.

Some files may be summaries, indexes, anchor notes, dashboards or working notes rather than structured entity notes.

Do not remove old aliases until the repository has stabilised after migration.

Do not change research claims while performing ID normalisation.
