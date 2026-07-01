# Relationship types

This note captures an emerging convention for graph-ready relationships between structured knowledge objects.

It is intentionally lightweight. Do not treat this as a required schema until real ingestion examples show which relationship types are useful and stable.

## Purpose

The repository already uses fields such as `related_evidence`, `related_needs`, `related_behaviours`, `related_pain_points`, `related_insights` and `related_themes`.

Those fields are useful for Obsidian navigation and early research breakdown. As the repository matures, some relationships may need to be more explicit so future queries, dashboards, generated journeys, civic AI tools or policy/design-history references can distinguish different meanings.

For example, a pain point may be related to a user need because it blocks the need, evidences the need, results from the need being unmet, or has been addressed by a service response. Those relationships should not all be treated as the same claim.

## Current MVP rule

Use existing `related_*` fields during safe ingestion.

When a relationship needs more precision, note it in the object body, PR summary or review notes. Do not add required relationship fields or validator rules yet.

The goal during the next ingestion passes is to observe which relationship types recur and which are actually useful.

## Candidate relationship types

Candidate types include:

| Relationship type | Meaning |
|---|---|
| `evidenced_by` | The target evidence directly or contextually supports the object. |
| `supports` | The source object helps uphold, enable or strengthen the target object. |
| `blocked_by` | The target object prevents, burdens, delays or undermines the source object. |
| `challenged_by` | The target evidence or object weakens, contradicts or limits the source object's interpretation. |
| `supersedes` | The source object replaces an earlier object while preserving lineage. |
| `local_variant_of` | The source object is a local or context-specific expression of a wider object. |
| `addressed_by` | A service, policy, solution, intervention or decision-history artefact claims to respond to the object. |
| `context_for` | The target object provides service, organisation, locality, policy or operational context for interpretation. |

Do not expand this list unless real examples require it.

## Possible future structure

A future optional frontmatter structure might look like this:

```yaml
relationships:
  - type: evidenced_by
    target: "[[EVID_000]]"
    note: Direct evidence for this wording and journey level.
  - type: blocked_by
    target: "[[PP_012]]"
    note: This pain point prevents the need being met in practice.
```

This is not required during the current MVP.

## Relationship to existing fields

Do not remove existing `related_*` fields.

They remain useful for quick capture, Obsidian navigation and backwards compatibility.

Typed relationships may later sit alongside them where the relationship meaning matters for analysis, reporting or generated views.

## User need protection rule

Policy, service, solution and design-history artefacts may reference user needs, but they should not determine or rewrite the canonical wording of user needs.

Use relationship types to show how external artefacts claim to respond to user needs, not to make user needs fit institutional framing.

## When to introduce this formally

Consider formalising typed relationships only after one or more safe-ingestion PRs show:

- repeated ambiguity in generic `related_*` links
- useful query or dashboard questions that need relationship meaning
- generated journey or service views that need to distinguish blockage, support, evidence and service response
- policy, design-history or solution-assessment references that need to point to stable objects without rewriting them

Until then, keep the convention observational and optional.
