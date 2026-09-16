# Namespace Attachment Command Facts

Source: NVMe Base Spec 2.0 section 5.22, Figures 294-296.

| Item | Value |
|---|---|
| Command | Namespace Attachment |
| Opcode | `15h` |
| Command set | Admin |
| Data transfer | Host to controller |
| Namespace | `NSID` used |
| Main selector | `CDW10.SEL` |
| Payload | 4096-byte Controller List |

## Required Command Behavior

| Operation | Required behavior |
|---|---|
| Controller Attach | Attaches the listed controllers to the namespace. |
| Controller Detach | Detaches the listed controllers from the namespace. |
| Persistence | Attach/detach operations persist across reset events and Virtualization Management commands that set a secondary controller offline. |
| Support coupling | If Namespace Attachment is supported, Namespace Management shall also be supported. |
| Completion | Posts a CQE to the Admin Completion Queue. |

## Failure Processing Rule

On failure, the byte offset of the first failing Controller List entry is reported in the Command Specific Information field of the Error Information Log Entry, and the controller does not process later entries.
