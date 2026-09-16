# ZNS-Modified Write Command Facts

Source: ZNS 1.1 section 3.3.7 and Figure 19.

| Item | Value |
|---|---|
| Base command | NVM Write |
| Opcode | `01h` |
| Base owner | NVM Command Set |
| ZNS owner | Additional zone restrictions and ZNS command-specific status values |
| Primary ZNS risks | Zone boundary, write pointer, zone state, active/open resources |

## ZNS Overlay Behavior

| Area | ZNS rule |
|---|---|
| Zone boundary | Command specifying logical blocks in more than one zone may fail with Zone Boundary Error. |
| Write pointer | Write to a Sequential Write Required zone must be at the zone write pointer. |
| Zone state | Full, Read Only, or Offline target zones can fail with ZNS statuses. |
| Resources | Active/open zone resource limits may abort the command. |
| Completion | Base completion remains NVM-defined with additional ZNS status values. |
