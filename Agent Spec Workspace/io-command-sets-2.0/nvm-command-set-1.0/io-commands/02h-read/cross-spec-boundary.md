# NVM Read Cross-Spec Boundary

## This Folder Owns

- NVM Read command fields, read payload ownership, and NVM read-specific statuses.

## This Folder Does Not Own

- ZNS zone boundary / Offline zone overlay behavior.
- PyNVMe API syntax.
- Vendor-specific media recovery details.

| Need | Read |
|---|---|
| ZNS overlay | `..\..\..\..\zns-command-set-1.1\modified-nvm-commands\02h-read` |
| Deallocated/unwritten behavior | `..\09h-dataset-management` |
