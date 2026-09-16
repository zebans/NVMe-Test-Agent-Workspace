# ZNS-Modified Verify Command Facts

Source: ZNS 1.1 section 3.3.6 and Figure 18.

| Item | Value |
|---|---|
| Base command | NVM Verify |
| Opcode | `0Ch` |
| Base owner | NVM Command Set |
| ZNS owner | Additional zone boundary and Offline zone status values |

Verify remains defined by the NVM Command Set. ZNS adds `Zone Boundary Error` and `Zone Is Offline`.
