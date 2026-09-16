# Reservation Acquire Content Audit

Primary source: `..\..\..\NVMe Base Spec\2.0\NVMe\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md`

Audited source range:

- Section 7.2
- Figures 391, 392, 393, 394

Status: `COMPLETE`

Captured:

- [x] Purpose.
- [x] CDW10 fields.
- [x] DPTR transfer direction and PRP/SGL usage.
- [x] RACQA values.
- [x] Reservation Acquire data structure.
- [x] RTYPE encoding.
- [x] Reserved fields and values.
- [x] IEKEY invalid-field rule.
- [x] Completion CQE rule.

Boundary:

- Section 8.19 reservation-state behavior is not duplicated here.
- Canonical files now replace the previous legacy multi-file layout.
