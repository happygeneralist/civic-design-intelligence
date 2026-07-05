# Documentation map

This map helps contributors, reviewers and LLM assistants find the right repository guidance without treating every document as equally authoritative.

It reflects the current documentation audit. It does not resolve known overlaps or contradictions; those need separate human review.

This is a navigation map, not a file-move plan. It classifies the current documents in place.

## Start here

Read these first when you are new to the repository or choosing what to do next.

- `../README.md` - repository purpose, public-source posture, structure and key documentation.
- `../GOVERNANCE.md` - practical governance rules, roles, evidence boundaries and review authority.
- `../CONTRIBUTING.md` - how to add or update material safely.
- `Roadmap_cursor.md` - current operational focus, active guardrails and what not to overbuild.
- `Safe_research_ingestion_MVP.md` - minimum safe-ingestion conventions for the current MVP.

## Authority labels

Use these labels to decide how much weight to give a document.

| Label | Meaning |
|---|---|
| Source of truth | Controls a decision area unless a human reviewer explicitly supersedes it. |
| Current operating rule | Describes how contributors, reviewers or LLM assistants should work now. |
| Supporting guidance | Helps apply a source-of-truth rule, but does not override it. |
| Concept note | Explores an idea or future model; do not treat it as current instruction by default. |
| Roadmap direction | Describes current or future sequencing, including what has been deferred. |
| Worked example | Shows guidance in a bounded domain; do not generalise it automatically. |
| Historical or migration record | Preserves audit or migration context; do not treat it as current operating guidance by default. |
| Reference/background | Useful context that may inform work but should not control decisions alone. |

## Provisional Source Of Truth

This table is provisional. It identifies the first document to trust for common decisions while known overlaps are reviewed.

| Decision area | Start with | Authority | Supporting documents |
|---|---|---|---|
| Repository purpose and public-source posture | `../README.md` | Source of truth | `Civic_design_intelligence_system.md`, `Source_use_policy.md` |
| Governance, roles and validation authority | `../GOVERNANCE.md` | Source of truth | `Review_process.md`, `Lifecycle_states.md` |
| Human contribution workflow | `../CONTRIBUTING.md` | Current operating rule | `Safe_research_ingestion_MVP.md`, `Object_change_logs.md` |
| Codex start-of-work behaviour | `../AGENTS.md` | Current operating rule | `../llm-instructions.md`, `Codex_repository_automation.md` |
| LLM operating boundaries | `../llm-instructions.md` | Source of truth | `LLM_safety_model.md`, `LLM_intervention_logging.md` |
| Current operational focus | `Roadmap_cursor.md` | Current operating rule | `Knowledge_evolution_implementation_roadmap.md` |
| Source eligibility and public-source use | `Source_use_policy.md` | Source of truth | `Source_capture_workflow.md`, `Secondary_research_ingestion.md` |
| Evidence standards and contribution safety | `Evidence_standards.md` | Source of truth | `Input_and_evidence_classification.md`, `Research_study_scope.md` |
| Source-to-evidence ingestion path | `Ingestion_slice_workflow.md` | Current operating rule | `Source_capture_workflow.md`, `Input_and_evidence_classification.md`, `Safe_research_ingestion_MVP.md` |
| Lifecycle, review status and validation meaning | `Lifecycle_states.md` | Source of truth | `Review_process.md`, `Repository_validation.md` |
| Naming, IDs and links | `Naming_and_linking_contract.md` | Source of truth | `Repository_validation.md`, `ID_and_link_migration.md` |
| User-need wording | `User_needs_writing_rules.md` | Source of truth | `User_need_quality_tests.md`, `Needs_hierarchy.md`, `Decision_shaped_user_needs.md` |
| Template use and maturity | `Templates_and_maturity.md` | Supporting guidance | `../Templates/`, `Repository_validation.md` |
| Object changelog decisions | `Object_change_logs.md` | Source of truth | `Knowledge_evolution_strategy.md`, `LLM_intervention_logging.md` |
| Obsidian use and repository navigation | `Obsidian_workflow.md` | Supporting guidance | `Naming_and_linking_contract.md`, `Templates_and_maturity.md` |
| Strategy and theory | `Civic_design_intelligence_system.md` | Concept note | `Theory_of_change_MVP.md`, `Bridging_civic_design_intelligence_and_civic_ai.md` |
| Migration history | `../migration/validation-baseline-report.md` | Historical or migration record | `ID_and_link_migration.md`, `Governance_legal_basis.md` |

## For this question, read this first

