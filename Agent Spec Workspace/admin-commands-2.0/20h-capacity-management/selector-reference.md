# Capacity Management Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Element Identifier | `CDW10` bits 31:16 | Meaning depends on Operation. |
| Operation | `CDW10` bits 03:00 | Capacity operation requested. |
| Capacity Lower | `CDW11` bits 31:00 | Low 32 bits of capacity in bytes for create operations. |
| Capacity Upper | `CDW12` bits 31:00 | High 32 bits of capacity in bytes for create operations. |

## Operation Values

| Operation | Meaning | Element Identifier meaning |
|---|---|---|
| `0h` | Select Capacity Configuration. | Capacity Configuration Identifier. |
| `1h` | Create Endurance Group. | Domain Identifier; `0h` lets controller select the domain. |
| `2h` | Delete Endurance Group. | Endurance Group Identifier to delete. |
| `3h` | Create NVM Set. | Endurance Group Identifier; `0h` lets controller select the Endurance Group. |
| `4h` | Delete NVM Set. | NVM Set Identifier to delete. |
| `5h`-`Fh` | Reserved. | Reserved. |

