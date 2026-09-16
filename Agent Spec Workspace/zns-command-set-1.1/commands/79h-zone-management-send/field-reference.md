# Zone Management Send Field Reference

Source: ZNS Figures 38-39.

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data pointer | Host-to-controller data buffer. | Used for Zone Descriptor Extension data when `ZSA=10h`. | Extension data transfer. |
| `CDW10-11` | `SLBA` | Lowest LBA of target zone. | Ignored when Select All is set; otherwise must be zone start LBA. | Target-zone selection and invalid-field tests. |
| `CDW13 bit 8` | Select All | Applies action to all matching zones. | Invalid for Set Zone Descriptor Extension. | Scope of action. |
| `CDW13 bits 7:0` | `ZSA` | Zone Send Action. | Close, Finish, Open, Reset, Offline, Set Zone Descriptor Extension. | Zone state transition. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

## Completion Field

| CQE location | Field | Meaning | Affects |
|---|---|---|---|
| Dword 0 bit 0 | Zone Capacity Changed | Set when zone capacity changed for one or more zones specified by the command. | Host may issue Zone Management Receive to determine what changed. |
