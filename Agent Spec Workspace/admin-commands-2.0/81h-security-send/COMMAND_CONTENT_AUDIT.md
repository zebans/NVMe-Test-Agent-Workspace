# Security Send Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.26 |
| Figures | 310-312 |
| Command | Security Send |
| Opcode | `81h` |
| State | COMPLETE |

## Coverage Checklist

- [x] `DPTR`, `SECP`, `SPSP1`, `SPSP0`, `NSSF`, and `TL`.
- [x] Security Protocol `EAh` values.
- [x] Send/Receive association boundary.
- [x] Base/SPC-5 boundary.
- [x] Status and reserved protocol validation.
- [x] SPEC/API/test-flow boundary stated.
