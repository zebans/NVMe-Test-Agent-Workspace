# ZNS-Modified Write Zeroes Restrictions

## Condition To Status Matrix

| Condition | Expected status / rule | Why it matters |
|---|---|---|
| Write Zeroes range spans more than one zone | `Zone Boundary Error` (`B8h`) | ZNS requires the command range to stay inside one zone. |
| Target zone is `ZSF:Full` | `Zone Is Full` (`B9h`) | Full zones cannot accept additional write-like operations. |
| Target zone is `ZSRO:Read Only` | `Zone Is Read Only` (`BAh`) | Read-only zones reject write-like operations. |
| Target zone is `ZSO:Offline` | `Zone Is Offline` (`BBh`) | Offline zones reject access. |
| Operation writes/deallocates in a way that is not valid at the zone write pointer | `Zone Invalid Write` (`BCh`) | ZNS write-like operations are constrained by write pointer rules. |
| Command would require another active zone resource and none is available | `Too Many Active Zones` (`BDh`) | Transition/resource accounting blocks the command. |
| Command would require another open zone resource and none is available | `Too Many Open Zones` (`BEh`) | Open-resource accounting blocks the command. |
| Write Zeroes deallocates logical blocks | Follow NVM deallocated/unwritten logical block rules plus ZNS allocation model | This affects returned data semantics after the command, not only completion status. |

## Boundaries

| Surface | Owner |
|---|---|
| Base Write Zeroes command fields, payload, PI, and metadata behavior | NVM Command Set |
| ZNS zone boundary, zone state, write pointer, and active/open resource restrictions | ZNS Command Set |
| Device-specific deallocated logical block read value | NVM Identify / vendor behavior |
