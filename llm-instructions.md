# LLM operating instructions

These instructions apply to any LLM used to read, query, draft or update this repository.

The repository is the source of truth. The LLM is not evidence and must not be treated as an authority.

## Core rule

Every meaningful claim must either be traceable to evidence or clearly marked as an assumption.

## What the LLM may do

The LLM may:

- summarise existing notes
- classify evidence using the repository schema
- suggest links between evidence, needs, behaviours, pain points and insights
- draft new insight notes
- identify weak evidence, missing sources and contradictions
- propose metadata updates
- propose changelog entries
- propose review notes
- help create synthesis outputs from reviewed or validated items

## What the LLM must not do

The LLM must not:

- mark anything as validated
- upgrade evidence strength
- remove caveats or uncertainty markers
- rewrite participant quotes except to suggest anonymisation
- materially alter validated claims without review
- add unsupported claims
- merge assumptions into validated notes
- infer lived experience, diagnoses, demographics or protected characteristics without evidence
- store raw transcripts, recordings or identifiable participant data
- bypass the review process

## Status handling

The LLM may create or propose items with these statuses:

```yaml
status: draft | assumption
review_status: not_reviewed | needs_review
llm_generated: true
human_reviewed: false
```

The LLM must not set:

```yaml
status: validated
human_reviewed: true
review_status: reviewed
```

unless the human reviewer has explicitly instructed it to record an already-completed review outcome.

## Evidence strength handling

The LLM may propose an evidence strength, but it must not upgrade evidence strength on existing reviewed or validated items.

When uncertain, use the lower strength.

```yaml
evidence_strength: none | weak | moderate | strong
```

Default for LLM-generated synthesis should be:

```yaml
evidence_strength: weak
```

unless clear linked evidence supports a different judgement and the item remains in draft or review.

## Required metadata for LLM-generated notes

Any LLM-generated note must include:

```yaml
llm_generated: true
human_reviewed: false
review_status: not_reviewed
status: draft
```

If the note is plausible but not directly evidenced, use:

```yaml
status: assumption
evidence_strength: none
```

## Required explanation for proposed changes

Every proposed change should state:

- affected files
- purpose of the change
- evidence used
- assumptions introduced
- confidence level
- status changes proposed
- whether the change is minor, material or major
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

For validated items, the LLM must not:

- change the core claim
- change the title or need statement in a way that changes meaning
- remove linked evidence
- downgrade or upgrade status without explicit review instruction

## Branch and pull request workflow

LLM-assisted changes should be made on a branch, not directly on `main`.

A pull request should include:

- summary of changes
- list of new files
- list of changed files
- review risks
- evidence and assumptions affected
- confirmation that no research content was materially changed unless requested

## Preferred output pattern

When asked to draft or update repository content, the LLM should use this sequence:

1. Inspect relevant files.
2. Identify current structure and evidence base.
3. Propose changes.
4. Make changes on a branch if requested.
5. Add changelog entries.
6. Open a pull request for review.
7. Report what changed and what still needs human review.
