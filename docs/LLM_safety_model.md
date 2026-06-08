# LLM safety model

This file explains how to use LLMs safely with the research repository.

## Safety goal

The goal is to use LLMs to increase research capacity without weakening evidence quality, traceability or governance.

LLMs can help with speed, structure, linking, drafting, refactoring and incremental updates. They cannot provide validation.

## Core safety model

```text
LLM can create or update analysis objects -> human reviews important items -> evidence supports -> item may be validated
```

The repository should never follow this pattern:

```text
LLM says it -> repository treats it as true
```

## Operating principle

```text
fast creation, slow validation
```

Fast creation means the LLM may create placeholder, candidate, draft and evidence-linked analysis objects while breaking down research.

Slow validation means those objects are not treated as reliable findings until their evidence, status, confidence, analysis state and review trail justify it.

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

The LLM may create, update, decompose, merge and refactor these objects, provided uncertainty and change history remain visible.

## Risk model

LLM-assisted research repositories have several risks.

### Unsupported synthesis

The LLM may generate plausible analysis objects that are not supported by evidence.

Control:

- require linked evidence where available
- label assumptions
- use `analysis_state: placeholder` or `analysis_state: candidate` for early work
- keep draft and validated states separate

### Status inflation

Draft, candidate or assumption-based items may gradually be treated as validated.

Control:

- use controlled status and analysis state values
- require human review for validation
- create dashboards for assumptions, candidates and drafts

### Evidence laundering

LLM-generated interpretations may be mistaken for evidence.

Control:

- state that LLM output is not evidence
- separate evidence notes from analysis notes
- require evidence links for major claims

### Caveat loss

Summaries or refactors may remove uncertainty, limitations or contradictory evidence.

Control:

- require uncertainty sections in insights
- prohibit removal of caveats from validated notes without review
- check contradictory evidence before promotion
- use changelogs for material changes

### Quote distortion

Participant quotes may be paraphrased or cleaned up in ways that change meaning.

Control:

- preserve quotes
- allow edits only for anonymisation or explicitly reviewed reasons
- keep interpretation outside the quote block

### Over-linking

The LLM may create weak or speculative links between evidence and analysis objects.

Control:

- mark suggested links as draft, candidate or review-needed
- review links before they support validated claims

### Privacy and sensitivity risk

The LLM may expose or reproduce sensitive detail.

Control:

- do not store raw transcripts or identifiable data
- anonymise before adding to the repo
- use sensitivity metadata
- avoid unnecessary demographic inference

### Historical drift

The LLM may change wording or structure in ways that obscure how an analysis object has evolved.

Control:

- use entry-level changelogs
- classify changes as minor, material or major
- use `supersedes` and `superseded_by` for splits, merges and replacements

## LLM permissions by object type

| Object type | LLM may create placeholder/candidate | LLM may edit draft/candidate | LLM may split/merge/refactor | LLM may validate | Human review required for validation |
|---|---:|---:|---:|---:|---:|
| Evidence | Limited | Limited | No | No | Yes |
| User need | Yes | Yes | Yes | No | Yes |
| Behaviour | Yes | Yes | Yes | No | Yes |
| Pain point | Yes | Yes | Yes | No | Yes |
| Insight | Yes | Yes | Yes | No | Yes |
| Theme | Yes | Yes | Yes | No | Yes |
| Persona | Yes | Yes | Yes | No | Yes |
| Journey | Yes | Yes | Yes | No | Yes |
| Opportunity | Yes | Yes | Yes | No | Yes |
| Review note | May draft | May draft | No | No | Yes |

## Safe LLM tasks

Good tasks for an LLM:

- Find evidence related to a user need, behaviour, pain point or insight.
- Suggest possible links between notes.
- Create candidate user needs from evidence.
- Create candidate behaviours from evidence.
- Create candidate pain points from evidence.
- Draft an insight from specified evidence.
- Decompose a broad need, behaviour, pain point or insight into smaller objects.
- Merge overlapping draft or candidate objects while preserving a supersession trail.
- Identify claims without evidence.
- Identify assumptions and weak evidence.
- Compare two insights for overlap.
- Draft review questions.
- Propose metadata corrections.
- Generate a changelog entry for proposed changes.

## Unsafe or restricted LLM tasks

Avoid or restrict:

- validating insights or analysis objects automatically
- changing validated claims directly
- rewriting participant quotes
- removing uncertainty sections
- upgrading confidence or evidence strength on reviewed or validated items
- creating public-facing outputs from assumptions without warning
- inferring sensitive characteristics not present in evidence
- hiding LLM involvement

## Required branch workflow

LLM-assisted changes should happen on a branch.

Recommended sequence:

1. Create a focused branch.
2. Inspect relevant files.
3. Create or update candidate and draft analysis objects.
4. Add evidence links where available.
5. Add changelog entries for material or major changes.
6. Open a pull request.
7. Review the diff.
8. Merge only after appropriate review.

## Pull request safety checklist

The PR should answer:

- What changed?
- Were any research claims changed?
- Were any validated notes changed?
- Were any assumptions introduced?
- Were any placeholder or candidate objects created?
- Were any evidence links added, removed or changed?
- Were any objects split, merged, superseded or deprecated?
- Did the LLM generate or materially shape any content?
- What needs human review?

## Minimum metadata for LLM-created notes

```yaml
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed
status: draft
analysis_state: drafted
```

For unsupported but plausible material:

```yaml
status: assumption
analysis_state: candidate
evidence_strength: none
confidence: low
```

For evidence-linked but unreviewed material:

```yaml
status: draft
analysis_state: evidence_linked
evidence_strength: weak
confidence: low | medium
review_status: needs_review
```

## Prompting pattern

When asking an LLM to work with the repository, use prompts that require evidence discipline.

Example:

```text
Review the linked evidence and create candidate user needs, behaviours and pain points. Do not mark anything as validated. Include evidence links, uncertainty, assumptions, confidence, evidence strength, analysis state and changelog entries.
```

Avoid prompts like:

```text
Create the final insight and update the repo.
```

## Human review responsibilities

The reviewer should check:

- evidence is real and relevant
- links support the claim
- assumptions are visible
- analysis state is appropriate
- uncertainty is not understated
- status is appropriate
- no sensitive data has been added
- participant material has not been distorted
- material changes have changelog entries

## Review outcome examples

### Approved as reviewed

The item is coherent and evidence-linked, but may not yet meet the threshold for validation.

### Changes requested

The item is useful but needs better evidence, clearer phrasing, weaker claims or improved metadata.

### Rejected

The item is unsupported, misleading, duplicative or unsafe.

### Deferred

The item may be useful, but more evidence or stakeholder review is needed.

## Safe default

When in doubt, mark LLM-generated material as:

```yaml
status: assumption
analysis_state: candidate
evidence_strength: none
confidence: low
review_status: needs_review
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
```

It is safer to underclaim and review later than to overclaim and contaminate the repository.
