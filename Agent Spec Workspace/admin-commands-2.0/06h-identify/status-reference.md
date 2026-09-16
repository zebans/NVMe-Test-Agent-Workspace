# Identify - Status Reference

Primary source: NVMe Base Specification 2.0, sections 3.3.3.2, 3.3.3.2.1, 5.17, and Figure 95.

Purpose: define Identify completion and status behavior. Use this when a test, firmware trace, or assertion needs the expected status for a CNS/NSID/CSI/UUID condition.

## Command Completion

Upon completion of the Identify command, the controller posts a completion queue entry to the Admin Completion Queue.

The Identify command section does not define command-specific CQE DW0 or DW1 fields. The common CQE layout applies.

| CQE Field | Source | Notes |
|---|---|---|
| DW0 | Figure 89 | Command specific; no Identify-specific meaning defined in section 5.17. |
| DW1 | Figure 89 | Command specific; no Identify-specific meaning defined in section 5.17. |
| DW2 | Figure 90 | SQ Identifier and SQ Head Pointer. |
| DW3 | Figure 91 / Figure 92 | Status Field, Phase Tag, Command Identifier. |

## Explicit Identify Status Behavior

| SCT | SC | Status | Condition | Source |
|---|---:|---|---|---|
| Generic Command Status (`0h`) | `02h` | Invalid Field in Command | Controller does not support the specified CNS value. | Section 5.17 |
| Command Specific Status (`1h`) | `2Ch` | Invalid I/O Command Set | Specified namespace is not associated with an I/O Command Set that supports the specified Identify CNS value. | Section 5.17; Figure 95 |
| Generic Command Status (`0h`) | `02h` | Invalid Field in Command | CNS `05h`: namespace's I/O Command Set does not support the requested Identify Namespace structure specified by CSI. | Section 5.17.2.5 |
| Generic Command Status (`0h`) | `0Bh` | Invalid Namespace or Format | CNS `05h`: Namespace Management not supported and NSID is `FFFFFFFFh`. | Section 5.17.2.5 |
| Generic Command Status (`0h`) | `02h` | Invalid Field in Command | CNS `06h`: host requests data for an I/O Command Set the controller does not support. | Section 5.17.2.6 |
| Generic Command Status (`0h`) | `02h` | Invalid Field in Command | CNS `07h`: CSI is not supported or not enabled. | Section 5.17.2.7 |
| Generic Command Status (`0h`) | `0Bh` | Invalid Namespace or Format | CNS `07h`: controller should abort if NSID is `FFFFFFFEh` or `FFFFFFFFh`. | Section 5.17.2.7 |
| Generic Command Status (`0h`) | `0Bh` | Invalid Namespace or Format | CNS `08h`: Namespace Management not supported and NSID is `FFFFFFFFh`. | Section 5.17.2.8 |
| Generic Command Status (`0h`) | `0Bh` | Invalid Namespace or Format | CNS `10h`: controller should abort if NSID is `FFFFFFFEh` or `FFFFFFFFh`. | Section 5.17.2.9 |
| Command Specific Status (`1h`) | `2Ch` | Invalid I/O Command Set | CNS `11h`: namespace is not associated with an I/O Command Set that specifies logical blocks. | Section 5.17.2.10; Figure 95 |
| Generic Command Status (`0h`) | `0Bh` | Invalid Namespace or Format | CNS `11h`: invalid NSID, or NSID `FFFFFFFFh` should abort. | Section 5.17.2.10 |
| Generic Command Status (`0h`) | `02h` | Invalid Field in Command | CNS `12h`: NSID is `FFFFFFFFh`; controller should abort. | Section 5.17.2.11 |
| Command Specific Status (`1h`) | `2Ch` | Invalid I/O Command Set | CNS `16h`: CSI is not associated with an I/O Command Set that supports Namespace Granularity List. | Section 5.17.2.15; Figure 95 |
| Generic Command Status (`0h`) | `00h` | Successful Completion | CNS `19h`: CDW11.ENDGID greater than ENDGIDMAX returns an empty Endurance Group List. | Section 5.17.2.18 |
| Generic Command Status (`0h`) | `02h` | Invalid Field in Command | CNS `1Ah`: CSI is not supported by the controller. | Section 5.17.2.19 |
| Generic Command Status (`0h`) | `0Bh` | Invalid Namespace or Format | CNS `1Ah`: controller should abort if NSID is `FFFFFFFEh` or `FFFFFFFFh`. | Section 5.17.2.19 |
| Generic Command Status (`0h`) | `02h` | Invalid Field in Command | CNS `1Bh`: namespace's I/O Command Set does not support the requested CSI-specific structure. | Section 5.17.2.20 |
| Generic Command Status (`0h`) | `0Bh` | Invalid Namespace or Format | CNS `1Bh`: invalid NSID, or NSID `FFFFFFFFh` should abort. | Section 5.17.2.20 |

## UUID Index Status Behavior

If the controller supports selection of a UUID by Identify and CDW14 specifies a UUID Index, Figure 477 defines the UUID Index field.

The command shall be aborted with `Invalid Field in Command` if:

- the controller does not support the UUID specified by the UUID Index for the specified information;
- the UUID entry selected by the UUID Index is cleared to `0h`; or
- the UUID entry selected by the UUID Index is the NVMe Invalid UUID.

## Common Status Context

| SCT | SC | Status | Relevance |
|---|---:|---|---|
| Generic Command Status (`0h`) | `00h` | Successful Completion | Common successful completion status. |
| Generic Command Status (`0h`) | `02h` | Invalid Field in Command | Explicitly used by Identify for unsupported CNS and invalid UUID Index cases. |
| Generic Command Status (`0h`) | `0Bh` | Invalid Namespace or Format | May arise from common NSID rules when an invalid NSID is specified for a command that uses NSID, unless otherwise specified. |
| Command Specific Status (`1h`) | `2Ch` | Invalid I/O Command Set | Explicitly used when namespace/CSI association does not support the requested Identify CNS behavior. |

## Notes

- If multiple status codes apply, Base Spec 2.0 says the controller selects the status code returned unless otherwise specified.
- Command-set-specific Identify payload behavior is not expanded in this Base Spec-only file.
- For global status definitions, see `..\..\Status_Code_Reference.md`.
- For command-to-status mapping, see `..\..\Command_Status_Matrix.md`.

