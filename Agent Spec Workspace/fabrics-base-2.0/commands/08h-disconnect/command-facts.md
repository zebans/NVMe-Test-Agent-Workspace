# Disconnect Command Facts

Source: NVMe Base Spec 2.0 section 6.4, Figures 384-385, Figure 375, and Figure 97.

| Item | Value |
|---|---|
| Command | Disconnect |
| Fabrics opcode | `OPC=7Fh` |
| Fabrics command type | `FCTYPE=08h` |
| Support | Optional |
| I/O Queue support | Supported |
| Admin Queue support | Not supported |
| Data transfer | No data transfer |
| Main field | `RECFMT` |

## Required Command Behavior

| Area | Requirement |
|---|---|
| Purpose | Deletes the I/O Queue on which the command is submitted. |
| Admin Queue | If submitted on Admin Queue, abort with `Invalid Queue Type`. |
| Transport connection | NVMe Transport connection is not deleted by issuing Disconnect. |
| Completion ordering | Disconnect CQE shall be the last entry submitted to the I/O Completion Queue by the controller. |
| After completion | Controller shall not process commands on that I/O Queue after sending Disconnect completion. |
