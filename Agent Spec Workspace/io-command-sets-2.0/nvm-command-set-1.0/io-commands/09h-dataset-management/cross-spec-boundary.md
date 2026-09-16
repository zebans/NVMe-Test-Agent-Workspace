# NVM Dataset Management Cross-Spec Boundary

## This Folder Owns

- NVM Dataset Management fields, range payload, processing limits, and deallocated/unwritten logical block behavior.

## This Folder Does Not Own

- ZNS Dataset Management overlay behavior.
- PyNVMe API syntax.
- Vendor-specific deallocation internals.

| Need | Read |
|---|---|
| ZNS overlay | `..\..\..\..\zns-command-set-1.1\modified-nvm-commands\09h-dataset-management` |
| Read/Compare/Verify/Copy behavior on deallocated blocks | Those command folders plus this folder's deallocated/unwritten rules. |
