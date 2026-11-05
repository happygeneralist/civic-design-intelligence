# Documentation map

This map distinguishes current authority, supporting guidance, concepts and historical examples. It is not a file-move plan.

## Start here

- [Repository purpose](../README.md)
- [Current roadmap cursor](Roadmap_cursor.md)
- [Needs semantic contract](Needs_semantic_contract.md)
- [Governance](../GOVERNANCE.md), [contributing](../CONTRIBUTING.md), [agent controls](../AGENTS.md)

## Authority for the current pilot

| Decision | Controlling reference | Supporting material |
| --- | --- | --- |
| Need identity, roles, contexts, value, fulfilment and civic anchoring | `Needs_semantic_contract.md` | `User_needs_writing_rules.md`, `Needs_hierarchy.md`, `Relationship_types.md` |
| Practical need formulation and review | `User_needs_writing_rules.md`, `User_need_quality_tests.md` | `User_needs_quality_public_summary.md`, `Solution_vector_sensitivity.md`, `Decision_shaped_user_needs.md` |
| Human authority, privacy and research validation | `../GOVERNANCE.md`, `Source_use_policy.md`, `Evidence_standards.md` | `Review_process.md`, `Lifecycle_states.md` |
| LLM and coding-agent behaviour | `../llm-instructions.md`, `../AGENTS.md` | `LLM_safety_model.md`, `LLM_intervention_logging.md` |
| Immediate sequencing and scope | `Roadmap_cursor.md` | `Knowledge_evolution_implementation_roadmap.md` is background where its earlier sequence differs |
| Fields, types, IDs and links | `../SCHEMA.md`, `Naming_and_linking_contract.md` | `Repository_validation.md`, actual `../Templates/` and validator |
| Candidate use and value assessment | `Ingestion_operating_model.md`, `Value_and_decision_evidence.md` | `Non_linear_research_ingestion.md` |
| Source-to-object work | `Ingestion_slice_workflow.md`, `Secondary_research_ingestion.md` | `Source_capture_workflow.md`, `Input_and_evidence_classification.md`, `Safe_research_ingestion_MVP.md` |
| Material knowledge changes | `Object_change_logs.md`, `LLM_intervention_logging.md` | `Knowledge_evolution_strategy.md`, `User_need_persistence_and_deprecation.md` |

The semantic contract explicitly clarifies older blanket advice about a single hierarchy, a small number of outputs, context in every sentence, automatic retirement after decomposition, or validation before any use. Those older examples must not override it. Research safety and human authority remain in force. Do not silently treat a historical draft or one worked example as universal method.

A broad parent can remain after constituent needs are created. Public-safe research can capture explicit assumptions and candidate relationships before full evidence. Different views must refer to the current stable object rather than rewrite it on demand. No new mandatory ontology is implied.

## Questions and routes

| Question | Read |
| --- | --- |
| How do needs support learning before validation? | `Needs_semantic_contract.md`, `Ingestion_operating_model.md`, `Non_linear_research_ingestion.md` |
| How do I decompose or ladder needs without forcing a tree? | `Needs_hierarchy.md`, `Relationship_types.md`, `User_need_quality_tests.md` |
| How do context and short/user-facing/value formulations work? | `Needs_semantic_contract.md`, `User_needs_writing_rules.md`, `Naming_and_linking_contract.md` |
| How do rights and capabilities constrain value analysis? | `Needs_semantic_contract.md`, `Value_and_decision_evidence.md` |
| What may be used as a source? | `Source_use_policy.md`, `Evidence_standards.md`, `Research_study_scope.md` |
| How do I capture or reconcile partial research? | `Non_linear_research_ingestion.md`, `Input_and_evidence_classification.md`, `Ingestion_slice_workflow.md` |
| What can an agent write or promote? | `../AGENTS.md`, `../llm-instructions.md`, `Lifecycle_states.md` |
| Where does the reviewer interface belong? | AI Capability Layer #39; CDI owns knowledge and review states, not a separate application |
| What checks should run? | `Repository_validation.md`, `../AGENTS.md`, `../tests/test_need_contract.py` |
| When does a change need a record? | `Object_change_logs.md`, `LLM_intervention_logging.md` |

