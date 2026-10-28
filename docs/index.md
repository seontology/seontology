---
description: What SEOntology is, who it is for, and where to find the ontology files.
---

# SEOntology

**SEOntology** is an open, Schema.org-aligned OWL 2 ontology for modeling search engine optimization work as a knowledge graph: web pages and their URLs, the queries they rank for, links and link groups, content chunks, search and analytics metrics, quality scores, and structured-data profiles. Agents, applications and researchers can use it as a shared vocabulary to reason about, audit and optimize web content.

!!! success "Best Student Paper at SEMANTiCS 2026"
    The paper *SEOntology: A Domain Ontology for Semantic Modeling of Search Engine Optimization Workflows* by Emilija Gjorgjevska, David Riccitelli, Milos Jovanovik and Andrea Volpini won [Best Student Paper at SEMANTiCS 2026](https://2026-eu.semantics.cc/page/awards.html) (Research Track).

![SEOntology overview](assets/images/seontology-doodle.png)

## At a glance

| | |
|---|---|
| Namespace | `https://w3id.org/seovoc/` |
| Preferred prefix | `seovoc:` |
| Builds on | [Schema.org](https://schema.org/) |
| License | MIT |
| Source | [github.com/seontology/seontology](https://github.com/seontology/seontology) |

## Start here

- **New to SEOntology?** Read [Getting started](guide/getting-started.md) for a first example in JSON-LD, Turtle and SPARQL.
- **Modeling your data?** The [core model](guide/core-model.md) explains how pages, queries, links, chunks and metrics fit together. The [ontology reference](https://seontology.github.io/seontology/reference/) documents every class and property.
- **Building an agent or tool?** See [For agents](for-agents.md) for the machine-readable files: the ontology in Turtle, RDF/XML and JSON-LD, a JSON-LD context, and `llms.txt`.
- **Proposing a change?** Follow [Contributing ontology proposals](contributing-ontology-proposals.md).

## Use cases

- AI-powered content summarization and metadata generation
- Semantic internal linking via chunk and query similarity
- Entity linking and disambiguation in web content
- Graph-based internal linking optimization
- Query clustering and intent modeling for content strategy
- Training goal-relevant reasoning models using SEOntology and GRPO
- Provenance tracking for SEO actions and content evolution
- Multilingual SEO alignment and semantic consistency
- SERP feature optimization for enhanced search visibility
- Automated image captioning and SEO optimization

## Sponsor

SEOntology was initially developed by [WordLift](https://wordlift.io/) and is enriched by contributions from SEO experts, knowledge engineers and developers.
