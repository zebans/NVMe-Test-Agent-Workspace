# Property Set Payload Reference

Property Set carries its write value in the command capsule, not in a separate data payload.

## Command Value

| Property size | `VALUE` usage |
|---|---|
| 4 bytes | Bytes `51:48` contain the value; bytes `55:52` are reserved. |
| 8 bytes | Bytes `55:48` contain the value. |

## Response Payload

| Response bytes | Meaning |
|---:|---|
| `07:00` | Reserved. |
| `09:08` | `SQHD`, current Submission Queue Head pointer for the associated SQ. |
| `13:12` | `CID`, completed Command Identifier. |
| `15:14` | `STS`, command status. |
