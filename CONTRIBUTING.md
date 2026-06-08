# Contributing

This file explains how to add or update material in the research repository.

## Contribution principles

Contributions should be:

- evidence-led
- anonymised
- traceable
- clearly labelled by status
- linked to relevant notes
- reviewed before being treated as validated

## Before adding material

Check whether the repository already contains:

- a relevant research study
- similar evidence
- a related user need
- an existing behaviour, pain point or insight
- a relevant theme or journey stage

Prefer linking and extending existing notes where appropriate. Create new notes when the concept is genuinely distinct.

## File naming

Use stable IDs and readable filenames.

Recommended pattern:

```text
RS_001_send_survey.md
EVID_001_signposting_quote.md
UN_001_match_options_to_needs.md
BEH_001_discusses_pathway_options.md
PP_001_fragmented_information.md
INS_001_aspiration_changes_with_age.md
```

Avoid untitled files and temporary names in committed work.

## Creating a new note

1. Choose the correct object type.
2. Copy the relevant template from `Templates/`.
3. Assign the next stable ID.
4. Complete required metadata.
5. Add links to related evidence or source material.
6. Set the correct status and review status.
7. Add a changelog entry.

## Evidence notes

Evidence notes should preserve the meaning of the source material.

Do not rewrite participant quotes except to anonymise identifying details.

Every evidence note should include, where known:

- source study
- actor
- context
- journey stage
- evidence kind
- anonymisation status
- confidence
- tags

If the source is unclear, mark this explicitly rather than guessing.

## User needs

User needs should be framed from the actor's perspective and should describe an underlying need, not a solution.

Avoid writing user needs as:

- feature requests
- service requirements
- organisational goals
- policy objectives
- generic aspirations without context

A user need may be drafted from assumptions, but it must be labelled as an assumption until anchored to evidence and reviewed.

## Insights

Insights should explain why something is happening and why it matters.

A good insight should include:

- a clear claim
- linked evidence
- interpretation
- uncertainty or limitations
- implications for service design, policy or delivery
- emerging user needs or opportunity areas where relevant

## Status changes

Only a human reviewer may promote an item to `validated`.

Do not change status, confidence or evidence strength without updating the entry-level changelog.

## Changelog entries

Every meaningful note should include an entry-level changelog.

Use this format:

```markdown
## Changelog

- YYYY-MM-DD: Created as draft. Evidence strength: weak. Review status: not reviewed.
- YYYY-MM-DD: Linked to [[EVID_004]] and updated confidence from low to medium after review.
```

Repository-wide changes should also be recorded in `CHANGELOG.md`.

## Branch workflow

Use a branch for changes whenever possible.

Recommended branch names:

```text
docs/research-repo-governance
schema/normalise-status-fields
research/add-send-survey-evidence
insights/draft-pathway-planning-insights
review/validate-user-needs
```

## Pull request checklist

Before opening a pull request, check:

- [ ] No raw identifiable data has been added.
- [ ] Evidence is anonymised or anonymisation status is explicit.
- [ ] New notes use the schema.
- [ ] Assumptions are labelled.
- [ ] LLM-generated notes are marked.
- [ ] Material changes have changelog entries.
- [ ] Validated content has not been changed without review.
- [ ] Links and IDs are consistent.

## Reviewing a pull request

Reviewers should check:

- whether claims are supported by evidence
- whether evidence strength is appropriate
- whether status values are justified
- whether uncertainty has been retained
- whether any assumptions have been introduced
- whether participant material remains anonymised
- whether the change should be minor, material or major

## LLM-assisted contributions

LLM-assisted contributions must follow `llm-instructions.md`.

LLM-generated content should be treated as draft or assumption until reviewed.
