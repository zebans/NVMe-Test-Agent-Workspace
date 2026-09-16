# NVM Write Uncorrectable Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| LBA range | `SLBA` + `NLB` | `NLB` is zero-based | Selects namespace LBA range to mark uncorrectable. |
| Size limit | Identify Controller `WUSL` with ONCS bit 1 | Limit or recommendation depending on ONCS bit 1 | Determines whether large ranges fail or may be delayed. |
