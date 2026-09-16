# ZNS-Modified Read Command Facts

Source: ZNS 1.1 section 3.3.5 and Figure 17.

| Item | Value |
|---|---|
| Base command | NVM Read |
| Opcode | `02h` |
| Base owner | NVM Command Set |
| ZNS owner | Additional zone boundary and Offline zone status values |

Read remains defined by the NVM Command Set. ZNS adds a narrower status set than write-like commands: `Zone Boundary Error` and `Zone Is Offline`.
