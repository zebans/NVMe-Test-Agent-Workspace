# NVM Copy Restrictions

| Condition | Rule / expected behavior |
|---|---|
| Descriptor Format unsupported | Abort with Invalid Field in Command. |
| Namespace uses 16b Guard PI and Descriptor Format is not `0h` | Abort with Invalid Namespace or Format. |
| Namespace uses 32b/64b Guard PI and Descriptor Format is not `1h` | Abort with Invalid Namespace or Format. |
| `NR` exceeds `MSRC` | Abort with Command Size Limit Exceeded. |
| Any Source Range Entry `NLB` exceeds `MSSRL` | Abort with Command Size Limit Exceeded. |
| Sum of all Source Range Entry `NLB` values exceeds `MCL` | Abort with Command Size Limit Exceeded. |
| Source range contains deallocated/unwritten logical block | Behavior follows deallocated/unwritten rules; Copy may fail with status `87h`. |
| Namespace uses ZNS (`CSI=02h`) | Apply ZNS overlay for source/destination zone boundary, destination write pointer, zone state, and active/open resources. |

Reserved command-specific fields and reserved descriptor fields have no NVM-defined meaning and should be cleared.
