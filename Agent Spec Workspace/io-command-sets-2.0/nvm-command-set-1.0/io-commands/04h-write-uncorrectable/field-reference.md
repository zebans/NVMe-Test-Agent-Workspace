# NVM Write Uncorrectable Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW10:11` | `SLBA` | Starting LBA. | 64-bit value; CDW10 low, CDW11 high. | Target range. |
| `CDW12` bits `15:00` | `NLB` | Number of logical blocks. | Zero-based. | Range size. |
| Other command-specific fields | Reserved | No NVM-defined meaning. | Host should clear. | Invalid-field testing. |
