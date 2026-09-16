# ZNS-Modified Write Zeroes Command Facts

Source: ZNS 1.1 section 3.3.9 and Figure 21.

| Item | Value |
|---|---|
| Base command | NVM Write Zeroes |
| Opcode | `08h` |
| Base owner | NVM Command Set |
| ZNS owner | Additional zone restrictions and ZNS command-specific status values |
| Primary ZNS risks | Zone boundary, write pointer, zone state, active/open resources, deallocation boundary |

## ZNS Overlay Behavior

| Area | ZNS rule |
|---|---|
| Zone boundary | Command specifying logical blocks in more than one zone may fail with Zone Boundary Error. |
| Write pointer | Write-like behavior may be subject to write pointer validity. |
| Zone state | Full, Read Only, or Offline target zones can fail with ZNS statuses. |
| Resources | Active/open zone resource limits may abort the command. |
| Deallocation | ZNS model distinguishes Write Zeroes cases that deallocate logical blocks from cases that do not. |
