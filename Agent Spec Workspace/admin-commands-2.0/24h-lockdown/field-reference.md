# Lockdown Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW10` bits 15:08 | `OFI` | Opcode or Feature Identifier. | Meaning determined by `SCP`. | Target command/feature. |
| `CDW10` bits 06:05 | `IFC` | Interface. | Admin SQ, Management Endpoint, or both. | Where prohibition/allow applies. |
| `CDW10` bit 04 | `PRHBT` | Prohibit. | `1` prohibits; `0` allows. | Lockdown state. |
| `CDW10` bits 03:00 | `SCP` | Scope. | Selects Admin opcode, Feature Identifier, MI opcode, or PCIe opcode meaning. | `OFI` interpretation. |
| `CDW14` bits 06:00 | UUID Index | UUID selector. | Used only when UUID selection is supported and `SCP=2h` vendor specific feature applies; ignored otherwise. | Vendor specific Feature Identifier selection. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

