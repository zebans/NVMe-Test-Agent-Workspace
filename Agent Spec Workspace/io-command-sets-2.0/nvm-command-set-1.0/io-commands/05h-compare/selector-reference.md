# NVM Compare Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| LBA range | `SLBA` + `NLB` | `NLB` is zero-based | Selects namespace LBA range to compare. |
| Comparison buffer | `DPTR` | Host-to-controller buffer | Supplies expected user data. |
| Metadata comparison | `MPTR` / metadata in data path | If metadata is provided, compare metadata excluding PI. | Extends comparison beyond user data. |
| Protection behavior | `PRINFO`, `STC`, `ELBAT/ELBATM`, `ELBST/EILBRT` | `PRACT` shall be cleared | Selects PI checking behavior. |
| Cache/media source | `FUA` | `0` no effect; `1` compare non-volatile media data | Selects media source behavior. |
| Error recovery effort | `LR` | `0` full recovery; `1` limited retry | Selects controller retry effort. |
