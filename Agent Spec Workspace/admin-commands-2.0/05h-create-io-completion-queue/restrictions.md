# Create I/O Completion Queue Restrictions

| Restriction | Meaning | Violation result |
|---|---|---|
| Admin CQ is not created here | Admin CQ is created through `ACQ`. | Use controller initialization path, not this command. |
| `QID` shall be valid and unused | I/O CQ identifier cannot be `0h`, unsupported, or already allocated. | `Invalid Queue Identifier` |
| `QSIZE` is zero-based but cannot be `0h` | Queue size field encodes entries minus one, with `0h` invalid here. | `Invalid Queue Size` |
| PRP offsets shall be `0h` | Queue memory entries are page-aligned queue descriptors. | `PRP Offset Invalid` |
| `PC=0` requires non-contiguous queue support | If `CAP.CQR=1`, controller requires contiguous queues. | `Invalid Field in Command` |
| CMB placement depends on CQPDS | Non-contiguous queue in CMB requires `CMBLOC.CQPDS=1`. | `Invalid Use of Controller Memory Buffer` |
