# Reservation Report Cross-Spec Boundary

## Owned By This Folder

| Area | Covered here |
|---|---|
| Command identity | Opcode `0Eh`, I/O command, controller-to-host transfer. |
| Command selectors | `NUMD`, `EDS`. |
| Payload layouts | Reservation Status, Extended Reservation Status, Registered Controller structures. |
| Explicit status | `Host Identifier Inconsistent Format` for Host Identifier / `EDS` mismatch. |

## Read Adjacent References When Needed

| Need | Reference |
|---|---|
| Reservation type encoding | Reservation Acquire / Reservation Release `RTYPE` reference. |
| Reservation-state behavior | Base Spec reservation behavior section. |
| Host Identifier configuration | Host Identifier feature. |
| PyNVMe usage | API layer such as `API_AGENTS.md`; this folder does not define API calls. |

## Boundary Rule

Do not turn this folder into a reservation state-machine guide. This command reports current state. The rules that create, clear, preempt, or persist that state belong to the reservation behavior section and the Register / Acquire / Release command folders.
