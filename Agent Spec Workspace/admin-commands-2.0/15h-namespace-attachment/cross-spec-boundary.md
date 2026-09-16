# Namespace Attachment Cross-Spec Boundary

## Owned By Base / This Folder

| Area | Covered here |
|---|---|
| Opcode and Admin command layout | Opcode `15h`, `SEL`, `NSID`, `DPTR`. |
| Attach/detach behavior | Controller Attach and Controller Detach. |
| Payload usage | 4096-byte Controller List and first-failure reporting. |
| Attachment limits | `MAXDNA` / `MAXCNA` failure surface. |
| Base-visible status | Namespace Attachment command-specific statuses from Figure 95. |

## Delegated Outside This Folder

| Area | Owner |
|---|---|
| Controller List byte-exact structure | Base section 4.4. |
| Namespace sharing/private capability | Identify Namespace `NMIC` and command-set-specific namespace data. |
| I/O Command Set support/enabled details | Command-set profile / selected command-set references. |
| ANA attach behavior details | ANA references and ANA-related Identify fields/logs. |
| PyNVMe API call syntax | API layer such as `API_AGENTS.md`. |

## Boundary Rule

Do not encode PyNVMe command calls or test-flow setup in this folder. This folder defines spec behavior and field/status meaning only.
