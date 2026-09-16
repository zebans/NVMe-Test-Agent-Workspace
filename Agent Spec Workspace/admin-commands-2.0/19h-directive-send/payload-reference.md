# Directive Send Payload Reference

| Area | Payload | Meaning |
|---|---|---|
| Command data buffer | Directive-dependent data | Transferred from host to controller. |
| Completion | CQE on Admin Completion Queue | Reports command status. |

## Operation Payload Map

| `DTYPE` | `DOPER` | Payload / return surface | Key fields |
|---:|---:|---|---|
| `00h` | `01h` | No command data buffer. | `CDW12.DTYPE` selects directive to enable/disable; `CDW12.ENDIR` enables when set and disables when clear. |
| `01h` | `01h` | No command data buffer. | `DSPEC` is the Stream Identifier to release. |
| `01h` | `02h` | No command data buffer. | Releases stream resources associated with the namespace and Host Identifier model. |