| Question | Read first | Then read |
|---|---|---|
| What is this repository for? | `../README.md` | `Civic_design_intelligence_system.md`, `Theory_of_change_MVP.md` |
| What is the current phase? | `Roadmap_cursor.md` | `Knowledge_evolution_implementation_roadmap.md` |
| What sources may be used? | `Source_use_policy.md` | `Evidence_standards.md`, `Secondary_research_ingestion.md`, `Source_capture_workflow.md` |
| How do I ingest a bounded slice of material? | `Ingestion_slice_workflow.md` | `Input_and_evidence_classification.md`, `Safe_research_ingestion_MVP.md`, `Non_linear_research_ingestion.md` |
| How should raw or public source material be captured? | `Source_capture_workflow.md` | `Secondary_research_ingestion.md`, `Input_and_evidence_classification.md` |
| How do I classify an input before decomposing it? | `Input_and_evidence_classification.md` | `Ingestion_slice_workflow.md` |
| How should user needs be written? | `User_needs_writing_rules.md` | `User_need_quality_tests.md`, `Needs_hierarchy.md`, `Decision_shaped_user_needs.md` |
| How do I decide status, analysis state or review status? | `Lifecycle_states.md` | `Review_process.md`, `Repository_validation.md` |
| When is an object changelog needed? | `Object_change_logs.md` | `Knowledge_evolution_strategy.md`, `LLM_intervention_logging.md` |
| What can an LLM do safely? | `../llm-instructions.md` | `LLM_safety_model.md`, `LLM_intervention_logging.md` |
| What should Codex do before editing? | `../AGENTS.md` | `Codex_repository_automation.md`, `../llm-instructions.md` |
| How should files, IDs and links work? | `Naming_and_linking_contract.md` | `Repository_validation.md`, `ID_and_link_migration.md` |
| How do I use Obsidian with this repository? | `Obsidian_workflow.md` | `Naming_and_linking_contract.md`, `Templates_and_maturity.md` |
| What validator should I run? | `Repository_validation.md` | `../AGENTS.md` |
| Which template should I use? | `Templates_and_maturity.md` | `../Templates/` |
| How should personas or journeys be treated? | `Personas_and_journeys.md` | `Lifecycle_states.md`, `LLM_safety_model.md` |
| What historical migration decisions exist? | `../migration/validation-baseline-report.md` | `../migration/id-normalisation-audit.md`, `../migration/filename-migration-plan.md`, `../migration/user-need-file-renaming-plan.md` |

## Canonical controls

These documents define the main rules contributors and LLM assistants should treat as controlling unless a human reviewer explicitly says otherwise.

- `../GOVERNANCE.md` - repository governance, roles, validation authority and change control.
- `../CONTRIBUTING.md` - contributor workflow and safe note creation.
- `../llm-instructions.md` - operating rules for LLMs.
- `Source_use_policy.md` - public-source-first evidence policy.
- `Evidence_standards.md` - evidence kinds, source requirements, confidence and contribution safety.
- `Review_process.md` - review and validation steps.
- `Lifecycle_states.md` - how `status`, `analysis_state` and `review_status` work together.
- `Naming_and_linking_contract.md` - stable IDs, readable filenames, aliases and link rules.
- `Repository_validation.md` - validator philosophy, scope and expected use.
- `Object_change_logs.md` - when object-level changelogs are required.
- `User_needs_writing_rules.md` - primary user-need drafting and review rules.
- `Needs_hierarchy.md` - MVP need levels and parent/child need guidance.

## Ingestion workflows

Use these when bringing material into the repository.

- `Roadmap_cursor.md` - current ingestion emphasis and near-term guardrails.
- `Safe_research_ingestion_MVP.md` - minimum safe-ingestion defaults.
- `Non_linear_research_ingestion.md` - how knowledge can enter before full traceability is complete.
- `Input_and_evidence_classification.md` - how to classify entry state, evidence voice and overclaiming risk.
- `Source_capture_workflow.md` - how to capture and map sources before evidence extraction.
- `Ingestion_slice_workflow.md` - bounded slice workflow and reconciliation brief structure.
- `Ingestion_operating_model.md` - expert-assisted, guided and future semi-automated ingestion modes.
- `Secondary_research_ingestion.md` - cautious handling of public secondary research.
- `Research_breakdown_workflow.md` - first-pass breakdown workflow from inbox or source material.
- `Research_study_scope.md` - source scope, transferability and applicability fields.
- `Researcher_input_checklist.md` - older lightweight checklist for researchers adding material.

