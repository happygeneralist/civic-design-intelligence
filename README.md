# Civic design intelligence system

This repository is an Obsidian-compatible civic design intelligence system for public-service design, policy and decision-support work. The initial worked domain is SEND pathway planning.

The repository is in a public-source-first rebuild. The initial domain remains SEND pathway planning, but active evidence should come only from public, openly licensed or explicitly authorised sources. Most needs, pain points, behaviours, insights and civic questions should be captured at the highest useful level, with local context added where it materially affects interpretation, evidence, delivery or decision-making.

It is intended to help researchers, designers, product/service teams and decision-makers capture anonymised evidence, connect it to user needs, civic needs, behaviours, pain points, insights, value dimensions and solution assessments, and maintain a clear audit trail for how research knowledge develops over time.

The repository is not only for designing good services. It should also provide the human intelligence needed to challenge weak, harmful or solution-led decisions with a defensible evidence base.

## Public-source posture

Civic Design Intelligence treats user needs, civic needs, pain points, behaviours, insights and related design-intelligence objects as reusable civic knowledge objects.

These objects are not treated as proprietary to a source organisation merely because they describe needs experienced in a public-service context. They may exist as generic candidate objects where they express a reusable public-service pattern.

Evidence provenance is managed separately.

A candidate object only becomes evidence-linked when it is supported by public, openly licensed or explicitly authorised sources. Evidence records, source records and research-study records must make provenance clear and must not rely on private employer, client, council, partner or unpublished research material unless permission, consent, ownership and publication constraints are explicit.

The repository is public-source-first. Suitable evidence sources may include public inspection reports, Ombudsman decisions, statutory guidance, public consultation outputs, public council papers, openly published user research, charity reports, public datasets and other material that is lawful and appropriate to reuse.

Candidate objects without public or authorised evidence remain assumptions or candidates. They must not be treated as reviewed, validated or evidence-linked knowledge until their provenance and evidence basis support that status.

## Strategic vision

The repository is part of an emerging **civic design intelligence system**: open knowledge infrastructure for public-service needs, evidence, pain and decisions.

It is designed to become a shared, inspectable and contestable knowledge backbone for public services. Over time, it should help public institutions, third-sector organisations, professionals and members of the public contribute to a better shared understanding of what people need, where services cause harm or friction, and where public outcomes remain unsupported.

The repository should separate:

- evidence sources and external contributions
- candidate or submitted knowledge
- reviewed canonical knowledge objects
- decision records and design histories that reference those objects

External insight should strengthen the system without directly overwriting the canonical layer. Contributions from families, residents, third-sector organisations, advocates, professionals, public reports, inspections and academic studies should be treated as valuable evidence inputs that can support, challenge, refine or supersede existing knowledge objects.

## Locales and local context

The system should be able to support localised evidence and decisions without turning every knowledge object into a local-only object.

Use locale metadata when local context changes how an object should be interpreted, for example because of local policy, operational constraints, demographic context, commissioning arrangements, service configuration or evidence source.

Do not localise objects by default. Where a need, pain point, behaviour or insight is likely to apply across places, capture it at the highest useful level and link local evidence to it. Local variants can be created later where evidence shows that the local context materially changes the meaning, risk, priority or response.

## What this repository is for

Use this repository to store and work with:

- research study summaries
- anonymised evidence, quotes, observations and data points
- public, partner or professional contributions after appropriate triage
- academic, sector, Ombudsman, inspection, policy and operational evidence where relevant
- user needs
- civic needs
- behaviours
- pain points
- insights
- themes
- journeys
- value dimensions
- solution options and assessments
- review notes
- synthesis outputs

The repository should support evidence-based service design, reduce duplicated research, make value visible, and make it easier to understand what is known, what is assumed, what is contested, and what still needs validation.

## What this repository is not for

Do not store:

- raw transcripts
- recordings
- identifiable participant data
- special category personal data that has not been anonymised
- unsupported claims presented as validated findings
- LLM-generated synthesis without clear status and review metadata
- politically preferred solution ideas presented as evidence-backed recommendations
- persona or segment models presented as canonical outputs before the modelling convention is agreed

