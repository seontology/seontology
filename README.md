![seontology logo-04](.assets/seontology_logo.png)


# SEOntology

## Description

The **SEOntology** is a framework that WordLift, other SEOs, software engineers, and knowledge graph experts developed for **content optimization**. Think of it as an operating system for your content strategy. This is an early draft.

## Features

- **Main Classes**: Our ontology provides a comprehensive coverage of various SEO elements, such as:
  - `WebPage`: The primary entity representing a specific webpage, extended from Schema.org.
  - `Query`: The query for which the webpage ranks in SERPs, usually obtained through Google Search Console.
  - `URL`: the unique identifier for the webpage.
  - `AnchorText`: the anchor text which is influenced by the Query that the WebPage ranks for.
  - `Link`: representing an internal or external link found on the webpage through crawling.
  - `Thing`: The most generic type of item, expressed as an extension of the Thing class in Schema.org.
  - `Schema`: all schema markup elements found on the webpage, in JSON-LD, or other formats.


- **Object Properties**: These define relationships between classes. For instance:
  - `hasQuery`: To indicate the queries for which a `WebPage` ranks.
  - `influencedByQuery`: Indicating the connection between the `AnchorText` and the `Query` class.
  - `hasURL`: Indicating the uniform resource locator (URL) for the `WebPage`.
  - `link`: indicating the links found on the `WebPage`.
  - `usesSchema`: indicating the schema markup used to describe the `WebPage` itself. 

- **Data Properties**: These properties store specific values related to classes. Notably:
  - `embeddingText`, `embedding`, `embeddingModel` for modeling embedding use cases with SEOntology.
  - Clicks & Impressions Metrics: `clicks7Days`, `click28Days`, `ctr7Days`, and so on for tracking webpage performance over time.
  - and more!
 
## SEOntology Visualized
![seontology logo-04](.assets/FINAL_SEONTOLOGY_WORDLIFT.png)

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
* Emilija Gjorgjevska. "[SEOntology : THe basis for Next-Gen SEO](https://www.youtube.com/watch?v=gM6egAImB1o)".  Zagreb SEO Summit Presentation

## Sponsor

This project is sponsored by [WordLift](https://www.wordlift.io/), a leading provider of AI-powered solutions for content optimization and knowledge graph creation. Their support enables us to continue developing and maintaining this open-source project, empowering our community with valuable tools and resources.

## Documentation

Detailed documentation will be soon available.

## License
This project is licensed under the MIT [LICENSE](LICENSE.md) - see the LICENSE.md file for details.
