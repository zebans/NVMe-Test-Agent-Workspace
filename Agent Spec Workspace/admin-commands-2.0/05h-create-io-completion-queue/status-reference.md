# Create I/O Completion Queue Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Invalid Queue Identifier` | `QID` is `0h`, outside supported range, or already in use. | CQ identity is illegal. |
| `Invalid Queue Size` | `QSIZE` is `0h` or larger than supported. | Requested queue depth is illegal. |
| `Invalid Interrupt Vector` | `IV` is invalid for the controller/transport. | Interrupt vector selection is illegal. |
| `Invalid Field in Command` | `PC=0` while `CAP.CQR=1`. | Controller requires contiguous queues. |
| `Invalid Use of Controller Memory Buffer` | Queue is located in CMB, `PC=0`, and `CMBLOC.CQPDS=0`. | CMB placement is illegal for this queue layout. |
| `PRP Offset Invalid` | `PRP1` or PRP List entries use non-zero offsets where offset `0h` is required. | Queue memory descriptor is malformed. |

## Notes

The first three statuses are command-specific for Create I/O Completion Queue. The remaining entries are important generic/cross-command validation outcomes explicitly relevant to this command's field rules.
