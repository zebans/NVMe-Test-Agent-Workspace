# KV Retrieve Status Reference

| Status | Meaning | Test/FW interpretation |
|---|---|---|
| `00h` Success | Value returned; CQE Dword 0 contains full value size. | Retrieve succeeded. |
| `82h` Namespace Not Ready | Namespace is not ready. | KV command cannot proceed. |
| `83h` Reservation Conflict | Reservation state conflicts with Retrieve. | Reservation access rule blocks command. |
| `84h` Format In Progress | Format is in progress. | Command blocked during format. |
| `86h` Invalid Key Size | KV key size is not valid. | Check `KL` and namespace KV format. |
| `87h` KV Key Does Not Exist | KV key does not exist. | Lookup miss. |
| `88h` Unrecovered Error | Unrecovered error reading from medium. | Media/read failure. |
| `0Bh` Invalid Namespace or Format | Namespace or namespace format invalid. | Wrong namespace/format/CSI. |

`KL > 16` is an Invalid Field in Command condition.
