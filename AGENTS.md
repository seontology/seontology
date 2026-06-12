# AGENTS.md

## Project Review

This repository currently contains one ontology project centered on SEOntology.

- Source of truth ontology file: `seovoc.owx`
- Generated ontology artifacts: `seovoc.owl`, `seovoc.ttl`
- Change detection checksum: `seovoc.owx.md5`
- Conversion automation script: `.bin/publish.sh`
- CI workflow: `.github/workflows/publish.yaml`

The publish workflow runs conversion and publishing logic from `.bin/publish.sh` on pushes/PRs to `main` and `develop`, and on semantic-style tags.

## Source of Truth and File Ownership

- Treat `seovoc.owx` as canonical for ontology edits.
- Do not hand-edit `seovoc.owl` or `seovoc.ttl` unless there is a documented emergency reason.
- Keep `seovoc.owx.md5` aligned with the current `seovoc.owx` contents.

## Agent Workflow

1. Review `git status` to identify local changes before starting work.
2. If ontology logic changes are needed, edit `seovoc.owx` in Protege (or equivalent OWL editor).
3. Run conversion to regenerate `seovoc.owl` and `seovoc.ttl` using ROBOT (same tooling used in `.bin/publish.sh`).
4. Recompute and update `seovoc.owx.md5` from the new `seovoc.owx`.
5. Verify diffs in all affected files for consistency and intended ontology changes.
6. Commit `seovoc.owx`, generated artifacts, and checksum together.

## Validation and Verification

This repository does not currently include a unit test framework or language runtime test suite.

Minimum required verification for ontology changes:

- Conversion completes successfully from `seovoc.owx` to both `seovoc.owl` and `seovoc.ttl`.
- `seovoc.owx.md5` matches the current `seovoc.owx`.
- Git diff confirms expected class/property/axiom changes and no unintended drift.

Suggested local validation commands:

```bash
# Compare stored and current checksum
cat seovoc.owx.md5
md5sum seovoc.owx

# Regenerate output formats (requires Docker and ROBOT image)
docker run --rm -v "$(pwd):/work" obolibrary/robot \
  robot convert --input "/work/seovoc.owx" --format owl --output "/work/seovoc.owl"

docker run --rm -v "$(pwd):/work" obolibrary/robot \
  robot convert --input "/work/seovoc.owx" --format ttl --output "/work/seovoc.ttl"
```

If conversion tooling is unavailable locally, document that limitation explicitly in your handoff.

## Documentation and Index Sync

When ontology scope or semantics change, update documentation in the same change set:

- `README.md`:
  - class/property descriptions
  - use cases and examples
  - setup/contribution steps if workflow changed
- Any new docs directories (`docs/`, `specs/`) if introduced later.
- Any repository index files (`README.md`, `INDEX.md`, or directory summaries) to keep navigation current.
- `TODO.md` if present, to mark completed work and add follow-up debt/tasks.

If a referenced documentation file does not yet exist in this repository, do not invent it unless explicitly requested; note the gap in your summary.

## Commit and PR Expectations

- Keep commits atomic: ontology source + generated outputs + checksum + relevant docs.
- Include a clear commit message summarizing semantic impact (what changed in the ontology and why).
- In PR descriptions, include:
  - ontology areas impacted (classes/properties/constraints)
  - any migration or compatibility concerns for downstream consumers
  - verification steps performed locally

## Safety and Non-Destructive Practices

- Never use destructive git commands (for example, `git reset --hard`) unless explicitly requested.
- Do not revert unrelated local changes.
- Prefer inspecting and preserving user-authored modifications already present in the worktree.
