# Repository Update 0.0.4

This patch release adds a proposal-first contribution workflow for SEOntology changes.

## Applied Changes

- Replaced the generic feature-request issue template with an ontology-proposal template.
- Added prompts for SEO use cases, competency questions, modeling decisions, external-vocabulary alignment, YAML-LD, Turtle examples, compatibility notes, and acceptance criteria.
- Added a contribution guide covering proposal review, maintainer approval, canonical ontology editing, generated artifacts, checksum updates, and validation.
- Updated README contribution instructions and documentation navigation.

## Compatibility Notes

This release changes repository contribution guidance only. It does not change `seovoc.owx`, generated ontology artifacts, ontology terms, or downstream data compatibility.

The issue template requests the `ontology-proposal` label. That label must exist in the GitHub repository before GitHub can apply it automatically.

## Verification

- Issue-template front matter and Markdown structure were reviewed.
- README and contribution-guide links were checked against files in the repository.
- The ontology checksum remains aligned because the canonical ontology source is unchanged.
