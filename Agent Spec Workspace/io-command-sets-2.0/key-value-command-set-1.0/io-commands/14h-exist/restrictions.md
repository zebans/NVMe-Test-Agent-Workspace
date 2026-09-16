# KV Exist Restrictions

| Condition | Rule / expected behavior |
|---|---|
| `KL > 16` | Abort with Invalid Field in Command. |
| Key exists | Complete successfully. |
| Key does not exist | Complete with KV Key Does Not Exist. |
| Format in progress | Format In Progress. |

Reserved command-specific fields have no KV-defined meaning and should be cleared.
