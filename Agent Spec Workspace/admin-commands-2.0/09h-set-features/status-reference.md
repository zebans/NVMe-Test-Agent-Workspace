# Set Features Status Reference

Source: NVMe Base Specification 2.0, section 5.27, Figure 370, and global command-specific status table.

## Command Specific Status Values

| SCT | SC | Name | Meaning | Typical trigger |
|---|---|---|---|---|
| Command Specific | `0Dh` | Feature Identifier Not Saveable | Selected `FID` does not support a saveable value. | `SV=1` for a non-saveable feature. |
| Command Specific | `0Eh` | Feature Not Changeable | Selected feature value is not changeable. | Attempting to change non-changeable feature value. |
| Command Specific | `0Fh` | Feature Not Namespace Specific | Selected `FID` is not namespace specific. | Namespace-specific access pattern used for controller-wide feature. |
| Command Specific | `14h` | Overlapping Range | Command-set specific range overlap. | I/O command set specific feature/range overlap. |
| Command Specific | `2Bh` | I/O Command Set Combination Rejected | Controller rejected requested I/O Command Set Combination. | Invalid or unsupported `FID=19h` `IOCSCI`. |

## Common Invalid Field Cases

| Case | Expected status family | Why |
|---|---|---|
| Unsupported `FID` | Invalid Field in Command | Feature is not supported by controller. |
| Reserved `FID` | Invalid Field in Command | No Base-defined feature. |
| Reserved feature-specific selector | Invalid Field in Command | Feature-specific reserved values have no behavior. |
| Invalid namespace for namespace-specific feature | Invalid Field in Command | NSID does not select a valid namespace/scope. |
| Feature-specific invalid object ID | Invalid Field in Command | Invalid ENDGID, NVM Set ID, interrupt vector, or I/O command set combination. |
| Command sequence violation | Command Sequence Error | Example: Number of Queues after I/O queues exist; HMB enable while already enabled; Fabrics Host Identifier change. |
