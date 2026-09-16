# KV Retrieve Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data Pointer | Host destination buffer. | PRP or SGL. | Returned value payload. |
| `CDW2:3` | KV key `[63:00]` | Least-significant 64 bits of key bytes. | Only first `KL` bytes are part of key identity. | Key selection. |
| `CDW10` bits `31:00` | `HBS` | Host Buffer Size in bytes. | If smaller than value size, only fitting prefix is returned. | Returned byte count. |
| `CDW11` bits `15:08` | `RO` | Retrieve Option. | bit8 raw data; clear returns decompressed data if compression supported. | Returned representation. |
| `CDW11` bits `07:00` | `KL` | Key Length in bytes. | `KL > 16` aborts with Invalid Field in Command. | Key size and identity. |
| `CDW14:15` | KV key `[127:64]` | Most-significant 64 bits of key bytes. | Used when `KL > 8`. | Key selection. |
| CQE Dword 0 | Value Size | Full KV value size in bytes on successful completion. | Returned even when host buffer is smaller. | Retry sizing. |
