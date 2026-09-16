# NVM Copy Cross-Spec Boundary

## This Folder Owns

- NVM Copy command fields, source range descriptor formats, Copy limits, and NVM Copy-specific statuses.

## This Folder Does Not Own

- ZNS Copy overlay behavior.
- PyNVMe API syntax.
- Vendor-specific internal copy implementation.

| Need | Read |
|---|---|
| ZNS overlay | `..\..\..\..\zns-command-set-1.1\modified-nvm-commands\19h-copy` |
| Deallocated/unwritten behavior | `..\09h-dataset-management` |
