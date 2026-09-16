# Sanitize Restrictions

Source: NVMe Base Specification 2.0, section 5.24 and section 8.21 boundary.

## Start Restrictions

| Restriction | Expected impact |
|---|---|
| Unsupported sanitize operation type selected. | Invalid Field in Command. |
| Any Persistent Memory Region is enabled in the NVM subsystem. | Sanitize Prohibited While Persistent Memory Region is Enabled. |
| Firmware activation with reset is pending. | Firmware activation reset-required status. |
| NVM subsystem is divided across multiple domains and operation cannot start. | Asymmetric Access Inaccessible or Persistent Loss. |
| Unsupported Sanitize command in Controller Memory Buffer path. | Command Not Supported for Queue in CMB. |

## In-Progress Behavior

| Event | Required behavior |
|---|---|
| Sanitize operation starts | Clear outstanding sanitize completion async events, update Sanitize Status log, abort disallowed commands, abort device self-test operations, suspend autonomous power state management, release stream identifiers. |
| Sanitize command starts operation | Sanitize Status log is updated before the command CQE is posted. |
| Disallowed command during sanitize | Aborted with Sanitize In Progress. |
| Operation fails | Disallowed commands may be aborted with Sanitize Failed until recovery. |

## Exit Failure Mode

| Prior state | Rule |
|---|---|
| No sanitize in progress and most recent sanitize did not fail | Exit Failure Mode completes successfully and performs no other action. |
| Failed unrestricted sanitize | Recovery may use subsequent sanitize in restricted/unrestricted mode or Exit Failure Mode. |
| Failed restricted sanitize | Recovery requires subsequent sanitize in restricted mode; Exit Failure Mode and unrestricted sanitize are aborted with Sanitize Failed. |

## Data Safety

If Sanitize command completes with any status other than Successful Completion, the controller shall not start the sanitize operation, shall not modify the Sanitize Status log page, and shall not alter user data for that command.
