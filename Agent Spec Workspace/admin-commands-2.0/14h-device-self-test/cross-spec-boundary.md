# Device Self-test Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Device Self-test command semantics.
- `NSID`, `CDW10.STC`, and `DSTO` interpretation for command processing.
- Figure 170-173 command behavior and statuses.
- Device Self-test Log interaction at command-behavior level.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Detailed Device Self-test Log field table beyond command interaction.
- Vendor specific self-test behavior for `STC=Eh`.
- Full section 8.6 operation timing examples.
- Test harness wait/poll strategy.

