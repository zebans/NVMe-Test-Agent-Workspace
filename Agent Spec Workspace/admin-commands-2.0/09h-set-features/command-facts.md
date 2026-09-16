# Set Features Command Facts

Source: NVMe Base Specification 2.0, section 5.27, Figures 313-315.

## Command Identity

| Item | Value |
|---|---|
| Command | Set Features |
| Admin opcode | `09h` |
| Data transfer | Host to controller |
| Data pointer | Used only when selected feature uses a data structure |
| NSID | Used; interpretation depends on selected feature |
| Primary selector | `CDW10.FID` |

## Command Dwords

| Dword | Bits | Field | Meaning | Test/FW impact |
|---|---:|---|---|---|
| DPTR | all | Data Pointer | Start of feature data buffer. If PRPs are used, buffer shall not be a PRP List and may not cross more than one page boundary. | Only valid for features with memory-buffer attributes. |
| CDW10 | 31 | `SV` | Save bit. Requests persistence through all power states and resets. | If feature is not saveable, `SV=1` aborts with `Feature Identifier Not Saveable`. |
| CDW10 | 30:08 | Reserved | Reserved. | Negative tests for reserved command bits. |
| CDW10 | 07:00 | `FID` | Feature Identifier. | Main dispatch selector. See [selector-reference.md](selector-reference.md). |
| CDW11 | all | Feature-specific | Feature-specific attributes. | Meaning depends on `FID`; see [field-reference.md](field-reference.md). |
| CDW12 | all | Feature-specific | Feature-specific attributes. | Used by Host Memory Buffer and some feature families. |
| CDW13 | all | Feature-specific | Feature-specific attributes. | Used by Host Memory Buffer and some feature families. |
| CDW14 | 06:00 | UUID Index | Selects UUID for vendor-specific features when supported. | Do not use unless UUID selection is supported for the selected vendor-specific `FID`. |
| CDW15 | all | Feature-specific | Feature-specific attributes. | Used by Host Memory Buffer and some feature families. |

## Required Behavior

- Unsupported `FID` aborts with `Invalid Field in Command`.
- If `SV=1` is used for a feature that is not saveable, the command aborts with `Feature Identifier Not Saveable`.
- If a feature is not changeable and requested value differs from existing value, the command aborts with `Feature Not Changeable`.
- If a feature is not changeable and requested value equals existing value, the controller may complete successfully or abort with `Feature Not Changeable`.
- If Set Features completes successfully, commands submitted after completion shall use the new setting.
- Commands already submitted or in execution when the feature changes may or may not use the new setting.
- Host software should rediscover, re-enumerate, or re-initialize capabilities affected by the changed feature.
