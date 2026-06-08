# LLM safety model

This file explains how to use LLMs safely with the research repository.

## Safety goal

The goal is to use LLMs to increase research capacity without weakening evidence quality, traceability or governance.

LLMs can help with speed, structure, linking and drafting. They cannot provide validation.

## Core safety model

```text
LLM can draft -> human reviews -> evidence supports -> item may be validated
```

The repository should never follow this pattern:

```text
LLM says it -> repository treats it as true
```

## Risk model

LLM-assisted research repositories have several risks.

### Unsupported synthesis

The LLM may generate plausible insights that are not supported by evidence.

Control:

- require linked evidence
- label assumptions
- keep draft and validated states separate

### Status inflation

Draft or assumption-based items may gradually be treated as validated.

Control:

- use controlled status values
- require human review for validation
- create dashboards for assumptions and drafts

### Evidence laundering

LLM-generated interpretations may be mistaken for evidence.

Control:

- state that LLM output is not evidence
- separate evidence notes from synthesis notes
- require evidence links for major claims

### Caveat loss

Summaries may remove uncertainty, limitations or contradictory evidence.

Control:

- require uncertainty sections in insights
- prohibit removal of caveats from validated notes without review
- check contradictory evidence before promotion

### Quote distortion

Participant quotes may be paraphrased or cleaned up in ways that change meaning.

Control:

- preserve quotes
- allow edits only for anonymisation or explicitly reviewed reasons
- keep interpretation outside the quote block

### Over-linking

The LLM may create weak or speculative links between evidence and synthesis notes.

Control:

- mark suggested links as draft or review-needed
- review links before they support validated claims

### Privacy and sensitivity risk

The LLM may expose or reproduce sensitive detail.

Control:

- do not store raw transcripts or identifiable data
- anonymise before adding to the repo
- use sensitivity metadata
- avoid unnecessary demographic inference

## LLM permissions by object type

| Object type | LLM may create draft | LLM may edit existing draft | LLM may validate | Human review required |
|---|---:|---:|---:|---:|
| Evidence | Limited | Limited | No | Yes |
| User need | Yes | Yes | No | Yes |
| Behaviour | Yes | Yes | No | Yes |
| Pain point | Yes | Yes | No | Yes |
| Insight | Yes | Yes | No | Yes |
| Theme | Yes | Yes | No | Yes |
| Persona | Yes | Yes | No | Yes |
| Journey | Yes | Yes | No | Yes |
| Review note | May draft | May draft | No | Yes |

## Safe LLM tasks

Good tasks for an LLM:

- Find evidence related to a user need.
- Suggest possible links between notes.
- Draft an insight from specified evidence.
- Identify claims without evidence.
- Identify assumptions and weak evidence.
- Compare two insights for overlap.
- Draft review questions.
- Propose metadata corrections.
- Generate a changelog entry for proposed changes.

## Unsafe or restricted LLM tasks

Avoid or restrict:

- validating insights automatically
- changing validated claims directly
- rewriting participant quotes
- removing uncertainty sections
- upgrading confidence or evidence strength
- creating public-facing outputs from assumptions without warning
- inferring sensitive characteristics not present in evidence

## Required branch workflow

LLM-assisted changes should happen on a branch.

Recommended sequence:

1. Create a focused branch.
2. Inspect relevant files.
3. Draft or update notes.
4. Add changelog entries.
5. Open a pull request.
6. Review the diff.
7. Merge only after human review.

## Pull request safety checklist

The PR should answer:

- What changed?
- Were any research claims changed?
- Were any validated notes changed?
- Were any assumptions introduced?
- Were any evidence links added, removed or changed?
- Did the LLM generate any content?
- What needs human review?

## Minimum metadata for LLM-created notes

```yaml
llm_generated: true
human_reviewed: false
review_status: not_reviewed
status: draft
```

For unsupported but plausible material:

```yaml
status: assumption
evidence_strength: none
confidence: low
```

## Prompting pattern

When asking an LLM to work with the repository, use prompts that require evidence discipline.

Example:

```text
Review the linked evidence and draft a new insight. Do not mark it as validated. Include evidence links, uncertainty, assumptions, confidence, evidence strength and a changelog entry.
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
- uncertainty is not understated
- status is appropriate
- no sensitive data has been added
- participant material has not been distorted

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
evidence_strength: weak
confidence: low
review_status: needs_review
```

It is safer to underclaim and review later than to overclaim and contaminate the repository.
