# MI In-Band and Out-of-Band Boundary

Status: `COMPLETE`

## Out-of-Band

| Area | Source |
|---|---|
| Out-of-band theory of operation | 1.3.1 |
| Physical layer: SMBus/I2C | 2.2 |
| Out-of-band message transport | 3.2 |
| MCTP packet fields | Figures 20-22 |
| Out-of-band message servicing | 4.2 |
| Control primitives | Figures 33-43 |
| Out-of-band command support | Figure 58 |

## In-Band

| Area | Source |
|---|---|
| In-band theory of operation | 1.3.2 |
| In-band tunneling message transport | 3.3 |
| In-band tunneling message servicing | 4.3 |
| NVMe-MI Send mapping | 4.3.1, Figures 44-49 |
| NVMe-MI Receive mapping | 4.3.2, Figures 50-54 |
| In-band command support | Figure 59 |

## Base Spec Boundary

Base Spec 2.0 owns the Admin command opcodes:

- `1Dh` NVMe-MI Send
- `1Eh` NVMe-MI Receive

This MI layer owns the message and command behavior tunneled through those Base Admin commands.
