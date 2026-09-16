# Vendor Specific Fabrics Cross-Spec Boundary

## Owned By Base / This Folder

| Area | Covered here |
|---|---|
| Range identity | `OPC=7Fh`, `FCTYPE=C0h`-`FFh`. |
| Support classification | Optional vendor-specific range. |

## Delegated Outside This Folder

| Area | Owner |
|---|---|
| Command semantics | Vendor documentation. |
| Fields and payloads | Vendor documentation. |
| Queue support | Vendor documentation. |
| Completion and status behavior | Vendor documentation. |
| PyNVMe API call syntax | API layer such as `API_AGENTS.md`. |

## Boundary Rule

Do not infer vendor-specific command behavior from Base Spec 2.0. Base only gives the range boundary.
