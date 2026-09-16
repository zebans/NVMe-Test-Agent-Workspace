# Namespace Attachment Payload Reference

## Controller List Payload

Namespace Attachment uses a 4096-byte host-to-controller Controller List.

| Payload | Meaning |
|---|---|
| Controller List | Identifies the controllers to attach to or detach from the namespace. |
| Size | 4096 bytes. |
| Direction | Host to controller. |
| Ownership | Controller List format is defined by Base section 4.4. |

If PRPs are used, the data buffer shall not be a PRP List and may not cross more than one page boundary.

## Failure Reporting Payload

On failure:

| Report location | Meaning |
|---|---|
| Error Information Log Entry, Command Specific Information field | Byte offset of the first failing Controller List entry. |

The controller does not process Controller List entries after the first failing entry.

## Completion Payload

The command posts a CQE to the Admin Completion Queue. No command-specific successful CQE payload is captured here.
