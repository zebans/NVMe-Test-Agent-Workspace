# Sanitize Content Audit

Status: COMPLETE for command-control, sanitize action lookup, restrictions, status, and boundary mapping.

Audited source:

- NVMe Base Spec 2.0 section 5.24.
- Figure 303 through Figure 305.
- Related sanitize-operation boundary in section 8.21.

Coverage:

- Opcode, no-NSID behavior, actions, `CDW10`, `CDW11`, PMR restriction, pending firmware activation restriction, exit failure mode, completion semantics, statuses, and section 8.21 boundary are captured.
- Command fields and high-risk state rules are split into canonical lookup files.
