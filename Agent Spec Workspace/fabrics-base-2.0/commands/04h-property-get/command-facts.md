# Property Get Command Facts

Source: NVMe Base Spec 2.0 section 6.5, Figures 386-387, and Fabrics command table Figure 375.

| Item | Value |
|---|---|
| Command | Property Get |
| Fabrics opcode | `OPC=7Fh` |
| Fabrics command type | `FCTYPE=04h` |
| Purpose | Returns a property value referenced by an offset. |
| Support | Mandatory |
| I/O Queue support | Not supported on I/O Queues |
| Main fields | `ATTRIB`, `OFST`, response `VALUE` |

## Required Command Behavior

| Area | Requirement |
|---|---|
| Property space | Property definitions come from Base Spec property space section 3.1.3. |
| Property size | `ATTRIB` selects 4-byte or 8-byte property access. |
| Offset | `OFST` selects the property offset to get. |
| Completion | Response returns `VALUE`, `SQHD`, `CID`, and `STS`. |
