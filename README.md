# Civic design intelligence system

An Obsidian-compatible learning system for public-service research, design, policy and human judgement. SEND is the first substantial domain, not the limit of the model.

CDI maintains **persistent, evolving and contestable knowledge objects**: user needs, civic needs, evidence, pain, behaviours, insights and value relationships. The aim is not perfect statements. It is to make imperfect knowledge reusable, investigate tensions and improve understanding through evidence and practical use.

Services and journeys are possible responses to human needs, not their boundary. Detailed delivery work should stay connected to human experience, capabilities, rights and institutional responsibilities. Those relationships must themselves remain inspectable and challengeable; they are not decorative labels or preference weights that efficiency can automatically override.

## Start here

- [Needs semantic contract](docs/Needs_semantic_contract.md): current formulations, meaningful decomposition, contexts, value, fulfilment, relationships and civic anchoring.
- [Roadmap cursor](docs/Roadmap_cursor.md): actual next work and what not to overbuild.
- [Documentation map](docs/README.md): authority and navigation.
- [User-needs writing rules](docs/User_needs_writing_rules.md): practical application.
- [Governance](GOVERNANCE.md), [contribution guide](CONTRIBUTING.md) and [LLM instructions](llm-instructions.md): safe work and human authority.

## Useful knowledge at different levels

The system supports fast creation and slower, proportionate validation. A clearly labelled assumption or candidate can already help people explore policy coverage, generate design options, discover omissions and plan research. A consequential claim needs the evidence, applicability and human judgement appropriate to that use.

The working bronze/silver/gold language describes knowledge roles, **not confidence or validation**:

| Role | Owner and content |
| --- | --- |
| Bronze | The authorised source archive preserves originals, identity, versions, provenance and restrictions. |
| Silver | CDI captures selected evidence, source context and bounded interpretation. |
| Gold | Persistent needs and related civic intelligence support reusable views and decisions; candidates can participate without being certified. |

There is no compulsory linear pipeline. Knowledge can enter provisionally and be reconciled back to sources. Do not invent evidence, complete every field by guessing or require a finished rights/value map before retaining a useful candidate.

## Current working position

At the 5 November 2026 checkpoint, the private companion archive holds 331 originals (328 PDFs and three HTML captures). CDI's merged five-source test contains five source/study records and 13 selected evidence records. Those are distinct counts; the full corpus has not yet been analysed.

The next substantive experiment is [SEND pilot #99](https://github.com/happygeneralist/civic-design-intelligence/issues/99), following the bounded source-informed skill/reviewer calibration owned by [AI Capability Layer #39](https://github.com/happygeneralist/ai-capability-layer/issues/39). It tests breadth, decomposition, higher-level connections, contexts, tensions and useful candidate-level analysis—not merely a short list of polished needs. See the roadmap for live sequencing and draft-versus-merged status.

## Stable objects, useful forms

A need has a stable ID and a persisted current working formulation. `short_name` makes maps and comparisons legible. Authentic user language remains evidence; a user-facing reformulation is not an invented participant quotation. Value-oriented and computational views refer to the same objects and relevant revisions rather than changing their meaning for each audience.

Needs can connect to multiple contexts, constituent needs, broader needs, capabilities, rights, pains and outcomes. Not every connection is a parent-child hierarchy or causal relationship. Partial support and disagreement must remain visible. There is no fixed small number of needs per report; there is also no quota to manufacture thousands of unsupported synonyms.

## Public-source and privacy posture

This repository is public-source-first. Active evidence must come from public, openly licensed or explicitly authorised sources with clear reuse and sensitivity boundaries. A generic candidate can remain an assumption without revealing confidential employer, client, council or participant material.

The companion `happygeneralist/civic-design-secondary-research` repository is **private** and owns original public-source documents and their acquisition provenance. Some complete originals are held from public redistribution. Do not copy them into public CDI merely because an agent can access the private archive.

Evidence records must retain source voice, context and limits. Local evidence can inform a reusable hypothesis without establishing national prevalence, severity or causation. Public availability, institutional authority and fluent model output do not by themselves establish correctness or permission to republish.

Do not store raw transcripts, recordings, direct participant identifiers, unredacted cases, identifiable sensitive data, unsupported claims presented as validated findings or hidden LLM-generated synthesis.

## Contributions and review

Families, residents, professionals, advocates, researchers and other contributors can supply evidence, challenge interpretations, identify missing needs and propose refinements. Triage contributions for source, meaning, privacy and safeguarding before changing canonical objects.

Canonical identity does not mean validated truth: candidates can have stable identities too. Human-reviewed and validated states require explicit human authority. Participant recognition, expert wording review, evidence assessment and demonstrated need fulfilment are different judgements.

Preserve material changes and supersession without erasing prior understanding. A useful broad need can remain when its children are identified. Existing needs should not be bulk-rewritten to make them fit a newly polished framework.

## Repository structure

```text
000_Inbox/             Loose or unresolved material
001_Research_studies/  Research activities and source/study records
002_Evidence/          Permitted evidence with source voice and context
003_User_needs/        User needs and civic needs in the MVP
004_Behaviours/        Observed or explicitly inferred behaviours
005_Pain_point/        Conditions, barriers, burdens, harms and risks
006_Insights/          Interpreted patterns and explanations
007_Themes/            Cross-cutting organisation
008_Personas/          Reserved; canonical persona modelling deferred
009_Journeys/          Journey analysis and contextual/generated views
Templates/            Existing record templates
docs/                 Semantics, operations, research views and reviews
tools/                Deterministic structural validation
tests/                Structural regression tests
```

Use existing supported types and templates for value dimensions, opportunities and review notes. Solution-assessment views can reference needs; do not introduce an unsupported type or rewrite a need to match a preferred intervention.

## Ownership

CDI owns the knowledge model, research objects, meaning and review state. The source archive owns originals. AI Capability Layer owns reusable skills, review interfaces, adapters and evaluations. Design Intelligence Orchestration owns protected methods. A public participation interface is a separate authorised contribution route, not public access to private research or internal review tooling.

## Working with the repository

Use Obsidian links, properties, Bases and generated views to navigate rather than asking a person to read thousands of Markdown files. IDs have at least three digits and can grow without renumbering. Preserve aliases and stable canonical formulations.

Read `AGENTS.md` before coding or agent writes. Use focused branches and draft PRs. Preserve unrelated work and do not merge automatically. Record research meaning changes in the object changelog and, where required, an LLM intervention log; use Git/PR summaries for administrative edits.

Run:

```bash
python3 -m unittest discover -s tests -v
python3 tools/validate_repository.py
python3 tools/validate_repository.py --include-templates
```

The checks verify structure and declared-state consistency. They do not certify source truth, independent review, legal compliance or semantic reliability. Report warnings without rewriting research merely to make them disappear.

## Key references

[Schema](SCHEMA.md) · [Lifecycle](docs/Lifecycle_states.md) · [Evidence standards](docs/Evidence_standards.md) · [Source use](docs/Source_use_policy.md) · [Non-linear ingestion](docs/Non_linear_research_ingestion.md) · [Relationship meanings](docs/Relationship_types.md) · [Value and decisions](docs/Value_and_decision_evidence.md) · [Naming and links](docs/Naming_and_linking_contract.md) · [Change logs](docs/Object_change_logs.md) · [Changelog](CHANGELOG.md)
