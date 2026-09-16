# Abort Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.1 |
| Figures | 140-141 |
| Command | Abort |
| Opcode | `08h` |
| State | COMPLETE |

## Coverage Checklist

- [x] `CDW10.SQID` and `CDW10.CID`.
- [x] Best-effort Abort behavior.
- [x] Identify Controller `ACL` dependency.
- [x] Abort completion DW0 bit 0 meaning.
- [x] Target completion ordering.
- [x] Command-specific statuses.
- [x] SPEC/API/test-flow boundary stated.
