# ZNS-Modified Flush Command Facts

Source: ZNS 1.1 section 3.3.4 and Figure 16.

| Item | Value |
|---|---|
| Base command | NVM Flush |
| Opcode | `00h` |
| Base owner | NVM Command Set |
| ZNS owner | Additional Offline zone status condition |

Flush remains defined by the NVM Command Set. ZNS adds a condition where the command may be aborted with `Zone Is Offline` if volatile write cache conditions apply and the specified zone is Offline.
