# Admin-Through-MI Cross-Spec Boundary

Status: `BOUNDARY-COMPLETE`

## Ownership Map

| Question | Use |
|---|---|
| Is an Admin opcode allowed over out-of-band MI? | `MI_ADMIN_THROUGH_COMMAND_TABLE.md` |
| What bytes carry `OPC`, `CTLID`, `DOFST`, `DLEN`, and SQE/CQE dwords? | `command-format-reference.md` and `field-reference.md` |
| Is the error an MI wrapper error or a tunneled Admin command status? | `status-boundary-reference.md` |
| What do `CDW10`-`CDW15` mean for the Admin command? | Linked `..\..\admin-commands-2.0\<opcode-folder>\` |
| What does a returned Admin payload field mean? | Linked Admin folder and any delegated command-set/Fabrics/MI/vendor layer |
| How is the MI message carried over SMBus/I2C or PCIe VDM? | `..\..\mctp-base-1.3.1\`, `..\..\mctp-smbus-i2c-1.1.0\`, or `..\..\mctp-pcie-vdm-1.0.1\` |
| What is the normal in-band Admin Submission Queue behavior? | Base Admin command layer, not this folder. |

## Boundary Statements

Admin-through-MI is out-of-band only in MI 1.2. All NVMe Admin Commands are prohibited using the in-band tunneling mechanism.

Admin-through-MI does not use the normal host Admin Submission Queue path. It carries Admin command semantics inside an NVMe-MI Command Message.

The MI wrapper owns target Controller ID, data slicing, message format, and wrapper status. The tunneled Admin command owns CDW semantics, completion status, and command-specific payload meanings.

Vendor-specific Admin commands remain vendor-defined even when Figure 114 marks the range optional.

