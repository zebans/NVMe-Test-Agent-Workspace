# Fabrics Base 2.0 Layer

Base Spec 2.0 Fabrics Command Set reference layer.

Use this folder when the question is about Base-owned Fabrics command capsules, response capsules, `OPC=7Fh`, `FCTYPE`, Fabrics command routing, Fabrics command status values, or the boundary between Base section 6 and transport-specific behavior.

## Source

```text
..\NVMe Base Spec\2.0\NVMe\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

## Read Path

| Need | Read |
|---|---|
| Agent rules | [FABRICS_AGENTS.md](FABRICS_AGENTS.md) |
| Command index | [FABRICS_COMMAND_SET_INDEX.md](FABRICS_COMMAND_SET_INDEX.md) |
| Status values | [FABRICS_STATUS_REFERENCE.md](FABRICS_STATUS_REFERENCE.md) |
| Base/Fabrics boundary | [BASE_TO_FABRICS_BOUNDARY.md](BASE_TO_FABRICS_BOUNDARY.md) |
| Command detail | The matching folder under `commands\`, selected by `FCTYPE` in [FABRICS_COMMAND_SET_INDEX.md](FABRICS_COMMAND_SET_INDEX.md) |

## Boundary

This layer owns Base Spec 2.0 section 6 Fabrics command facts. Transport-specific status values and transport behavior remain delegated to the applicable NVMe transport binding specification.
