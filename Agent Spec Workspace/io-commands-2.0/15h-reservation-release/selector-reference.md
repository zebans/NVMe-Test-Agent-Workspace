# Reservation Release Selector Reference

Source: NVMe Base Specification 2.0, section 7.4, Figures 399 and 394.

## Reservation Release Action (`RRELA`)

| RRELA | Action | Meaning |
|---|---|---|
| `000b` | Release | Release a reservation held on the namespace. |
| `001b` | Clear | Clear reservation state. |
| `010b`-`111b` | Reserved | Invalid. |

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
