# Disconnect Field Reference

Source: Base Spec 2.0 section 6.4, Figure 384.

| Bytes | Field | Meaning | Important values / rules | Affects |
|---:|---|---|---|---|
| `00` | `OPC` | Fabrics command opcode. | Set to `7Fh`. | Fabrics command dispatch. |
| `01` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `03:02` | `CID` | Command Identifier. | Identifies the command. | Completion matching. |
| `04` | `FCTYPE` | Fabrics Command Type. | Set to `08h` for Disconnect. | Command type dispatch. |
| `23:05` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `39:24` | `SGL1` | Reserved. | No data is transferred. | Reserved-field validation. |
| `41:40` | `RECFMT` | Disconnect record format. | This definition uses `0h`; unsupported values return `Incompatible Format`. | Capsule compatibility. |
| `63:48` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
