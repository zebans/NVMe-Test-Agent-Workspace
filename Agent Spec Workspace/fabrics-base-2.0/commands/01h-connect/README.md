# Connect - FCTYPE 01h

Fabrics Base command reference for creating a Submission Queue and Completion Queue pair.

Use this folder when the question is about Connect, `RECFMT`, `QID`, `SQSIZE`, `CATTR`, `KATO`, Connect Command Data, `HOSTID`, `CNTLID`, `SUBNQN`, `HOSTNQN`, Connect Response, `AUTHREQ`, `SQHD`, or Connect-specific statuses.

## Read Path

| Need | Read |
|---|---|
| Command identity and queue model | [command-facts.md](command-facts.md) |
| Queue / format / attribute selectors | [selector-reference.md](selector-reference.md) |
| SQE field lookup | [field-reference.md](field-reference.md) |
| Connect Command Data and response payload | [payload-reference.md](payload-reference.md) |
| Completion and status lookup | [status-reference.md](status-reference.md) |
| Connect restrictions and sequence rules | [restrictions.md](restrictions.md) |
| Base vs transport/API boundary | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Completion state of this folder | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Connect is the command that establishes Fabrics queue connectivity. Admin Queue Connect creates the host/controller association; I/O Queue Connect depends on that association already existing and being enabled.
