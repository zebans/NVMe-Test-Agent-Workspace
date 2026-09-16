# Namespace Attachment - Opcode 15h

Base Spec 2.0 Admin command reference for attaching and detaching controllers from a namespace.

Use this folder when the question is about Controller Attach/Detach, `SEL`, 4096-byte Controller List, controller-list validation, `MAXDNA`, `MAXCNA`, namespace sharing/private behavior, first failing Controller List entry reporting, or command-set support/enabled failures.

## Read Path

| Need | Read |
|---|---|
| Command identity and transfer model | [command-facts.md](command-facts.md) |
| Attach/Detach selector behavior | [selector-reference.md](selector-reference.md) |
| Command and Controller List fields | [field-reference.md](field-reference.md) |
| Controller List payload and error reporting | [payload-reference.md](payload-reference.md) |
| Status lookup | [status-reference.md](status-reference.md) |
| Restrictions and attachment limits | [restrictions.md](restrictions.md) |
| Controller List / command-set boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completion state of this folder | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Namespace Attachment makes an existing namespace visible to one or more controllers. It does not create a namespace; use Namespace Management first when the namespace does not yet exist.
