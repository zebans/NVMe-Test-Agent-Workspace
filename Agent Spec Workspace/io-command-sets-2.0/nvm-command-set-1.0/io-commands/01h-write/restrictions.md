# NVM Write Restrictions

| Condition | Rule / expected behavior |
|---|---|
| Namespace is write protected | Return Namespace is Write Protected. |
| Range contains read-only blocks | Return Attempted Write to Read Only Range, unless caused by namespace write-protection state. |
| `PRINFO` or PI tag fields conflict with namespace PI format | Return Invalid Protection Information. |
| DSM attributes conflict | Return Conflicting Attributes. |
| Namespace uses ZNS (`CSI=02h`) | Apply ZNS overlay rules for zone boundary, write pointer, zone state, and active/open resources. |

Reserved command-specific fields have no NVM-defined meaning and should be cleared.
