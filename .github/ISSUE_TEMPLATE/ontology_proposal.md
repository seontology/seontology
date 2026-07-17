---
name: Ontology proposal
about: Propose a new SEOntology class, property, semantic change, or documentation clarification
title: '[Ontology proposal]: '
labels: ontology-proposal
assignees: ''

---

## SEO use case

Describe the SEO workflow, analysis, automation, or reasoning task this proposal supports.

## Competency question

What question should SEOntology be able to answer after this change?

Example: "Which pages target queries with informational intent but lack supporting entity coverage?"

## Proposed change type

Select one:

- [ ] New class
- [ ] New object property
- [ ] New data property
- [ ] Change to existing semantics
- [ ] Documentation clarification
- [ ] Other

## Proposed term

Provide the preferred term name, label, and short definition.

```yaml
term: seovoc:
label:
definition:
type:
```

## Why existing terms are insufficient

List the existing SEOntology terms you considered and explain why they do not cover this use case.

## Modeling notes

Provide the expected domain, range, inverse property, and any constraints.

```yaml
domain:
range:
inverseOf:
subClassOf:
subPropertyOf:
```

## External vocabulary alignment

List any related terms from Schema.org, SKOS, PROV-O, DC Terms, or another vocabulary.

```yaml
sameAs:
closeMatch:
relatedMatch:
```

## YAML-LD definition

Provide a concrete YAML-LD definition once the proposal has matured.

```yaml
@context:
  seovoc: https://w3id.org/seovoc/

```

## TTL example

Provide a concrete Turtle example showing how the proposed term should be used.

```ttl
@prefix seovoc: <https://w3id.org/seovoc/> .
@prefix schema: <https://schema.org/> .

```

## Compatibility and migration notes

Describe whether this changes existing semantics, requires data migration, or affects downstream consumers.

## Acceptance criteria

- [ ] Use case and competency question are clear.
- [ ] Existing SEOntology terms have been checked.
- [ ] External vocabulary alignment has been considered.
- [ ] YAML-LD definition is provided.
- [ ] TTL example is provided.
- [ ] Domain and range are documented.
- [ ] Compatibility impact is documented.
