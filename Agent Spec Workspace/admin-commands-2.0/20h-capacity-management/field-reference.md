# Capacity Management Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW10` bits 31:16 | Element Identifier | Operation-specific identifier. | Non-zero unknown existing capacity entity -> `Invalid Field in Command`. | Capacity object selection. |
| `CDW10` bits 15:04 | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |
| `CDW10` bits 03:00 | Operation | Operation to perform. | `0h` select config, `1h` create EG, `2h` delete EG, `3h` create NVM Set, `4h` delete NVM Set. | Capacity management action. |
| `CDW11` bits 31:00 | Capacity Lower | Least significant 32 bits of capacity in bytes. | Used for Create Endurance Group / Create NVM Set; reserved otherwise. | Create capacity size. |
| `CDW12` bits 31:00 | Capacity Upper | Most significant 32 bits of capacity in bytes. | Used for Create Endurance Group / Create NVM Set; reserved otherwise. | Create capacity size. |

