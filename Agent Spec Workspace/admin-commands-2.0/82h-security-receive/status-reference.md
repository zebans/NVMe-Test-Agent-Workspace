# Security Receive Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| `Invalid Field in Command` | Unsupported Security Protocol value is specified. | `SECP` is not supported for Security Receive. |
| Common status / protocol-specific status | Other failures. | Base Spec does not define a Security Receive-specific command status in Figure 95. |

