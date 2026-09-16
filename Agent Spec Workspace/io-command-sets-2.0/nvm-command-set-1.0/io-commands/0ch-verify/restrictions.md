# NVM Verify Restrictions

| Condition | Rule / expected behavior |
|---|---|
| `PRACT` is not cleared | Abort with Invalid Field in Command. |
| `PRINFO` or expected tag fields conflict with namespace PI format | Return Invalid Protection Information. |
| `VSL` non-zero and ONCS bit 7 clear, and range exceeds limit | Abort with Invalid Field in Command. |
| `VSL` non-zero and ONCS bit 7 set, and range exceeds recommendation | Command can encounter processing delays. |
| Range contains deallocated/unwritten logical blocks and DULBE is enabled | Abort with Deallocated or Unwritten Logical Block status. |
| Namespace uses ZNS (`CSI=02h`) | Apply ZNS overlay rules for zone boundary and Offline zone conditions. |

Reserved command-specific fields have no NVM-defined meaning and should be cleared.
