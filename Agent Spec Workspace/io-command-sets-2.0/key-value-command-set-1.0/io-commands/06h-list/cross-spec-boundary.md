# KV List Cross-Spec Boundary

## This Folder Owns

- KV List command fields, starting-key behavior, returned key list layout, and List-specific statuses.

## This Folder Does Not Own

- Vendor-specific ordering when starting key does not exist.
- PyNVMe API syntax.
- Internal key storage/indexing.

| Need | Read |
|---|---|
| KV format limits | `..\..\..\KEY_VALUE_COMMAND_SET_INDEX.md` until Identify KV detail folders are expanded. |
