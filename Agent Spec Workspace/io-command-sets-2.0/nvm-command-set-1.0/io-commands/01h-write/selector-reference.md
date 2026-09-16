# NVM Write Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| LBA range | `SLBA` + `NLB` | `NLB` is zero-based | Selects namespace LBA range to write. |
| Protection behavior | `PRINFO`, `STC`, `LBAT/LBATM`, `LBST/ILBRT` | Depends on namespace PI format | Selects PI generation/check behavior. |
| Cache persistence | `FUA` | `0` no effect; `1` commit before completion | Selects completion persistence requirement. |
| Error recovery effort | `LR` | `0` full recovery; `1` limited retry | Selects controller retry effort. |
| Directive | `DTYPE` + `DSPEC` | Base Directives model | Selects directive-specific behavior such as Streams. |
| DSM hints | `CDW13` bits `07:00` | Incompressible, sequential, latency, frequency | Advisory optimization information. |

## DSM Hint Bits

| Bits | Field | Meaning |
|---|---|---|
| `07` | Incompressible | Set means data is not compressible. |
| `06` | Sequential Request | Set means command is part of a sequential write. |
| `05:04` | Access Latency | `00b` none, `01b` idle, `10b` normal, `11b` low. |
| `03:00` | Access Frequency | `0h` none, `1h` typical, `2h` infrequent write/read, `3h` infrequent write/frequent read, `4h` frequent write/infrequent read, `5h` frequent write/read, `6h` one-time write, `7h`-`Fh` reserved. |
