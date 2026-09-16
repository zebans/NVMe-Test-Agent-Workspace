# MI Admin-Through Agent Rules

You are reading the NVMe-MI 1.2 Admin-through-MI layer.

This layer contains SPEC facts only. Do not write PyNVMe API calls, pytest fixtures, shell commands, or complete test flows.

Read in this order:

```text
README.md
MI_ADMIN_THROUGH_COMMAND_TABLE.md
command-format-reference.md
field-reference.md
support-overlays-reference.md when the question involves Get Log Page, Get Features, Set Features, sanitize, or Format NVM support through a Management Endpoint
status-boundary-reference.md
cross-spec-boundary.md
..\MI_STATUS_AND_ERROR_REFERENCE.md when MI response status values are needed
..\MI_INBAND_OUTOFBAND_BOUNDARY.md when mechanism ownership matters
..\..\admin-commands-2.0\<opcode-folder>\ when Base Admin command semantics are needed
original MI source section 6 only when exact wording must be re-audited
```

Use this layer when a question involves:

- Whether an NVMe Admin command is Mandatory, Optional, or Prohibited over the out-of-band MI mechanism.
- Storage Device versus Enclosure Admin-through-MI support differences.
- Admin-through-MI request bytes, response bytes, DOFST, DLEN, CTLID, or SQEDW mapping.
- Management Endpoint log page support, feature support, or sanitize/format allowed-command overlays.
- Whether a status belongs to the MI wrapper or to the tunneled NVMe Admin command completion.

Do not use this layer as the source of Base Admin command CDW semantics. After identifying the Admin opcode and support rule, route to the linked `admin-commands-2.0` command folder for the command body.
