# NVM Verify Cross-Spec Boundary

## This Folder Owns

- NVM Verify command fields, no-transfer behavior, VSL behavior, and Verify-specific status surfaces.

## This Folder Does Not Own

- ZNS Verify overlay behavior.
- PyNVMe API syntax.
- Vendor-specific media verification internals.

| Need | Read |
|---|---|
| ZNS overlay | `..\..\..\..\zns-command-set-1.1\modified-nvm-commands\0ch-verify` |
| Deallocated/unwritten behavior | `..\09h-dataset-management` |
