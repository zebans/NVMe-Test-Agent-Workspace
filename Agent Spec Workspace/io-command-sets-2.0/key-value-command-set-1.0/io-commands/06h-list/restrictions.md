# KV List Restrictions

| Condition | Rule / expected behavior |
|---|---|
| `KL > 16` | Abort with Invalid Field in Command. |
| `KL` invalid for selected KV format | Invalid Key Size. |
| Host buffer too small for all keys | Return only complete keys that fit. |
| Starting key exists | Starting key is the first key returned. |
| Starting key does not exist | First returned key is vendor specific, with stability constraints when no Sanitize, Format NVM, Store, or Delete commands intervene. |
| Sanitize, Format NVM, Store, or Delete occurs between List operations | Ordering stability assumption no longer holds. |

Reserved command-specific fields have no KV-defined meaning and should be cleared.
