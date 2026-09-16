# ZNS-Modified Copy Command Facts

Source: ZNS 1.1 section 3.3.2 and Figure 14.

| Item | Value |
|---|---|
| Base command | NVM Copy |
| Opcode | `19h` |
| Base owner | NVM Command Set |
| ZNS owner | Additional source/destination zone restrictions and ZNS command-specific status values |
| Primary ZNS risks | Source/destination boundary, destination write pointer, source/destination zone state, active/open resources |

## ZNS Overlay Behavior

| Area | ZNS rule |
|---|---|
| Source range | Source Range Entry crossing zones may fail with Zone Boundary Error. |
| Destination range | Destination LBA range crossing zones may fail with Zone Boundary Error. |
| Destination write pointer | Destination write not at the write pointer may fail with Zone Invalid Write. |
| Destination zone state | Full, Read Only, or Offline destination zones can fail with ZNS statuses. |
| Source zone state | Offline source zones can fail with Zone Is Offline. |
| Resources | Active/open zone resource limits may abort the command. |
