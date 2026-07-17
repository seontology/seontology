# Ontology Update 0.0.3

This update implements the structured-data profile model approved in GitHub issue #60.

## Applied Changes

- Added `PageType` for reusable page-purpose or content classifications independent from A/B-testing cohorts.
- Added `StructuredDataProfile` as a specialization of W3C `prof:Profile` without importing PROF.
- Added `hasPageType`, `hasApplicableStructuredDataProfile`, `usesStructuredDataProfile`, and `generatedUsingStructuredDataProfile`.
- Added advisory annotations for expected page, main-entity, and supporting Schema.org types.
- Added a versioned downstream Product-page profile, PROF descriptor, SHACL shape, and positive/negative JSON-LD fixtures.

## Compatibility Notes

This release is additive. Existing `PageGroup`, `groupType`, `hasPage`, and `isPageOf` ontology axioms remain unchanged and retain their A/B-testing meanings. README wording that previously described PageGroup as a broad semantic or structural grouping has been corrected.

Profile applicability does not imply explicit page selection. Selection does not imply generation, and generation does not imply validation or conformance. No property chain or universal page-type-to-Schema.org mapping has been introduced.

The expected-type terms are annotation properties with no logical domain or range. Downstream SHACL, not OWL, defines required, recommended, optional, prohibited, conditional, and cardinality constraints.

## Verification

The update is verified by:

- converting `seovoc.owx` to RDF/XML and Turtle with ROBOT;
- validating the ontology against the OWL 2 DL profile;
- parsing the canonical and generated ontology artifacts;
- checking all new declarations, domains, ranges, annotation-property roles, and PROF subclass alignment;
- confirming no existing PageGroup axioms changed and no property chain was introduced;
- parsing all Turtle and JSON-LD examples;
- validating one conforming and three intentionally non-conforming graphs with Meta-SHACL and PySHACL;
- confirming `seovoc.owx.md5` matches the canonical source and regeneration is stable.

The repository has no runtime unit-test suite. Fixture coverage exercises every new public class and property, and the ontology assertions cover all nine new public terms.
