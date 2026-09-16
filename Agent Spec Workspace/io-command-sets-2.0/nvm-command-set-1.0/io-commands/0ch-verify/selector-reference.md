# NVM Verify Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| LBA range | `SLBA` + `NLB` | `NLB` is zero-based | Selects namespace LBA range to verify. |
| Protection behavior | `PRINFO`, `STC`, `ELBAT/ELBATM`, `ELBST/EILBRT` | `PRACT` shall be cleared | Selects PI checking behavior. |
| Media source | `FUA` | `0` no effect; `1` verify committed non-volatile media data | Selects volatile-cache handling. |
| Error recovery effort | `LR` | `0` full recovery; `1` limited retry | Selects controller retry effort. |
