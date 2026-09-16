# Connect Content Audit

Status: `COMMAND-CONTROL-COMPLETE + CANONICAL`

Audited source:

- Base Spec 2.0 section 6.3
- Figure 380
- Figure 381
- Figure 382
- Figure 383
- Figure 97

Captured:

- `OPC=7Fh`
- `FCTYPE=01h`
- SQE fields
- Connect command data
- Connect response
- Figure 383 status-specific Dword 0 behavior
- SQ flow control negotiation
- dynamic/static controller model restrictions
- command-specific status values

Not expanded:

- Transport binding mechanics for address reachability.
- Full authentication protocol exchange beyond `AUTHREQ` ownership.

Canonical files:

- [x] `command-facts.md`
- [x] `selector-reference.md`
- [x] `field-reference.md`
- [x] `payload-reference.md`
- [x] `status-reference.md`
- [x] `restrictions.md`
- [x] `cross-spec-boundary.md`
