# Research study scope

Research studies are source and context objects. They describe where evidence came from, who produced or commissioned it, what population or service context it represents, and how cautiously the evidence should be reused.

They should not be treated as canonical knowledge objects. A local study can support a cross-context user need, and a national report can still have local or institutional limits.

## Core rule

```text
Capture evidence locally. Maintain knowledge at the highest defensible level.
```

Localise the source first. Only localise a user need, civic need, pain point, behaviour or insight when local context materially changes the meaning, risk, priority or response.

## Why this matters

The repository is intended to combine evidence from many sources and institutions, including local research, third-sector reports, professional knowledge, statutory reports, complaints, Ombudsman decisions, academic work, operational data and public contributions.

Without source scope, local evidence can be over-generalised. Without knowledge scope, general patterns can be fragmented into unnecessary local duplicates.

The aim is to preserve both:

- where the evidence came from
- how far the resulting understanding can defensibly travel

## Source context fields

Use these fields in research study frontmatter.

```yaml
source_context:
  geographic_scope: local | regional | national | international | mixed | unclear
  primary_locale:
  locales:
  institution_scope: single_institution | multi_institution | cross_sector | external_research | community_research | unclear
  source_type: primary_research | public_report | inspection | complaint | operational_data | academic | third_sector | professional_knowledge | mixed | unclear
  commissioning_or_source_body:
```

### `geographic_scope`

Use the smallest honest description of where the study evidence comes from.

- `local`: evidence from one place, local area, council area, neighbourhood, service geography or local system
- `regional`: evidence from multiple places in a region
- `national`: evidence from a national source or national sample
- `international`: evidence from outside the UK or across countries
- `mixed`: evidence combines more than one geographic level
- `unclear`: the source does not yet make this clear

### `primary_locale`

Use when one place is the main context, for example:

```yaml
primary_locale: Example local area
```

Leave blank when there is no primary locale or it is unclear.

### `locales`

Use for the places explicitly represented by the evidence.

```yaml
locales:
  - Example local area
  - South London
```

Do not add places by inference. If the study does not say where participants, services or institutions are based, leave this blank and use `unclear` where needed.

### `institution_scope`

Use this to describe how institutionally bounded the evidence is.

- `single_institution`: one school, service, team, council, provider or organisation
- `multi_institution`: multiple institutions of the same broad type
- `cross_sector`: multiple institution types, such as local authority, schools, colleges and charities
- `external_research`: produced outside the repository's local institutional context
- `community_research`: evidence primarily from residents, families, carers, young people or community networks
- `unclear`: not yet clear from the source

### `source_type`

Use this to distinguish research from other evidence sources.

A study can use `mixed` if it combines source types.

## Applicability fields

Use these fields to describe how cautiously findings should be reused.

```yaml
applicability:
  transferability: unclear | local_only | plausible_cross_context | supported_cross_context
  limits:
  notes:
```

### `transferability`

- `unclear`: not enough is known to judge how far the findings can travel
- `local_only`: the finding depends on local policy, provision, governance, geography, service configuration or named local processes
- `plausible_cross_context`: the evidence is local or bounded, but the pattern may apply in other contexts and should be compared with further sources
- `supported_cross_context`: the pattern is supported across multiple contexts, methods, places or institution types

Do not use `supported_cross_context` from a single local study unless the study itself includes credible cross-context comparison.

### `limits`

Use short notes about what limits reuse.

Examples:

```yaml
limits:
  - Local SEND provision affects available options.
  - Sample recruited through parent networks.
  - Online format may exclude people with lower digital access.
```

### `notes`

Use this for brief judgement about the study's applicability.

Example:

```yaml
notes: Local evidence may point to a wider pattern, but it should be compared with public or explicitly authorised evidence before being treated as cross-context.
```

## Relationship to knowledge objects

Research study scope describes the source.

Knowledge object scope describes the claim.

A user need, civic need, pain point, behaviour or insight should not automatically inherit the locality of a study. Instead, capture evidence coverage on the knowledge object where useful.

Example:

```yaml
evidence_coverage:
  locales:
    - Example local area
  source_types:
    - primary_research
    - professional_knowledge
  institution_types:
    - local_authority
    - schools
    - colleges
    - charities
  evidence_pattern: single_source | convergent | mixed | contradictory | unclear
```

Use `locale_specific` or local variants only when locality changes meaning.

## Examples

### Local evidence supporting a cross-context need

```yaml
source_context:
  geographic_scope: local
  primary_locale: Example local area
  locales:
    - Example local area
  institution_scope: community_research
  source_type: primary_research
applicability:
  transferability: plausible_cross_context
  limits:
    - Recruited through local SEND parent networks.
  notes: The evidence is local, but the need for reliable information about post-16 options may apply beyond one place.
```

### Local-only source

```yaml
source_context:
  geographic_scope: local
  primary_locale: Example local area
  locales:
    - Example local area
  institution_scope: single_institution
  source_type: operational_data
applicability:
  transferability: local_only
  limits:
    - Depends on local eligibility, workflow or commissioning rules.
  notes: Useful for local delivery decisions but not a general SEND pathway claim.
```

### Unclear source

```yaml
source_context:
  geographic_scope: unclear
  primary_locale:
  locales:
  institution_scope: unclear
  source_type: primary_research
applicability:
  transferability: unclear
  limits:
    - Locality and institutional context need review.
  notes: Do not use for cross-context claims until the study metadata is clarified.
```

## Practical decision rule

When adding a new research study, ask:

1. Where did this evidence come from?
2. Which institution types or communities does it represent?
3. What might limit reuse?
4. Could the underlying pattern plausibly travel to other contexts?
5. Would local context change the meaning of any derived need, pain point, behaviour or insight?

Where unsure, use `unclear` and add a limitation rather than over-claiming.
