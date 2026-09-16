# Connect Payload Reference

Source: Base Spec 2.0 section 6.3, Figures 381-383.

## Connect Command Data

| Bytes | Field | Meaning | Important values / rules |
|---:|---|---|---|
| `15:00` | `HOSTID` | Host Identifier. | Controller shall set the Host Identifier Feature to this value; cleared `0h` causes `Connect Invalid Parameters`. |
| `17:16` | `CNTLID` | Requested Controller ID. | Dynamic model Admin Queue Connect requires `FFFFh`; static model uses `FFFEh` to request any Controller ID. |
| `255:18` | Reserved | Reserved. | Host should clear. |
| `511:256` | `SUBNQN` | NVM Subsystem NVMe Qualified Name. | Invalid values may cause `Connect Invalid Parameters` or discovery restart behavior. |
| `767:512` | `HOSTNQN` | Host NVMe Qualified Name. | Invalid or unauthorized host may cause Connect failure. |
| `1023:768` | Reserved | Reserved. | Host should clear. |

## Connect Response

| Bytes | Field | Meaning |
|---:|---|---|
| `03:00` | Status Code Specific | Depends on returned status. |
| `07:04` | Reserved | Reserved. |
| `09:08` | `SQHD` | If SQ flow control disable was accepted, `FFFFh`; otherwise current SQ head pointer and SQ flow control enabled. |
| `11:10` | Reserved | Reserved. |
| `13:12` | `CID` | Completed Command Identifier. |
| `15:14` | `STS` | Status. |

## Status Code Specific Dword 0

| Status | Dword 0 meaning |
|---|---|
| Success | `CNTLID` in bytes `01:00`; `AUTHREQ` in bits `15:00` describing authentication/security requirements. |
| Connect Invalid Parameters | `IPO` indicates invalid parameter offset; `IATTR` indicates whether offset is from SQE or data. |
| All other status values | Bytes `03:00` reserved. |
