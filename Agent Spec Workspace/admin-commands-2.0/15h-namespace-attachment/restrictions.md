# Namespace Attachment Restrictions

## Controller List

| Restriction | Meaning |
|---|---|
| Payload size | Uses a 4096-byte Controller List. |
| PRP rule | If PRPs are used, buffer shall not be a PRP List and may not cross more than one page boundary. |
| Admin controller | Controller List including an Admin controller is invalid. |
| First failure | Controller stops processing later entries after first failing Controller List entry. |

## Attach

| Restriction | Meaning |
|---|---|
| Attachment limits | Attach checks `MAXDNA` and `MAXCNA`; exceeding either limit fails. |
| Private namespace | Private namespace cannot be attached to multiple controllers. |
| Command-set support | Target controller must support the namespace's I/O Command Set. |
| Command-set enablement | Command set must be enabled by the I/O Command Set Profile feature. |
| ANA | ANA conditions can cause attach failure. |

## Detach

| Restriction | Meaning |
|---|---|
| Must be attached | Detach of a controller not attached to the namespace fails. |
| Persistence | Attach/detach operations persist across reset events and certain Virtualization Management offline operations. |

## Support Coupling

If Namespace Attachment is supported, Namespace Management shall also be supported.
