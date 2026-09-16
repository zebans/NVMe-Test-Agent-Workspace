# KV List Status Reference

| Status | Meaning | Test/FW interpretation |
|---|---|---|
| `00h` Success | Key list returned. | Parse returned `NRK` and key entries. |
| `84h` Format In Progress | Format is in progress. | Command blocked during format. |
| `86h` Invalid Key Size | KV key size is not valid. | Check `KL` and namespace KV format. |
| `0Bh` Invalid Namespace or Format | Namespace or namespace format invalid. | Wrong namespace/format/CSI. |

`KL > 16` is an Invalid Field in Command condition.
