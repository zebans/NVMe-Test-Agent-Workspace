# Abort Status Reference

| Status | Applies to | Meaning |
|---|---|---|
| `Command Abort Requested` | Target command completion | Target command was aborted due to Abort. |
| `Abort Command Limit Exceeded` | Abort command completion | Concurrent outstanding Abort commands exceeded Identify Controller `ACL`. |

## Result Bit

| Abort CQE DW0 bit 0 | Meaning |
|---|---|
| `0` | Command to abort was successfully aborted. |
| `1` | Command to abort was not aborted for any reason. |

