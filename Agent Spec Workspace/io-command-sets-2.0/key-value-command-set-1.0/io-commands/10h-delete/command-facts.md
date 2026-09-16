# KV Delete Command Facts

| Item | Value |
|---|---|
| Command | Delete |
| Opcode | `10h` |
| Source | Key Value Command Set 1.0 section 3.2.1, Figures 6-9 |
| Data direction | No data transfer |
| NSID | Uses Namespace Identifier; `FFFFFFFFh` not supported unless explicitly allowed by source figure. |
| Payload | No command data payload |

Delete deletes the specified KV key and its associated KV value from the namespace. Delete is atomic with respect to the associated key/value pair.
