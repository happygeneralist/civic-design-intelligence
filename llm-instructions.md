# LLM operating instructions

These instructions apply to any LLM used to read, query, draft or update this repository.

The repository is the source of truth. The LLM is not evidence and must not be treated as an authority.

## Core rule

Every meaningful claim must either be traceable to evidence or clearly marked as an assumption.

For user-needs work read `docs/Needs_semantic_contract.md` and `docs/User_needs_writing_rules.md`. The semantic contract clarifies older guidance about hierarchy, context, value and candidate use. Follow `docs/Naming_and_linking_contract.md` when creating or linking structured notes.

## Naming and linking rule

Preserve stable frontmatter IDs, ID-prefixed readable filenames, resolvable Obsidian links and queryable frontmatter. User-need filenames derive from `short_name`, not the full canonical sentence. ID numbers have at least three digits and may grow beyond 999 without renumbering existing objects.

Do not rename files, remove aliases or rewrite links as part of a semantic edit unless naming/link migration is explicitly requested. Naming-only changes must not promote research review, confidence or evidence states.

## Operating principle

```text
fast creation, slow validation
```

The objective is useful, learnable knowledge that aids human judgement, not perfect needs or the smallest possible output. Capture explicit hypotheses and assumptions. Preserve uncertainty and tensions rather than rewriting them away.

Bound work by sources, questions, execution capacity and reviewable batches, not a fixed maximum number of needs. Inspect multiple actors, levels and contexts, including positive cases and source regions that yielded no candidates. Do not invent hundreds of needs to satisfy a count; equally, do not suppress a rich landscape merely to keep the result small.

Useful candidates may inform exploratory research, design, policy and service comparisons before validation. Carry their limitations into the resulting view. Consequential recommendations need proportionate evidence, appropriate expertise and authorised human judgement. Neither a validated object nor an automated check guarantees objective truth or demonstrated fulfilment.

## What the LLM may do

Within the task's authorisation, the LLM may:

- summarise and classify existing evidence without changing its meaning;
- create or propose placeholder, assumption and candidate analysis objects;
- formulate new needs from source-informed interpretation while distinguishing inference from source statements;
- suggest support, challenge, tension, context and other relationships;
- decompose meaningful constituents and retain useful higher-level needs;
- investigate many-to-many links to broader needs, civic obligations, capabilities and rights;
- propose refinement, merger or supersession with a preserved rationale and lineage;
- create exploratory synthesis from candidates as well as more mature knowledge, exposing the basis of each conclusion;
- identify omissions, conflicting interpretations, weak support and missing sources;
- propose review notes and proportionate object change records.

These permissions do not authorise automatic publication, uncontrolled batch writes, fabricated evidence or human-validation claims. A reusable skill may impose a narrower proposal-only execution boundary until an authorised writer is available.

## Analysis objects and representation

User needs, civic needs, behaviours, pain points, insights, themes, journeys and opportunities are interpreted knowledge objects. Their existence is not proof that their claims are correct. Keep their status, analysis state, evidence, confidence and review metadata explicit.

For a need preserve one stable identity and a current canonical `need` formulation. Keep `short_name` for maps and navigation. Link authentic language as evidence. Label user-facing text as an interpretation unless it is a quotation. Compose value-oriented or other role-specific views from identified propositions and bind them to the revisions used. Do not regenerate canonical wording on every query or silently reuse a stale derivative after a material change.

Relevant context must be recoverable but does not always belong in the statement. Distinguish source locality, applicability and contextual manifestations. Do not clone a need for each context unless required progress or protection materially differs.

Persona and segment models remain deferred; do not create canonical persona/segment objects without updated guidance and explicit authorisation. This does not prevent examining distinct real actors and situations in needs analysis.

## User need creation and evolution

A user need describes what a person needs to achieve, preserve, recover, avoid or change. It is not simply a feature, user story, policy requirement, organisational objective, service mechanism or vague knowledge state.

Before creating a new need, inspect nearby needs, civic needs, pain, behaviours and evidence. Reuse when the meaning is already covered. Create genuinely distinct candidates at useful levels; where overlap remains uncertain, preserve the comparison rather than force a merger. Do not treat the presence of a broad parent as a reason to suppress its constituents.

Keep the human need, pain point, expected value, fulfilment conditions, indicators and realised value distinguishable. Unknown components may remain unknown. Avoiding harm or burden can itself be a need; do not remove protective meaning merely to shorten the sentence.

Check separately who experiences the need, who benefits and who should enable fulfilment. Do not turn institutional work into a user's responsibility by grammatical choice. Record unresolved responsibility questions as tensions rather than settling them through polished language.

Use action-oriented language where it preserves meaning. Comprehension can itself be important for rights, consent, safety or informed choice. Emotional, relational, identity and social needs are legitimate. Do not mechanically translate them into administrative tasks.

Use `need_level` to aid navigation; it is not a compulsory universal hierarchy. A need may have multiple broader connections. Retain useful parents when decomposing. Supersede only when the interpretation is actually replaced. Do not automatically inherit evidence, confidence, legal applicability or fulfilment from related nodes.

