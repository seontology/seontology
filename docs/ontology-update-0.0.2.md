# Ontology Update 0.0.2

This update applies the ontology changes reviewed in GitHub issues #20, #22, #23, #30, #52, and #55.

## Applied Changes

- Added `seovoc:isThinContent` as a boolean datatype property on `schema:Thing`.
- Added GA4 WebPage metrics: `users`, `sessions`, `engagedSessions`, `engagementRate`, `averageEngagementTime`, `conversions`, `trafficSource`, and `landingPage`.
- Added query clustering support with `QueryCluster`, `ClusteringStrategy`, `hasClusterQuery`, `isClusterQueryOf`, `clusteredBy`, `dominantSearchIntent`, `clusterVolume`, and `keywordsCount`.
- Corrected `seovoc:isLinkOf` so it points from `Link` back to `LinkGroup`, matching `hasLink`.
- Corrected `seovoc:evaluationID` to use `xsd:string`.
- Corrected `seovoc:contentDepthScore` to use `xsd:float`.
- Preserved page-level `seoScore` and `readabilityGradeLevel` for compatibility.

## Compatibility Notes

The canonical model for structured navigational links is:

```text
WebPage -> hasLinkGroup -> LinkGroup -> hasLink -> Link
```

The direct `seovoc:link` property remains available for ungrouped or raw extracted links. Legacy data that used `seovoc:isLinkOf` from `Link` directly to `WebPage` should either use `seovoc:link` or introduce a `LinkGroup` connected from the page with `seovoc:hasLinkGroup`.

Query clustering intentionally uses `hasClusterQuery` and `isClusterQueryOf` instead of overloading `hasQuery` and `isQueryOf`, which remain scoped to `WebPage` and `Query`.

## Verification

The update was verified by:

- converting `seovoc.owx` to `seovoc.owl` with ROBOT;
- converting `seovoc.owx` to `seovoc.ttl` with ROBOT;
- parsing generated RDF artifacts;
- checking issue-mapped domains, ranges, classes, and inverse properties across source and generated artifacts;
- confirming `seovoc.owx.md5` matches the current `seovoc.owx`.
