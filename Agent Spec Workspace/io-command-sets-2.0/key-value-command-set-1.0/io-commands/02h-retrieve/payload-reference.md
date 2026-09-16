# KV Retrieve Payload Reference

| Payload surface | Direction | Meaning |
|---|---|---|
| KV value buffer | Controller to host | Value bytes associated with selected key. |
| CQE Dword 0 | Controller to host completion field | Full KV value size in bytes on success. |

If `HBS` is less than the KV value size, the controller returns the portion that fits, starting at the beginning of the KV value, and CQE Dword 0 still reports the full value size.

If `HBS` is greater than the KV value size, the controller returns the media data and CQE Dword 0 reports the value size.
