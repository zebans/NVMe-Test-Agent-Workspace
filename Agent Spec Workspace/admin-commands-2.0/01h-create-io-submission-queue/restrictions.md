# Create I/O Submission Queue Restrictions

| Restriction | Meaning | Violation result |
|---|---|---|
| Admin SQ is not created here | Admin SQ is created through `ASQ`. | Use controller initialization path, not this command. |
| `QID` shall be valid and unused | I/O SQ identifier cannot be `0h`, unsupported, or already allocated. | `Invalid Queue Identifier` |
| `QSIZE` is zero-based but cannot be `0h` | Queue size field encodes entries minus one, with `0h` invalid here. | `Invalid Queue Size` |
| `CQID` shall refer to an existing I/O CQ | Completion target must already be created. | `Invalid Queue Identifier` or `Completion Queue Invalid` |
| PRP offsets shall be `0h` | Queue memory entries are page-aligned queue descriptors. | `PRP Offset Invalid` |
| `PC=0` requires non-contiguous queue support | If `CAP.CQR=1`, controller requires contiguous queues. | `Invalid Field in Command` |
| CMB placement depends on CQPDS | Non-contiguous queue in CMB requires `CMBLOC.CQPDS=1`. | `Invalid Use of Controller Memory Buffer` |
| NVM Set association is optional and capability-dependent | Unknown non-zero `NVMSETID` is invalid when SQ Associations are supported. | `Invalid Field in Command` |

## NVM Set Guidance

If `NVMSETID` is non-zero and accepted, host software should not submit commands for namespaces associated with other NVM Sets through this SQ.
