# Reservation Release Status Reference

Source: NVMe Base Specification 2.0, section 7.4.

## Explicit Status Behavior

| SCT | SC | Status | Condition |
|---|---:|---|---|
| Generic Command Status | `02h` | Invalid Field in Command | `IEKEY=1`. |
| Generic Command Status | `02h` | Invalid Field in Command | `RRELA=Release` and `RTYPE` does not match current reservation type; controller should return this status. |
| Generic Command Status | `02h` | Invalid Field in Command | Reserved `RRELA` or `RTYPE` value. |

## Boundary Statuses

Reservation conflict, key mismatch, access conflict, and reservation-state behavior belong to section 8.19 and global status definitions.
