# Vendor Specific I/O Commands Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Source table | Figure 390 |
| Opcode range | `80h`-`FFh` |
| State | COMPLETE |

## Coverage Checklist

- [x] Vendor-specific I/O opcode range.
- [x] NSID usage boundary.
- [x] Boundary against invented fields/status/payload.
- [x] SPEC/API/test-flow boundary stated.
