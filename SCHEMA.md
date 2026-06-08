# Repository schema

This file defines the common structure for notes in the research repository.

The schema is intended to make the repository queryable, reviewable and safe to use with LLM-assisted workflows.

## General rules

Every structured note should have YAML frontmatter.

Every note should have:

```yaml
type:
id:
status:
evidence_strength:
confidence:
llm_generated:
human_reviewed:
review_status:
tags:
```

Use lower case values for controlled fields unless the ID convention requires capitals.

## Controlled values

### `status`

```yaml
status: captured | draft | assumption | reviewed | validated | deprecated
```

- `captured`: evidence or information has been recorded but not synthesised.
- `draft`: synthesis has been drafted but not reviewed.
- `assumption`: plausible but not directly supported by sufficient evidence.
- `reviewed`: checked by a human reviewer, but not necessarily validated.
- `validated`: supported by evidence and approved for use as a reliable finding.
- `deprecated`: superseded, withdrawn or no longer recommended for use.

### `evidence_strength`

```yaml
evidence_strength: none | weak | moderate | strong
```

- `none`: no supporting evidence is linked.
- `weak`: limited, indirect or single-source evidence.
- `moderate`: multiple relevant evidence items, but with limitations.
- `strong`: multiple credible evidence items across relevant sources or methods.

### `confidence`

```yaml
confidence: low | medium | high
```

Confidence is the researcher's current judgement about reliability. It should not be used as a substitute for evidence strength.

### `review_status`

```yaml
review_status: not_reviewed | needs_review | reviewed | rejected
```

### Boolean fields

```yaml
llm_generated: true | false
human_reviewed: true | false
anonymisation_checked: true | false
```

## ID conventions

Use stable IDs. Do not renumber existing items just because the order changes.

```text
RS_001     research study
EVID_001   evidence item
UN_001     user need
BEH_001    behaviour
PP_001     pain point
INS_001    insight
TH_001     theme
PER_001    persona
JNY_001    journey
REV_001    review note
CLM_001    claim
```

## Object types

### Research study

```yaml
type: research_study
id: RS_001
title:
research_lead:
date_range:
method:
participants:
setting:
status: captured | reviewed | validated | deprecated
related_evidence:
related_insights:
tags:
```

A research study describes an activity or source collection. It should not contain raw identifiable data.

### Evidence

```yaml
type: evidence
id: EVID_001
source_study: "[[RS_001]]"
evidence_kind: quote | observation | survey_result | statistic | document_extract | desk_research | professional_judgement
actor:
context:
journey_stage:
date_collected:
method:
sensitivity: low | medium | high
anonymisation_checked: true | false
confidence: low | medium | high
status: captured | reviewed | deprecated
related_needs:
related_behaviours:
related_pain_points:
related_insights:
tags:
```

Evidence should preserve the meaning of what was captured. Participant quotes should not be rewritten except to remove or mask identifying information.

### User need

```yaml
type: user_need
id: UN_001
actor:
journey_stage:
need:
status: draft | assumption | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
related_evidence:
related_behaviours:
related_pain_points:
related_insights:
importance: low | medium | high
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
tags:
```

A user need should describe what a person needs to achieve, understand, decide, access, feel or recover from. It should not be written as a solution, feature request or organisational objective.

### Behaviour

```yaml
type: behaviour
id: BEH_001
actor:
journey_stage:
behaviour:
status: draft | assumption | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
related_evidence:
related_needs:
related_pain_points:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
tags:
```

A behaviour should describe something a person does, avoids, repeats, compensates for or attempts in context.

### Pain point

```yaml
type: pain_point
id: PP_001
actor:
journey_stage:
pain_point:
status: draft | assumption | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
related_evidence:
related_needs:
related_behaviours:
related_insights:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
tags:
```

A pain point should describe a barrier, burden, failure, friction, emotional cost or structural problem experienced by an actor.

### Insight

```yaml
type: insight
id: INS_001
title:
actor:
journey_stage:
status: draft | assumption | reviewed | validated | deprecated
evidence_strength: none | weak | moderate | strong
confidence: low | medium | high
related_evidence:
related_needs:
related_behaviours:
related_pain_points:
related_themes:
claims:
llm_generated: true | false
human_reviewed: true | false
review_status: not_reviewed | needs_review | reviewed | rejected
tags:
```

An insight is a research-backed interpretation that explains why something is happening and why it matters. It should include evidence, interpretation, uncertainty and implications.

### Review note

```yaml
type: review_note
id: REV_001
reviewed_item:
reviewer:
review_date:
review_outcome: approved | changes_requested | rejected | deferred
status:
evidence_strength:
confidence:
tags:
```

Review notes should document material decisions, especially when an item is promoted, downgraded, deprecated or materially changed.

## Entry-level changelog

Every structured note should include an entry-level changelog section.

```markdown
## Changelog

- YYYY-MM-DD: Created as draft. Evidence strength: weak. Review status: not reviewed.
```

Record material changes to claims, status, confidence, evidence strength, evidence links and review outcomes.

## Material change levels

```yaml
change_level: minor | material | major
```

- `minor`: spelling, formatting, metadata tidy-up or link correction.
- `material`: changes the interpretation, evidence links, confidence or status.
- `major`: substantially reframes a finding, changes validated content or affects published outputs.
