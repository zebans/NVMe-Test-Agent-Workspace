# Directive Send Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 Directive Send command shell.
- `DPTR`, `NUMD`, `DSPEC`, `DTYPE`, and `DOPER` field meanings.
- Conditional ownership of `CDW12/CDW13`.
- Boundary to directive-specific behavior in section 8.7.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Directive Type tables and operation-specific payloads from section 8.7.
- Directive-specific command status expansion.
- Test flow sequencing for individual directives.

