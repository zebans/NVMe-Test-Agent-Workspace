# NVM Write Zeroes Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| LBA range | `SLBA` + `NLB` | `NLB` is zero-based | Selects namespace LBA range to zero. |
| Deallocation request | `DEAC` | `0` no host deallocation request; `1` request deallocation | Selects deallocation behavior when namespace supports zero-value reads from deallocated LBAs. |
| Protection behavior | `PRINFO`, `STC`, `LBAT/LBATM`, `LBST/ILBRT` | `PRCHK=000b`; `STC=0` | Selects PI generation/check behavior. |
| Persistence | `FUA` | `0` no effect; `1` write to non-volatile media before completion | Selects persistence requirement. |
| Error recovery effort | `LR` | `0` full recovery; `1` limited retry | Selects controller retry effort. |
