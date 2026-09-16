# Property Get Payload Reference

Property Get returns the requested property value in the response capsule.

## Response `VALUE`

| Property size | Response value usage |
|---|---|
| 4 bytes | Bytes `03:00` contain the value; bytes `07:04` are reserved. |
| 8 bytes | Bytes `07:00` contain the value. |

## Response Fields

| Response bytes | Field | Meaning |
|---:|---|---|
| `07:00` | `VALUE` | Requested property value, with 4-byte special handling above. |
| `09:08` | `SQHD` | Current Submission Queue Head pointer for the associated SQ. |
| `13:12` | `CID` | Completed Command Identifier. |
| `15:14` | `STS` | Command status. |
