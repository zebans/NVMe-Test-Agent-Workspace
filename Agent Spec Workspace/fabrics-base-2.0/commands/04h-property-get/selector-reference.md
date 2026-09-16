# Property Get Selector Reference

## `ATTRIB` Property Size

| `ATTRIB[2:0]` | Property size | Meaning |
|---:|---|---|
| `000b` | 4 bytes | Response bytes `03:00` contain the value; bytes `07:04` are reserved. |
| `001b` | 8 bytes | Response bytes `07:00` contain the value. |
| `010b`-`111b` | Reserved | Reserved property size encodings. |

`ATTRIB[7:3]` are reserved.

## Offset Selector

| Field | Meaning |
|---|---|
| `OFST` | Offset to the property to get. |

Invalid property or invalid offset completes with `Invalid Field in Command`.