## Source and ingestion guidance

- `Source_capture_workflow.md` — source preservation, scope and provenance.
- `Secondary_research_ingestion.md` — companion private archive, source voice and registration.
- `Input_and_evidence_classification.md` — entry state and evidential basis.
- `Safe_research_ingestion_MVP.md` — minimum safe defaults; not a requirement for a tiny output set.
- `Ingestion_slice_workflow.md` — bounded research work; source scope is not a candidate-count cap.
- `Ingestion_operating_model.md` — modes and candidate-level value.
- `Non_linear_research_ingestion.md` — capture before complete traceability, without disguising gaps.
- `Research_breakdown_workflow.md` — public-safe workflow overview.
- `Research_study_scope.md` — source context and transferability.
- `Researcher_input_checklist.md` — older supporting checklist.
- `LLM_research_breakdown_prompts.md` — public summary, not a protected prompt catalogue.

## Object guidance

- `Needs_semantic_contract.md` — shared semantic roles and learning principle.
- `User_needs_writing_rules.md` — formulation rules.
- `User_need_quality_tests.md` — advisory quality questions and omission checks.
- `Needs_hierarchy.md` — levels, decomposition, laddering and contexts.
- `Relationship_types.md` — relationship propositions and tensions, without a required new schema.
- `User_need_persistence_and_deprecation.md` — persistence and historical evolution guidance; retirement applies when a proposition is replaced, not merely expanded into children.
- `Decision_shaped_user_needs.md` — optional decision-support framing.
- `Solution_vector_sensitivity.md` — effects of wording; possible response diversity is not by itself proof that a broad need is invalid.
- `Need_patterns.md`, `Context_and_pattern_sensemaking.md` — supporting pattern concepts.
- `Personas_and_journeys.md` — deferred canonical personas and contextual/generated views.
- `Value_and_decision_evidence.md` — expected/realised value, fulfilment and rights-aware comparison.
- `Change_events_structure.md` — optional future event records, not duplicate Git history.

## Templates

Use the actual templates under `../Templates/` for user needs, civic needs, evidence, behaviours, pain points, insights, themes, opportunities, value dimensions, journeys, research studies, review notes and loose capture. Canonical persona modelling remains deferred. Optional body sections are not an obligation to invent missing information.

Validate template changes with `python3 tools/validate_repository.py --include-templates`. Passing structural checks does not establish semantic correctness or human review.

## Strategy and background

`Civic_design_intelligence_system.md`, `Theory_of_change_MVP.md`, `Bridging_civic_design_intelligence_and_civic_ai.md`, `Knowledge_evolution_strategy.md` and `drafts/AI_public_page_draft.md` explain the broader ambition. They do not authorise unbounded agent writes, automatic policy decisions or disclosure of private sources.

`Obsidian_workflow.md`, `Templates_and_maturity.md` and `Codex_repository_automation.md` support practical use. The current roadmap takes precedence over old sequencing. Preserve protected detailed methods in Design Intelligence Orchestration, reusable capability in AI Capability Layer, and source originals in their authorised archive.

## Historical and migration material

`Documentation_inventory_provisional.md`, `Repository_documentation_architecture_plan.md`, `ID_and_link_migration.md`, `Governance_legal_basis.md` and `../migration/` retain earlier decisions and snapshots. They are not current instructions where a controlling document explicitly supersedes them. This update is not a wholesale historical rewrite or an independent revalidation of their sources.

## Worked research views

- [SEND waiting, support and navigation: five-source comparison](research-views/ISSUE_097_send_waiting_support_navigation.md) — provisional, LLM-assisted, human review still outstanding.
- [5 November needs operating audit](reviews/2026-11-05_needs_operating_audit.md) — scope, corrections, executable checks and unresolved research-record questions.
