# Property Get Cross-Spec Boundary

## Owned By Fabrics Base / This Folder

| Area | Covered here |
|---|---|
| Capsule fields | `OPC`, `FCTYPE`, `ATTRIB`, `OFST`. |
| Property size selection | `ATTRIB` 4-byte and 8-byte encodings. |
| Response value layout | `VALUE` bytes for 4-byte and 8-byte reads. |
| Queue support | Not supported on I/O Queues. |
| Completion shell | `SQHD`, `CID`, `STS`. |

## Delegated Outside This Folder

| Area | Owner |
|---|---|
| Property meanings | Base property space section 3.1.3; canonical lookup: `..\..\..\controller-properties-2.0\README.md`. |
| Transport-specific mechanics | Applicable NVMe transport binding. |
| PyNVMe API call syntax | API layer such as `API_AGENTS.md`. |

## Boundary Rule

This folder tells what the Fabrics Base command capsule and response mean. It does not duplicate every property definition or transport binding behavior.
