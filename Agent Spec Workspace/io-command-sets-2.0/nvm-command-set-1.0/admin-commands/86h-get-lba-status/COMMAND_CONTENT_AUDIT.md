# NVM Get LBA Status Content Audit

Status: COMPLETE for NVM command fields, selector behavior, returned payload layout, completion conditions, restrictions, and cross-spec boundaries.

Source: NVM Command Set Specification 1.0 sections 4.1.3.3, 4.1.4.5, 4.2.1, and 5.8.1; Figures 85, 93-95, and 107-112.

## Coverage Checklist

- [x] Command identity and Base opcode relationship.
- [x] Capability and supporting feature/log page context.
- [x] `DPTR`, `SLBA`, `MNDW`, `ATYPE`, and `RL`.
- [x] `ATYPE=10h` and `ATYPE=11h` behavior.
- [x] LBA Status Descriptor List offsets and `CMPC` values.
- [x] LBA Status Descriptor Entry offsets and status bits.
- [x] LBA Status Information log page relationship.
- [x] Boundary to Base Admin opcode, ZNS, API, and test-flow layers.

## Completion Meaning

This folder is complete for NVM Get LBA Status lookup. It is intentionally not a PyNVMe recipe and does not define ZNS-specific zone behavior.
