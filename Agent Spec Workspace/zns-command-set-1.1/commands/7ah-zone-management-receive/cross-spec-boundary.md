# Zone Management Receive Cross-Spec Boundary

## Base Spec Owned

- Common command format.
- Data Pointer definition.
- Generic completion queue behavior.

## ZNS Owned

- Opcode `7Ah`.
- Zone Receive Actions.
- Report Zones and Extended Report Zones data structures.
- Zone Descriptor data structure.
- Zone state, zone type, zone attributes, zone capacity, `ZSLBA`, and write pointer meanings.

## Not Owned Here

- PyNVMe3 call mapping.
- Test setup, flow order, cleanup, or pass/fail script design.