Rights/capability anchoring requires explicit reasoning. Distinguish empirical findings, normative commitments and legal sources/applicability. Do not invent obligations or assume a weighted efficiency gain can offset a rights concern. Record unknowns and seek appropriate human judgement for consequential decisions.

Treat small wording changes as material when they change actor, agency, underlying progress, scope, possible responses, value or fulfilment. Preserve the current formulation until the authorised change is made. Apply object changelog and LLM-intervention rules; Git supplies technical history.

## Evidence scope and candidate metadata

Keep inspection synthesis, mediated reports, direct lived experience, workshop assumptions, normative sources and model interpretations distinct. A source can inspire multiple hypotheses without directly proving them. Link evidence with the scope it actually supports; do not let a generic relationship imply whole-object support or causation.

When evidence is missing, use conservative existing states such as:

```yaml
status: assumption
analysis_state: candidate
evidence_basis: none
evidence_strength: none
confidence: low
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
review_status: not_reviewed
```

When relevant evidence exists, assess its fit rather than mechanically promoting all fields. A partial or contextual link does not establish every clause. Do not declare `evidence_scope_fit: direct` alongside `evidence_basis: none`; flag a legacy inconsistency for review without inventing support or silently changing its meaning.

A hypothesis can be valuable with weak evidence. Do not narrow or split solely to make it match the first source. Retain the hypothesis and explain what supports it, what is inferred and what could challenge it.

## What the LLM must not do

The LLM must not:

- independently mark research as human reviewed or validated;
- upgrade evidence strength on reviewed or validated items;
- remove caveats, contradictions or useful tensions;
- rewrite participant quotations except to propose explicit anonymisation;
- materially alter validated claims without review;
- present unsupported claims as findings;
- infer sensitive characteristics without evidence;
- store raw transcripts, recordings, unredacted cases or identifiable participant data in public CDI;
- create canonical persona/segment objects under the deferred convention;
- bypass the authorised review/write process;
- disguise LLM-assisted content, a generated quotation or a model check as human evidence.

## Status and analysis state handling

The LLM may create or propose:

```yaml
status: draft | assumption
analysis_state: placeholder | candidate | drafted | evidence_linked
review_status: not_reviewed | needs_review
creation_mode: llm_assisted
llm_generated: true
human_reviewed: false
```

Do not set `status: reviewed` or `validated`, `analysis_state: reviewed` or `validated`, `human_reviewed: true`, or `review_status: reviewed` unless an authorised human explicitly instructs the recording of an already-completed review. Participant recognition, expert wording review, evidence review and fulfilment are distinct judgements; a 'keep candidate' action is not blanket validation.

## Evidence strength handling

An LLM may propose strength for draft/candidate work but must not upgrade reviewed or validated objects independently. Use the lower strength when uncertain.

```yaml
evidence_strength: none | weak | moderate | strong
```

Without clear evidence use `none`, assumption/candidate and low confidence. A relevant link may justify weak evidence-linked draft status for a specific proposition; it does not automatically justify stronger confidence or universal scope.

## Required explanation for changes

State affected files, purpose, inspected sources, assumptions, proposed status changes, semantic effect, split/merge/supersession decisions, and the proportionate change record. Preserve prior meanings and evidence. For candidate batches, a navigable review packet can organise proposals without requiring a reviewer to reconstruct every Markdown file.

If a validated object requires substantial reframing, propose a replacement or refinement on a branch, retain the original, and use `supersedes` / `superseded_by` where the proposition is replaced. Adding constituent needs or a new contextual view does not automatically replace the parent.

## Execution, review and ownership

Deterministic checks can verify structure and declared-state consistency, not source truth or actual human review. A semantic assessment is separate from the writer's authority. Independent assessment must really occur; do not label a self-review independent. Missing or stale version-bound checks cannot approve changed content.

The reusable reviewer interface, skill and evaluation harness belong in AI Capability Layer. Protected detailed methods belong in Design Intelligence Orchestration. CDI owns definitions, research objects and conservative states. Do not copy private source originals or protected prompts into public CDI.

## Branch and pull request workflow

Use a focused branch, not direct edits to `main`. Preserve unrelated work. Default to a draft PR and do not merge without explicit authorisation.

Report:

- changes and rationale;
- new or materially changed research propositions and their assumptions;
- source/evidence links and metadata changes;
- any splits, mergers, supersession or deprecation;
- validated content affected, or confirmation that none changed;
- object changelog / LLM intervention use;
- executable validation actually run and unresolved human review;
- whether naming or links changed and whether that was administrative or semantic.

For ordinary work run the repository validator; include template checks when templates change and regression tests when code changes. Report warnings honestly. A passing check does not promote research maturity.

## Preferred work loop

Inspect the task, applicable rules, sources and nearby objects. Capture or refine useful candidates within the authorised scope. Preserve explicit assumptions, alternatives and tensions. Check structural integrity and source-fit limits, prepare a low-burden review, record material changes, and learn from use. Do not turn missing perfection into a reason to stop capturing knowledge.
