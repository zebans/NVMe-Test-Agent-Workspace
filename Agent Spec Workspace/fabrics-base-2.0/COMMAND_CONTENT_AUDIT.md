# Fabrics Base Content Audit

Audit date: 2026-06-24

Status: `BOUNDARY-COMPLETE + COMMAND-INDEX-COMPLETE + COMMAND-CONTROL-COMPLETE`

## Audited Source

| Source | Coverage |
|---|---|
| Base Spec 2.0 section 3.3.2.1.1 | Fabrics command capsule SQE format, `OPC=7Fh`, `FCTYPE`. |
| Base Spec 2.0 section 3.3.2.1.2 | Fabrics response capsule CQE format and SQHD boundary. |
| Base Spec 2.0 section 6 / Figure 375 | Fabrics command type table and queue support. |
| Base Spec 2.0 Figure 97 | Fabrics command-specific status values. |

## Completion Meaning

`BOUNDARY-COMPLETE` means this folder identifies the Base Spec 2.0 source anchors and related source owners for non-Base details.

`COMMAND-INDEX-COMPLETE` means all Figure 375 Fabrics command types are indexed by `FCTYPE`.

`COMMAND-CONTROL-COMPLETE` means each non-vendor-specific Fabrics command has Base-owned fields, completion/status, restrictions, and `COMMAND_CONTENT_AUDIT.md` files.

## Not Yet Expanded

- Transport-specific status values `B0h` to `BFh`.
- Security protocol payload details from SPC-5.
- Full Base property semantics from section 3.1.3.

These should be expanded only when a downstream test-flow task needs exact fields or transport-specific behavior.
