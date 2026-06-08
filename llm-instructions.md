# LLM operating instructions

These instructions apply to any LLM used to read, query, draft or update this repository.

The repository is the source of truth. The LLM is not evidence and must not be treated as an authority.

## Core rule

Every meaningful claim must either be traceable to evidence or clearly marked as an assumption.

## Operating principle

The repository should support:

```text
fast creation, slow validation
```

LLMs may help move quickly. The safety control is not to prevent LLM-assisted drafting or editing. The safety control is to preserve evidence links, uncertainty, status, review state and changelog history.

## What the LLM may do

The LLM may:

- summarise existing notes
- classify evidence using the repository schema
- suggest links between evidence, user needs, behaviours, pain points, insights, themes, journeys and opportunities
- create placeholder analysis objects
- create candidate user needs, behaviours, pain points, insights, themes, journeys and opportunities
- draft new analysis objects from specified evidence
- decompose broad analysis objects into smaller objects
- merge or refactor overlapping draft objects, with a changelog and supersession trail
- incrementally update draft or candidate objects as new evidence or thinking emerges
- identify weak evidence, missing sources and contradictions
- propose metadata updates
- propose changelog entries
- propose review notes
- help create synthesis outputs from reviewed or validated items

## Analysis objects

Analysis objects are interpreted research objects created from evidence, researcher judgement and synthesis.

They include:

- user needs
- behaviours
- pain points
- insights
- themes
- journeys
- personas
- opportunities

LLMs may create and alter these objects, provided the item remains clearly marked by status, analysis state, evidence strength, confidence, creation mode and review status.

## What the LLM must not do

The LLM must not:

- mark anything as validated
- upgrade evidence strength on reviewed or validated items
- remove caveats or uncertainty markers
- rewrite participant quotes except to suggest anonymisation
- materially alter validated claims without review
- add unsupported claims without marking them as assumptions
- merge assumptions into validated notes
- infer lived experience, diagnoses, demographics or protected characteristics without evidence
- store raw transcripts, recordings or identifiable participant data
- bypass the review process
- hide the fact that an item was LLM-assisted

## Status and analysis state handling

The LLM may create or propose items with these statuses and states:

```yaml
status: draft | assumption
analysis_state: placeholder | candidate | drafted | evidence_linked
review_status: not_reviewed | needs_review
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
```

The LLM must not set:

```yaml
status: validated
analysis_state: validated
human_reviewed: true
review_status: reviewed
```

unless the human reviewer has explicitly instructed it to record an already-completed review outcome.

## Evidence strength handling

The LLM may propose an evidence strength for draft or candidate work, but it must not upgrade evidence strength on existing reviewed or validated items.

When uncertain, use the lower strength.

```yaml
evidence_strength: none | weak | moderate | strong
```

Default for LLM-generated analysis without clear linked evidence should be:

```yaml
evidence_strength: none
status: assumption
analysis_state: candidate
confidence: low
```

Default for LLM-generated analysis with at least one relevant evidence link should be:

```yaml
evidence_strength: weak
status: draft
analysis_state: evidence_linked
confidence: low | medium
```

## Required metadata for LLM-generated notes

Any LLM-generated note must include:

```yaml
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed
status: draft
analysis_state: drafted
change_level: none | minor | material | major
```

If the note is plausible but not directly evidenced, use:

```yaml
status: assumption
analysis_state: candidate
evidence_strength: none
confidence: low
```

## Required explanation for proposed changes

Every proposed change should state:

- affected files
- purpose of the change
- evidence used
- assumptions introduced
- confidence level
- status changes proposed
- analysis state changes proposed
- whether the change is minor, material or major
- whether any item was split, merged, superseded or deprecated
- suggested changelog entry

## Participant quotes

Participant quotes should be preserved as captured, except where anonymisation is needed.

The LLM may suggest an anonymised version, but the original quote should not be silently rewritten.

## Validated items

For validated items, the LLM may:

- summarise the item
- identify linked evidence
- identify gaps or possible contradictions
- propose a review note
- propose a new draft replacement or refinement on a branch

For validated items, the LLM must not:

- change the core claim directly
- change the title, need statement, behaviour, pain point or insight in a way that changes meaning without review
- remove linked evidence
- downgrade or upgrade status without explicit review instruction

If a validated item needs substantial change, create a proposed replacement, mark the change as material or major, and use `supersedes` / `superseded_by` where appropriate.

## Splitting, merging and refactoring

The LLM may split, merge or refactor draft and candidate analysis objects.

For each split, merge or substantial reframing, it must:

- preserve the original item unless explicitly asked to replace it
- record `change_level: major`
- update `supersedes` and `superseded_by` where relevant
- add an entry-level changelog
- keep the result as draft, assumption or needs review

## Branch and pull request workflow

LLM-assisted changes should be made on a branch, not directly on `main`.

A pull request should include:

- summary of changes
- list of new files
- list of changed files
- review risks
- evidence and assumptions affected
- new placeholder or candidate items created
- items split, merged, superseded or deprecated
- confirmation that no validated research content was materially changed unless requested

## Preferred output pattern

When asked to draft or update repository content, the LLM should use this sequence:

1. Inspect relevant files.
2. Identify current structure and evidence base.
3. Create or update draft/candidate analysis objects as requested.
4. Preserve evidence links, status, analysis state and uncertainty.
5. Add changelog entries.
6. Make changes on a branch if requested.
7. Open or update a pull request for review.
8. Report what changed and what still needs human review.
