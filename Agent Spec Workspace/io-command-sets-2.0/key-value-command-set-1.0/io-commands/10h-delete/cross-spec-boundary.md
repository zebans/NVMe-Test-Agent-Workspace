# KV Delete Cross-Spec Boundary

## This Folder Owns

- KV Delete command fields, key selection, delete atomicity, and Delete-specific statuses.

## This Folder Does Not Own

- PyNVMe API syntax.
- Vendor-specific key ordering/storage implementation.
- Base reservation command definitions.

| Need | Read |
|---|---|
| KV Configuration `EDNEK` | `..\..\..\KEY_VALUE_COMMAND_SET_INDEX.md` contains the KV Feature `20h` field snapshot. |
| Reservation behavior | Base reservation command folders. |
