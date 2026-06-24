---
type: user_need
id: UN_010
short_name: Deprecated bundled pathway planning need
actor: Parent/carer of a young person with SEND
journey_stage: Pathway_planning
need: Deprecated bundled draft need from EVID_005. Use the superseding draft needs for active interpretation.
need_level: journey
parent_needs:
child_needs:
related_capabilities:
  - interpretability
  - agency
  - minimum_viable_dignity
related_civic_needs:
related_rights:
related_outcomes:
  - confident pathway planning
  - reduced self-discovery burden
evidence_scope_fit: direct
wording_sensitivity: high
status: deprecated
analysis_state: deprecated
evidence_basis: traceable
evidence_strength: weak
confidence: low
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: needs_review
change_level: material
supersedes:
superseded_by:
  - "[[UN_012]]"
  - "[[UN_013]]"
  - "[[UN_014]]"
  - "[[UN_007]]"
  - "[[UN_008]]"
  - "[[UN_009]]"
  - "[[UN_011]]"
  - "[[UN_016]]"
related_evidence:
  - "[[EVID_005]]"
related_behaviours:
related_pain_points:
related_insights:
importance: high
tags:
  - send
  - pathway-planning
  - parent-carer
  - rights
  - confidence
  - adjustments
  - bundled-need
---

# Deprecated bundled need about steps, rights and adjustments

## Working formulation

A parent/carer of a young person with SEND needs to know they have considered the important steps, rights and adjustments, so they can act with confidence rather than constant doubt.

## Deprecation rationale

This object is deprecated because it bundles several distinct jobs into one user need.

It combines:

- planning pathway steps
- checking rights and entitlements
- assessing or communicating adjustments and support needs
- reconciling information from different sources
- reducing doubt and increasing confidence

Those signals are important, but they do not share one coherent solution vector. A single guide, local offer page or pathway-planning tool could contain responses to all of them, but that would be a container solution rather than evidence that they are one need.

The original wording also uses the cognitive verb `know`. In this case, the wording hides more specific actions such as planning, checking, assessing, reconciling, revisiting and securing support.

This object should not be promoted, validated or used as a stable need. Use the superseding draft needs instead, while preserving this object as a record of the earlier bundled interpretation.

## Superseding draft needs

This bundled need is decomposed across existing and new draft needs:

- [[UN_012]]: planning before key education choices become fixed
- [[UN_013]]: assessing realistic options for the young person's circumstances
- [[UN_014]]: identifying viable routes if expected grades are not achieved
- [[UN_007]]: reconciling pathway information from different sources
- [[UN_008]]: assessing whether options are workable in daily life
- [[UN_009]]: revisiting pathway decisions after they have started
- [[UN_011]]: recognising the young person as an individual
- [[UN_016]]: checking rights and entitlements

## Evidence basis

- Supporting evidence: [[EVID_005]]
- Contextual evidence: [[RS_007]]
- Contradictory or limiting evidence:

## Interpretation

The evidence remains useful, but the earlier interpretation was too broad. Confidence is better treated as an outcome or value dimension across more specific needs, rather than as the glue holding several different jobs together.

The rights and entitlements signal is now captured separately in [[UN_016]]. Existing draft needs already cover pathway timing, realistic options, fallback routes, information reconciliation, practical feasibility, adaptation and recognition of the young person as an individual.

## Need hierarchy

- Parent needs:
- Child needs:
- Related capabilities: interpretability; agency; minimum viable dignity
- Related civic needs:
- Related rights:
- Related outcomes: confident pathway planning; reduced self-discovery burden

## Related problem-space objects

- Behaviours:
- Pain points:
- Insights:
- Value dimensions: confidence to act; reduced burden; rights awareness

## What remains uncertain

- Further review should check whether a higher-level parent need about guidance through pathway planning is needed.
- Further review should check whether one or more civic needs are needed around legible entitlements, navigable support and reduced reliance on informal advocacy capacity.
- The evidence remains low confidence because [[EVID_005]] is an evidence summary rather than a checked original transcript.

## Review notes

- Review date: TBC
- Reviewer: TBC
- Outcome: deprecated; needs review
- Notes: Deprecated because the object bundles multiple jobs and uses a cognitive formulation that hides more specific needs. This deprecation is an LLM-assisted semantic change and should be reviewed before treating the superseding structure as stable.

## Changelog

- 2026-06-12: Created as draft user need from [[EVID_005]]. Status: draft. Analysis state: evidence_linked. Evidence strength: weak. Review status: needs_review.
- 2026-06-12: Updated evidence link from [[EVID_004]] to [[EVID_005]] after renumbering the new evidence summary to avoid duplicate IDs.
- 2026-06-24: Deprecated as a bundled draft need after applying user need quality tests. Superseded by existing draft needs [[UN_012]], [[UN_013]], [[UN_014]], [[UN_007]], [[UN_008]], [[UN_009]], [[UN_011]] and new draft need [[UN_016]]. This is a material semantic change and remains needs_review.
- 2026-06-24: Updated the frontmatter `need` and `short_name` fields to make the deprecated state explicit while preserving the original bundled formulation in the body for traceability.
