---
description: How SEOntology's main classes and properties fit together, grouped by area (pages, queries, links, content, metrics, quality, structured data).
---

# Core model

SEOntology is centered on the **`WebPage`**: the pages a site publishes, the **queries** they rank for, the **links** between them, the **content** they contain, and the **measurements** taken about them. This page groups the main terms by area. The [ontology reference](https://seontology.github.io/seontology/reference/) lists every term with its domain, range and description.

## Pages and site structure

| Term | Meaning |
|---|---|
| `WebPage` | A specific web page; extends Schema.org's `WebPage`. |
| `URL` | The page's URL. `hasURL` / `isURLOf` binds a page to its canonical URL. |
| `Domain` | A grouping of pages by domain or subdomain. |
| `DirectorySegment` | A logical site segment derived from URL paths. |
| `PageType` | A reusable classification of a page's purpose (for example product detail or editorial), assigned with `hasPageType`. |
| `PageGroup` | An A/B-testing cohort, such as a control or test group. Use `PageType` for functional classifications. |
| `Language` | The language of content, for multilingual SEO. |

Page-level text properties include `title`, `metaDescription`, `bodyText`, `urlSlug` and `slugNgram`.

## Queries and intent

| Term | Meaning |
|---|---|
| `Query` | A search query a page ranks for, usually from Google Search Console. `hasQuery` / `isQueryOf` link pages and queries. |
| `hasPrimaryQuery` | The primary target query of a `WebPage` or `Chunk`. |
| `QueryCluster` | A set of related queries grouped for content planning and gap analysis. Members are linked with `hasClusterQuery` / `isClusterQueryOf`. |
| `ClusteringStrategy` | The method or model used to build a cluster (`clusteredBy`). |
| `Intent` | Search intent, linked with `hasIntent`; a cluster's dominant intent uses `dominantSearchIntent`. |
| `EntityGap` | A missing or unlinked entity relevant to a query (`hasEntityGap`). |
| `Persona` | The target audience archetype of a page (`hasPersona`). |

Query classification properties include `queryType`, `keywordType`, `queryCategory` and `intent`. Cluster metrics include `clusterVolume` and `keywordsCount`.

## Links

Each hyperlink on a page is a **`Link`**. A page reaches its links in one of two ways:

- **Grouped**: **`hasLinkGroup`** from the `WebPage` to a **`LinkGroup`**, then **`hasLink`** from the group to each `Link`. This is the canonical pattern for navigation, footers, related-content blocks and other clusters of links.
- **Ungrouped**: the direct **`link`** property from `WebPage` to `Link`, for raw extracted links or a single inline link in body text.

A `LinkGroup` carries `linkGroupName`, free text for display ("Footer links"), `linkGroupType`, the machine-checkable placement (`header`, `footer`, `body`, `sidebar` or `navigation`), and `linkGroupID`.

A `Link` describes one hyperlink and where it points:

| Term | Meaning |
|---|---|
| `linkTargetUrl` | The absolute href, as a string. Always set it: it is the destination fact you have from parsing the markup alone. |
| `linkTarget` | The resolved destination node: a `WebPage` in the graph, a `URL` node, or the entity the destination represents. Set it only once the destination has been resolved. Its inverse is `isLinkTargetOf`. |
| `linkText` | The anchor text. Accepts language-tagged literals. |
| `linkRel` | One `rel` token per value: `nofollow`, `sponsored`, `ugc`, `noopener`, and so on. |
| `linkLocation` | Placement of an ungrouped link, with the same values as `linkGroupType`. When a `LinkGroup` exists, its `linkGroupType` takes precedence. |
| `position` | Order of the link within its group. |

Internal versus external is not a property of the link. Compare domains instead: a link is internal when its `linkTarget` page shares a `Domain` (`hasDomain`) with the source page, or, for destinations that were not crawled, when the `linkTargetUrl` host matches the source page's `domainName`.

`anchorResource`, `linkgroupID`, `noFollow`, `linkType` and the `AnchorText` class are deprecated. See [Compatibility notes](compatibility.md#links).

The [Links](links.md) guide explains the model in depth, with worked examples and queries.

## Content and entities

| Term | Meaning |
|---|---|
| `Chunk` | A self-contained section of a page, used for vector search and structured representation. Linked with `hasChunk` / `isChunkOf`; described by `chunkText`, `chunkPosition`, `tokenCount` and related properties. |
| `Topic` | The central subject of a page. |
| `schema:Thing` | Any entity. `about` links a page to its main entity and `mentions` to entities it mentions; both range over Schema.org's `Thing`. |
| `ImageObject` | An image and its SEO metadata, with `aiGeneratedCaption` and `captionQualityScore`. |
| `Model` | An AI or ML model used for summarization, classification, scoring or captioning. |

Embedding inputs and outputs are recorded with `embeddingText` and `embeddingValue`.

## Search and analytics metrics

- **Search Console**: `clicks`, `impressions` and `ctr`, plus windowed variants for 7 days, 28 days, 3 months and 6 months (for example `clicks28Days`, `impressions3Months`, `ctr6Months`, `averagePosition28Days`). Windowed metrics can be attached to a `Query` or a `WebPage`.
- **GA4**: `users`, `sessions`, `engagedSessions`, `engagementRate`, `averageEngagementTime`, `conversions`, `trafficSource` and `landingPage`, interpreted in the measurement context of the dataset that produced them.
- **Traffic sources**: a `TrafficSource` is a source as reported by analytics (`google`, `(direct)`, `chatgpt.com`). `hasTrafficChannel` assigns it to a `TrafficChannel` such as organic search, referral or AI assistant, so AI-assistant referrals can be told apart from generic referrals.
- **Forecasts**: `forecastedTraffic`.

## Quality and evaluation

Link a `WebPage` to a **`QualityScore`** with `hasQualityScore`, or a `Chunk` with `hasChunkQualityScore`, to record assessment results such as `contentAccuracyScore`, `contentDepthScore`, `seoScore` and `readabilityScore`. `evaluationID` identifies an evaluation run. `isThinContent` is a boolean thin-content classification.

## Structured data

`Schema` represents the structured-data markup of a page (`hasSchemaMarkup` / `describesPage`). `StructuredDataProfile` describes a structured-data policy aligned with W3C PROF. Profiles can be applicable to a page type, selected for a page, or used to generate markup; these are separate states. See [Structured data profiles](../structured-data-profiles.md).
