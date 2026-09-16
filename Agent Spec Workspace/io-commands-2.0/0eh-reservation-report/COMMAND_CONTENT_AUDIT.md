# Reservation Report Content Audit

Primary source: `..\..\..\NVMe Base Spec\2.0\NVMe\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md`

Audited source range:

- Section 7.5
- Figures 401, 402, 403, 404, 405, 406, 407

Status: `COMPLETE`

Captured:

- [x] Purpose and opcode identity.
- [x] Controller-to-host transfer direction and `DPTR` usage.
- [x] `CDW10.NUMD` behavior.
- [x] `CDW11.EDS` behavior.
- [x] Host Identifier format mismatch status.
- [x] Reservation Status structure control fields: `GEN`, `RTYPE`, `REGCTL`, `PTPLS`.
- [x] `GEN` increment and rollover rules.
- [x] Extended structure selection.
- [x] Registered Controller structure high-level fields.
- [x] Completion CQE rule.

Boundary:

- Reservation Report is treated as a reporting command, not the full reservation state-machine definition.
- Full state transitions remain tied to Reservation Register, Reservation Acquire, Reservation Release, and the reservation behavior section.
- Canonical files now replace the previous legacy multi-file layout.
