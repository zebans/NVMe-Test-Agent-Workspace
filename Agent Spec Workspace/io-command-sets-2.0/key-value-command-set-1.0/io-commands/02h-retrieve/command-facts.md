# KV Retrieve Command Facts

| Item | Value |
|---|---|
| Command | Retrieve |
| Opcode | `02h` |
| Source | Key Value Command Set 1.0 section 3.2.3, Figures 17-22 |
| Data direction | Controller to host |
| NSID | Uses Namespace Identifier |
| Payload | KV value data buffer |

Retrieve returns the value associated with the specified key. On success, CQE Dword 0 contains the full KV value size in bytes.
