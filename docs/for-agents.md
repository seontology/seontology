---
description: Machine-readable entry points for LLM agents and RDF tools — ontology files, JSON-LD context, Markdown pages, llms.txt and content negotiation.
---

# For agents

This site is built to be read by software as well as people. Everything below is static and needs no JavaScript.

## Entry points

| What | URL | Media type |
|---|---|---|
| Index for LLM agents | [`/llms.txt`](https://seontology.github.io/seontology/llms.txt) | `text/plain` |
| Guide and term index in one file | [`/llms-full.txt`](https://seontology.github.io/seontology/llms-full.txt) | `text/plain` |
| Term index (every class and property, with domain and range) | [`/reference/index.md`](https://seontology.github.io/seontology/reference/index.md) | `text/markdown` |
| Ontology | [`/seovoc.ttl`](https://seontology.github.io/seontology/seovoc.ttl) | `text/turtle` |
| Ontology | [`/seovoc.owl`](https://seontology.github.io/seontology/seovoc.owl) | `application/rdf+xml` |
| Ontology | [`/seovoc.jsonld`](https://seontology.github.io/seontology/seovoc.jsonld) | `application/ld+json` |
| JSON-LD context | [`/context.jsonld`](https://seontology.github.io/seontology/context.jsonld) | `application/ld+json` |

Every guide page is also published as Markdown: add `index.md` to the page URL, for example [`/guide/getting-started/index.md`](https://seontology.github.io/seontology/guide/getting-started/index.md). Each HTML page links to its Markdown version and to the ontology files with `<link rel="alternate">`.

## Resolving term IRIs

The namespace `https://w3id.org/seovoc/` is a persistent identifier. It redirects according to the `Accept` header:

| Request | Redirects to |
|---|---|
| `Accept: text/html` (browsers) | the term's entry in the HTML reference |
| `Accept: text/turtle` | `seovoc.ttl` |
| `Accept: application/rdf+xml` | `seovoc.owl` |
| `Accept: application/ld+json` | `seovoc.jsonld` |

```bash
curl -L -H 'Accept: text/turtle' https://w3id.org/seovoc/WebPage
```

`https://w3id.org/seovoc/context.jsonld` always returns the JSON-LD context.

## Writing SEOntology data

Use the context to write compact JSON-LD:

```json
{
  "@context": "https://w3id.org/seovoc/context.jsonld",
  "@type": "WebPage",
  "title": "Blue widgets",
  "clicks28Days": 1240
}
```

Object properties are typed as IRIs and numeric data properties carry their XSD datatypes, so the expanded RDF matches the ontology. See [Getting started](guide/getting-started.md) for a fuller example.

## Guidance for agents

- Prefer the term index or `seovoc.ttl` over the HTML reference; they contain the same definitions in less space.
- Check a property's domain and range in the term index before asserting it. Several metrics apply to both `Query` and `WebPage`.
- Do not use deprecated terms in new data (for example `averagePositon7Days`; use `averagePosition7Days`).
- When the ontology does not cover a concept, propose it through the [contribution workflow](contributing-ontology-proposals.md) rather than inventing `seovoc:` terms.
