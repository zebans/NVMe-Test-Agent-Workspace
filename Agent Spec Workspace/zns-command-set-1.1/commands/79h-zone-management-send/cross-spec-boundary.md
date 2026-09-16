# Zone Management Send Cross-Spec Boundary

## Base Spec Owned

- Common command format.
- Generic completion queue behavior.
- Namespace Write Protection definition.

## ZNS Owned

- Opcode `79h`.
- Zone Send Action field.
- Select All behavior.
- Zone state transitions.
- Zone Descriptor Extension handling.
- Zone Capacity Changed CQE bit.
- Command-specific status values.
- Active/open resource failure behavior.

## Not Owned Here

- PyNVMe3 call mapping.
- Test setup, flow order, cleanup, or pass/fail script design.
