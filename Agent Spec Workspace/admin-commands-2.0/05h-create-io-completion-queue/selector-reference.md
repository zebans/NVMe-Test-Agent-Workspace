# Create I/O Completion Queue Selector Reference

| Selector | Location | Meaning | Validity rule | Status on violation |
|---|---|---|---|---|
| Completion Queue Identifier | `CDW10.QID` | Selects the I/O CQ identifier to create. | Shall be non-zero, supported, and unused. | `Invalid Queue Identifier` |
| Queue size | `CDW10.QSIZE` | Selects CQ size as zero-based value. | `0h` or larger-than-supported values are invalid. | `Invalid Queue Size` |
| Interrupt Vector | `CDW11.IV` | Selects interrupt vector for the CQ. | Transport/controller-specific validity. | `Invalid Interrupt Vector` |
| Physical Contiguous | `CDW11.PC` | Selects contiguous vs PRP List-backed queue memory. | If `PC=0` while `CAP.CQR=1`, invalid. | `Invalid Field in Command` |

## Lookup Notes

- Use `QID` to identify which CQ is being created.
- Use `QSIZE` to interpret actual entry count as `QSIZE + 1`.
- Use `PC` with `CAP.CQR` and CMB/CQPDS capability state to determine memory-layout validity.
