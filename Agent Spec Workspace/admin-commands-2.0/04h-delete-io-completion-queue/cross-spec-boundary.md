# Delete I/O Completion Queue Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Delete I/O Completion Queue command semantics.
- `CDW10.QID` target selection.
- Admin CQ exclusion.
- Associated I/O SQ deletion ordering.
- Command-specific status meanings for this command.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Test flow sequencing beyond spec-required queue deletion ordering.
- Transport-specific queue memory mapping behavior.
- Controller implementation internals.
