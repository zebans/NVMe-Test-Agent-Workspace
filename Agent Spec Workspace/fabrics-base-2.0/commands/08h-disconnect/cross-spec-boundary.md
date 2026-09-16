# Disconnect Cross-Spec Boundary

## Owned By Fabrics Base / This Folder

| Area | Covered here |
|---|---|
| Capsule fields | `OPC`, `FCTYPE`, `RECFMT`. |
| Queue support | I/O Queue only; Admin Queue returns `Invalid Queue Type`. |
| Queue deletion | Deletes the I/O Queue on which the command is submitted. |
| Completion ordering | Disconnect CQE is last entry submitted to the I/O CQ. |
| Base-visible status | Incompatible Format, Controller Busy, Invalid Queue Type. |

## Delegated Outside This Folder

| Area | Owner |
|---|---|
| Transport connection deletion and resources | Applicable NVMe Transport binding. |
| PyNVMe API call syntax | API layer such as `API_AGENTS.md`. |

## Boundary Rule

Disconnect deletes the NVMe Fabrics I/O Queue, not the NVMe Transport connection itself.
