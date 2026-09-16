# NVM Copy Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| Destination range | `SDLBA` + sum of all source `NLB` values | Consecutive destination range | Selects write destination. |
| Source entries | `NR` + payload | `NR` is zero-based | Selects number of source ranges. |
| Descriptor format | `CDW12` bits `11:08` | `0h` or `1h` | Selects Source Range Entry layout. |
| Read PI behavior | `PRINFOR` and source entry expected tags | Depends on namespace PI format | Selects source read PI checks. |
| Write PI behavior | `PRINFOW`, `STCW`, `LBAT/LBATM`, `LBST/ILBRT` | Depends on namespace PI format | Selects destination write PI behavior. |
| Directive | `DTYPE` + `DSPEC` | Base Directives model | Selects write-portion directive behavior. |

Descriptor Format `1h` is required when namespace is formatted for 32b or 64b Guard PI; Descriptor Format `0h` is required for 16b Guard PI.
