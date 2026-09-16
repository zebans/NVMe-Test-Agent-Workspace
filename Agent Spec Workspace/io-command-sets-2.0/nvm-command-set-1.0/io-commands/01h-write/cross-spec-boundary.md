# NVM Write Cross-Spec Boundary

## This Folder Owns

- NVM Write command fields and NVM command-specific statuses.
- User data / metadata / PI payload ownership for normal NVM namespaces.

## This Folder Does Not Own

- ZNS zone-state, write pointer, or zone boundary restrictions.
- PyNVMe API syntax.
- Vendor-specific write behavior.

| Need | Read |
|---|---|
| ZNS overlay | `..\..\..\..\zns-command-set-1.1\modified-nvm-commands\01h-write` |
| API call syntax | API layer |
