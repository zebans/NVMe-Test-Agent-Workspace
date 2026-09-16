# Set Features - Opcode 09h

Base Spec 2.0 Admin command reference for setting feature attributes selected by Feature Identifier (`FID`).

Use this folder when a test or firmware question involves `FID`, `SV`, feature saveability/changeability, namespace-specific feature behavior, feature data buffers, Host Memory Buffer, Host Identifier, Reservation Notification Mask, Reservation Persistence, Namespace Write Protection, or I/O Command Set Profile.

## Read Path

| Need | Read |
|---|---|
| Opcode, transfer direction, and command dwords | [command-facts.md](command-facts.md) |
| Which feature a `FID` selects | [selector-reference.md](selector-reference.md) |
| Which features use command dwords vs data buffers | [payload-reference.md](payload-reference.md) |
| Feature command fields and common bit meanings | [field-reference.md](field-reference.md) |
| Set Features command-specific statuses | [status-reference.md](status-reference.md) |
| Base vs I/O command set vs vendor ownership | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Coverage status | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Set Features is selector-driven. First identify the `FID`, then check whether the feature is saveable, changeable, namespace-specific, and whether it uses only command dwords or a data buffer.

For tests, do not treat a successful Set Features completion as meaning every already-submitted command used the new setting. Base Spec only guarantees that commands submitted after successful completion use the new setting.
