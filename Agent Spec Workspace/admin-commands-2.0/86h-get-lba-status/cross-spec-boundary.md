# Get LBA Status Cross-Spec Boundary

## This Folder Owns

- Base Admin opcode `86h`.
- Controller-to-host data direction.
- `NSID=FFFFFFFFh` not-supported boundary from Base opcode table.
- Routing to NVM/ZNS command-set-specific definition.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Get LBA Status command-specific dwords.
- Returned LBA Status payload layout.
- NVM/ZNS command-specific status behavior.

## Canonical Downstream Lookup

| Need | Read |
|---|---|
| Base opcode, data direction, NSID boundary | This folder. |
| NVM request fields and returned descriptor semantics | `..\..\io-command-sets-2.0\nvm-command-set-1.0\admin-commands\86h-get-lba-status`. |
| ZNS namespace-specific interpretation | `..\..\io-command-sets-2.0\ZNS_COMMAND_SET_INDEX.md` and `..\..\zns-command-set-1.1`. |
| PyNVMe call syntax | API layer, not SPEC layer. |
