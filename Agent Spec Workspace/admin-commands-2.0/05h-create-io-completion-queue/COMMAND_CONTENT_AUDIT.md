# Create I/O Completion Queue Content Audit

## Source Coverage

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.4 |
| Command | Create I/O Completion Queue |
| Opcode | `05h` |
| State | COMPLETE |

## Coverage Checklist

- [x] Command purpose and host-to-controller queue memory behavior.
- [x] `PRP1` contiguous/non-contiguous rules.
- [x] PRP List lifetime and undefined modification behavior.
- [x] PRP offset invalid behavior.
- [x] `CDW10.QSIZE` and `CDW10.QID` rules.
- [x] `CDW11.IV`, `CDW11.IEN`, and `CDW11.PC` rules.
- [x] `CAP.CQR` and CMB/CQPDS restrictions.
- [x] Completion to Admin Completion Queue.
- [x] Command-specific status values.
- [x] SPEC/API/test-flow boundary stated.
