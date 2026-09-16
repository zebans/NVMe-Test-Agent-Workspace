# Reservation Register Status Reference

Source: NVMe Base Specification 2.0, section 7.3.

## Explicit Status Behavior

| SCT | SC | Status | Condition |
|---|---:|---|---|
| Generic Command Status | `02h` | Invalid Field in Command | Reserved `CPTPL` or `RREGA` value. |

## Boundary Statuses

Reservation conflict, key mismatch, access conflict, and reservation-state behavior belong to section 8.19 and global status definitions.
