# KV Delete Status Reference

| Status | Meaning | Test/FW interpretation |
|---|---|---|
| `00h` Success | KV key and associated KV value have been deleted. | Delete took effect. |
| `87h` KV Key Does Not Exist | KV key does not exist. | Absence reported; behavior may also be influenced by KV Configuration `EDNEK`. |
| `0Bh` Invalid Namespace or Format | Namespace or namespace format is invalid, or namespace is not associated with KV Command Set. | Wrong namespace/format/CSI. |
| `82h` Namespace Not Ready | Namespace is not ready. | KV command cannot proceed. |
| `83h` Reservation Conflict | Reservation state conflicts with Delete. | Reservation access rule blocks command. |
| `84h` Format In Progress | Format is in progress. | Command blocked during format. |

`KL > 16` is an Invalid Field in Command condition.
