# Property Set Command Facts

Source: NVMe Base Spec 2.0 section 6.6, Figures 388-389, and Fabrics command table Figure 375.

| Item | Value |
|---|---|
| Command | Property Set |
| Fabrics opcode | `OPC=7Fh` |
| Fabrics command type | `FCTYPE=00h` |
| Purpose | Sets a property value referenced by an offset. |
| Support | Mandatory |
| I/O Queue support | Not supported on I/O Queues |
| Main fields | `ATTRIB`, `OFST`, `VALUE` |

## Required Command Behavior

| Area | Requirement |
|---|---|
| Property space | Property definitions come from Base Spec property space section 3.1.3. |
| Property size | `ATTRIB` selects 4-byte or 8-byte property access. |
| Offset | `OFST` selects the property offset to set. |
| Value | `VALUE` contains the value written to the property. |
| Completion | Response provides status; response bytes `07:00` are reserved. |
