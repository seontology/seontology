---
description: Changes that affect existing SEOntology data, deprecated terms, and which modeling pattern to prefer.
---

# Compatibility notes

## Metrics

- **Windowed search metrics can be attached to pages as well as queries.** The domains of the windowed Search Console metrics (`clicks7Days`, `clicks28Days`, `clicks3Months`, `clicks6Months`, the matching `impressions*`, `ctr*` and `averagePosition*` properties, and their trend properties) were widened from `Query` to `Query ∪ WebPage`. Existing query-level data remains valid; no migration is needed.
- **A 6-month window was added**: `clicks6Months`, `impressions6Months`, `ctr6Months` and `averagePosition6Months`.
- **`averagePositon7Days` is deprecated** because its IRI is misspelled. Use `averagePosition7Days`. The old IRI is kept so existing data stays valid.

## Links

- `hasLinkGroup` from `WebPage` to `LinkGroup`, followed by `hasLink` from `LinkGroup` to `Link`, is the canonical pattern for grouped links. The direct `link` property remains for ungrouped or raw extracted links.
- `isLinkOf` points from `Link` back to `LinkGroup`, as the inverse of `hasLink`. Data that used `isLinkOf` to point from a `Link` directly to a `WebPage` should use `link` for ungrouped links, or add a `LinkGroup` and connect the page with `hasLinkGroup`.
- `linkGroupType` complements `linkGroupName`. The name is free-text display; the type (`header`, `footer`, `body`, `sidebar`, `navigation`) is the value consumers can filter on.

## Other

- `evaluationID` uses `xsd:string`, so identifiers such as `eval_1745567328195` are valid.
- Page-level quality properties such as `seoScore` and `readabilityGradeLevel` are kept. New integrations should link a `WebPage` or `Chunk` to a `QualityScore` instead.
- Query clusters use `hasClusterQuery` / `isClusterQueryOf`. `hasQuery` / `isQueryOf` stay scoped to `WebPage` and `Query`.
- `PageGroup` stays scoped to A/B-testing cohorts. Use `PageType` for functional classifications; nothing infers one from the other.
- Structured-data profile applicability, selection, generation and validated conformance are separate states. A profile being applicable does not authorize generation or guarantee search-engine eligibility.
