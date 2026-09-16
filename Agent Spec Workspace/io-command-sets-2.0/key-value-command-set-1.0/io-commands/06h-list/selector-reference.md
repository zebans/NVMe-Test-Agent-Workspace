# KV List Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| Namespace | `NSID` | KV namespace | Selects namespace. |
| Starting key | `KL` + key bytes | `KL <= 16` | Selects starting point in key list. |
| Host buffer size | `HBS` | Bytes | Limits number of complete keys returned. |

If the starting key exists, it is the first key returned. If it does not exist, the first returned key is vendor specific, but stable under the source's no-modification conditions.
