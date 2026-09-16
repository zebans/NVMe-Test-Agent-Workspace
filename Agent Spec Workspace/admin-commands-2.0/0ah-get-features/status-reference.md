# Get Features Status Reference

Source: NVMe Base Specification 2.0, section 5.15 and feature-specific rules in section 5.27.1.

Figure 95 does not list a Get Features-specific command-specific status value. Get Features uses generic status behavior and feature-specific abort conditions.

## Common Invalid Cases

| Case | Expected status family | Why |
|---|---|---|
| Unsupported `FID` | Invalid Field in Command | Feature is not supported by controller. |
| Reserved `SEL` value | Invalid Field in Command | `SEL=100b`-`111b` are reserved. |
| Invalid namespace for namespace-specific feature | Invalid Field in Command | NSID does not select a valid namespace/scope. |
| Get Reservation Notification Mask with `NSID=FFFFFFFFh` | Invalid Field in Command | Feature requires a specific namespace for Get. |
| Get Reservation Persistence with `NSID=FFFFFFFFh` | Invalid Field in Command | Feature requires a specific namespace for Get. |
| Get Spinup Control when no rotational media endurance group exists | Invalid Field in Command | Feature not applicable. |
| Feature-specific invalid object ID | Invalid Field in Command | Invalid NVM Set ID, Endurance Group ID, interrupt vector, or command-set selector. |

## Supported Capabilities

Use `SEL=011b` to avoid guessing whether Set Features can save or change a feature. The returned CQE Dword 0 capability bits are the safest input for later Set Features test planning.
