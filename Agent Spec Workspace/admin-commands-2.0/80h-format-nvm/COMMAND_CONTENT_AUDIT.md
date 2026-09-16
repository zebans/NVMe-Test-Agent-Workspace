# Format NVM Content Audit

Status: COMPLETE for command-control, destructive scope, field lookup, restrictions, status, and boundary mapping.

Audited source:

- NVMe Base Spec 2.0 section 5.14.
- Figure 188 through Figure 190.

Coverage:

- Scope, destructive behavior, secure erase modes, FNA/NSID interactions, `CDW10` fields, Host Behavior Support `LBAFEE`, command concurrency, completion, statuses, and I/O Command Set boundary are captured.
- Command fields and high-risk rules are split into canonical lookup files.
