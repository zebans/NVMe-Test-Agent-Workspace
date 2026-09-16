# Property Get Field Reference

Source: Base Spec 2.0 section 6.5, Figure 386.

| Bytes | Field | Meaning | Important values / rules | Affects |
|---:|---|---|---|---|
| `00` | `OPC` | Fabrics command opcode. | Set to `7Fh`. | Fabrics command dispatch. |
| `01` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `03:02` | `CID` | Command Identifier. | Identifies the command. | Completion matching. |
| `04` | `FCTYPE` | Fabrics Command Type. | Set to `04h` for Property Get. | Command type dispatch. |
| `39:05` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `40` | `ATTRIB` | Property attributes. | Bits `2:0` property size; bits `7:3` reserved. | 4-byte vs 8-byte property access. |
| `43:41` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `47:44` | `OFST` | Property offset. | Offset to property to get. | Property selection. |
| `63:48` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
