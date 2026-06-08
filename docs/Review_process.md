# Review process

This file defines how repository items move from capture or draft into reviewed and validated states.

## Review purpose

Review protects the repository from:

- unsupported claims
- overconfident synthesis
- hidden assumptions
- evidence drift
- accidental loss of caveats
- unsafe handling of participant material
- LLM-generated material being treated as evidence

## Review states

The repository uses two related fields: `status` and `review_status`.

### Status

```yaml
status: captured | draft | assumption | reviewed | validated | deprecated
```

### Review status

```yaml
review_status: not_reviewed | needs_review | reviewed | rejected
```

`status` describes the epistemic state of the item. `review_status` describes where it is in the review workflow.

## Promotion path

### Evidence

```text
captured -> reviewed -> deprecated, if no longer usable
```

Evidence is usually not `validated` in the same sense as an insight or user need. It is captured, anonymised, checked and reviewed.

### User needs, behaviours, pain points and insights

```text
draft -> reviewed -> validated
assumption -> reviewed -> validated, if evidence supports it
assumption -> deprecated, if evidence contradicts it or it is no longer useful
```

## Review checklist for evidence

- [ ] The source study is identified or the missing source is explicitly noted.
- [ ] The evidence kind is clear.
- [ ] The actor is clear where known.
- [ ] The quote, observation or data point is anonymised.
- [ ] No raw transcript, recording or identifiable participant data is included.
- [ ] The confidence level is appropriate.
- [ ] Links to related notes are accurate.
- [ ] The changelog has been updated if the evidence has changed.

## Review checklist for user needs

- [ ] The need is framed from the user's perspective.
- [ ] The need is not a solution, feature or organisational goal.
- [ ] The actor and journey stage are clear.
- [ ] The need links to relevant evidence, or is marked as an assumption.
- [ ] Evidence strength is appropriate.
- [ ] Confidence is appropriate.
- [ ] Related behaviours, pain points and insights are linked where relevant.
- [ ] The status is justified.
- [ ] The changelog is up to date.

## Review checklist for behaviours

- [ ] The behaviour describes something a person does, avoids, repeats or compensates for.
- [ ] The behaviour is linked to evidence, or marked as an assumption.
- [ ] The actor and journey stage are clear.
- [ ] Barriers, triggers or conditions are separated from the behaviour itself.
- [ ] Evidence strength and confidence are appropriate.
- [ ] The changelog is up to date.

## Review checklist for pain points

- [ ] The pain point describes a barrier, burden, failure, friction or emotional cost.
- [ ] It is linked to evidence, or clearly marked as an assumption.
- [ ] It is not written as a proposed solution.
- [ ] The affected actor is clear.
- [ ] The service, system or journey context is clear where known.
- [ ] Evidence strength and confidence are appropriate.
- [ ] The changelog is up to date.

## Review checklist for insights

- [ ] The core claim is clear.
- [ ] The insight explains why something is happening and why it matters.
- [ ] Major claims link to evidence.
- [ ] Contradictory or limiting evidence has been considered.
- [ ] Assumptions are explicitly labelled.
- [ ] Design, service or policy implications are separated from evidence.
- [ ] Evidence strength and confidence are appropriate.
- [ ] The item has not been over-promoted.
- [ ] The changelog is up to date.

## Review checklist for LLM-generated content

- [ ] `llm_generated: true` is present.
- [ ] `human_reviewed: false` remains until a human review has happened.
- [ ] The item is not marked as validated.
- [ ] Claims are traceable to evidence or marked as assumptions.
- [ ] No participant quote has been silently rewritten.
- [ ] No caveats have been removed.
- [ ] Evidence strength has not been upgraded without review.
- [ ] The proposed changelog entry is accurate.

## Recording review decisions

For small changes, record the decision in the item's changelog.

For material or major changes, create a review note or add a detailed review section.

Example:

```markdown
## Review

- Review date: 2026-06-08
- Reviewer:
- Outcome: changes requested
- Rationale: Claim is plausible but only linked to one weak evidence item.
- Required action: Keep as assumption until additional evidence is added.
```

## Validation threshold

An item may be marked as validated only when:

- it has been reviewed by a human
- it links to relevant evidence
- evidence strength is at least moderate, unless a clear exception is documented
- the claim is precise enough to test or challenge
- limitations are documented
- the changelog records the promotion

## Deprecation

Use `deprecated` when an item is superseded, contradicted, duplicated or no longer safe to use.

Deprecated notes should not be deleted unless there is a safety, legal or data protection reason. Prefer preserving the audit trail.
