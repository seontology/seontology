![seontology logo-04](.assets/seontology_logo.png)


# SEOntology

## Description

> **Accepted at SEMANTiCS 2026 — Research Track**  
> SEOntology has been accepted as a research paper at [SEMANTiCS 2026](https://2026-eu.semantics.cc/page/accepted_research): **“SEOntology: A Domain Ontology for Semantic Modeling of Search Engine Optimization Workflows”** by Emilija Gjorgjevska, David Riccitelli, Milos Jovanovik, and Andrea Volpini.

The **SEOntology** is the open-source semantic framework, initially developed by WordLift and then enriched with contributions from SEO experts, knowledge engineers, and developers. It serves as a semantic operating system for modern SEO, enabling agents, apps, and researchers to reason about, audit, and optimize web content through a shared vocabulary. To simplify, think of it as an operating system for your content strategy. This ontology bridges SEO practice with linked data standards, powering automation, structured reasoning, and explainable AI across the entire content lifecycle. This is an early draft.

## Use Cases Covered

- **AI-Powered Content Summarization and Metadata Generation**
- **Semantic Internal Linking via Chunk and Query Similarity**
- **Entity Linking and Disambiguation in Web Content**
- **Graph-Based Internal Linking Optimization**
- **Query Clustering and Intent Modeling for Content Strategy**
- **Training Goal-Relevant Reasoning Models Using SEOntology and GRPO**
- **Provenance Tracking for SEO Actions and Content Evolution**
- **Multilingual SEO Alignment and Semantic Consistency**
- **SERP Feature Optimization for Enhanced Search Visibility**
- **Automated Image Captioning and SEO Optimization**

## Features

- **Main Classes**: Our ontology provides a comprehensive coverage of various SEO elements, such as:
  - `WebPage`: The primary entity representing a specific webpage, extended from Schema.org.
  - `Query`: The query for which the webpage ranks in SERPs, usually obtained through Google Search Console.
  - `URL`: The unique identifier for the webpage.
  - `AnchorText`: The anchor text which is influenced by the Query that the WebPage ranks for.
  - `Link`: Representing an internal or external link found on the webpage through crawling.
  - `LinkGroup`: A collection of links that are logically grouped, such as menus or footers.
  - `Chunk`: A semantically meaningful text segment or section within a webpage.
  - `EntityGap`: A placeholder for missing or unlinked entities relevant to the content.
  - `ImageObject`: A representation of an image and its associated SEO metadata.
  - `Language`: The language associated with content, useful for multilingual SEO.
  - `Topic`: The central concept or subject a WebPage is about.
  - `Schema`: All schema markup elements found on the webpage, in JSON-LD or other formats.
  - `Model`: AI or ML models used for tasks such as summarization, classification, or scoring.
  - `QualityScore`: A scoring container that aggregates content and SEO quality dimensions.
  - `QueryCluster`: A set of semantically or SERP-related search queries grouped for content planning and gap analysis.
  - `ClusteringStrategy`: The method, model, or algorithm used to generate a QueryCluster.
  - `Persona`: The modeled archetype of a target user or audience segment.
  - `DirectorySegment`: A logical segment in the site structure, derived from URL paths.
  - `Domain`: A high-level grouping of pages based on domain or subdomain.
  - `PageGroup`: An A/B-testing cohort such as a control or test group.
  - `PageType`: A reusable page-purpose or content classification for a WebPage, independent of A/B-testing cohorts.
  - `StructuredDataProfile`: A declarative structured-data profile aligned with W3C PROF.
  - `Thing`: The most generic type of item, expressed as an extension of the Thing class in Schema.org.

- **Selected Object Properties**: These define relationships between core SEO entities:
  - `hasQuery` / `isQueryOf`: Links a WebPage to one or more Queries it ranks for.
  - `hasPrimaryQuery` / `isPrimaryQueryOf`: Connects a WebPage or Chunk to its primary target Query.
  - `hasChunk` / `isChunkOf`: Links a WebPage to its content segments (Chunks).
  - `hasImage` / `isImageOf`: Connects a WebPage with embedded ImageObjects.
  - `hasLinkGroup` / `isLinkGroupOf`: Associates a WebPage with its LinkGroups.
  - `hasLink` / `isLinkOf`: Connects a LinkGroup to individual Links.
  - `hasClusterQuery` / `isClusterQueryOf`: Connects a QueryCluster to its member Queries without changing the WebPage-oriented `hasQuery` relationship.
  - `clusteredBy`: Links a QueryCluster to the ClusteringStrategy used to generate it.
  - `dominantSearchIntent`: Links a QueryCluster to its dominant search Intent.
  - `hasPersona` / `isPersonaOf`: Maps a WebPage to its targeted Persona.
  - `hasURL` / `isURLOf`: Binds a WebPage to its canonical URL.
  - `about` / `isDescribedBy`: Relates a WebPage to the main entity (Thing) it discusses.
  - `mentions`: Identifies entities (Thing) mentioned within the content.
  - `hasEntityGap` / `isEntityGapOf`: Captures missing or unlinked entities for a Query.
  - `hasQualityScore` / `isQualityScoreOf`: Relates a WebPage to a container of quality metrics.
  - `hasSchemaMarkup` / `describesPage`: Links a WebPage with its structured schema markup.
  - `hasPageType`: Assigns one or more reusable PageType classifications to a WebPage.
  - `hasApplicableStructuredDataProfile`: Identifies candidate profiles for a PageType without selecting or applying them automatically.
  - `usesStructuredDataProfile`: Records the profile explicitly selected for a WebPage.
  - `generatedUsingStructuredDataProfile`: Records generation provenance for a Schema artifact without asserting conformance.
  - `hasModel` / `isModelOfImage`: Associates an AI model with an image used or generated.
  - `hasLanguage` / `isLanguageOfImage`: Defines the language of an image or associated text content.
  - `hasTopic` / `isMainTopicOf`: Captures the core Topic of a WebPage.

- **Selected Data Properties**: These attributes capture literal values and numerical metrics:
  - `title`: The HTML or SERP title of the WebPage.
  - `metaDescription`: The SEO meta description used for snippet generation.
  - `bodyText`: The full textual content extracted from a WebPage.
  - `chunkText`, `chunkPosition`: The text and order of appearance of a Chunk within a WebPage.
  - `anchorValue`: The literal string value of an AnchorText.
  - `aiGeneratedCaption`, `captionQualityScore`: AI-generated image metadata and quality assessment.
  - `embeddingText`, `embeddingValue`: Textual input and vector output for AI embedding models.
  - `contentAccuracyScore`, `contentDepthScore`, `seoScore`, `readabilityScore`: Quality dimensions that help assess and optimize content.
  - `clicks`, `ctr`, `impressions`: Performance metrics retrieved from tools like Google Search Console.
  - `users`, `sessions`, `engagedSessions`, `engagementRate`, `averageEngagementTime`, `conversions`, `trafficSource`, `landingPage`: GA4 engagement and traffic metrics associated with a WebPage in the measurement context supplied by the producing analytics dataset.
  - `isThinContent`: A boolean classification signal indicating whether a Schema.org Thing has been classified as thin content.
  - `clusterVolume`, `keywordsCount`: Aggregated demand and size metrics for QueryCluster instances.
  - `forecastedTraffic`: Predicted traffic volume based on a model.
  - `queryType`, `keywordType`, `queryCategory`: Classification of a query by intent or semantics.
  - `slugNgram`, `urlSlug`: Linguistic and structural attributes derived from the URL.
  - `intent`: The inferred or labeled intent behind a search Query or WebPage target.
  - `evaluationID`: An identifier used for tracking scoring or benchmarking results.
  - and more!

## Compatibility Notes

- `seovoc:hasLinkGroup` from `WebPage` to `LinkGroup`, followed by `seovoc:hasLink` from `LinkGroup` to `Link`, is the canonical pattern for structured navigational link groups. The direct `seovoc:link` property remains available as a compatibility shortcut for ungrouped or raw extracted links.
- `seovoc:isLinkOf` now points from `Link` back to `LinkGroup`, matching its inverse relationship with `seovoc:hasLink`. Legacy data that used `isLinkOf` to point directly from `Link` to `WebPage` should either use `seovoc:link` for ungrouped/raw links or introduce a `LinkGroup` and connect the page with `seovoc:hasLinkGroup`.
- `seovoc:evaluationID` uses `xsd:string` so identifiers such as `eval_1745567328195` can be represented.
- Existing page-level quality properties such as `seovoc:seoScore` and `seovoc:readabilityGradeLevel` are preserved for compatibility. New integrations should prefer linking a `WebPage` or `Chunk` to a `QualityScore` when modeling assessment results.
- Query clustering uses `seovoc:hasClusterQuery` / `seovoc:isClusterQueryOf` instead of overloading `seovoc:hasQuery` / `seovoc:isQueryOf`, which remain scoped to `WebPage` and `Query`.
- `PageGroup` remains scoped to A/B-testing cohorts. Use `PageType` for functional classifications such as product-detail or editorial pages; no inference connects the two concepts.
- Structured-data profile applicability, explicit selection, artifact generation, and validated conformance are separate states. Profile applicability does not authorize generation or guarantee search-engine eligibility or outcomes.
 
## SEOntology Fully Visualized
![SEO VOC HQ](.assets/seovoc_full.svg)

## Getting Started

### Prerequisites

- [Protege](https://protege.stanford.edu/) or any other ontology editing tool
- Basic knowledge of [OWL/RDF/SPARQL/any other relevant technology]
- [TIB EU visualisation software](https://service.tib.eu/webvowl/) to analyze the ontology (Select 'ontology' from the bottom menu -> click 'Select ontology file')
  
### Installation & Setup

1. Clone this repository:
   ```bash
   git clone [URL to your repo]
   ```
2. Open the ontology file in Protege or your preferred ontology editor.

## How to Contribute

1. Fork this repository.
2. Create a new branch for your changes.
3. Make and commit your changes.
4. Push your branch to your fork.
5. Open a pull request from your fork to this repository.
6. After review and discussion, if your changes are approved, they will be merged.

## Versioning

We use [Semantic Versioning](http://semver.org/) for this project.

## Communication & Discussion

- [Thread on X](https://x.com/cyberandy/status/1715853285838430358?s=20)
- For issues, use the GitHub [issues](link_to_issues_page) page.

## Publications

* Andrea Volpini. "[Introducing SEOntology: The Future Of SEO In The Age Of AI](https://www.searchenginejournal.com/introducing-seontology-the-future-of-seo-in-the-age-of-ai/524773/)". Search Engine Journal, August 2024.
* Emilija Gjorgjevska. "[SEOntology: The Basis for Next-Gen SEO](https://www.youtube.com/watch?v=gM6egAImB1o)". Zagreb SEO Summit, June 2024.

## Sponsor

This project is sponsored by [WordLift](https://www.wordlift.io/), a leading provider of AI-powered solutions for content optimization and knowledge graph creation. Their support enables us to continue developing and maintaining this open-source project, empowering our community with valuable tools and resources.

## Documentation

- [Structured Data Profiles](docs/structured-data-profiles.md)
- [Ontology update 0.0.3](docs/ontology-update-0.0.3.md)
- [Ontology update 0.0.2](docs/ontology-update-0.0.2.md)

## License
This project is licensed under the MIT [LICENSE](LICENSE.md) - see the LICENSE.md file for details.

## Transparency 

Regarding the performance evaluation (before and after) reported in our paper: it is intentionally limited to an aggregated and anonymized overview. The underlying post test was conducted in an applied setting with client-related data, internal workflows, and team feedback collected across operational channels such as Slack. Because the raw reports, task records, and feedback traces may reveal client information, company specific processes, or legally restricted operational details, we cannot release the full evaluation material publicly. Instead, we report only the aspects that can be shared responsibly: the task context, the before and after comparison enabled by the ontology, the observed efficiency and quality improvements, and a high level summary of team feedback. This limitation affects the reproducibility of the field evaluation, but it preserves confidentiality while still providing evidence of practical utility in a real deployment context.

## Citation

If you use SEOntology, please cite the repository and the accepted SEMANTiCS 2026 paper:

```bibtex
@software{gjorgjevska2026seontology,
  title        = {SEOntology: A Domain Ontology for Semantic Modeling of Search Engine Optimization Workflows},
  author       = {Gjorgjevska, Emilija and Riccitelli, David and Jovanovik, Milos and Volpini, Andrea},
  year         = {2026},
  url          = {https://github.com/seontology/seontology},
  note         = {Accepted at SEMANTiCS 2026 Research & Innovation Track}
}
