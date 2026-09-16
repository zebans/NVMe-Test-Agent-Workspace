# KV Exist Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Namespace | `NSID` | Selects KV namespace. |
| Key length | `CDW11.KL` | Selects how many key bytes are significant. |
| Key bytes | `CDW2/CDW3/CDW14/CDW15` | Selects the key to query. |

Two keys with the same bytes but different `KL` are different KV keys.
