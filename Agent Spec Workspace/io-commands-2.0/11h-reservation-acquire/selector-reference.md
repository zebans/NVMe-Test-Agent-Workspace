# Reservation Acquire Selector Reference

Source: NVMe Base Specification 2.0, section 7.2, Figures 392 and 394.

## Reservation Acquire Action (`RACQA`)

| RACQA | Action | Meaning |
|---|---|---|
| `000b` | Acquire | Acquire a reservation. |
| `001b` | Preempt | Preempt a reservation held on the namespace. |
| `010b` | Preempt and Abort | Preempt a reservation and abort affected commands. |
| `011b`-`111b` | Reserved | Invalid. |

## Reservation Type (`RTYPE`)

| RTYPE | Meaning |
|---|---|
| `0h` | Reserved |
| `1h` | Write Exclusive Reservation |
| `2h` | Exclusive Access Reservation |
| `3h` | Write Exclusive - Registrants Only Reservation |
| `4h` | Exclusive Access - Registrants Only Reservation |
| `5h` | Write Exclusive - All Registrants Reservation |
| `6h` | Exclusive Access - All Registrants Reservation |
| `7h`-`FFh` | Reserved |
