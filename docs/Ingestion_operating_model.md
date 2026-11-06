# Ingestion operating model

This document describes how research ingestion should work as the repository moves from expert-led experimentation towards repeatable, reviewable and eventually more automated workflows.

It should be read alongside:

- `docs/Non_linear_research_ingestion.md`
- `docs/Safe_research_ingestion_MVP.md`
- `docs/Ingestion_slice_workflow.md`
- `docs/User_needs_writing_rules.md`

## Product problem

The repository needs to ingest a significant amount of research material while preserving meaning, provenance, uncertainty and object quality.

The current expert-assisted workflow is useful while the model is still being discovered, but it must not become the permanent operating model.

The repository should not depend on one expert holding the ingestion model in their head.

## Operating principle

```text
Move from expert-led ingestion to system-supported ingestion, with human review focused on exception handling, semantic risk and public accountability.
```

The system should help contributors and reviewers get knowledge into the repository without requiring them to understand every object convention, schema decision or previous research judgement.

## Useful knowledge before validation

The aim is to develop a living, reusable population of user needs and related civic knowledge, not to wait until every object is fully reviewed before deriving any value. **An evidence-grounded candidate user need is already a useful knowledge object** when the source, actor, context, wording, limits and review status are visible. Its value and use should deepen as the same persistent object is tested, challenged and refined; do not generate a new need merely because a small wording improvement is proposed.

Different uses require different evidence claims:

- **Capture and exploration:** identify candidates, missing needs, overlaps, positive and negative cases, and research questions, even where evidence is partial.
- **Provisional comparison:** use candidates to investigate possible gaps between needs, policy intent, service provision, solution concepts and public value. Carry each candidate's evidence scope and uncertainty into the comparison; record apparent gaps as hypotheses, not as demonstrated policy failure or actual user outcomes.
- **Consequential decisions:** require proportionate source checking, evidence fit, context/applicability review and authorised human judgement before relying on a claim for policy, service, prioritisation, evaluation or public communication. These checks are about the **claim and intended use**, not a requirement that every repository object first become validated.

User needs remain first-class, stable-identity but revisable interpretations. Small changes to actor, action, object, context or outcome can change which responses are appropriate. Review the evidence and nearby existing objects before proposing material wording changes, splits, mergers or supersession; preserve rationale and earlier meaning. The correct result of an extraction or decomposition may be **no new user need**.

### Working knowledge layers (not maturity states)

The terms below are a working description to test with real material, **not** a new schema, approval ladder, three-level confidence scale or assertion that all objects must pass through a linear sequence:

| Layer | Current repository role | Useful output |
| --- | --- | --- |
| **Bronze — preserved source material** | `civic-design-secondary-research` owns original documents, source identity, versions, provenance and restrictions. | Reliable source discovery and inspection. |
| **Silver — selected evidence and bounded interpretation** | CDI holds research/source records, evidence claims, contextual/limiting relationships, contradictions and provisional analysis. | Pattern investigation and explicit evidential boundaries. |
| **Gold — reusable needs and civic intelligence** | CDI holds persistent user/civic needs and their links to pain, behaviours, outcomes and value; candidates **can participate** without being human validated. | Research planning, provisional policy/service comparisons and increasingly defensible decision support. |

Knowledge role, evidence basis, confidence, lifecycle and human review are **independent dimensions**. These tiers must not imply that a captured source or evidence record is inferior or that a candidate need is certified. An object may enter at a suitable level and be reconciled backwards to evidence when necessary. Use existing CDI fields; do not introduce `bronze`, `silver` or `gold` frontmatter as a substitute for them.

