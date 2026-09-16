# Capacity Management Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Insufficient Capacity` | Requested capacity cannot be allocated. | Capacity request exceeds available/configurable capacity. |
| `Identifier Unavailable` | Required identifier cannot be allocated. | Controller cannot provide requested Endurance Group / NVM Set identifier. |
| `Invalid Field in Command` | Non-zero Element Identifier does not correspond to an existing capacity entity where required; reserved/unsupported operation cases may also apply. | Selector does not map to valid capacity object/operation. |

