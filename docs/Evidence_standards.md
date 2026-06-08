# Evidence standards

This file defines what counts as evidence in the repository and how evidence should be handled.

## Principle

Evidence is material that has been captured, observed, measured or sourced. Interpretation of evidence should happen in linked synthesis notes, not be hidden inside evidence records.

## Evidence kinds

Use the `evidence_kind` field to classify evidence.

```yaml
evidence_kind: quote | observation | survey_result | statistic | document_extract | desk_research | professional_judgement
```

## Evidence kind definitions

### Quote

A direct anonymised participant quote.

Quotes should preserve meaning and wording as far as possible. Edit only for anonymisation, clarity of redaction or agreed ethical reasons.

### Observation

A researcher observation from a session, service interaction, workshop or fieldwork context.

Observations should separate what was observed from what the researcher inferred.

### Survey result

A finding from survey data, such as a response pattern, proportion, ranking or coded free-text theme.

Survey results should include sample information where available.

### Statistic

A numeric data point from research, administrative data, public data, literature or analysis.

Statistics require a source, date or method note. Unsupported statistics should be marked as low confidence or assumption until sourced.

### Document extract

A relevant extract from a policy, service document, report, guidance note or operational document.

Document extracts should include source title, date and link or reference where possible.

### Desk research

A finding from secondary research, literature, policy analysis or public sources.

Desk research should be clearly distinguished from primary research with users.

### Professional judgement

A claim or interpretation from a practitioner, professional, stakeholder or subject matter expert.

Professional judgement can be valuable but should not automatically be treated as user evidence.

## Evidence metadata

Evidence notes should include:

```yaml
type: evidence
id:
source_study:
evidence_kind:
actor:
context:
journey_stage:
date_collected:
method:
sensitivity:
anonymisation_checked:
confidence:
status:
related_needs:
related_behaviours:
related_pain_points:
related_insights:
tags:
```

## Confidence

Use confidence to record the current reliability judgement for the evidence item.

```yaml
confidence: low | medium | high
```

### Low confidence

Use when:

- the source is unclear
- the evidence is anecdotal or isolated
- the context is incomplete
- the claim is a statistic without a visible source
- the evidence may be ambiguous

### Medium confidence

Use when:

- the source is clear
- the context is mostly clear
- the item is relevant and plausible
- limitations remain

### High confidence

Use when:

- the source is clear
- the context is clear
- anonymisation has been checked
- the item is directly relevant
- limitations are understood

## Evidence strength versus confidence

Evidence strength applies mainly to synthesis objects such as user needs, behaviours, pain points and insights.

Confidence applies to the reliability of an individual evidence item or interpretation.

A single high-confidence quote may still provide only weak evidence for a broad insight.

## Source requirements

Every evidence item should link to a source study or source reference where possible.

If the source is unknown, use:

```yaml
source_study:
confidence: low
status: captured
```

Then add a note explaining what is missing.

Do not invent source studies or references.

## Anonymisation

Before evidence is treated as reviewed, check that it does not include:

- names
- addresses
- contact details
- school names where identifying
- rare or unique combinations of details
- exact dates where unnecessary
- case details that could identify a person

Use:

```yaml
anonymisation_checked: true | false
sensitivity: low | medium | high
```

## What evidence can support

### Can support validated findings

- multiple anonymised quotes with clear source context
- well-documented observations
- survey results with clear method and sample
- sourced statistics
- triangulated desk research

### Usually supports draft or assumption only

- single ambiguous quote
- unsupported statistic
- professional judgement without user evidence
- LLM-generated summary
- notes with unclear source
- early pattern without review

## LLM-generated material

LLM-generated material is not evidence.

An LLM can summarise evidence, suggest codes or draft interpretations, but the evidence remains the underlying quote, observation, data point or source.

Use LLM-generated content to create:

- draft notes
- assumption notes
- suggested links
- review prompts
- research gaps

Do not use LLM output alone to validate an insight or user need.

## Contradictory evidence

Do not ignore contradictory evidence.

When evidence conflicts, record the tension in the relevant synthesis note.

Useful headings:

```markdown
## Supporting evidence

## Contradictory or limiting evidence

## What remains uncertain
```

## Evidence changelog

Evidence notes should record material changes.

Examples:

```markdown
## Changelog

- 2026-06-08: Created from anonymised quote. Source study linked. Confidence: medium.
- 2026-06-10: Added anonymisation check and linked to [[UN_003]].
```
