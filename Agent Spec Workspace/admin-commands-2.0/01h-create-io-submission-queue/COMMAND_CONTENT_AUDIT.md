# Create I/O Submission Queue Content Audit

## Source Coverage

| Item | Value |
|---|---|
| Source | NVMe Base Spec 2.0 |
| Section | 5.5 |
| Command | Create I/O Submission Queue |
| Opcode | `01h` |
| State | COMPLETE |

## Coverage Checklist

- [x] Command purpose and host-to-controller queue memory behavior.
- [x] `PRP1` contiguous/non-contiguous rules.
- [x] PRP List lifetime and undefined modification behavior.
- [x] PRP offset invalid behavior.
- [x] `CDW10.QSIZE` and `CDW10.QID` rules.
- [x] `CDW11.CQID` and `Completion Queue Invalid` behavior.
- [x] `CDW11.QPRIO` values and arbitration dependency.
- [x] `CDW11.PC`, `CAP.CQR`, and CMB/CQPDS restrictions.
- [x] `CDW12.NVMSETID` / SQ Associations behavior.
- [x] Completion to Admin Completion Queue.
- [x] Command-specific status values.
- [x] SPEC/API/test-flow boundary stated.
