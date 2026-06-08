# ID normalisation audit

This file will be used to audit existing IDs, filenames and links before any migration is attempted.

No research notes should be renamed or edited until this audit has been reviewed.

## Audit scope

The audit should cover:

- research studies
- evidence notes
- user needs
- behaviours
- pain points
- insights
- themes
- personas
- journeys
- opportunities
- review notes
- relationship fields
- wikilinks

## Known issues to check

These are known or suspected from earlier repository inspection.

| Area | Issue | Risk | Action |
|---|---|---:|---|
| Research studies | Some study files may use filenames like `S001_survey.md` while IDs use `RS_001` | Medium | Confirm whether filename should change or alias is enough |
| Evidence | Some evidence notes may use names like `Quote_001` rather than `EVID_001` | Medium | Map evidence notes to canonical `EVID_` IDs |
| Source links | Some evidence may point to `[[Study_001]]` while the canonical study ID is `RS_001` | High | Resolve source references carefully before migration |
| User needs | Some notes already use `UN_001` format | Low | Check consistency and related evidence links |
| Anchor summaries | Some files may be LLM-generated summaries rather than canonical objects | Medium | Do not assign canonical IDs unless they become structured objects |
| Obsidian links | Wikilinks may use filenames rather than IDs | Medium | Update links only after mapping is reviewed |

## Audit table

Use this table for manual or automated audit results.

| Current path | Current filename | Type | Current ID | Expected prefix | Proposed ID | Proposed path | Source study | Related links | Wikilinks | Risk | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `001_Research_studies/S001_survey.md` | `S001_survey.md` | `research_study` | `RS_001` | `RS_` | TBD | TBD | n/a | TBD | TBD | Medium | Check filename and inbound links before renaming |
| `002_Evidence/Quote_001.md` | `Quote_001.md` | `evidence` | TBD | `EVID_` | TBD | TBD | TBD | TBD | TBD | Medium | Confirm current frontmatter ID and references |
| `003_User_needs/UN_001.md` | `UN_001.md` | `user_need` | `UN_001` | `UN_` | `UN_001` | likely unchanged | TBD | TBD | TBD | Low | Check related evidence links |

## Proposed mapping table

Use this table after the audit has been completed.

| Old path | New path | Old ID | New ID | Object type | Old aliases | Links to update | Risk | Notes |
|---|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Review questions

Before migration, answer:

- Are all structured entity notes identified?
- Are any notes duplicates?
- Are any notes working notes rather than canonical objects?
- Do any notes need aliases during transition?
- Are any source references ambiguous?
- Are any reviewed or validated notes affected?
- Can the migration be split into low-risk and high-risk batches?

## Migration decision

Do not proceed to migration until this section is completed.

```text
Audit reviewed by:
Review date:
Decision: proceed | revise audit | split migration | do not proceed
Notes:
```
