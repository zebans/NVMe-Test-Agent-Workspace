# KV List Command Facts

| Item | Value |
|---|---|
| Command | List |
| Opcode | `06h` |
| Source | Key Value Command Set 1.0 section 3.2.2, Figures 10-16 |
| Data direction | Controller to host |
| NSID | Uses Namespace Identifier |
| Payload | Returned list of KV keys |

List returns a list of keys that exist in the namespace starting at the specified key. Key order is not specified, but the spec defines stability conditions when no Sanitize, Format NVM, Store, or Delete commands intervene.
