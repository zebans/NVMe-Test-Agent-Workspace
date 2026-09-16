# NVM Read Restrictions

| Condition | Rule / expected behavior |
|---|---|
| `PRINFO` or expected tag fields conflict with namespace PI format | Return Invalid Protection Information. |
| DSM attributes conflict | Return Conflicting Attributes. |
| Range contains deallocated/unwritten logical blocks and DULBE is enabled | Abort with Deallocated or Unwritten Logical Block status. |
| Range contains deallocated/unwritten logical blocks and DULBE is not enabled | Return deterministic values defined by `DLFEAT`. |
| Namespace uses ZNS (`CSI=02h`) | Apply ZNS overlay rules for zone boundary and Offline zone conditions. |

Reserved command-specific fields have no NVM-defined meaning and should be cleared.
