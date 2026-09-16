# Reservation Release Content Audit

Primary source: `..\..\..\NVMe Base Spec\2.0\NVMe\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md`

Audited source range:

- Section 7.4
- Figures 398, 399, 400
- Figure 394 RTYPE encoding

Status: `COMPLETE`

Captured:

- [x] Purpose.
- [x] CDW10 fields.
- [x] DPTR transfer direction and PRP/SGL usage.
- [x] RRELA values.
- [x] RTYPE match rule for Release.
- [x] IEKEY invalid-field rule.
- [x] Reservation Release data structure.
- [x] Reserved fields and values.
- [x] Completion CQE rule.

Boundary:

- Section 8.19 reservation-state behavior is not duplicated here.
- Canonical files now replace the previous legacy multi-file layout.
