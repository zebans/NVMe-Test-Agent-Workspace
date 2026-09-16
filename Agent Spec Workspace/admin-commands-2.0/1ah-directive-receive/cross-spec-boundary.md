# Directive Receive Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Directive Receive command shell.
- `DPTR`, `NUMD`, `DSPEC`, `DTYPE`, and `DOPER` field meanings.
- `NUMD` truncation / over-allocation behavior.
- Boundary to directive-specific behavior in section 8.7.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Directive Type tables and operation-specific payloads from section 8.7.
- Full directive-specific command status expansion.
- Test flow sequencing for individual directives.

