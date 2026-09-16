# Keep Alive Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| Command-specific fields | Reserved | Keep Alive command has no command-specific input fields. | Host should clear. | Reserved-field validation. |
| Identify Controller | `KAS` | Keep Alive Timer granularity. | `0h` means Keep Alive feature is not supported. | Timeout interpretation. |
| Identify Controller | `TBKAS` | Traffic Based Keep Alive Support. | `0` command-based; `1` traffic-based restart behavior supported. | Timer restart model. |
| Feature / Connect | `KATO` | Keep Alive Timeout value. | `0h` disables timer unless transport requires Keep Alive. | Timer enablement and timeout interval. |

