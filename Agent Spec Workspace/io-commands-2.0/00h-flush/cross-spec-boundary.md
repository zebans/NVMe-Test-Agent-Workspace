# Flush Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Flush command semantics.
- `NSID`, `VWC[2:1]`, and all-namespace Flush behavior.
- Flush cache/no-effect behavior and completion queue rule.

## This Folder Does Not Own

- PyNVMe API call syntax.
- NVM Write command behavior.
- Controller-internal cache implementation.
- ZNS overlay behavior; see ZNS modified Flush folder for ZNS-specific status additions.

