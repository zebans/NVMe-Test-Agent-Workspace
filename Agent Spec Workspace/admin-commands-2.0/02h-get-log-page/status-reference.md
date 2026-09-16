# Get Log Page Status Reference

Source: NVMe Base Specification 2.0, section 5.16, Figure 268.

## Command Specific Status Values

| SCT | SC | Name | Meaning | Typical trigger |
|---|---|---|---|---|
| Command Specific | `09h` | Invalid Log Page | Requested LID is reserved, unsupported, or invalid for the controller. | `LID` not supported by Supported Log Pages, reserved LID, invalid log page selection. |
| Command Specific | `29h` | I/O Command Set Not Supported | Requested Command Set Identifier is not supported. | Command-set specific log with unsupported `CSI`. |

## Common Invalid Field Cases

| Case | Expected status family | Why |
|---|---|---|
| NSID invalid for controller/subsystem-scope log page | Invalid Field in Command | The selected log page scope does not accept that NSID. |
| `OT=1` but selected LID does not support index offset | Invalid Field in Command | `IOS=0` in Supported Log Pages for that LID. |
| Offset exceeds log page size or list entry count | Invalid Field in Command | Offset points outside defined payload. |
| Non-zero reserved command bits | Invalid Field in Command | Reserved command fields have no defined meaning. |
| LSP used for a LID that does not define LSP | Invalid Field in Command or reserved-field behavior | LSP is log-specific and reserved unless defined. |
| Invalid Domain ID / Endurance Group ID / NVM Set ID | Invalid Field in Command | CDW11 Log Specific Identifier selects a nonexistent object. |
| Persistent Event Log context action conflicts | Command Sequence Error or Invalid Field in Command | Example: read without context, establish context when one already exists, unsupported action. |

## Version Note

Base Spec 2.0 defines `Invalid Log Page` for invalid/reserved/unsupported LID. NVMe 1.3 and earlier behavior may report `Invalid Field in Command` for cases that Base 2.0 names as `Invalid Log Page`.
