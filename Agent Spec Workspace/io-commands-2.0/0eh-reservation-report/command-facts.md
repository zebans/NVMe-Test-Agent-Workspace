# Reservation Report Command Facts

Source: NVMe Base Spec 2.0 section 7.5, Figures 401-407.

| Item | Value |
|---|---|
| Command | Reservation Report |
| Opcode | `0Eh` |
| Command set | Common I/O |
| Submission queue | I/O Submission Queue |
| Data transfer | Controller to host |
| Namespace | `NSID` used |
| Data pointer | Used; points to Reservation Status data buffer |
| Main selectors | `NUMD`, `EDS` |

## Required Command Behavior

| Area | Requirement |
|---|---|
| `NSID` | Specifies the namespace for which reservation status is returned. `FFFFFFFFh` is not supported unless a later command-set rule explicitly allows it. |
| Data buffer | `DPTR` specifies PRP Entry 1, PRP Entry 2, or SGL Entry 1 for the controller-to-host transfer. |
| `NUMD` | Zero-based number of dwords to transfer. |
| `EDS` | Selects normal or extended Reservation Status data structure and must match the configured Host Identifier format. |
| Reserved fields | Reserved command fields shall be cleared by host software. |

## Completion

On completion, the controller posts a completion queue entry to the I/O Completion Queue associated with the I/O Submission Queue.
