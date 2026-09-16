# Lockdown Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Opcode or Feature Identifier | `CDW10.OFI` bits 15:08 | Command opcode or Set Features Feature Identifier selected by `SCP`. |
| Interface | `CDW10.IFC` bits 06:05 | Interfaces affected by this command. |
| Prohibit | `CDW10.PRHBT` bit 04 | Prohibit or allow execution. |
| Scope | `CDW10.SCP` bits 03:00 | Defines what `OFI` contains. |
| UUID Index | `CDW14` bits 06:00 | UUID Index when supported and applicable to vendor specific Feature Identifier. |

## Interface Values

| `IFC` | Affected interfaces |
|---|---|
| `00b` | Admin Submission Queue. |
| `01b` | Admin Submission Queue and out-of-band on a Management Endpoint. |
| `10b` | Out-of-band on a Management Endpoint. |
| `11b` | Reserved. |

## Scope Values

| `SCP` | `OFI` meaning |
|---|---|
| `0h` | Admin command opcode. |
| `1h` | Reserved. |
| `2h` | Set Features Feature Identifier. |
| `3h` | Management Interface Command Set opcode. |
| `4h` | PCIe Command Set opcode. |
| `5h`-`Fh` | Reserved. |

