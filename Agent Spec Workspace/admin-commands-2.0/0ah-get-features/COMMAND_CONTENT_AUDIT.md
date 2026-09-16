# Get Features Content Audit

Status: COMPLETE for command-control, FID/SEL dispatch, high-value returned field lookup, status, and boundary mapping.

Audited source:

- NVMe Base Spec 2.0 section 5.15.
- Figure 191 through Figure 195.
- Feature format references in Figure 194.

Coverage:

- Opcode, data direction, NSID usage, `DPTR`, `SEL`, `FID`, `CDW11`, UUID index, saved/default fallback, supported-capabilities CQE Dword 0, and feature-payload ownership are captured.
- High-value returned fields are expanded in `field-reference.md`.
- Feature-specific large data buffers are routed through `payload-reference.md`; external or feature-owned structures keep their explicit owner instead of being guessed here.
