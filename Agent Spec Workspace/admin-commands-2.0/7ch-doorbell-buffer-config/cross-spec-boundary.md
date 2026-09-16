# Doorbell Buffer Config Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Doorbell Buffer Config command fields and buffer layout.
- `PRP1`, `PRP2`, `(4 << CAP.DSTRD)`, and `max(NSQA, NCQA)` relationship.
- Invalid buffer address status behavior.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Host memory allocation implementation.
- Para-virtualized controller implementation details.
- Runtime queue creation/destruction flow.

