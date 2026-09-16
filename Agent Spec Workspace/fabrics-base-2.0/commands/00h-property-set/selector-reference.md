# Property Set Selector Reference

## `ATTRIB` Property Size

| `ATTRIB[2:0]` | Property size | Meaning |
|---:|---|---|
| `000b` | 4 bytes | `VALUE` bytes `51:48` contain the value; bytes `55:52` are reserved. |
| `001b` | 8 bytes | `VALUE` bytes `55:48` contain the value. |
| `010b`-`111b` | Reserved | Reserved property size encodings. |

`ATTRIB[7:3]` are reserved.

## Offset Selector

| Field | Meaning |
|---|---|
| `OFST` | Offset to the property to set. |

Invalid property or invalid offset completes with `Invalid Field in Command`.
