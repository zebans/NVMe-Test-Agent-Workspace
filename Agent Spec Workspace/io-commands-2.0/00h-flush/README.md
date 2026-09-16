# Flush - Opcode 00h

Base Spec 2.0 I/O command reference for making volatile write cache contents non-volatile.

Use this folder when the question is about Flush scope, `NSID=FFFFFFFFh`, `VWC[2:1]`, volatile write cache enabled/disabled behavior, sanitize interaction, or Flush completion.

## Read Path

| Need | Read |
|---|---|
| Command identity and behavior | [command-facts.md](command-facts.md) |
| Scope selector rules | [selector-reference.md](selector-reference.md) |
| Field lookup | [field-reference.md](field-reference.md) |
| Completion behavior | [payload-reference.md](payload-reference.md) |
| Status lookup | [status-reference.md](status-reference.md) |
| Restrictions | [restrictions.md](restrictions.md) |
| Boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completion state | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |
