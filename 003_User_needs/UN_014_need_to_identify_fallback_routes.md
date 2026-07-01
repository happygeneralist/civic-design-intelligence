---
type: user_need
id: UN_014
short_name: Need to identify fallback routes
actor: Parent/carer of a young person with SEND
journey_stage: Pathway_planning
need: A parent/carer of a young person with SEND needs to identify viable post-16 routes if expected grades are not achieved, so they can plan a credible next step.
need_level: task
need_shape:
  - decision_support
parent_needs:
  - "[[UN_013]]"
child_needs:
related_capabilities:
  - agency
  - interpretability
related_civic_needs:
related_rights:
related_outcomes:
  - credible fallback planning
  - reduced late-stage uncertainty
evidence_scope_fit: direct
wording_sensitivity: medium
status: assumption
analysis_state: candidate
evidence_basis: none
evidence_strength: none
confidence: low
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: needs_review
change_level: material
supersedes:
superseded_by:
related_evidence:
related_behaviours:
related_pain_points:
related_insights:
importance: high
tags:
  - send
  - pathway-planning
  - parent-carer
  - post-16
  - entry-requirements
---
# Identify viable routes if expected grades are not achieved

## Working formulation

A parent/carer of a young person with SEND needs to identify viable post-16 routes if expected grades are not achieved, so they can plan a credible next step.

## Wording rationale

The wording reframes the evidence as an action-oriented need: identifying viable routes. It avoids turning uncertainty about GCSE outcomes into a vague information need and avoids prescribing a specific service response.

## Public-source reset note

Retained as a generic candidate civic knowledge object. Source-specific evidence links were removed during the public-source reset. This object should not be treated as evidence-linked until supported by public or explicitly authorised sources.

## Interpretation

This candidate assumes that pathway planning is not credible if families do not know what options remain available when standard grades or entry requirements are not met. This is a concrete decision-support need within a broader need to compare realistic options.

## Need hierarchy

- Parent needs: [[UN_013]]
- Child needs:
- Related capabilities: agency; interpretability
- Related civic needs:
- Related rights:
- Related outcomes: credible fallback planning; reduced late-stage uncertainty

## Related problem-space objects

- Behaviours:
- Pain points:
- Insights:
- Value dimensions: contingency planning; confidence to act; reduced burden

## What remains uncertain

- The specific routes and entry requirement issues need checking against public or explicitly authorised evidence.
- This may need a related civic need if evidence shows a systemic obligation to make fallback routes visible.

## Review notes

- Review date: TBC
- Reviewer: TBC
- Outcome: needs review
- Notes: Check whether `post-16` is the right scope or whether this should cover post-18 transition as well.

## Changelog


- 2026-06-24: Removed source-specific evidence links during public-source reset. Retained as a generic candidate civic knowledge object. Status changed to assumption; analysis_state changed to candidate; evidence_basis and evidence_strength changed to none. Review status remains needs_review.
- 2026-06-12: Renumbered from `UN_004` to `UN_014` to avoid collision with existing `UN_004.md`.
- 2026-06-15: Added `short_name` as a compact mapping label. Canonical need wording, evidence links and review state unchanged.
- 2026-06-16: Added `need_shape: decision_support` and `planning` to make the existing decision-support interpretation queryable. Canonical need wording, evidence links and review state unchanged.
- 2026-06-16: Removed `planning` from `need_shape` because `decision_support` is the only formally introduced MVP value. Canonical need wording, evidence links and review state unchanged.
