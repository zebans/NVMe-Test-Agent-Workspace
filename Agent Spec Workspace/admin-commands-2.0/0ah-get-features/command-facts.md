# Get Features Command Facts

Source: NVMe Base Specification 2.0, section 5.15, Figures 191-195.

## Command Identity

| Item | Value |
|---|---|
| Command | Get Features |
| Admin opcode | `0Ah` |
| Data transfer | Controller to host |
| Data pointer | Used only when selected feature returns a data structure |
| NSID | Used; interpretation depends on selected feature |
| Primary selectors | `CDW10.FID`, `CDW10.SEL` |

## Command Dwords

| Dword | Bits | Field | Meaning | Test/FW impact |
|---|---:|---|---|---|
| DPTR | all | Data Pointer | Start of returned feature data buffer. | Ignored when selected feature does not return a data structure. |
| CDW10 | 10:08 | `SEL` | Selects current, default, saved, or supported-capabilities value. | Determines returned value type. |
| CDW10 | 07:00 | `FID` | Feature Identifier. | Main feature selector. |
| CDW11 | all | Feature-specific | Feature-specific selector/input. | Used by features such as Host Metadata. |
| CDW14 | 06:00 | UUID Index | Selects UUID for vendor-specific features when supported. | Do not use unless supported for selected vendor-specific `FID`. |

## Completion

- If `SEL != 011b`, CQE Dword 0 may contain feature-dependent information.
- If the feature returns a data buffer, the returned data buffer is feature-specific.
- If `SEL=011b`, CQE Dword 0 contains supported-capabilities bits: Changeable, Namespace Specific, and Saveable.
