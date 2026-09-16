# Directive Send Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.11 |
| Figures | 178-180 |
| Command | Directive Send |
| Opcode | `19h` |
| State | COMPLETE |

## Coverage Checklist

- [x] `DPTR`, `NUMD`, `DSPEC`, `DTYPE`, and `DOPER`.
- [x] Conditional `NSID=FFFFFFFFh` note.
- [x] Conditional `CDW12/CDW13` boundary.
- [x] Directive Type / Operation dependency.
- [x] Status boundary to section 8.7.
- [x] SPEC/API/test-flow boundary stated.
