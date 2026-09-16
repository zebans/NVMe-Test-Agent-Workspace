# NVM Write Zeroes Cross-Spec Boundary

## This Folder Owns

- NVM Write Zeroes command fields, NVM zero/deallocate behavior, and NVM command-specific statuses.

## This Folder Does Not Own

- ZNS zone-state, write pointer, or zone boundary restrictions.
- PyNVMe API syntax.
- Vendor-specific deallocation implementation details.

| Need | Read |
|---|---|
| ZNS overlay | `..\..\..\..\zns-command-set-1.1\modified-nvm-commands\08h-write-zeroes` |
| Deallocated/unwritten read behavior | `..\09h-dataset-management` |
