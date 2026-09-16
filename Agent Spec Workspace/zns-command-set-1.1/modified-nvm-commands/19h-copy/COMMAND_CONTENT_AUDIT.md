# ZNS-Modified Copy Content Audit

Status: `COMPLETE + CANONICAL`

Audited source:

- ZNS 1.1 section 3.3.2.
- ZNS Figure 14.

Captured:

- [x] Copy remains owned by the NVM Command Set.
- [x] ZNS adds source and destination zone boundary restrictions.
- [x] ZNS adds destination zone state restrictions for Full, Read Only, Offline, and write pointer position.
- [x] ZNS adds source zone Offline handling.
- [x] ZNS adds active/open zone resource limit status conditions.
- [x] Additional ZNS status values `B8h` through `BEh` are captured in `status-reference.md`.

Boundary:

- This folder does not duplicate NVM Copy command fields or Source Range Entry structure.
- Use the NVM Command Set reference for base Copy command layout and this folder for ZNS-specific status and zone-state restrictions.

Canonical files:

- [x] `command-facts.md`
- [x] `selector-reference.md`
- [x] `field-reference.md`
- [x] `payload-reference.md`
- [x] `status-reference.md`
- [x] `restrictions.md`
- [x] `cross-spec-boundary.md`
