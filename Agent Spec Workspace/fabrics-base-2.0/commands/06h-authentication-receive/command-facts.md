# Authentication Receive Command Facts

Source: NVMe Base Spec 2.0 section 6.1, Figures 376-377, and Figure 375.

| Item | Value |
|---|---|
| Command | Authentication Receive |
| Fabrics opcode | `OPC=7Fh` |
| Fabrics command type | `FCTYPE=06h` |
| Support | Optional |
| I/O Queue support | Supported |
| Data transfer | Controller to host |
| Main fields | `SGL1`, `SPSP0`, `SPSP1`, `SECP`, `AL` |

## Required Command Behavior

| Area | Requirement |
|---|---|
| Purpose | Transfers status and data results of one or more Authentication Send commands previously submitted to the controller. |
| Pairing model | Association with previous Authentication Send commands depends on the Security Protocol. |
| Returned data format | Depends on the Security Protocol. |
| Retention | Authentication Receive data shall not be retained if communication is lost or if a Controller Level Reset occurs. |
| Security protocol | `SECP` specifies the security protocol as defined in SPC-5. |
