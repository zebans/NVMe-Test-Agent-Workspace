# Delete I/O Submission Queue Cross-Spec Boundary

## Owned Here

| Area | Covered here |
|---|---|
| Command identity | Admin opcode `00h`. |
| Queue selector | `CDW10.QID`. |
| Delete behavior | I/O SQ deletion and Admin SQ exclusion. |
| Completion behavior | Admin CQ completion timing and deleted-SQ completion rule. |

## Delegated Outside This Folder

| Area | Owner |
|---|---|
| Queue memory allocation mechanics | Host/controller implementation and Base queue memory rules. |
| PyNVMe API syntax | API layer such as `API_AGENTS.md`. |
