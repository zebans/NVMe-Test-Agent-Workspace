# Virtualization Management Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `CDW10` bits 31:16 | `CNTLID` | Target controller identifier. | Must correspond to this primary controller for `ACT=1h`, or associated secondary controller for secondary actions. | Controller target validation. |
| `CDW10` bits 10:08 | `RT` | Resource Type. | `000b` VQ, `001b` VI. | Resource pool selection. |
| `CDW10` bits 03:00 | `ACT` | Action. | `1h`, `7h`, `8h`, `9h` defined. | Operation selection. |
| `CDW11` bits 15:00 | `NR` | Number of Controller Resources. | Number to allocate or assign. | Resource quantity validation. |
| CQE DW0 bits 15:00 | `NRM` | Number of Controller Resources Modified. | May be smaller or larger than requested. | Completion result interpretation. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

