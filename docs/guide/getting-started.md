---
description: Describe a web page, its queries, content chunks and links with SEOntology in JSON-LD and Turtle, then query it with SPARQL.
---

# Getting started

SEOntology terms live in the namespace `https://w3id.org/seovoc/`, usually written with the prefix `seovoc:`. A term IRI such as `https://w3id.org/seovoc/WebPage` resolves to its documentation in a browser and to the ontology file for RDF clients.

## Get the ontology

| Format | File |
|---|---|
| Turtle | [`seovoc.ttl`](https://seontology.github.io/seontology/seovoc.ttl) |
| RDF/XML | [`seovoc.owl`](https://seontology.github.io/seontology/seovoc.owl) |
| JSON-LD | [`seovoc.jsonld`](https://seontology.github.io/seontology/seovoc.jsonld) |
| JSON-LD context | [`context.jsonld`](https://seontology.github.io/seontology/context.jsonld) |

You can also open the ontology in [Protégé](https://protege.stanford.edu/) or explore it visually with [WebVOWL](https://service.tib.eu/webvowl/).

## A first example in JSON-LD

The example below describes one page: its canonical URL, 28-day Search Console metrics, a query it ranks for, a content chunk, and a footer link group. The SEOntology JSON-LD context maps short names such as `hasQuery` to their `seovoc:` IRIs and gives numeric metrics their XSD datatypes.

```json
{
  "@context": "https://w3id.org/seovoc/context.jsonld",
  "@id": "https://example.com/blue-widgets/",
  "@type": "WebPage",
  "title": "Blue widgets",
  "metaDescription": "Compare our range of blue widgets.",
  "hasURL": {
    "@id": "https://example.com/blue-widgets/#url",
    "@type": "URL",
    "value": "https://example.com/blue-widgets/"
  },
  "clicks28Days": 1240,
  "impressions28Days": 38110,
  "hasQuery": [
    {
      "@id": "https://example.com/queries/blue-widgets",
      "@type": "Query",
      "name": "blue widgets",
      "clicks28Days": 320,
      "averagePosition28Days": 3.4
    }
  ],
  "hasChunk": [
    {
      "@type": "Chunk",
      "chunkPosition": 1,
      "chunkText": "Blue widgets come in three sizes..."
    }
  ],
  "hasLinkGroup": {
    "@type": "LinkGroup",
    "linkGroupName": "Footer links",
    "linkGroupType": "footer",
    "hasLink": [{ "@type": "Link", "linkText": "About us" }]
  }
}
```

!!! note "Mixing with Schema.org"
    The context defines SEOntology terms only. Several of them (`name`, `about`, `mentions`, `text`) share a local name with Schema.org properties, and with this context they map to `seovoc:`. To use Schema.org properties in the same document, write them with a prefix, for example `"schema:headline"`. The context declares the `schema:` prefix.

## The same data in Turtle

```turtle
@prefix seovoc: <https://w3id.org/seovoc/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .

<https://example.com/blue-widgets/> a seovoc:WebPage ;
    seovoc:title "Blue widgets" ;
    seovoc:metaDescription "Compare our range of blue widgets." ;
    seovoc:hasURL <https://example.com/blue-widgets/#url> ;
    seovoc:clicks28Days "1240"^^xsd:long ;
    seovoc:impressions28Days "38110"^^xsd:long ;
    seovoc:hasQuery <https://example.com/queries/blue-widgets> ;
    seovoc:hasChunk [
        a seovoc:Chunk ;
        seovoc:chunkPosition "1"^^xsd:int ;
        seovoc:chunkText "Blue widgets come in three sizes..."
    ] ;
    seovoc:hasLinkGroup [
        a seovoc:LinkGroup ;
        seovoc:linkGroupName "Footer links" ;
        seovoc:linkGroupType "footer" ;
        seovoc:hasLink [ a seovoc:Link ; seovoc:linkText "About us" ]
    ] .

<https://example.com/blue-widgets/#url> a seovoc:URL ;
    seovoc:value "https://example.com/blue-widgets/" .

<https://example.com/queries/blue-widgets> a seovoc:Query ;
    seovoc:name "blue widgets" ;
    seovoc:clicks28Days "320"^^xsd:long ;
    seovoc:averagePosition28Days "3.4"^^xsd:double .
```

## Query it with SPARQL

Find pages and the queries they rank for, ordered by the query's 28-day clicks:

```sparql
PREFIX seovoc: <https://w3id.org/seovoc/>

SELECT ?page ?title ?query ?clicks ?position
WHERE {
  ?page a seovoc:WebPage ;
        seovoc:title ?title ;
        seovoc:hasQuery ?q .
  ?q seovoc:name ?query ;
     seovoc:clicks28Days ?clicks .
  OPTIONAL { ?q seovoc:averagePosition28Days ?position }
}
ORDER BY DESC(?clicks)
```

Exclude boilerplate navigation when analyzing editorial links:

```sparql
PREFIX seovoc: <https://w3id.org/seovoc/>

SELECT ?page ?text
WHERE {
  ?page seovoc:hasLinkGroup ?group .
  ?group seovoc:hasLink ?link .
  ?link seovoc:linkText ?text .
  FILTER NOT EXISTS {
    ?group seovoc:linkGroupType ?type .
    FILTER (?type IN ("header", "footer", "navigation"))
  }
}
```

## Next steps

- Read the [core model](core-model.md) to see how the main classes relate.
- Look up any term in the [ontology reference](https://seontology.github.io/seontology/reference/).
- See the [structured data profiles](../structured-data-profiles.md) for a complete worked example with SHACL shapes.
