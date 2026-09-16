# Create I/O Submission Queue Selector Reference

| Selector | Location | Meaning | Validity rule | Status on violation |
|---|---|---|---|---|
| Submission Queue Identifier | `CDW10.QID` | Selects the I/O SQ identifier to create. | Shall be non-zero, supported, and unused. | `Invalid Queue Identifier` |
| Queue size | `CDW10.QSIZE` | Selects SQ size as zero-based value. | `0h` or larger-than-supported values are invalid. | `Invalid Queue Size` |
| Completion Queue Identifier | `CDW11.CQID` | Selects the I/O CQ used for completions from this SQ. | `0h` or outside supported range is invalid; in-range but not created is completion-queue invalid. | `Invalid Queue Identifier` or `Completion Queue Invalid` |
| Queue priority | `CDW11.QPRIO` | Selects SQ priority class. | Used only with weighted round robin with urgent priority class arbitration; otherwise ignored. | Usually no error when ignored. |
| Physical Contiguous | `CDW11.PC` | Selects contiguous vs PRP List-backed queue memory. | If `PC=0` while `CAP.CQR=1`, invalid. | `Invalid Field in Command` |
| NVM Set association | `CDW12.NVMSETID` | Optionally associates SQ with an NVM Set. | Non-zero unsupported/unknown NVM Set when SQ Associations are supported is invalid. | `Invalid Field in Command` |

## Lookup Notes

- Use `QID` to identify which SQ is being created.
- Use `CQID` to verify the completion target exists before the SQ is created.
- Use `NVMSETID` only when SQ Associations are relevant.
