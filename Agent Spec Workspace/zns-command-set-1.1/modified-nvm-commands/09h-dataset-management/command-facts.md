# ZNS-Modified Dataset Management Command Facts

Source: ZNS 1.1 section 3.3.3 and Figure 15.

| Item | Value |
|---|---|
| Base command | NVM Dataset Management |
| Opcode | `09h` |
| Base owner | NVM Command Set |
| ZNS owner | Additional Offline zone status condition |

Dataset Management remains defined by the NVM Command Set. ZNS adds a condition where an Offline zone specified by the Dataset Management operation can abort with `Zone Is Offline`.