## Object guidance

Use these to create, review, interpret or evolve structured knowledge objects.

- `User_needs_writing_rules.md` - user-need wording rules.
- `User_need_quality_tests.md` - quality tests and validator warning basis.
- `Needs_hierarchy.md` - user, civic, experience, service, journey, task, page and interaction levels.
- `Decision_shaped_user_needs.md` - optional `need_shape: decision_support` convention.
- `User_need_persistence_and_deprecation.md` - persistence, supersession, deprecation and pain point lifecycle thinking.
- `Solution_vector_sensitivity.md` - how wording changes can alter implied solution direction.
- `Need_patterns.md` - emerging reusable need-pattern concept.
- `Context_and_pattern_sensemaking.md` - locality, service-area and pattern sensemaking.
- `Relationship_types.md` - emerging typed-relationship convention.
- `Personas_and_journeys.md` - provisional guidance for personas, segments and generated journeys.
- `Value_and_decision_evidence.md` - value dimensions, solution assessment concepts and decision evidence.
- `Change_events_structure.md` - optional future event records for meaningful knowledge changes.

## Strategy and theory

These explain the wider purpose and future direction. They should guide interpretation, but they are not usually the first documents for day-to-day object creation.

- `Civic_design_intelligence_system.md` - strategic definition and open civic intelligence model.
- `Theory_of_change_MVP.md` - minimum viable theory of change.
- `Bridging_civic_design_intelligence_and_civic_ai.md` - relationship to civic AI, collective intelligence and open government.
- `Knowledge_evolution_strategy.md` - strategy for preserving knowledge evolution over time.
- `Value_and_decision_evidence.md` - decision and value rationale for the repository.
- `drafts/AI_public_page_draft.md` - draft public-facing explanation of AI use.

## Roadmap and status

Use these to understand what is current, what has been deferred and what should not be overbuilt yet.

- `Roadmap_cursor.md` - current operational pointer.
- `Knowledge_evolution_implementation_roadmap.md` - staged roadmap and implementation sequencing.

## Automation and agent guidance

Use these when Codex, ChatGPT or another LLM is doing repository work.

- `../AGENTS.md` - Codex start-of-work checks, branch workflow, changelog rules and validation expectations.
- `../llm-instructions.md` - LLM operating instructions.
- `LLM_safety_model.md` - LLM risk model, safe tasks and review responsibilities.
- `LLM_intervention_logging.md` - when to log material LLM semantic changes.
- `LLM_research_breakdown_prompts.md` - reusable prompts for first-pass breakdown and review.
- `Codex_repository_automation.md` - appropriate Codex uses and boundaries.

## Templates

Templates shape future repository objects. Treat changes to them as repository infrastructure changes and validate with template checks.

- `../Templates/User_need_template.md`
- `../Templates/Civic_need_template.md`
- `../Templates/Evidence_template.md`
- `../Templates/Behaviour_template.md`
- `../Templates/Pain_point_template.md`
- `../Templates/Insight_template.md`
- `../Templates/Theme_template.md`
- `../Templates/Opportunity_template.md`
- `../Templates/Value_dimension_template.md`
- `../Templates/Journey_template.md`
- `../Templates/Persona_template.md`
- `../Templates/Research_study_template.md`
- `../Templates/Study_template.md`
- `../Templates/Review_note_template.md`
- `../Templates/Loose_capture_template.md`

## Migration and historical records

These preserve migration context and audit history. Do not treat them as the current operating guide when a canonical or roadmap document says otherwise.

- `../migration/validation-baseline-report.md`
- `../migration/id-normalisation-audit.md`
- `../migration/filename-migration-plan.md`
- `../migration/user-need-file-renaming-plan.md`
- `ID_and_link_migration.md`
- `Governance_legal_basis.md`

## Known audit notes not resolved here

The documentation audit identified overlaps and possible contradictions. This map records where to look; it does not resolve them.

- LLM rules are repeated across governance, contributor, LLM and Codex guidance.
- Ingestion guidance is intentionally distributed across source capture, input classification, slice workflow and safe-ingestion documents.
- Some older first-pass guidance uses `evidence_basis: indicative` where newer safe-ingestion defaults may use `evidence_basis: none` or `evidence_strength: none`.
- Persona guidance is intentionally cautious, but the exact boundary between deferred canonical personas and generated/contextual views still needs human review.
- Some templates may lag newer guidance, especially evidence-kind and source-capture fields.
- Some legal or migration documents are historical and may not fully reflect the current public-source-first posture.
