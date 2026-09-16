# Authentication Send Command Facts

Source: NVMe Base Spec 2.0 section 6.2, Figures 378-379, and Figure 375.

| Item | Value |
|---|---|
| Command | Authentication Send |
| Fabrics opcode | `OPC=7Fh` |
| Fabrics command type | `FCTYPE=05h` |
| Support | Optional |
| I/O Queue support | Supported |
| Data transfer | Host to controller |
| Main fields | `SGL1`, `SPSP0`, `SPSP1`, `SECP`, `TL` |

## Required Command Behavior

| Area | Requirement |
|---|---|
| Purpose | Transfers security protocol data to the controller. |
| Returned data/status | Retrieved with Authentication Receive. |
| Pairing model | Association between Authentication Send and later Authentication Receive is Security Protocol field dependent as defined in SPC-5. |
| Security protocol | `SECP` specifies the security protocol as defined in SPC-5. |
