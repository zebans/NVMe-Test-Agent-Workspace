# NVM Write Uncorrectable Restrictions

| Condition | Rule / expected behavior |
|---|---|
| Namespace is write protected | Return Namespace is Write Protected. |
| Range contains read-only blocks | Return Attempted Write to Read Only Range, unless caused by namespace write-protection state. |
| `WUSL` non-zero and ONCS bit 1 clear, and range exceeds limit | Abort with Invalid Field in Command. |
| `WUSL` non-zero and ONCS bit 1 set, and range exceeds recommendation | Command can encounter processing delays. |
| Command succeeds | Later reads fail with Unrecovered Read Error until a write clears the invalid status. |
| Namespace uses ZNS (`CSI=02h`) | Apply ZNS overlay rules for zone boundary, write pointer, zone state, and active/open resources. |

Reserved command-specific fields have no NVM-defined meaning and should be cleared.
