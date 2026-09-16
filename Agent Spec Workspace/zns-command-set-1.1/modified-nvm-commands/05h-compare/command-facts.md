# ZNS-Modified Compare Command Facts

Source: ZNS 1.1 section 3.3.1 and Figure 13.

| Item | Value |
|---|---|
| Base command | NVM Compare |
| Opcode | `05h` |
| Base owner | NVM Command Set |
| ZNS owner | Additional zone requirements and ZNS command-specific status values |
| Primary ZNS risks | Zone boundary, zone state, active/open resources |

Compare remains defined by the NVM Command Set. ZNS adds zone-type requirements and ZNS command-specific statuses.
