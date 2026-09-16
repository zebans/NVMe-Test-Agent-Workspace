# Get Features - Opcode 0Ah

Base Spec 2.0 Admin command reference for retrieving feature attributes selected by Feature Identifier (`FID`) and Select (`SEL`).

Use this folder when a test or firmware question involves `SEL`, current/default/saved/supported feature values, feature capability bits, feature data buffers, Get Features returned CQE Dword 0, or feature-specific returned attributes.

## Read Path

| Need | Read |
|---|---|
| Opcode, transfer direction, and command dwords | [command-facts.md](command-facts.md) |
| `SEL` and `FID` selector behavior | [selector-reference.md](selector-reference.md) |
| Which features return CQE DW0 vs data buffer | [payload-reference.md](payload-reference.md) |
| Returned fields and supported-capability bits | [field-reference.md](field-reference.md) |
| Status and common invalid cases | [status-reference.md](status-reference.md) |
| Base vs I/O command set vs vendor ownership | [cross-spec-boundary.md](cross-spec-boundary.md) |
| Coverage status | [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) |

## Human Guideline

Get Features is a query command. `FID` selects the feature and `SEL` selects which version of the value is requested: current, default, saved, or supported capabilities.

For tests, `SEL=011b` is special: CQE Dword 0 reports whether the feature is saveable, namespace specific, and changeable. It does not return the normal current/default/saved value.
