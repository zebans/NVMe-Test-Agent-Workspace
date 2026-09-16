# Command Status Matrix - NVMe Base Spec 2.0

This file maps commands to status codes that NVMe Base Specification 2.0 explicitly associates with those commands in global status tables or command sections.

Primary source:

```text
NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

Source anchors:

- Figure 94: Generic Command Status Values
- Figure 95: Command Specific Status Values
- Figure 96: Command Specific Status Values, I/O Commands
- Figure 97: Command Specific Status Values, Fabrics Commands
- Command-specific sections and figures

This matrix is not a complete test oracle. Use command-specific reference files for selector-specific behavior and restrictions.

## Matrix Rules

- `SCT=0h` means Generic Command Status.
- `SCT=1h` means Command Specific Status.
- `SCT=2h` means Media and Data Integrity Errors.
- `SCT=3h` means Path Related Status.
- Include only status values explicitly tied to a command by Base Spec 2.0.
- Do not infer command applicability from common sense or implementation behavior.

## Admin Command Status Matrix

| Command | Opcode | Explicitly Associated Status Values | Source |
|---|---:|---|---|
| Create I/O Submission Queue | `01h` | `SCT=1h/SC=00h` Completion Queue Invalid; `01h` Invalid Queue Identifier; `02h` Invalid Queue Size | Figure 95 |
| Create I/O Completion Queue | `05h` | `SCT=1h/SC=01h` Invalid Queue Identifier; `02h` Invalid Queue Size; `08h` Invalid Interrupt Vector | Figure 95 |
| Delete I/O Completion Queue | `04h` | `SCT=1h/SC=01h` Invalid Queue Identifier; `0Ch` Invalid Queue Deletion | Figure 95 |
| Delete I/O Submission Queue | `00h` | `SCT=1h/SC=01h` Invalid Queue Identifier | Figure 95 |
| Abort | `08h` | `SCT=1h/SC=03h` Abort Command Limit Exceeded | Figure 95 |
| Asynchronous Event Request | `0Ch` | `SCT=1h/SC=05h` Asynchronous Event Request Limit Exceeded | Figure 95 |
| Firmware Commit | `10h` | `SCT=1h/SC=06h` Invalid Firmware Slot; `07h` Invalid Firmware Image; `0Bh` Firmware Activation Requires Conventional Reset; `10h` Firmware Activation Requires NVM Subsystem Reset; `11h` Firmware Activation Requires Controller Level Reset; `12h` Firmware Activation Requires Maximum Time Violation; `13h` Firmware Activation Prohibited; `14h` Overlapping Range; `1Eh` Boot Partition Write Prohibited | Figure 95 |
| Firmware Image Download | `11h` | `SCT=1h/SC=14h` Overlapping Range | Figure 95 |
| Format NVM | `80h` | `SCT=1h/SC=0Ah` Invalid Format | Figure 95 |
| Get Log Page | `02h` | `SCT=1h/SC=09h` Invalid Log Page; `29h` I/O Command Set Not Supported; `90h` Discover Restart for Fabrics Discovery Log Page | Figure 95; Figure 97; Figure 268 |
| Identify | `06h` | `SCT=0h/SC=02h` Invalid Field in Command for unsupported CNS; `SCT=1h/SC=2Ch` Invalid I/O Command Set when namespace is not associated with an I/O Command Set supporting the CNS value | Section 5.17; Figure 95 |
| Namespace Management | `0Dh` | `SCT=1h/SC=0Ah` Invalid Format; `15h` Namespace Insufficient Capacity; `16h` Namespace Identifier Unavailable; `1Bh` Thin Provisioning Not Supported; `24h` ANA Group Identifier Invalid; `29h` I/O Command Set Not Supported; `2Ch` Invalid I/O Command Set | Figure 95 |
| Namespace Attachment | `15h` | `SCT=1h/SC=18h` Namespace Already Attached; `19h` Namespace Is Private; `1Ah` Namespace Not Attached; `1Ch` Controller List Invalid; `25h` ANA Attach Failed; `27h` Namespace Attachment Limit Exceeded; `29h` I/O Command Set Not Supported; `2Ah` I/O Command Set Not Enabled | Figure 95 |
| Set Features | `09h` | `SCT=1h/SC=0Dh` Feature Identifier Not Saveable; `0Eh` Feature Not Changeable; `0Fh` Feature Not Namespace Specific; `14h` Overlapping Range; `2Bh` I/O Command Set Combination Rejected | Figure 95 |
| Device Self-test | `14h` | `SCT=1h/SC=1Dh` Device Self-test In Progress | Figure 95 |
| Capacity Management | `20h` | `SCT=1h/SC=26h` Insufficient Capacity; `2Dh` Identifier Unavailable | Figure 95 |
| Lockdown | `24h` | `SCT=1h/SC=28h` Prohibition of Command Execution Not Supported | Figure 95; Figure 293 |
| Sanitize | `84h` | `SCT=1h/SC=0Bh` Firmware Activation Requires Conventional Reset; `10h` Firmware Activation Requires NVM Subsystem Reset; `11h` Firmware Activation Requires Controller Level Reset; `23h` Sanitize Prohibited While Persistent Memory Region is Enabled | Figure 95 |
| Virtualization Management | `1Ch` | `SCT=1h/SC=1Fh` Invalid Controller Identifier; `20h` Invalid Secondary Controller State; `21h` Invalid Number of Controller Resources; `22h` Invalid Resource Identifier | Figure 95 |

## Common Generic Status Values

The following generic status values are not listed per command in this matrix unless the command section explicitly ties them to that command. They may still apply according to common command rules:

- `SCT=0h/SC=00h` Successful Completion
- `SCT=0h/SC=01h` Invalid Command Opcode
- `SCT=0h/SC=02h` Invalid Field in Command
- `SCT=0h/SC=0Bh` Invalid Namespace or Format
- `SCT=0h/SC=0Ch` Command Sequence Error
- `SCT=0h/SC=24h` Admin Command Media Not Ready, only for Admin commands and conditions allowed by Base Spec 2.0

## I/O Command Status Notes

Base Spec 2.0 defines common I/O commands in Figure 390. I/O Command Set-specific status values are summarized in `Status_Code_Reference.md`, Figure 96. Command-specific applicability beyond the common commands may require the applicable I/O Command Set specification and is not expanded in this Base Spec-only pass.

