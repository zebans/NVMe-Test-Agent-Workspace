# Get LBA Status Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Source table | Figure 138 |
| Command | Get LBA Status |
| Opcode | `86h` |
| State | COMPLETE |

## Coverage Checklist

- [x] Opcode and data direction.
- [x] NSID boundary.
- [x] NVM/ZNS command-set-specific ownership boundary.
- [x] Canonical payload routing file exists so lookup does not stop at a boundary stub.
- [x] SPEC/API/test-flow boundary stated.
