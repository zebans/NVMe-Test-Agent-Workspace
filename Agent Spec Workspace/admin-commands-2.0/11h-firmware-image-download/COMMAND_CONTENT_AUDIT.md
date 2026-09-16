# Firmware Image Download Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.13 |
| Figures | 184-187 |
| Command | Firmware Image Download |
| Opcode | `11h` |
| State | COMPLETE |

## Coverage Checklist

- [x] `DPTR`, `CDW10.NUMD`, and `CDW11.OFST`.
- [x] `FWUG` alignment/granularity dependency.
- [x] Firmware piece and Boot Partition ordering rules.
- [x] Download / Commit / reset discard behavior.
- [x] Status values and validation outcomes.
- [x] SPEC/API/test-flow boundary stated.
