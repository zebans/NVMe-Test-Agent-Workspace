# KV Exist Status Reference

| Status | Meaning | Test/FW interpretation |
|---|---|---|
| `00h` Success | KV key exists. | Existence query positive. |
| `82h` Namespace Not Ready | Namespace is not ready. | KV command cannot proceed. |
| `84h` Format In Progress | Format is in progress. | Command blocked during format. |
| `87h` KV Key Does Not Exist | KV key does not exist. | Existence query negative. |

`KL > 16` is an Invalid Field in Command condition.
