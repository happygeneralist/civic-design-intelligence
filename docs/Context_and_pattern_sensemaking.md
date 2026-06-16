# Context and pattern sensemaking

This note captures the emerging repository approach to locality, service areas, operational context and reusable need patterns.

It is a direction-setting note, not a schema change.

## Core principle

Capture lived experience first. Map service, organisation and locality context around it.

```text
Evidence has an origin.
Needs have an applicability horizon.
Patterns emerge over time.
```

A need may first be observed in one place, service area or operational setting. That first observed context should be preserved as evidence provenance, but it should not permanently define the boundary of the need unless the need is inherently place-specific or service-specific.

## Why this matters

Public services are organised around operational areas such as SEND, housing, transport, benefits, education or health.

People's lived experience does not usually follow those boundaries.

A person may experience:

- needing to know what support is available nearby
- needing to travel reliably to access education, work or care
- needing to know who is responsible when support breaks down
- needing to compare realistic options before committing to a route
- needing to avoid repeating their story across services

These needs may appear first in SEND pathway-planning research, but later recur in housing, transport, adult social care, health, education, benefits or local community support.

The repository should allow those patterns to emerge without losing the original evidence context.

## Do not over-localise canonical needs

Avoid making the first observed locality or service area part of the canonical wording unless it is essential to the meaning.

Avoid:

```text
Need to understand East Merseyside SEND travel support.
```

Prefer:

```text
Need to know what travel support is available locally.
```

Then capture context separately:

```yaml
service_contexts:
  - SEND
  - transport

locality_contexts:
  - East Merseyside

organisation_contexts:
  - local_authority
  - transport_provider
```

This keeps the need reusable while preserving where it was observed.

## Distinguish origin from applicability

The repository should distinguish:

- where evidence came from
- where a need has been observed
- where a need might plausibly apply
- where a need is established as recurring
- which service or organisation may be responsible for acting on it

These are related but not the same.

Example early state:

```yaml
evidence_location:
  - East Merseyside

service_contexts:
  - SEND

applicability_scope: local_observed
pattern_status: emerging
```

Example later state after similar evidence appears elsewhere:

```yaml
evidence_location:
  - East Merseyside
  - Kent
  - Manchester

service_contexts:
  - SEND
  - transport
  - housing

applicability_scope: cross_locality
pattern_status: recurring
```

This should not be treated as validation by itself. It is a way to make the scope of sensemaking visible.

## Possible future states

The exact controlled values should not be finalised yet, but future modelling may need states such as:

```text
local_observed
local_recurring
cross_locality_candidate
cross_service_candidate
established_pattern
nationally_relevant
place_specific
service_specific
```

These states are about applicability and pattern recognition. They are not the same as evidence strength or review status.

A need can be well evidenced locally while still weakly evidenced nationally.

A need can be recurring across localities while still needing human review before it is used for policy, design or operational decisions.

## Service areas are context, not lived experience

Service areas such as SEND, housing or transport should normally be treated as operational context.

They help answer:

- where the need appears
- which organisation or service may have responsibility
- which operational systems are implicated
- where value may be blocked
- where interventions or policy responses may sit

They should not become the primary structure of the need itself.

## Locality is context, not automatic scope

Locality can exist at several levels:

```text
national
regional
local_authority
neighbourhood
estate
street
site
```

The repository may eventually need to support all of these, but street-level or site-level context can create privacy and identifiability risk.

For now, locality should be captured cautiously and only where it is useful for sensemaking, service context or operational responsibility.

## Sensemaking questions

This approach should eventually help answer:

- Which needs started as local but recur across places?
- Which needs appear across multiple service areas?
- Which local findings may indicate national design or policy issues?
- Which national assumptions are contradicted by local evidence?
- Which needs are genuinely place-specific?
- Which operational areas share the same lived-experience need?
- Where does local evidence suggest a wider public-service pattern?

## Guidance for the next ingestion pass

During the next SEND pathway-planning ingestion pass, do not build a full locality or service-area taxonomy.

Instead:

- capture lived-experience needs directly
- preserve evidence provenance
- note locality and service context where it appears in the evidence
- avoid encoding operational ownership into canonical need wording
- leave uncertain context mappings as candidate or needs-review
- watch for needs that may be reusable beyond SEND

The goal is to learn from examples before creating stricter fields, validators or taxonomies.
