# ZNS-Modified Write Content Audit

Status: `COMPLETE + CANONICAL`

Audited:

- ZNS section 3.3.7.
- ZNS Figure 19.

Captured:

- [x] Write remains owned by the NVM Command Set.
- [x] ZNS adds zone boundary restrictions.
- [x] ZNS adds write pointer restriction.
- [x] ZNS adds target zone state restrictions for Full, Read Only, and Offline.
- [x] ZNS adds active/open zone resource status conditions.
- [x] Additional ZNS status values `B8h` through `BEh` are captured in `status-reference.md`.

Delegated / outside this command folder:

- NVM Write CDW field definitions.
- Base NVM Write completion and status behavior.
- Full shared ZNS zone model.

Canonical files:

- [x] `command-facts.md`
- [x] `selector-reference.md`
- [x] `field-reference.md`
- [x] `payload-reference.md`
- [x] `status-reference.md`
- [x] `restrictions.md`
- [x] `cross-spec-boundary.md`
