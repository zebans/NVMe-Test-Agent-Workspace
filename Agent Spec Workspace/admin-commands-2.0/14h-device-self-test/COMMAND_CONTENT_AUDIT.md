# Device Self-test Content Audit

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.9 |
| Figures | 170-173 |
| Command | Device Self-test |
| Opcode | `14h` |
| State | COMPLETE |

## Coverage Checklist

- [x] `NSID` namespace test action values.
- [x] `CDW10.STC` values.
- [x] Self-test in progress processing matrix.
- [x] Device Self-test Log interaction at command level.
- [x] `DSTO` scope note.
- [x] Command-specific and namespace-related statuses.
- [x] SPEC/API/test-flow boundary stated.
