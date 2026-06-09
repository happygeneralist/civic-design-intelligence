# LLM intervention logging strategy

LLMs can be useful for migration, synthesis and structuring work, but they can also silently change meaning.

This is especially risky in a research repository where language is not merely presentation. Language can carry evidence, emotion, uncertainty, relational context, power dynamics and implied intervention choices.

This document defines when LLM-assisted changes should be logged separately from Git history and object change logs.

## Core principle

LLM-assisted changes should be classified by semantic risk before they are treated as accepted knowledge.

An LLM edit is not automatically wrong, but it is also not automatically trustworthy. When an LLM changes meaning, evidence relationships or interpretation, the repository should preserve a record of that intervention and mark it for human review where appropriate.

## Why Git is not enough

Git records exact file changes. It does not explain semantic intent or risk.

Git can show that a sentence changed from one wording to another. It cannot reliably answer:

- Did the meaning change?
- Did the LLM narrow or expand the implied solution space?
- Did the LLM remove evidence-specific language?
- Did it turn uncertainty into confidence?
- Did it collapse several different needs into one tidy statement?
- Did a human accept the change?

LLM intervention logs exist to answer those questions.

## Common LLM risks in this repository

LLMs may unintentionally:

- polish away specificity
- generalise concrete evidence
- rewrite participant language into organisational language
- remove emotional or relational nuance
- turn uncertainty into overconfidence
- convert civic or systemic needs into simple content or usability needs
- make evidence sound more coherent than it is
- merge distinct needs, behaviours or pain points
- change actor, level, journey stage or problem framing
- infer relationships that are plausible but not evidence-linked

These are semantic risks, not formatting risks.

## Semantic change classification

Every LLM-assisted edit should be classified before or during the work.

Recommended values:

```yaml
semantic_change: none
semantic_change: possible
semantic_change: material
```

Definitions:

- `none`: metadata, formatting, folder movement or ID normalisation only
- `possible`: wording changed, but the intended meaning is the same
- `material`: meaning, interpretation, evidence basis, relationships, actor, level or implied intervention space changed

## When an LLM intervention log is required

Create an LLM intervention log when an LLM does any of the following:

- rewrites a user need statement
- rewrites evidence-derived language
- summarises raw evidence into an insight
- merges or splits user needs, pain points, behaviours, insights or themes
- changes evidence basis, confidence, status or review status
- adds or removes relationships to evidence, needs, behaviours, pain points or insights
- changes actor, journey stage, need level or civic/service framing
- turns a loose note into a structured object where interpretation is required
- produces a material synthesis used for product, service or policy reasoning

An LLM intervention log is usually not required for:

- YAML formatting
- ID format normalisation
- filename cleanup
- moving loose notes to the inbox
- adding lifecycle fields without changing wording or interpretation
- fixing casing or spelling

Administrative changes can be recorded in the PR summary or a lightweight object change-log entry.

## Human review rules

If `semantic_change: possible`, the object should normally be marked:

```yaml
review_status: needs_review
```

unless a human immediately reviews and accepts the change.

If `semantic_change: material`, the object must be marked:

```yaml
review_status: needs_review
human_reviewed: false
```

unless a human review occurs as part of the same change.

For first-class objects such as user needs, material LLM-assisted changes should not be treated as validated until reviewed.

## Recommended LLM intervention log format

LLM intervention logs should live outside the edited object. They should be append-only records of semantic intervention.

Recommended location:

```text
011_Change_events/LLM/
```

Recommended filename pattern:

```text
YYYY-MM-DD_OBJECT-ID_short-description.md
```

Example:

```text
011_Change_events/LLM/2026-06-20_UN_001_need-wording-refinement.md
```

Suggested content:

```markdown
# LLM intervention: UN_001 need wording refinement

## Metadata

- Date: 2026-06-20
- Object: [[UN_001]]
- Object type: user_need
- Actor type: llm
- Actor: ChatGPT
- Human reviewed: false
- Review status: needs_review
- Semantic change: material
- Risk level: material

## Change intent

Clarify the user need statement based on linked evidence.

## What changed semantically

The wording shifted from a generic information-access framing to an interpretive decision-support framing.

## Potential risk

This change may alter the implied intervention space from content provision to relational or guided support.

## Evidence considered

- [[EVID_001]]
- [[BEH_001]]

## Review notes

Pending human review.
```

## What the log should capture

The intervention log should describe semantic effects, not duplicate the Git diff.

It should capture:

- change intent
- semantic change classification
- evidence considered
- meaning risks
- review status
- whether the change affects solution space
- whether participant/user language was preserved
- whether uncertainty changed

## What the log should not become

The LLM intervention log should not become:

- a copy of the full file diff
- a long transcript of the chat
- a replacement for Git history
- a mandatory burden for every tiny edit
- a place for the LLM to rewrite the object again

Keep it focused on meaning and governance.

## Operating model for LLM-assisted edits

Before editing, the LLM should state:

```text
Planned change type:
Expected semantic risk:
LLM intervention log required: yes/no
```

After editing, the LLM should report:

```text
Meaning changed: yes/no/possibly
Evidence relationships changed: yes/no
Review status changed: yes/no
LLM intervention log created: yes/no
```

This gives the human reviewer a clear governance checkpoint.

## Suggested fields for affected objects

The edited object may include latest-state fields such as:

```yaml
last_meaningful_change: 2026-06-20
last_change_actor: llm_assisted
last_change_type: wording_refined
semantic_change_review: needs_review
```

These fields point to the state of the object. The detailed audit remains in the event log.

## Strategic purpose

The goal is not to make LLM use difficult. The goal is to prevent silent semantic drift.

LLMs can help create useful structure and synthesis. But in this repository, synthesis is an epistemic act. It changes what the team thinks it knows.

Material LLM changes therefore need a visible trace.