The next substantive test is [candidate-needs pilot #99](https://github.com/happygeneralist/civic-design-intelligence/issues/99), building on the Essex fit review in PR #88, delay claim review in PR #94 and the five-source PR #98. **Test deep specialist operations before building a broad agent router.** Whether need evaluation and decomposition are modes of one skill or distinct reusable skills remains an evaluation question.

## Three operating modes

### 1. Expert-assisted ingestion

This is the current mode.

Use it for:

- early ingestion slices
- new or messy source types
- sensitive user needs
- unclear object boundaries
- uncertain behaviour or pain point granularity
- first examples of a new workflow
- material where emotional, social, civic or relational meaning could easily be flattened

Typical workflow:

```text
ChatGPT sensemaking
→ Codex repository reconnaissance
→ human semantic review
→ Codex implementation PR
→ human review and merge
```

This mode is slower, but it teaches the system which rules, examples and checks need to become repeatable.

### 2. Guided contributor ingestion

This is the medium-term target.

A contributor should be able to add material through a guided workflow without understanding the whole repository.

The workflow might be:

```text
upload or input material
→ answer guided questions
→ LLM creates an ingestion slice
→ system proposes evidence, objects and links
→ reviewer accepts, edits, rejects or flags
→ PR is created automatically
```

The system should show prompts such as:

- this may be a user need
- this looks like a behaviour, not a need
- this may overlap with an existing object
- this pain point may already exist
- this wording may contain a solution
- this evidence link is missing
- this severity judgement needs comparison with nearby pain points
- this needs human judgement before publication

The contributor should not need to decide every object boundary alone.

### 3. Semi-automated ingestion pipeline

This is a later mode for repeated source types and larger ingestion volumes.

Possible workflow:

```text
source capture
→ automatic source metadata
→ candidate evidence extraction
→ candidate object generation
→ automated object matching
→ risk and uncertainty surfacing
→ PR with reconciliation brief
→ human review where needed
```

The pipeline may automate capture, comparison, linking and risk surfacing. It should be cautious about automating semantic acceptance.

## Tool roles

### ChatGPT

Use ChatGPT for semantic judgement, sensemaking and review.

Good uses:

- framing an ingestion slice
- interpreting ambiguous material
- deciding whether something is a user need, civic need, behaviour, pain point or insight
- preserving emotional, social, relational and civic meaning
- checking user need wording
- reviewing Codex reconciliation briefs
- identifying semantic risks before implementation
- writing reviewer questions

Do not use ChatGPT as the only implementation layer for broad repository edits.

### Codex

Use Codex for repository-scale file work and repeatable implementation.

Good uses:

- reading many repository files
- searching for nearby objects
- checking existing links and IDs
- creating branches and files
- updating frontmatter and Markdown links
- running validation
- opening PRs
- producing reconciliation notes from repository inspection

Codex should be used with constrained instructions.

Prefer:

```text
Read these docs and inspect these folders. Produce a reconciliation brief only. Do not edit files.
```

Avoid:

```text
Ingest this research into the system.
```

### Human reviewers

Humans remain responsible for semantic acceptance, especially where the work changes interpretation, object boundaries, evidence relationships, maturity or review state.

Human review is especially important for:

- user need wording
- civic need creation
- pain point severity and lifecycle state
- behaviour granularity
- object merges, splits and supersession
- public or partner-facing interpretation
- sensitive lived-experience material

## What can be automated safely first

Prioritise automation that reduces friction without over-automating judgement.

Good early candidates:

- source folder creation in `civic-design-secondary-research`
- source metadata stubs
- evidence-map stubs
- source records in `civic-design-intelligence`
- ingestion PR body templates
- reconciliation note templates
- ID allocation checks
- filename and `short_name` checks
- link resolution checks
- duplicate candidate search
- nearby object search
- missing evidence-link warnings
- solution-shaped user need warnings
- conservative metadata defaults
- review status and maturity guardrails

These support throughput without pretending the system has validated meaning.

## What should not be automated yet

Do not automate:

- marking user needs reviewed or validated
- deciding a user need is mature
- promoting evidence strength
- deciding pain point severity without comparison and review
- creating civic needs from weak signals without review
- merging, splitting or superseding first-class objects without review
- changing lifecycle state automatically
- rewriting emotional or social needs into functional task language
- marking human review complete

These are semantic or governance decisions.

## Public and collaborator review direction

The repository should eventually support public, partner or collaborator contribution without allowing uncontrolled changes to canonical objects.

A public-facing process should create reviewable contributions, not direct mutations.

Possible workflow:

```text
public or partner contribution
→ contribution record
→ triage
→ candidate evidence or object update
→ review
→ PR
→ merge
```

Future contributors may help:

- submit new evidence
- challenge a user need
- say that a need does not reflect their experience
- identify missing context
- confirm recurrence of a pain point
- flag outdated or resolved pain
- add locality or service examples
- comment on wording
- provide third-sector or practitioner evidence

This supports openness and legitimacy while preserving repository control.

## Four product layers

The future product can be thought of as four layers:

```text
1. Capture layer
   Forms, uploads, source capture, public and partner submissions

2. Interpretation layer
   LLM-assisted decomposition into candidate evidence and objects

3. Reconciliation layer
   Matching against existing repository objects, surfacing overlap and risk

4. Review and publication layer
   Human or public review, PRs, merge and visible change history
```

At the moment, expert-assisted work spans all four layers manually. The product direction is to separate them so each layer can be improved, delegated or automated where appropriate.

## Operational continuity principle

The repository should remain usable if the original expert contributors are unavailable.

This means:

- important workflows should be documented
- prompts should become repeatable instructions
- decisions should be captured in PR summaries or object change logs where appropriate
- contributors should be guided by checklists and examples
- automation should reduce dependency on memory
- the system should make uncertainty visible rather than relying on private judgement

## Near-term product strategy

Do not build a full ingestion platform yet.

Use the current ingestion backlog to learn the repeatable workflow. Then automate the parts that are repeated often enough and expose the review steps that benefit from wider participation.

Near-term sequence:

1. Use expert-assisted ingestion for a few small slices.
2. Capture the repeatable steps and prompts.
3. Identify repeated friction points.
4. Automate low-risk support tasks first.
5. Design guided contributor review only after real examples show what contributors need.

## Success criteria

The ingestion operating model is working when:

- useful knowledge can enter before full maturity without being overclaimed
- ingestion slices include reconciliation, not only extraction
- contributors do not need to understand the whole repository to add useful material
- Codex can safely handle repository-scale work without making unchecked semantic decisions
- ChatGPT or human review is used where semantic judgement matters
- PRs make object decisions and unresolved questions visible
- the system becomes less dependent on one person over time
- automation reduces friction without silently validating interpretation
