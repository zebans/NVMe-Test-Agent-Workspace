# Zone Append Cross-Spec Boundary

## Base Spec Owned

- Common Command Format.
- Data Pointer and Metadata Pointer field definitions.
- Generic completion queue structure.
- Generic status behavior.

## NVM Command Set Owned

- End-to-end protection information baseline behavior.
- PRINFO and PRCHK behavior.
- Atomicity parameters.

## ZNS Owned

- Opcode `7Dh`.
- Zone Append command semantics.
- `ZSLBA` zone selection rule.
- `PIREMAP` behavior.
- `ALBA` completion behavior.
- Zone-specific command status values.

## Not Owned Here

- PyNVMe3 call mapping.
- Test setup, flow order, cleanup, or pass/fail script design.
