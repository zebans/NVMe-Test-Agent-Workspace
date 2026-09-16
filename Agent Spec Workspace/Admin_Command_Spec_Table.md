# Admin Command Spec Table - NVMe Base Spec 2.0

This table is a root-level spec index for Admin commands defined by NVMe Base Specification 2.0.

Primary source:

```text
NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

Source anchor: Section 5 and Figure 138, "Opcodes for Admin Commands".

This table is not a test flow and does not define implementation API usage.

## Data Transfer Encoding

Figure 138 note 3 defines command data transfer direction:

| Encoding | Meaning |
|---|---|
| `00b` | No data transfer |
| `01b` | Host to controller |
| `10b` | Controller to host |
| `11b` | Bidirectional |

## NSID Notes

Figure 138 note 2 says a subset of commands use NSID. If NSID is used, `FFFFFFFFh` is supported unless a Figure 138 footnote indicates the command does not support it or supports it only under specific conditions. If NSID is not used, the field is cleared to `0h`.

## Admin Commands

| Opcode | Command | Section | NSID Usage | Data Transfer | Command Set Specific | Base Spec Notes |
|---|---|---:|---|---|---|---|
| `00h` | Delete I/O Submission Queue | 5.7 | No | `00b` no data | No | Opcodes not listed are reserved. |
| `01h` | Create I/O Submission Queue | 5.5 | No | `01b` host to controller | No | Creates I/O SQ. |
| `02h` | Get Log Page | 5.16 | Yes | `10b` controller to host | No | Log page details depend on LID and related sections. |
| `04h` | Delete I/O Completion Queue | 5.6 | No | `00b` no data | No | Deletes I/O CQ. |
| `05h` | Create I/O Completion Queue | 5.4 | No | `01b` host to controller | No | Creates I/O CQ. |
| `06h` | Identify | 5.17 | Depends on CNS | `10b` controller to host | No | Figure 138 note 6: NSID use depends on CNS value as described by Identify. |
| `08h` | Abort | 5.1 | No | `00b` no data | No | Aborts a command by SQID/CID. |
| `09h` | Set Features | 5.27 | Yes | `01b` host to controller | No | Feature-specific fields and data are selected by `FID`. |
| `0Ah` | Get Features | 5.15 | Yes | `10b` controller to host | No | Feature-specific returned values/data are selected by `FID` and `SEL`. |
| `0Ch` | Asynchronous Event Request | 5.2 | No | `00b` no data | No | Completes when an asynchronous event is reported. |
| `0Dh` | Namespace Management | 5.23 | Yes | `01b` host to controller | No | Namespace create data may be I/O Command Set-specific. |
| `10h` | Firmware Commit | 5.12 | No | `00b` no data | No | Firmware activation behavior may require reset. |
| `11h` | Firmware Image Download | 5.13 | No | `01b` host to controller | No | Downloads firmware image data. |
| `14h` | Device Self-test | 5.9 | Yes, restricted | `00b` no data | No | Figure 138 note 4: does not support NSID `FFFFFFFFh`. |
| `15h` | Namespace Attachment | 5.22 | Yes | `01b` host to controller | No | Attach/detach namespace to controller list. |
| `18h` | Keep Alive | 5.18 | No | `00b` no data | No | Keep Alive command. |
| `19h` | Directive Send | 5.11 | Yes, conditional | `01b` host to controller | No | Figure 138 note 5: NSID `FFFFFFFFh` support depends on Directive Operation. |
| `1Ah` | Directive Receive | 5.10 | Yes, conditional | `10b` controller to host | No | Figure 138 note 5: NSID `FFFFFFFFh` support depends on Directive Operation. |
| `1Ch` | Virtualization Management | 5.28 | No | `00b` no data | No | Virtualization resource management. |
| `1Dh` | NVMe-MI Send | 5.21 | No | `01b` host to controller | No | NVMe-MI Send Admin command. |
| `1Eh` | NVMe-MI Receive | 5.20 | No | `10b` controller to host | No | NVMe-MI Receive Admin command. |
| `20h` | Capacity Management | 5.3 | No | `00b` no data | No | Capacity management command. |
| `24h` | Lockdown | 5.19 | No | `00b` no data | No | Command and feature lockdown. |
| `7Ch` | Doorbell Buffer Config | 5.8 | No | `00b` no data | No | Shadow doorbell/EventIdx buffer configuration. |
| `7Fh` | Fabrics Commands | Section 6 | Fabrics-specific | `11b` bidirectional | No | Figure 138 note 9: all Fabrics commands use opcode `7Fh`; use `fabrics-base-2.0` for `FCTYPE` command identity. |
| `80h` | Format NVM | 5.14 | Yes | `00b` no data | No | Format behavior can affect namespaces and command processing. |
| `81h` | Security Send | 5.26 | Security-protocol-specific | `01b` host to controller | No | Figure 138 note 7: NSID use is Security Protocol-specific. |
| `82h` | Security Receive | 5.25 | Security-protocol-specific | `10b` controller to host | No | Figure 138 note 7: NSID use is Security Protocol-specific. |
| `84h` | Sanitize | 5.24 | No | `00b` no data | No | Sanitization restrictions apply; see section 8.21 and Figure 139. |
| `86h` | Get LBA Status | Base Spec lists opcode; command-set-specific | Yes, restricted | `10b` controller to host | NVM, ZNS | Figure 138 note 4: does not support NSID `FFFFFFFFh`; detailed definition is command-set-specific. |
| `C0h`-`FFh` | Vendor Specific Admin Commands | 8.23 / vendor-specific | Vendor-specific | Encoded by opcode bits / vendor-specific | Vendor-specific | Vendor-specific commands follow Figure 138 data transfer convention. |

## Figure 138 Notes Summary

- Opcodes not listed are reserved.
- NSID `FFFFFFFFh` support is command-dependent and governed by Figure 138 footnotes.
- Data transfer encoding is defined by note 3.
- `Get LBA Status` and `Device Self-test` do not support NSID `FFFFFFFFh`.
- Directive Send/Receive NSID `FFFFFFFFh` support depends on Directive Operation.
- Identify NSID use depends on CNS.
- Security Send/Receive NSID use is Security Protocol-specific.
- `No`, `A`, `NVM`, and `ZNS` identify whether the command is I/O Command Set-specific.
- All Fabrics commands use opcode `7Fh`; the specific Fabrics command is selected by `FCTYPE` and indexed in `fabrics-base-2.0`.
