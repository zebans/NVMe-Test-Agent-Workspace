# KV List Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data Pointer | Host destination buffer. | PRP or SGL. | Returned key list. |
| `CDW2:3` | KV key `[63:00]` | Least-significant 64 bits of starting key. | Only first `KL` bytes are significant. | List starting point. |
| `CDW10` bits `31:00` | `HBS` | Host Buffer Size in bytes. | Number of complete keys returned is bounded by buffer. | Returned key count. |
| `CDW11` bits `07:00` | `KL` | Key Length in bytes. | `KL > 16` aborts with Invalid Field in Command. | Starting key size. |
| `CDW14:15` | KV key `[127:64]` | Most-significant 64 bits of starting key. | Used when `KL > 8`. | List starting point. |
| Returned bytes `03:00` | `NRK` | Number of Returned Keys. | Count of key data structures in returned payload. | Parser loop bound. |
