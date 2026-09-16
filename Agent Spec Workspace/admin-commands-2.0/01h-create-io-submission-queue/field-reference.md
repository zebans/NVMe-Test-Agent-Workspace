# Create I/O Submission Queue Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `PRP1` | SQ base / PRP List pointer | Queue memory descriptor. | Contiguous SQ base when `PC=1`; PRP List pointer when `PC=0`; offsets shall be `0h`. | Queue memory placement and `PRP Offset Invalid`. |
| `CDW10` | `QSIZE` | Zero-based queue size. | `0h` or too-large values should return `Invalid Queue Size`. | Queue depth validation. |
| `CDW10` | `QID` | I/O Submission Queue Identifier. | Shall be non-zero, within supported range, and unused. | Queue identity validation. |
| `CDW11` | `CQID` | I/O Completion Queue used for completions from this SQ. | `0h`/out-of-range -> `Invalid Queue Identifier`; in-range but not created -> `Completion Queue Invalid`. | SQ-to-CQ binding. |
| `CDW11` | `QPRIO` | Queue priority. | `00b` Urgent, `01b` High, `10b` Medium, `11b` Low; only used with weighted round robin with urgent priority class arbitration. | Arbitration behavior. |
| `CDW11` | `PC` | Physically Contiguous. | `1` = physically contiguous; `0` = not physically contiguous. | PRP interpretation, `CAP.CQR`, CMB/CQPDS restrictions. |
| `CDW12` | `NVMSETID` | NVM Set Identifier association for the SQ. | `0h` or unsupported SQ Associations means no specific NVM Set association. | NVM Set-scoped command submission guidance. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |
