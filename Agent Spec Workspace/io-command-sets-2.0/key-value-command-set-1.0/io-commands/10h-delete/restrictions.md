# KV Delete Restrictions

| Condition | Rule / expected behavior |
|---|---|
| `KL > 16` | Abort with Invalid Field in Command. |
| Key does not exist and KV Configuration `EDNEK=1` | Abort with KV Key Does Not Exist. |
| Key does not exist and KV Configuration `EDNEK=0` | Complete as if key existed and was deleted. |
| Namespace is not KV formatted | Invalid Namespace or Format. |
| Reservation conflict exists | Reservation Conflict. |

Reserved command-specific fields have no KV-defined meaning and should be cleared.
