# ZNS-Modified Write Uncorrectable Command Facts

Source: ZNS 1.1 section 3.3.8 and Figure 20.

| Item | Value |
|---|---|
| Base command | NVM Write Uncorrectable |
| Opcode | `04h` |
| Base owner | NVM Command Set |
| ZNS owner | Additional zone restrictions and ZNS command-specific status values |
| Primary ZNS risks | Zone boundary, write pointer, zone state, active/open resources |

Write Uncorrectable remains defined by the NVM Command Set. ZNS adds zone-type requirements, write pointer validity, zone-state statuses, and resource-limit statuses.