## Repository structure

```text
001_Research_studies/   Research activities and study summaries
002_Evidence/           Anonymised quotes, observations and data points
003_User_needs/         User needs, and civic needs during the MVP phase
004_Behaviours/         Observed or inferred behaviours
005_Pain_point/         Pain points and barriers
006_Insights/           Draft, reviewed and validated insights
007_Themes/             Cross-cutting themes
008_Personas/           Reserved for future persona or archetype work
009_Journeys/           Journey maps and journey-stage analysis
Templates/              Templates for creating structured notes
docs/                   Supporting documentation and governance material
```

Personas and segment models are deferred during the current MVP. They should not be created as canonical repository objects until the modelling approach has been developed, tested and documented.

## Core principle

Every meaningful claim should be traceable to evidence, or clearly marked as an assumption.

The repository distinguishes between:

- captured evidence
- submitted or candidate knowledge
- draft synthesis
- assumptions
- reviewed analysis
- validated findings
- value dimensions
- solution options and recommendations
- deprecated or superseded material

## Current MVP focus

The immediate MVP is safe ingestion of publicly available SEND pathway-planning evidence, using the current public-source rebuild as the worked context.

Use `docs/Safe_research_ingestion_MVP.md` before breaking research into structured objects. It defines the minimum conventions for creating evidence, behaviours, pain points, user needs, civic needs, insights and themes without making immature knowledge look settled.

Use `docs/Object_change_logs.md` when changing existing objects. The core rule is:

```text
If the change affects how the object should be interpreted, used, trusted or acted on, record it.

If the change only affects formatting, metadata or validation hygiene, rely on Git and the pull request summary.
```

## How to use this repository

1. Capture anonymised evidence in `002_Evidence/`.
2. Link evidence to studies, sources, actors, journey stages and tags.
3. Code evidence into user needs, civic needs, behaviours and pain points.
4. Draft insights from linked evidence.
5. Connect needs and insights to value dimensions where useful.
6. Assess solution options against needs, value, evidence, risks and assumptions.
7. Review assumptions, evidence basis and confidence.
8. Promote reviewed work to validated status only when the evidence supports it.
9. Record meaningful object-level changes in entry-level changelogs.
10. Use `CHANGELOG.md` for repository-level changes.

## Working with Obsidian

This repository is designed to work as an Obsidian vault. Use links, backlinks, properties and Bases to navigate between evidence, needs, behaviours, insights, value dimensions and solution assessments.

Shared Obsidian settings and Bases should support common repository behaviour. Personal workspace state, local plugin state and local-only notes should stay out of shared history.

## Working with LLMs

LLMs may be used to help classify, link, summarise and draft research material, but they must not be treated as evidence.

LLMs must not mark anything as validated, upgrade evidence strength, remove caveats or materially change validated research claims without human review.

See `llm-instructions.md` and `docs/LLM_safety_model.md`.

## Key documentation

- `docs/Civic_design_intelligence_system.md` defines the open civic design intelligence vision, contribution model and relationship to design histories.
- `docs/Safe_research_ingestion_MVP.md` defines the minimum safe-ingestion workflow for the current SEND pathway-planning worked example.
- `docs/Source_use_policy.md` defines the public-source-first evidence policy.
- `docs/User_needs_writing_rules.md` defines user need wording, including the `short_name` convention.
- `docs/Object_change_logs.md` defines when object-level changelogs are required and when Git and pull request history are enough.
- `docs/Obsidian_workflow.md` defines the recommended Obsidian workflow.
- `SCHEMA.md` defines object types, required fields and controlled values.
- `GOVERNANCE.md` defines repository governance and review responsibilities.
- `CONTRIBUTING.md` defines how to add and update material safely.
- `CHANGELOG.md` records repository-level changes.
- `docs/Evidence_standards.md` defines what counts as evidence.
- `docs/Review_process.md` defines review and validation steps.
- `docs/Value_and_decision_evidence.md` defines how value, solution assessment and decision evidence are handled.
