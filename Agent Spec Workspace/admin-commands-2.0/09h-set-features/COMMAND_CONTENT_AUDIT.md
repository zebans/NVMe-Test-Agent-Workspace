# Set Features Content Audit

Status: COMPLETE for command-control, FID dispatch, high-value feature field lookup, status, and boundary mapping.

Audited source:

- NVMe Base Spec 2.0 section 5.27.
- Figure 313 through Figure 316.
- Command-specific status list in Figure 370.

Coverage:

- Opcode, data direction, NSID usage, `DPTR`, `SV`, `FID`, feature-specific command dwords, UUID index, FID dispatch, save/change behavior, status behavior, and feature-payload ownership are captured.
- High-value feature fields are expanded in `field-reference.md`.
- Large feature data structures are routed through `payload-reference.md` and summarized in `field-reference.md`; external or feature-owned substructures keep their explicit owner instead of being guessed here.
