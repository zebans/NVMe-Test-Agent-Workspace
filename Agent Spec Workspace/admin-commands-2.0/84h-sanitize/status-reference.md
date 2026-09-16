# Sanitize Status Reference

Source: NVMe Base Specification 2.0, section 5.24, Figure 305, and section 8.21 boundary.

## Command Specific Status Values

| SCT | SC | Name | Meaning | Typical trigger |
|---|---|---|---|---|
| Command Specific | `0Bh` | Firmware Activation Requires Conventional Reset | Sanitize could not start because pending firmware activation requires Conventional Reset. | Firmware activation pending. |
| Command Specific | `10h` | Firmware Activation Requires NVM Subsystem Reset | Sanitize could not start because pending firmware activation requires NVM Subsystem Reset. | Firmware activation pending. |
| Command Specific | `11h` | Firmware Activation Requires Controller Level Reset | Sanitize could not start because pending firmware activation requires Controller Level Reset. | Firmware activation pending or unspecified reset-required fallback. |
| Command Specific | `20h` | Namespace is Write Protected | Command is prohibited while namespace is write protected. | Write-protected state. |
| Command Specific | `23h` | Sanitize Prohibited While Persistent Memory Region is Enabled | PMR enabled prohibits sanitize. | PMR enabled. |

## Common Status Conditions

| Status | Typical trigger |
|---|---|
| Invalid Field in Command | Unsupported `SANACT`, reserved action, invalid no-deallocate behavior, unsupported operation type. |
| Sanitize In Progress | Disallowed command processed while sanitize operation is in progress. |
| Sanitize Failed | Failed sanitize state blocks disallowed commands or invalid failure recovery path. |
| Command Not Supported for Queue in CMB | Implementation does not support Sanitize when Admin SQ/CQ is in Controller Memory Buffer. |
| Asymmetric Access Inaccessible / Persistent Loss | Multi-domain division prevents operation start. |
