# KV Store Payload Reference

| Payload surface | Direction | Meaning |
|---|---|---|
| KV value buffer | Host to controller | Value bytes to associate with the selected key. |
| `VS=0h` | No value bytes | Key exists with no associated value. |

Compression internals, if supported by the controller, are outside the scope of the KV specification.
