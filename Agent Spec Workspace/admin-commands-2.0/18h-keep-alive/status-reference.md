# Keep Alive Status Reference

| Status | When it applies | Test/FW interpretation |
|---|---|---|
| Common command status | Keep Alive command completion. | Figure 95 does not list a Keep Alive-specific command status for opcode `18h`. |
| `Keep Alive Timer Expired` | Error Information / timeout condition, not Keep Alive command-specific status. | Indicates timer expiration; belongs to Keep Alive feature/timer behavior. |
| `Keep Alive Timeout Invalid` | Set Features / Connect KATO validation, not Keep Alive command-specific status. | Timeout configuration is invalid. |

