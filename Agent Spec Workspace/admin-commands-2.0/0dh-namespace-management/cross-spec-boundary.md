# Namespace Management Cross-Spec Boundary

## Owned By Base / This Folder

| Area | Covered here |
|---|---|
| Opcode and Admin command layout | Opcode `0Dh`, `SEL`, `NSID`, `DPTR`, `CSI`. |
| Create/Delete control flow | Create namespace, Delete namespace, delete-all behavior. |
| Base create buffer layout | Base regions and ownership boundaries. |
| Completion | Created `NSID` in CQE Dword 0 for Create. |
| Base-visible status | Namespace Management command-specific statuses from Figure 95. |

## Delegated Outside This Folder

| Area | Owner |
|---|---|
| I/O Command Set-specific create fields | Selected I/O Command Set spec, based on `CSI`. |
| Exact logical-block namespace format fields | NVM / ZNS / other selected command-set spec. |
| Capacity values used for planning | Identify Controller and related capacity-management references. |
| PyNVMe API call syntax | API layer such as `API_AGENTS.md`. |

## Boundary Rule

Do not encode PyNVMe command calls or test-flow setup in this folder. This folder defines spec behavior and field/status meaning only.
