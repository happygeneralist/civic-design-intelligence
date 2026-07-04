# Openness and protection model

Status: draft
Related issue: #62

## Purpose

This note captures an initial position on how Civic Design Intelligence should balance open public-interest reuse with responsible protection of the operational method.

The repository is intended to support reuse across public institutions. However, some parts of the work now encode a distinctive LLM-assisted design intelligence method: research ingestion, evidence structuring, user need handling, civic need modelling, pain point lifecycle management, traceability conventions and maturity controls.

The aim is not to close the repository. The aim is to make the openness model intentional before publishing the most operationally reusable parts of the workflow.

## Working principle

The knowledge model should be open. The orchestration method should be protected until the project has a clearer licensing, governance and sustainability model.

## Layers

### 1. Open civic knowledge layer

This layer should generally be public and reusable.

It may include:

- public principles
- research object concepts
- example schemas
- evidence and traceability conventions
- user need and civic need modelling guidance
- pain point lifecycle concepts
- public documentation
- sample objects where appropriate

This layer supports civic reuse, scrutiny, contribution and adoption.

### 2. Controlled implementation layer

This layer may be open, but may need clearer licensing, attribution or contribution expectations.

It may include:

- structured templates
- schema definitions
- repository conventions
- object lifecycle rules
- quality and maturity guidance
- contribution workflows

This layer should remain practical and lightweight, but should not be published casually where doing so would undermine stewardship, attribution or sustainability.

### 3. Protected orchestration layer

This layer should not be public by default.

It may include:

- full LLM system instructions
- ingestion prompts
- transformation prompts
- automated structuring workflows
- evaluation rubrics
- assistant orchestration patterns
- detailed operational playbooks

This material may be kept outside the public repository, summarised at a higher level, or published later under a more deliberate licensing and stewardship model.

## Open questions

- What should be public by default?
- What should be private by default?
- What licensing model best supports public-sector reuse while protecting the originator's work?
- Should LLM instructions be treated as part of the open repository, private project infrastructure, or separately licensed material?
- How should attribution, reuse and contribution expectations be expressed?
- Could the public repository remain open while implementation support, hosted tooling, training or orchestration becomes a service?

## Current implication

Until the openness model is agreed, avoid committing detailed LLM ingestion prompts, full system instructions, orchestration playbooks or automation recipes to the public repository.

High-level safety guidance and public documentation can remain open where it helps users understand the repository without giving away the full operating method.