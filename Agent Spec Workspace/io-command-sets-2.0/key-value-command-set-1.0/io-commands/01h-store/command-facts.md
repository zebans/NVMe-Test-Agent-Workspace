# KV Store Command Facts

| Item | Value |
|---|---|
| Command | Store |
| Opcode | `01h` |
| Source | Key Value Command Set 1.0 section 3.2.5, Figures 27-32 |
| Data direction | Host to controller |
| NSID | Uses Namespace Identifier |
| Payload | KV value data buffer |

Store stores a KV key/value pair to the namespace. Store is atomic with respect to the associated key/value pair: Retrieve sees either the previous value or the complete new value, not a mixture.
