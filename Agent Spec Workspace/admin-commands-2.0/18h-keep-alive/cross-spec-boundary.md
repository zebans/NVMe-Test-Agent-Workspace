# Keep Alive Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Keep Alive command semantics.
- Keep Alive Timer restart rules referenced by section 5.18 and section 3.9.
- `KAS`, `TBKAS`, and `KATO` relationship at command-behavior level.
- Boundary between Keep Alive command status and Keep Alive feature/timer statuses.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Transport-specific Keep Alive requirements beyond Base Spec boundary notes.
- Full Set Features / Connect command validation details for `KATO`.
- Test harness timeout scheduling.

