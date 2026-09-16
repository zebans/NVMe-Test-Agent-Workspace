# Get Log Page Content Audit

Status: COMPLETE for command-control, LID dispatch, test/FW-oriented payload field lookup, status, and boundary mapping.

Source: NVMe Base Specification 2.0, section 5.16, Figures 196-268.

## Included

| Area | Status | Notes |
|---|---|---|
| Opcode and transfer direction | Complete | `02h`, Admin, controller-to-host data transfer. |
| Command dwords | Complete | DPTR, CDW10, CDW11, CDW12, CDW13, CDW14. |
| LID selector table | Complete | Figure 202, including reserved, I/O command set specific, discovery, reservation, sanitize, and vendor ranges. |
| Offset rules | Complete | Byte offset vs index offset, dword alignment, IOS requirement, LPA dependency. |
| Status values | Complete | Figure 268 plus common `Invalid Field in Command` cases from section 5.16. |
| Returned payload lookup | Complete | `field-reference.md` maps each Base-owned LID family to test/FW-oriented offsets, fields, key bit meanings, and descriptor dispatch. |
| Large/nested payload families | Complete for Base-owned lookup | ANA descriptors, Persistent Event headers/event dispatch, Media Unit Status descriptors, Supported Capacity Configuration descriptors, Discovery entries, Reservation Notification, and Sanitize Status are expanded enough for direct field lookup. External, vendor, or command-set-specific parts are explicitly marked by owner instead of being invented here. |

## Verification Notes

- The folder now uses the canonical command reference split instead of the previous two-file layout.
- `field-reference.md` is optimized for Codex lookup of fields and meanings. It preserves precise offsets/bit meanings for test-relevant Base-owned fields and routes vendor/command-set-specific payloads to their owning layer.
- Reserved ranges are treated as Base-defined absence of behavior. Tests may verify rejection or non-support, but should not invent reserved meanings.
