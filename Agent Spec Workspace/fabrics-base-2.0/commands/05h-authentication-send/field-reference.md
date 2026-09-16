# Authentication Send Field Reference

Source: Base Spec 2.0 section 6.2, Figure 378.

| Bytes | Field | Meaning | Important values / rules | Affects |
|---:|---|---|---|---|
| `00` | `OPC` | Fabrics command opcode. | Set to `7Fh`. | Fabrics command dispatch. |
| `01` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `03:02` | `CID` | Command Identifier. | Identifies the command. | Completion matching. |
| `04` | `FCTYPE` | Fabrics Command Type. | Set to `05h` for Authentication Send. | Command type dispatch. |
| `23:05` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `39:24` | `SGL1` | SGL descriptor. | Transport SGL Data Block or Keyed SGL Data Block descriptor. | Security protocol data transfer. |
| `40` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `41` | `SPSP0` | Security Protocol Specific bits `07:00`. | Defined by SPC-5. | Protocol-specific command selection. |
| `42` | `SPSP1` | Security Protocol Specific bits `15:08`. | Defined by SPC-5. | Protocol-specific command selection. |
| `43` | `SECP` | Security Protocol. | Defined by SPC-5. | Security protocol selection. |
| `47:44` | `TL` | Transfer Length. | Security-protocol-specific as defined in SPC-5 where `INC_512` is cleared. | Payload length. |
| `63:48` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
