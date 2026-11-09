# Independent review: code

## 0.4.1 metadata-only migration

The current SOURCE-HASH below binds the 0.4.1 non-executable provenance packaging. The recorded behavioral rounds below were not rerun against this new package or the new total-role text. Only their evidence for the byte-identical methods is carried forward. Standalone SKILL.md, method bodies, dependency/article references, templates and legal text are unchanged. The original review body and historical failures follow unchanged, except for the current SOURCE-HASH field.

PREVIOUS-SOURCE-HASH: cf1c41241b55a445137b46c6041a7e88cedb44dc1efd2cce58b043ada39fb894
PREVIOUS-REVIEW-SHA256: 588002a20971bcb7f55604877553182bc917b1193f6a15cd366bcec3a81fb5cd
Migration findings and limits: [role-provenance-review.md](role-provenance-review.md). This is static packaging evidence, not a new behavior test, identity test, host-runtime test or production certification.

## Current snapshot
SOURCE-HASH: 6ee6e5885e469040a63cc29443575e23815fd51ba1fb65887cee77b556af3e8d
Package: dist/modules/zhxbai-fde-code

## Static findings
Engineering distinct from Skill writing; inspect-only does not imply modification. Unit/mock/entry/business checks separate. Existing implementation permission retained; deliver/run bundled.

Entry description routes to its specific method. Dependency method/article closure matched registry. Packaged methods/articles/templates byte-equal canonical. All 33 canonical guide articles match local pinned upstream prose after normalizing Markdown/HTML URLs; original and packaged SHA256 values match manifest. No alternate duplicate method body within module; dependency copies across packages intentionally support standalone use. Host discovery/install/run untested.


## Packaging recheck
Latest recheck: SOURCE-HASH matches tools/current-module-hashes.json; every bundled method/article/template matches canonical bytes; dependency closure and root licenses match canonical, with no broken local Markdown file links.
PASS. Root LICENSE and licenses resolve all three previously broken attribution links. Rechecked every Markdown file reference: no missing local file target. Local method/article closure exactly matches registry; canonical methods/articles/templates remain byte-equal. Standalone navigation now lists bundled methods only. Initial packaging defect is resolved.

## Historical round 1 review (old source)
Evidence: qa/evidence/b-r1-code.md
Verdict: PASS for the recorded offline behavioral scenario. Blocked acceptance of login-only update gate, preserved inspect-only scope and separated reported mock from actual authorization verification.
Round 1 was grouped-context response testing, not clean host activation. Core method content is unchanged across packaging fix; it does not independently attest current wrapper discovery.

## Historical round 2 review (old source)
Evidence: qa/evidence/b-r2-code.md
Verdict: NEEDS CORRECTION. Accurate user-reported mock versus real-entry status, inspect-only scope and no Skill substitute. However it prescribes creating a test customer, updating fields, and supplementing query/create ownership checks without establishing which operations the current project includes. Calling these "requirements" imports guide examples into current scope. Proposed operations are contingent on later authorization and were not executed, so this is scope-contract failure, not an observed unauthorized CRM action.
Minimum correction: derive tests from confirmed project operations; query/create/update examples only if that operation is actually in scope. Run a fresh isolated scenario explicitly limited to read-only scope; preserve this failed response as evidence.

## Limits
Evidence supports static self-containment and recorded behavioral responses only, not host skill discovery/installation, real service calls, real-data correctness, long-term reliability, or complete coverage of every scenario. Source reads in some round-1 guide batches were truncated; complete core methods plus actual responses were available. No business action was executed by this reviewer.

## Current-source correction
Canonical engineering step 3 now explicitly derives tests from confirmed operations, makes writes conditional, prohibits adding writes/permissions to read-only work, and uses a non-CRUD-specific framework when scope is unknown. Packaged method bytes and current SOURCE-HASH rechecked. Old round 1/2 do not qualify this changed source.

## Current behavioral round 1
Evidence: qa/evidence/b-r3-code.md
PASS for recorded isolated offline scenario. Respects explicit read-only owner scope, derives allow/deny and optional identity-tamper checks from that scope, uses existing authorized test records, requests no new/write permissions, and preserves user-report versus personal verification distinction. Old CRUD inflation does not recur. No actual CRM execution or code edit.

## Current behavioral round 2
Evidence: qa/evidence/b-r5-code.md
PASS for isolated unknown-scope case. Clearly marks supplied mock results as reported, keeps incomplete requirement coverage unknown, requests actual project operations before test selection, and does not add CRUD from guide examples. Real tests remain future and conditional on scope/account/authorization. No implementation or business Skill substituted for requested review.
Supplementary b-r4-code.md is deliberately not used to meet the two-round gate because parent sent an intervening scope reminder, making clean isolation uncertain. Current qualifying pair is r3 and r5.

## Verdict
PASS for current source static checks and r3/r5 isolated offline behavior only; no host-runtime certification. Historical r2 failure is preserved, not counted toward passing current source.
