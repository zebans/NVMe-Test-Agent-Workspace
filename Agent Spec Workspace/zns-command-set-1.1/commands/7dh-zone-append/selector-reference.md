# Zone Append Selector Reference

Zone Append does not have a small action selector like `ZSA` or `ZRA`. The high-signal selectors are command fields that change interpretation or validity.

| Selector / field | Meaning | Important values / rules | Affects |
|---|---|---|---|
| `ZSLBA` | Target zone selector. | Shall be the lowest LBA of the target zone. | Target zone and invalid-field tests. |
| `NLB` | Number of logical blocks, zero-based. | Combined with `ZSLBA` and zone capacity determines range. | Zone Boundary Error / capacity behavior. |
| `PIREMAP` | Protection Information Remap. | Required/forbidden depending on PI type. | Invalid Protection Information and reference tag handling. |
| `PRINFO` | Protection Information field. | NVM-owned PI behavior; ZNS modifies reference-tag remap behavior. | PI validation. |
| `LR` | Limited Retry. | NVM-owned behavior. | Retry semantics. |
| `FUA` | Force Unit Access. | NVM-owned behavior. | Persistence semantics. |

## `PIREMAP` Rules

| Namespace PI format | `PIREMAP` requirement | Failure if violated |
|---|---|---|
| Type 1 protection | `PIREMAP` shall be set. | Invalid Protection Information if cleared. |
| Type 3 protection | `PIREMAP` shall be clear. | Invalid Protection Information if set. |

## Ordering Rule

Multiple outstanding Zone Append commands to the same zone have undefined ordering. A test should not assume ordering between them unless it serializes submissions.
