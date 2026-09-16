# NVM Write Uncorrectable Cross-Spec Boundary

## This Folder Owns

- NVM Write Uncorrectable command fields, WUSL behavior, and Unrecovered Read Error aftermath.

## This Folder Does Not Own

- ZNS overlay behavior.
- PyNVMe API syntax.
- Vendor-specific media failure implementation.

| Need | Read |
|---|---|
| ZNS overlay | `..\..\..\..\zns-command-set-1.1\modified-nvm-commands\04h-write-uncorrectable` |
| Get LBA Status reporting of Write Uncorrectable LBAs | `..\..\admin-commands\86h-get-lba-status` |
