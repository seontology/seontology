# Contributing Ontology Proposals

SEOntology is an ontology repository. Contributions should start as GitHub issues that describe concrete SEO use cases and mature into reviewed ontology modeling proposals before the canonical ontology file is changed.

## Contribution Flow

1. Open a GitHub issue.

   Describe the SEO use case, competency question, proposed class or property, and why existing SEOntology terms are not sufficient.

2. Maintainers review and triage the issue.

   The maintainer classifies the request as one of:

   - new class
   - new object property
   - new data property
   - change to existing semantics
   - documentation clarification
   - out of scope

3. Review the modeling approach before editing the ontology.

   The discussion should confirm whether the concept already exists, whether an external vocabulary such as Schema.org, SKOS, PROV-O, or DC Terms already covers it, and whether the proposal should be modeled as a class, property, controlled value, or annotation.

4. Mature the issue into a complete modeling proposal.

   Before approval, the issue should include:

   - clear YAML-LD definition
   - concrete TTL example
   - proposed labels and comments
   - domain and range
   - inverse property, if applicable
   - alignment to external vocabularies, if any
   - migration or compatibility notes, if existing semantics change

5. Maintainer approves the proposal.

   Approval should happen in the issue before ontology editing starts.

6. Update the ontology source.

   After approval, update `seovoc.owx`, regenerate `seovoc.owl` and `seovoc.ttl`, update `seovoc.owx.md5`, and update public documentation when the change affects usage or compatibility.

7. Validate the change before merge.

   Required validation includes successful ROBOT conversion, updated checksum, diff review of source and generated artifacts, and confirmation that the included examples match the approved model.

## Proposal Quality Checklist

A proposal is ready for maintainer approval when it answers:

- What SEO workflow or reasoning task needs this term?
- What question should the ontology be able to answer after the change?
- Why are existing terms insufficient?
- Is the proposed term a class, object property, data property, annotation, or controlled value?
- What are the domain and range?
- Does the term need an inverse property?
- Is there an equivalent or related term in an external vocabulary?
- What concrete YAML-LD and TTL examples demonstrate the intended use?
- Would this change break or reinterpret existing data?
