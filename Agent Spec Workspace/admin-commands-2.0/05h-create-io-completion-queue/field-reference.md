# Create I/O Completion Queue Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `PRP1` | CQ base / PRP List pointer | Queue memory descriptor. | Contiguous CQ base when `PC=1`; PRP List pointer when `PC=0`; offsets shall be `0h`. | Queue memory placement and `PRP Offset Invalid`. |
| `CDW10` | `QSIZE` | Zero-based queue size. | `0h` or too-large values should return `Invalid Queue Size`. | Queue depth validation. |
| `CDW10` | `QID` | I/O Completion Queue Identifier. | Shall be non-zero, within supported range, and unused. | Queue identity validation. |
| `CDW11` | `IV` | Interrupt Vector. | Transport-specific; clear to `0h` if undefined by transport. | Interrupt routing and `Invalid Interrupt Vector`. |
| `CDW11` | `IEN` | Interrupt Enable. | Enables/disables interrupt generation for this CQ. | Completion interrupt behavior. |
| `CDW11` | `PC` | Physically Contiguous. | `1` = physically contiguous; `0` = not physically contiguous. | PRP interpretation, `CAP.CQR`, CMB/CQPDS restrictions. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |
