# KV Store Status Reference

| Status | Meaning | Test/FW interpretation |
|---|---|---|
| `00h` Success | Key/value pair stored. | Store took effect atomically. |
| `81h` Capacity Exceeded | Device capacity exceeded. | Namespace lacks capacity for requested key/value pair. |
| `82h` Namespace Not Ready | Namespace is not ready. | KV command cannot proceed. |
| `83h` Reservation Conflict | Reservation state conflicts with Store. | Reservation access rule blocks command. |
| `84h` Format In Progress | Format is in progress. | Command blocked during format. |
| `85h` Invalid Value Size | Value size is not valid. | Check `VS` against namespace KV format. |
| `86h` Invalid Key Size | KV key size is not valid. | Check `KL` and namespace KV format. |
| `87h` KV Key Does Not Exist | Store Option bit 8 set and key does not exist. | Update-only condition failed. |
| `89h` Key Exists | Store Option bit 9 set and key exists. | Create-only condition failed. |
| `0Bh` Invalid Namespace or Format | Namespace or format invalid. | Wrong namespace/format/CSI. |

`KL > 16` is an Invalid Field in Command condition.
