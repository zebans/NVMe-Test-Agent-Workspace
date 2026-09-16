# KV Retrieve Restrictions

| Condition | Rule / expected behavior |
|---|---|
| `KL > 16` | Abort with Invalid Field in Command. |
| `KL` invalid for selected KV format | Invalid Key Size. |
| Key does not exist | KV Key Does Not Exist. |
| `HBS` smaller than value size | Return prefix that fits and report full value size in CQE Dword 0. |
| `RO` bit 8 set | Return raw data; compression algorithm details are outside spec. |

Reserved command-specific fields have no KV-defined meaning and should be cleared.
