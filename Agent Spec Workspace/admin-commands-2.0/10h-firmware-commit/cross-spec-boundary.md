# Firmware Commit Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Firmware Commit command semantics.
- `FS`, `CA`, `BPID`, and Firmware Commit CQE DW0 `MUD` meanings.
- Firmware Commit command-specific statuses.
- High-level Boot Partition/Firmware activation behavior stated by Base Spec.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Actual firmware image file format validation.
- Full firmware activation process in section 3.11.
- Full Boot Partition behavior in section 8.2.
- Platform reset orchestration.

