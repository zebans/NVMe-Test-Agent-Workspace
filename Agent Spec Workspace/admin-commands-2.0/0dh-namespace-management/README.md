# Namespace Management - Opcode 0Dh

Base Spec 2.0 Admin command reference for creating and deleting namespaces.

Use this folder when the question is about Namespace Create/Delete, `SEL`, `NSID`, create data buffer, `CSI`, created namespace ID in CQE Dword 0, namespace capacity/identifier failures, `ANAGRPID`, or command-set ownership of namespace create fields.

## Read Path

| Need | Read |
|---|---|
| Command identity and transfer model | [command-facts.md](command-facts.md) |
| Create/Delete selector behavior | [selector-reference.md](selector-reference.md) |
| Command and create-structure fields | [field-reference.md](field-reference.md) |
| Create data buffer / completion payload | [payload-reference.md](payload-reference.md) |
| Status lookup | [status-reference.md](status-reference.md) |
| Restrictions and side effects | [restrictions.md](restrictions.md) |
| Base vs I/O command-set boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completion state of this folder | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Namespace Management creates or deletes namespaces, but Create does not attach the namespace to a controller. After a successful Create, use Namespace Attachment to make the namespace usable by one or more controllers.
