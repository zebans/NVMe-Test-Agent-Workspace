# NVM Dataset Management Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data Pointer | Host data buffer containing range descriptors. | Each descriptor is 16 bytes. | Range payload. |
| `CDW10` bits `07:00` | `NR` | Number of ranges. | Zero-based; max encoded value covers 256 ranges. | Number of descriptors. |
| `CDW11` bit `02` | `AD` | Attribute - Deallocate. | Set means NVM subsystem may deallocate all provided ranges. | Deallocation behavior. |
| `CDW11` bit `01` | `IDW` | Integral Dataset for Write. | Optimize for write access as integral unit. | Advisory optimization. |
| `CDW11` bit `00` | `IDR` | Integral Dataset for Read. | Optimize for read access as integral unit. | Advisory optimization. |
| Range bytes `03:00` | Context Attributes | Intended access pattern / hints. | See context attribute table. | Controller optimization. |
| Range bytes `07:04` | Length in logical blocks | Range length. | One-based value. | Range size. |
| Range bytes `15:08` | Starting LBA | First LBA in the range. | 64-bit value. | Target range. |

## Context Attributes

| Bits | Field | Meaning |
|---|---|---|
| `31:24` | Command Access Size | Expected logical blocks per Read/Write command; `0h` means none. |
| `10` | Write Prepare | Range expected to be written soon. |
| `09` | Sequential Write Range | Dataset optimized for sequential write. |
| `08` | Sequential Read Range | Dataset optimized for sequential read. |
| `05:04` | Access Latency | `00b` none, `01b` idle, `10b` normal, `11b` low. |
| `03:00` | Access Frequency | `0h` none, `1h` typical, `2h` infrequent write/read, `3h` infrequent write/frequent read, `4h` frequent write/infrequent read, `5h` frequent write/read, `6h`-`Fh` reserved. |
