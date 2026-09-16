# ZNS-Modified Compare Restrictions

## Condition To Status Matrix

| Condition | Expected status / rule | Why it matters |
|---|---|---|
| Compare range spans more than one zone | `Zone Boundary Error` (`B8h`) | ZNS restricts the range to one zone when boundary crossing is not allowed. |
| Accessed zone is `ZSF:Full` | `Zone Is Full` (`B9h`) | ZNS Figure 13 lists this as a Compare-specific completion status. |
| Accessed zone is `ZSRO:Read Only` | `Zone Is Read Only` (`BAh`) | ZNS Figure 13 lists this as a Compare-specific completion status. |
| Accessed zone is `ZSO:Offline` | `Zone Is Offline` (`BBh`) | Offline zones reject the access. |
| Operation hits a ZNS invalid-write condition | `Zone Invalid Write` (`BCh`) | ZNS Figure 13 includes the status even though base Compare data comparison remains NVM-owned. |
| Command would require another active zone resource and none is available | `Too Many Active Zones` (`BDh`) | Resource accounting may block the operation. |
| Command would require another open zone resource and none is available | `Too Many Open Zones` (`BEh`) | Open-resource accounting may block the operation. |

## Boundaries

| Surface | Owner |
|---|---|
| Base Compare command fields, payload, PI, metadata, and compare-failure behavior | NVM Command Set |
| ZNS zone boundary, zone state, and resource restrictions | ZNS Command Set |
