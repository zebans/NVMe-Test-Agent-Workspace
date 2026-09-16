# KV List Payload Reference

## Return Data Structure

| Offset | Field | Meaning |
|---:|---|---|
| `03:00` | `NRK` | Number of Returned Keys in this data structure. |
| after `03:00` | Key data structure list | `NRK` key entries. |

## Key Data Structure

| Offset within entry | Field | Meaning |
|---:|---|---|
| `01:00` | `KL` | Length in bytes of this returned key. |
| `n:02` | Key | Key bytes. |
| `m:n` | Pad | Padding, if needed, to end the data structure on a 4-byte boundary. |

The number of keys returned is the minimum of the number of keys in the controller and the number of complete keys that fit in the host buffer.
