# KV Store Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| Namespace | `NSID` | KV namespace | Selects namespace. |
| Key | `KL` + key bytes | `KL <= 16` | Selects key. |
| Value size | `VS` | Bytes; `0h` allowed | Selects value length. |
| No compression | `SO` bit `10` | `1` do not compress; `0` compress if supported | Compression control; algorithm is outside spec. |
| Create-only | `SO` bit `9` | `1` do not store if key exists | Returns Key Exists when key exists. |
| Update-only | `SO` bit `8` | `1` do not store if key does not exist | Returns KV Key Does Not Exist when key is absent. |

If both bit 9 and bit 8 are set, the command is only satisfiable if the key both exists and does not exist, so test expectations should treat this as conflicting Store Options.
