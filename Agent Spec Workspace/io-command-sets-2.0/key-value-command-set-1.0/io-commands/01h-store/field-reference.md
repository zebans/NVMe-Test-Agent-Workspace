# KV Store Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data Pointer | Host value buffer source. | PRP or SGL. | KV value payload. |
| `CDW2:3` | KV key `[63:00]` | Least-significant 64 bits of key bytes. | Only first `KL` bytes are part of key identity. | Key selection. |
| `CDW10` bits `31:00` | `VS` | Value Size in bytes. | `0h` means key exists with no associated value. | Value payload length. |
| `CDW11` bits `15:08` | `SO` | Store Option. | bit10 no compression; bit9 do not store if key exists; bit8 do not store if key does not exist. | Store condition/compression behavior. |
| `CDW11` bits `07:00` | `KL` | Key Length in bytes. | `KL > 16` aborts with Invalid Field in Command. | Key size and identity. |
| `CDW14:15` | KV key `[127:64]` | Most-significant 64 bits of key bytes. | Used when `KL > 8`. | Key selection. |
| Other command-specific fields | Reserved | No KV-defined meaning. | Host should clear. | Invalid-field testing. |
