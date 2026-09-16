# ZNS-Modified Write Zeroes Content Audit

Status: `COMPLETE + CANONICAL`

Audited:

- ZNS section 3.3.9.
- ZNS Figure 21.

Captured:

- [x] Write Zeroes remains owned by the NVM Command Set.
- [x] ZNS adds zone boundary restrictions.
- [x] ZNS adds write pointer and zone state restrictions.
- [x] ZNS adds active/open zone resource status conditions.
- [x] ZNS deallocation behavior boundary is captured.
- [x] Additional ZNS status values `B8h` through `BEh` are captured in `status-reference.md`.

Delegated / outside this command folder:

- NVM Write Zeroes CDW field definitions.
- Base NVM Write Zeroes completion and status behavior.
- Detailed deallocation behavior where owned by the NVM/ZNS model.

Canonical files:

- [x] `command-facts.md`
- [x] `selector-reference.md`
- [x] `field-reference.md`
- [x] `payload-reference.md`
- [x] `status-reference.md`
- [x] `restrictions.md`
- [x] `cross-spec-boundary.md`
