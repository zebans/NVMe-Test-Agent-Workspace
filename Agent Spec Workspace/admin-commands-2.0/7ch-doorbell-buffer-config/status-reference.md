# Doorbell Buffer Config Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Invalid Field in Command` | Shadow Doorbell buffer or EventIdx buffer memory address is invalid. | Buffer pointer/alignment/address validation failed. |
| Common command status | Other command processing failures. | Figure 95 does not list a Doorbell Buffer Config-specific status. |

