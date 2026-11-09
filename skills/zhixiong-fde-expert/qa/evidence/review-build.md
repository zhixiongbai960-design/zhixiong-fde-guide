# Independent review: build

## 0.4.1 metadata-only migration

The current SOURCE-HASH below binds the 0.4.1 non-executable provenance packaging. The recorded behavioral rounds below were not rerun against this new package or the new total-role text. Only their evidence for the byte-identical methods is carried forward. Standalone SKILL.md, method bodies, dependency/article references, templates and legal text are unchanged. The original review body and historical failures follow unchanged, except for the current SOURCE-HASH field.

PREVIOUS-SOURCE-HASH: d8921b43e4fb365523fda442e6f6d115fd086eb6216c91754e714e2a671d076a
PREVIOUS-REVIEW-SHA256: 0410b8ecc221e0f60160cf9619432f8de5f74f882cf28456b00b733ac3b237c7
Migration findings and limits: [role-provenance-review.md](role-provenance-review.md). This is static packaging evidence, not a new behavior test, identity test, host-runtime test or production certification.

## Current snapshot
SOURCE-HASH: 6d0d542c48516451ee5ed7bdda4fda3fb45acfe25a2f229022c05985afa9a12f
Package: dist/modules/zhxbai-fde-build

## Static findings
Method/configuration separated; complete Skill source required. Normal/failure/novel-change tests and host-test limits explicit. Source output never authorizes installation/publication.

Entry description routes to its specific method. Dependency method/article closure matched registry. Packaged methods/articles/templates byte-equal canonical. All 33 canonical guide articles match local pinned upstream prose after normalizing Markdown/HTML URLs; original and packaged SHA256 values match manifest. No alternate duplicate method body within module; dependency copies across packages intentionally support standalone use. Host discovery/install/run untested.


## Packaging recheck
Latest recheck: SOURCE-HASH matches tools/current-module-hashes.json; every bundled method/article/template matches canonical bytes; dependency closure and root licenses match canonical, with no broken local Markdown file links.
PASS. Root LICENSE and licenses resolve all three previously broken attribution links. Rechecked every Markdown file reference: no missing local file target. Local method/article closure exactly matches registry; canonical methods/articles/templates remain byte-equal. Standalone navigation now lists bundled methods only. Initial packaging defect is resolved.

## Historical round 1 review (old source)
Evidence: qa/evidence/c-r1-build.md
Verdict: PASS for the recorded offline behavioral scenario. Produced full frontmatter/method/configuration/Decimal reference implementation and unrun test plan. No installation or execution claim. Generated business artifact itself remains unexecuted.
Round 1 was grouped-context response testing, not clean host activation. Core method content is unchanged across packaging fix; it does not independently attest current wrapper discovery.

## Historical round 2 review (old source)
Evidence: qa/evidence/c-r2-build.md
Verdict: NEEDS CORRECTION of generated artifact contract before passing. Seven source bodies are supplied with valid-looking deterministic Decimal comparisons, private configuration separation, empty integration placeholders and explicit unrun status. No real secret values, interface success, installation or execution were invented. Public distribution uses a whitelist rather than relying on gitignore as redaction.

Concrete defect: generated SKILL.md says outputs preserve request_id, rule version and rule source. scripts/gate.py blocked(code) emits none of these on every failure, including failures after valid request_id/config data are available (e.g. missing amount). This breaks its declared failure traceability contract. Either retain validated available metadata and null for unavailable metadata with tests, or explicitly narrow the output contract and describe failure association accurately. Do not report the generated tests as run; this review inspected text only.

## Limits
Evidence supports static self-containment and recorded behavioral responses only, not host skill discovery/installation, real service calls, real-data correctness, long-term reliability, or complete coverage of every scenario. Source reads in some round-1 guide batches were truncated; complete core methods plus actual responses were available. No business action was executed by this reviewer.

## Current-source correction
Authoritative build method now requires separate success/failure output contracts, implementation field-by-field checks, safe available identifiers or explicit null/absence, and failure-field assertions. Current packaged method bytes equal canonical; current hash recorded above. Old r1/r2 do not qualify changed source. Parent reports old generated code's ten tests pass, but these omit the defective traceability contract and cannot override the observed defect.

## Current behavioral round 1
Evidence: qa/evidence/c-r3-build.md (includes original context plus unchanged JSON artifact).
PASS. Original prompt explicitly supplies finite JSON-number input, nonempty anonymous string request_id, fixed v1/user-confirmed provenance and four mandatory response fields. Three complete source bodies implement that precise contract via one response constructor. Invalid ID/parse failures produce null ID; valid ID survives later amount/internal failures; fixed provenance is retained. Tests assert entire failure objects, invalid input non-echo, duplicate keys, override attempts and read/internal exceptions. No invented unit prerequisite or external integration is added. Anonymousness is explicitly a caller obligation; string validation does not pretend to prove it. Static AST and JSON checks are recorded separately from unrun tests and absent host validation. Process/start/stdout failure limit is stated.

### Additional execution evidence, not a substitute round
qa/evidence/build-generated-code-r3-check.md records parent's later standard-library synthetic execution: 13 tests, exit 0. This reviewer read the record rather than rerunning code. It includes failure correlation/provenance assertions missing from old r2. It is not target-host activation, interface integration or production certification; original tester's unrun statement remains accurate for its own stage.

## Current behavioral round 2
Evidence: qa/evidence/c-r4-build.md.
PASS. Actual supplied defect scenario is now present verbatim. Response pinpoints success key mismatch, lost failure fields, private configuration in public source, insufficient single-status test and unsupported production claim. Supplies consistent success/early-failure/later-failure examples plus ten regression categories; source provenance null semantics and safe correlation are explicit. Does not request real secrets, silently publish/install, fabricate business threshold or claim tests ran. Proposed schema changes and additional states remain recommendations, not invented existing business facts.

## Verdict
PASS for current-source static self-containment and r3/r4 isolated offline behavioral evidence. Historic r2 output-contract failure remains preserved and does not qualify current source. No target-host or production certification.
