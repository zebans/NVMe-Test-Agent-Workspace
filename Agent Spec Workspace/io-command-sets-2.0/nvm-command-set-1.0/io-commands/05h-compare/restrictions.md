# NVM Compare Restrictions

| Condition | Rule / expected behavior |
|---|---|
| Any miscompare between media data and host comparison buffer | Complete with Compare Failure. |
| Metadata is provided | Compare metadata excluding protection information. |
| `PRACT` in `PRINFO` is not cleared | Invalid-field / invalid PI behavior. |
| `PRINFO` or expected tag fields conflict with namespace PI format | Return Invalid Protection Information. |
| Range contains deallocated/unwritten logical blocks and DULBE is enabled | Abort with Deallocated or Unwritten Logical Block status. |
| Namespace uses ZNS (`CSI=02h`) | Apply ZNS overlay rules for zone boundary, zone state, and resource conditions. |

Reserved command-specific fields have no NVM-defined meaning and should be cleared.
