# Doorbell Buffer Config Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.8 |
| Figures | 167-169 |
| Command | Doorbell Buffer Config |
| Opcode | `7Ch` |
| State | COMPLETE |

## Coverage Checklist

- [x] `PRP1` and `PRP2` buffer pointers.
- [x] Shadow Doorbell and EventIdx ownership.
- [x] Buffer offset formula.
- [x] `CAP.DSTRD` and `max(NSQA, NCQA)` relationship.
- [x] Invalid address status.
- [x] SPEC/API/test-flow boundary stated.
