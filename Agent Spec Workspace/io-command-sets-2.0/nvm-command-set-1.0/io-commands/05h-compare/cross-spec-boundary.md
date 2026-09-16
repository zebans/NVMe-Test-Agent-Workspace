# NVM Compare Cross-Spec Boundary

## This Folder Owns

- NVM Compare command fields, comparison payload ownership, and NVM Compare-specific statuses.

## This Folder Does Not Own

- ZNS Compare overlay behavior.
- PyNVMe API syntax.
- Vendor-specific comparison behavior.

| Need | Read |
|---|---|
| ZNS overlay | `..\..\..\..\zns-command-set-1.1\modified-nvm-commands\05h-compare` |
| Deallocated/unwritten behavior | `..\09h-dataset-management` |
