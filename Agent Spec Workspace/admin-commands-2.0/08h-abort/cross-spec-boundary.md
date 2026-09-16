# Abort Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Abort command semantics.
- `CDW10.SQID`, `CDW10.CID`, and Abort CQE DW0 bit 0 meanings.
- Abort command-specific status meanings.
- Identify Controller `ACL` dependency.

## This Folder Does Not Own

- PyNVMe API call syntax.
- How a test framework tracks outstanding commands.
- Controller-internal abort implementation.
- Command-specific cleanup behavior for the command being aborted.

