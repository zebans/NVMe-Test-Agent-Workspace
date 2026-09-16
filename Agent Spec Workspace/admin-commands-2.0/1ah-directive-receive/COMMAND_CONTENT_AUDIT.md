# Directive Receive Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.10 |
| Figures | 174-177 |
| Command | Directive Receive |
| Opcode | `1Ah` |
| State | COMPLETE |

## Coverage Checklist

- [x] `DPTR`, `NUMD`, `DSPEC`, `DTYPE`, and `DOPER`.
- [x] Conditional `NSID=FFFFFFFFh` note.
- [x] Conditional `CDW12/CDW13` boundary.
- [x] `NUMD` truncation / over-allocation behavior.
- [x] `Namespace is Write Protected` status.
- [x] SPEC/API/test-flow boundary stated.
