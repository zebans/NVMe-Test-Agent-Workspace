# Create I/O Submission Queue Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Completion Queue Invalid` | `CQID` is within supported range but does not identify a created I/O CQ. | Completion target exists syntactically but not as an active CQ. |
| `Invalid Queue Identifier` | `QID` is `0h`, outside supported range, already in use, or `CQID` is `0h`/outside supported range. | Queue identifier selection is illegal. |
| `Invalid Queue Size` | `QSIZE` is `0h` or larger than supported. | Requested queue depth is illegal. |
| `Invalid Field in Command` | `PC=0` while `CAP.CQR=1`, or non-zero unknown `NVMSETID` when SQ Associations are supported. | Command field conflicts with controller capability/state. |
| `Invalid Use of Controller Memory Buffer` | Queue is located in CMB, `PC=0`, and `CMBLOC.CQPDS=0`. | CMB placement is illegal for this queue layout. |
| `PRP Offset Invalid` | `PRP1` or PRP List entries use non-zero offsets where offset `0h` is required. | Queue memory descriptor is malformed. |

## Notes

The first three statuses are command-specific for Create I/O Submission Queue. The remaining entries are important generic/cross-command validation outcomes explicitly relevant to this command's field rules.
