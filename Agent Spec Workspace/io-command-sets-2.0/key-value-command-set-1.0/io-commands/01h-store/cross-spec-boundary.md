# KV Store Cross-Spec Boundary

## This Folder Owns

- KV Store command fields, Store Options, value payload, atomicity, and Store-specific statuses.

## This Folder Does Not Own

- PyNVMe API syntax.
- Compression algorithms or implementation.
- Vendor-specific media layout.

| Need | Read |
|---|---|
| KV format limits | `..\..\..\KEY_VALUE_COMMAND_SET_INDEX.md` until Identify KV detail folders are expanded. |
| Reservation behavior | Base reservation command folders. |
