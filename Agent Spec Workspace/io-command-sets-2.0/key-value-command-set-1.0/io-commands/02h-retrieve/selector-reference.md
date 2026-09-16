# KV Retrieve Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| Namespace | `NSID` | KV namespace | Selects namespace. |
| Key | `KL` + key bytes | `KL <= 16` | Selects key to retrieve. |
| Buffer size | `HBS` | Bytes | Selects maximum returned value bytes. |
| Raw data option | `RO` bit `8` | `1` raw data; `0` decompressed if supported | Selects returned representation. |
