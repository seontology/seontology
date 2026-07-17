# Structured Data Profiles

SEOntology separates page classification, structured-data policy, generated artifacts, and validation results. This keeps a page type from being confused with the entity described by the page and prevents candidate policy from being recorded as proven conformance.

## Core Model

`PageType` instances classify pages by purpose or content role. They are independent from `PageGroup`, which remains reserved for A/B-testing cohorts.

```text
PageType
  └─ hasApplicableStructuredDataProfile → StructuredDataProfile

WebPage
  ├─ hasPageType → PageType
  └─ usesStructuredDataProfile → StructuredDataProfile

Schema
  └─ generatedUsingStructuredDataProfile → StructuredDataProfile
```

`StructuredDataProfile` specializes [`prof:Profile`](https://www.w3.org/TR/dx-prof/). SEOntology does not import PROF or SHACL. Downstream profiles use PROF resource descriptors to publish shapes, templates, examples, or guidance.

The three expected-type annotations describe graph roles without creating OWL constraints:

- `expectedPageSchemaType`: the expected class of the page node;
- `expectedMainEntitySchemaType`: the expected class of the node linked through `schema:mainEntity`;
- `expectedSupportingSchemaType`: an expected supporting graph-node class.

Their values are class IRIs used as annotations. They do not type graph nodes, require generation, or establish conformance. Downstream SHACL shapes provide executable constraints.

## Lifecycle Semantics

The following stages are deliberately independent:

1. A profile is a candidate because it is applicable to a `PageType`.
2. An application selects a profile for a particular `WebPage` after entity-grounding and policy checks.
3. A `Schema` artifact records which profile was used during generation.
4. A SHACL execution produces a `sh:ValidationReport` with `sh:conforms true` or `false`.
5. After a successful, traceable validation, the validated resource may assert `dct:conformsTo` the profile.

There is no OWL property chain between these stages. A page can have multiple page types and profiles, and application logic remains responsible for selection and precedence.

## Competency Questions

1. Which PageType values classify a WebPage?
2. Which structured-data profiles are applicable to a PageType?
3. Which profile was explicitly selected for a WebPage?
4. Which profile generated a Schema artifact?
5. Which page, main-entity, and supporting types does a profile advise?
6. Which PROF resources implement the downstream constraints?
7. Did a specific validation execution conform independently of profile applicability and generation?

## YAML-LD Example

This compact proposal syntax describes the lifecycle links. The executable examples use JSON-LD and Turtle because those formats are supported by the repository validation tools.

```yaml
'@context':
  schema: http://schema.org/
  seovoc: https://w3id.org/seovoc/

'@graph':
  - '@id': https://example.com/structured-data-profile/ProductDetailPageType
    '@type': seovoc:PageType
    seovoc:hasApplicableStructuredDataProfile:
      '@id': https://example.com/structured-data-profile/ProductPageProfile-v1

  - '@id': https://example.com/structured-data-profile/ProductPageProfile-v1
    '@type': seovoc:StructuredDataProfile
    seovoc:expectedPageSchemaType:
      '@id': schema:WebPage
    seovoc:expectedMainEntitySchemaType:
      '@id': schema:Product
    seovoc:expectedSupportingSchemaType:
      '@id': schema:BreadcrumbList

  - '@id': https://example.com/products/example-product
    '@type':
      - seovoc:WebPage
      - schema:WebPage
    seovoc:hasPageType:
      '@id': https://example.com/structured-data-profile/ProductDetailPageType
    seovoc:usesStructuredDataProfile:
      '@id': https://example.com/structured-data-profile/ProductPageProfile-v1
    schema:mainEntity:
      '@id': https://example.com/entities/example-product
```

The complete Turtle example in [`product-page-profile.ttl`](../examples/structured-data-profiles/product-page-profile.ttl) adds versioned profile metadata, the policy owner and consumer, a PROF resource descriptor, a distinct Product main entity, a supporting BreadcrumbList, and a concrete Schema artifact.

## Executable Validation Example

The fixtures under [`examples/structured-data-profiles/`](../examples/structured-data-profiles/) describe an illustrative Example Publisher policy. They are not universal Schema.org or search-engine requirements.

The shape validates a merged page-scoped RDF graph. The valid fixture identifies a stable page IRI and a distinct stable Product IRI linked through `schema:mainEntity`. Negative fixtures isolate three failures:

- the page has no main entity;
- a BreadcrumbList is incorrectly used as the main entity;
- the Product lacks the name required by the example publisher policy.

PySHACL requires the JSON-LD input format to be explicit:

```bash
uvx --from pyshacl pyshacl -m -df json-ld -sf turtle \
  -s examples/structured-data-profiles/product-page-shape.ttl \
  examples/structured-data-profiles/valid-product-page.jsonld
```

The valid fixture must return exit code `0`; each semantic-negative fixture must return exit code `1` with the intended result path. JSON-LD parsing is tested separately so a syntax error cannot be mistaken for a policy violation.

After successful validation, a system may record conformance separately:

```turtle
ex:validatedPageGraph dct:conformsTo ex:ProductPageProfile-v1 .
```

This triple is intentionally absent from the pre-validation fixtures.

## SEO and GEO Boundaries

Five validation and outcome layers must not be conflated:

1. the JSON-LD or RDF serialization parses;
2. vocabulary usage is compatible with Schema.org;
3. the page-scoped graph conforms to a named downstream SHACL profile;
4. a consumer may consider the markup eligible under its current policies;
5. observable SEO or GEO outcomes may or may not follow.

Structured data should remain grounded in and consistent with visible page content under the [Google structured-data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies). Passing this example profile does not guarantee crawling, indexing, rich-result eligibility or display, rankings, citations, AI Overview or AI Mode inclusion, or any other search outcome. Google documents that its [AI search features](https://developers.google.com/search/docs/appearance/ai-features) require no special Schema.org markup.
