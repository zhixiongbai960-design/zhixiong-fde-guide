# Offline packaging

## Current 0.5.0 advisory packages

All 18 module versions and the expert/source snapshot are 0.5.0. Genuine current-hash module responses and independent reviews are bound in qa/modules.json; the old attestation is retained in qa/history. The original ambiguous review chain remains unresolved history, while the separately pre-reviewed review-v2 chain supplies the current accepted pair.

`python3 tools/package.py verify --target modules` checks the exact tested module trees. `python3 tools/package_expert.py build` and `verify` use the unchanged QA gate. The final expert package needs separate sequential cross-route tests before a full-plan pass can be claimed. Packaging, behavior, publication and real host installation are distinct results.

`package.py build-total` produces the legacy name from current methods, not the frozen 0.4.2 package. Do not replace historical total or fde-* entries. Run the current full packaging suite with `python3 -m unittest discover -s tests -v`; only the expected expert version was adapted to 0.5.0, with negative tests and original baseline preserved.

## Original method and legacy-total builder

Run from any working directory with Python 3. No additional dependencies or downloaded code are executed. Paths are fixed relative to this script's project root; no arbitrary source/output option exists.

- `python3 tools/package.py build-modules`: validate source and build all standalone packages.
- `python3 tools/package.py hashes`: emit current per-module source hashes.
- `python3 tools/package.py build-total`: assemble only after module QA gate passes.
- `python3 tools/package.py verify --target modules` (or `total`): check exact release file integrity and current source/QA equivalence.
- `python3 tools/package.py rollback --target total`: swap the current and previous verified release. Source changes do not prevent rollback. After rollback, current-source verification may correctly fail because the old version differs.
- `python3 -m unittest discover -s tests -v`: synthetic packaging safety tests, not behavior QA.

Run one writer at a time. Build inputs are validated before output changes. A staged tree is verified and promoted via same-filesystem renames; caught promotion failures restore the previous release. There is a brief gap between old and new directory renames, not a claim of crash-proof multi-directory transactions. Do not run installation/readers during promotion. A successful rebuild preserves one previous release at `dist/<target>.previous`. Rollback preserves the replaced release there too.

## Source and attestation

`src/registry.json` has `modules`, with each module containing `id`, `name`, `title`, `description`, `method_file`, `articles`, and `dependencies`. References are filenames, dependency IDs must exist and form a DAG. All source/output/evidence symlinks are rejected. A module includes its dependency closure, their articles, transitively referenced templates, legal records, and closure-specific source records. The guide index is generated for the selected subset. Root SKILL wrappers link methods rather than inlining bodies, preserving relative references.

Module hashes cover selected source bytes, only closure registry entries, selected article provenance and packager implementation. Global navigation, total entrypoint/version, unrelated module metadata and unrelated article records do not participate. Shared tooling, templates and legal changes intentionally invalidate every package that carries them; closure metadata changes invalidate only affected packages. Record hashes only after content/tooling are final. A module QA entry in `qa/modules.json` uses:

```json
{"modules": [{"id": "module-id", "source_hash": "hashes-command-output", "rounds": [{"id": "round-1", "transcript_path": "qa/module-id-round-1.md", "reviewer_verdict": "pass", "notes": "Concrete reviewer findings"}, {"id": "round-2", "transcript_path": "qa/module-id-round-2.md", "reviewer_verdict": "pass", "notes": "Concrete reviewer findings"}], "independent_review": {"path": "qa/module-id-review.md", "verdict": "pass"}}]}
```

This is a schema illustration, never evidence. Every module must have at least two distinct rounds and distinct nonempty transcript files, plus a separate nonempty independent review file. Evidence paths must stay under `qa/`. The gate rejects missing, stale, incomplete or failed attestations. It cannot prove a transcript is genuine, a reviewer is independent, or a semantic judgment is correct. The responsible human must check actual behavior and reviewer identity; never manufacture reports to satisfy the gate. Total snapshots preserve the checked reports and attestation, covered by the release integrity manifest.

Both package types place LICENSE and licenses/ at package root. Standalone navigation includes only its method closure; registry is excluded, and requirement-specific provenance is omitted when that method is absent. Total packages retain all source records under references/. Canonical provenance links are not rewritten.

Use `python3 tools/package.py affected --module need` (repeat `--module` for multiple IDs) to list changed modules and transitive dependents. This dependency query covers module changes; for article changes compare current hashes, and shared tooling/legal changes require all-module review. Standalone references/module-registry.json contains only the included closure.

Templates are selected only when referenced by included methods/templates using a templates/ path. Missing referenced templates fail validation; unused templates do not affect module identity.
