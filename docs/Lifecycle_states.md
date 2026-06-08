# Lifecycle states

This file explains how to use `status`, `analysis_state` and `review_status` together.

These fields answer different questions:

| Field | Question | Meaning |
|---|---|---|
| `status` | How should we treat the claim? | Epistemic standing |
| `analysis_state` | Where is this object in the workflow? | Analysis maturity |
| `review_status` | What has happened in review? | Process control |

## Core rule

Use all three fields together. Do not rely on one field to do all the work.

A note can be useful before it is mature, and mature before it is validated.

## Common combinations

| Situation | `status` | `analysis_state` | `review_status` | Use |
|---|---|---|---|---|
| Loose captured material | `captured` | `captured` | `not_reviewed` | Working material or source-level note |
| Structured evidence item | `captured` | `captured` | `not_reviewed` | Evidence preserved but not checked |
| Reviewed evidence item | `reviewed` | `reviewed` | `reviewed` | Evidence checked for source, sensitivity and usefulness |
| Placeholder analysis object | `assumption` | `placeholder` | `not_reviewed` | Holds a possible need, behaviour, pain point or insight |
| Candidate from LLM extraction | `assumption` | `candidate` | `not_reviewed` | Useful map item, not yet reliable |
| Candidate with weak evidence | `draft` | `candidate` | `needs_review` | Early synthesis with some support |
| Drafted analysis object | `draft` | `drafted` | `not_reviewed` | Formulated enough to work with |
| Evidence-linked draft | `draft` | `evidence_linked` | `needs_review` | Linked to evidence but not yet checked |
| Human-reviewed but not validated | `reviewed` | `reviewed` | `reviewed` | Checked and usable with caveats |
| Validated finding | `validated` | `validated` | `reviewed` | Reliable enough for appropriate decisions |
| Rejected candidate | `deprecated` | `deprecated` | `rejected` | Not useful or unsafe to use |
| Superseded item | `deprecated` | `deprecated` | `reviewed` | Replaced by another item but kept for history |

## Recommended defaults

### Loose capture

Use this for quick notes, early analysis or working material.

```yaml
status: captured
analysis_state: captured
review_status: not_reviewed
```

### LLM-created candidate object without direct evidence links

Use this when the object helps map the territory but is not yet supported by specific evidence.

```yaml
status: assumption
analysis_state: candidate
review_status: not_reviewed
evidence_strength: none
confidence: low
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
```

### LLM-created object with at least one relevant evidence link

Use this when the LLM has linked the object to evidence, but a human has not checked the link.

```yaml
status: draft
analysis_state: evidence_linked
review_status: needs_review
evidence_strength: weak
confidence: low | medium
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
```

### Human-reviewed object that is not yet validated

Use this when a human has reviewed the object, but the evidence is not yet strong enough for validation.

```yaml
status: reviewed
analysis_state: reviewed
review_status: reviewed
human_reviewed: true
```

### Validated object

Use this only after human review and sufficient evidence.

```yaml
status: validated
analysis_state: validated
review_status: reviewed
human_reviewed: true
evidence_strength: moderate | strong
```

## Invalid or risky combinations

Avoid these combinations unless there is a documented reason.

| Combination | Why it is risky |
|---|---|
| `status: validated` + `review_status: not_reviewed` | Validation requires human review |
| `status: validated` + `human_reviewed: false` | Validation cannot be LLM-only |
| `analysis_state: validated` + `evidence_strength: none` | Validated objects need evidence |
| `status: assumption` + `analysis_state: validated` | Contradictory maturity and epistemic state |
| `status: captured` on a user need or insight | Captured is mainly for evidence or loose material |
| `review_status: reviewed` + `human_reviewed: false` | Review status should reflect human review |
| `llm_generated: true` + missing `creation_mode` | LLM involvement must be visible |

## How to choose between `assumption`, `draft` and `reviewed`

Use `assumption` when the object is plausible but weakly evidenced or not directly evidenced.

Use `draft` when the object has been formulated and may have some evidence, but has not been reviewed.

Use `reviewed` when a human has checked the formulation, evidence links and caveats, but has not necessarily validated it.

## How to choose between `candidate`, `drafted` and `evidence_linked`

Use `candidate` when the object is worth keeping in the map but still rough.

Use `drafted` when the object has a usable formulation.

Use `evidence_linked` when the object has explicit links to evidence, even if those links still need review.

## Validation threshold

An object should normally reach validation only when:

- a human has reviewed it
- evidence is linked and relevant
- evidence strength is at least moderate, unless an exception is documented
- uncertainty and limitations are clear
- wording is stable enough for the decision it supports
- the changelog records the promotion

## Practical guidance

When in doubt, underclaim.

It is better to mark something as a useful candidate than to overstate its reliability.

The repository should contain incomplete knowledge, but incomplete knowledge must remain visibly incomplete.
