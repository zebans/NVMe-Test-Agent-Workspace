# KV Store Restrictions

| Condition | Rule / expected behavior |
|---|---|
| `KL > 16` | Abort with Invalid Field in Command. |
| `VS` invalid for selected KV format | Invalid Value Size. |
| `KL` invalid for selected KV format | Invalid Key Size. |
| Store Option bit 9 set and key exists | Key Exists. |
| Store Option bit 8 set and key does not exist | KV Key Does Not Exist. |
| Namespace capacity exceeded | Capacity Exceeded. |
| Store succeeds | Operation is atomic for the associated key/value pair. |

Reserved command-specific fields have no KV-defined meaning and should be cleared.
