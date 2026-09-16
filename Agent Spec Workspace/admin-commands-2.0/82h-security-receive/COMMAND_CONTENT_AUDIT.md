# Security Receive Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.25 |
| Figures | 306-309 |
| Command | Security Receive |
| Opcode | `82h` |
| State | COMPLETE |

## Coverage Checklist

- [x] `DPTR`, `SECP`, `SPSP1`, `SPSP0`, `NSSF`, and `AL`.
- [x] Security Protocol `00h` discovery behavior.
- [x] Security Protocol `EAh` values.
- [x] Receive data retention boundary.
- [x] Base/SPC-5 boundary.
- [x] Status and unsupported protocol validation.
- [x] SPEC/API/test-flow boundary stated.
