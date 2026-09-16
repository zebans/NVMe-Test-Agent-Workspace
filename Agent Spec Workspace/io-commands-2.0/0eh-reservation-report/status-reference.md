# Reservation Report Status Reference

## Explicit Command-Relevant Status

| Status type | Status | When to expect |
|---|---|---|
| Generic | `Host Identifier Inconsistent Format` (`SC=18h`) | Host Identifier format and `EDS` do not match: 64-bit Host Identifier with `EDS=1`, or 128-bit Host Identifier with `EDS=0`. |

## Other Relevant Status Boundaries

| Category | When to consider it |
|---|---|
| Generic invalid field | Reserved command fields or malformed command parameters. |
| Reservation conflict / access statuses | Usually driven by reservation state and command access rules outside the report-format definition. |
| Namespace / controller state statuses | May apply if namespace access or controller state prevents command execution. |

## Testing Note

For Reservation Report, the clearest command-specific negative test is `EDS` versus Host Identifier format mismatch. Key ownership and permission conflicts are usually better tested with Reservation Register, Acquire, and Release, then observed through Reservation Report.
