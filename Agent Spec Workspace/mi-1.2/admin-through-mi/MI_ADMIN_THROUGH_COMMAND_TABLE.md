# MI Admin-Through Command Table

Status: `FIELD-COMPLETE + ROUTING-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 6, Figure 114.

Figure 114 lists NVMe Admin Commands that are Mandatory, Optional, or Prohibited for the out-of-band mechanism on an NVMe Storage Device and an NVMe Enclosure.

Legend:

| Symbol | Meaning |
|---|---|
| `M` | Mandatory |
| `O` | Optional |
| `P` | Prohibited from being supported |

Important source note: the local converted MI markdown has visible table extraction damage around Figure 114. The support values below follow Figure 114, while opcode values are normalized against the Base Admin opcode table to avoid carrying extraction mistakes such as duplicate or swapped opcodes.

## Support Table

| Admin Opcode | Admin Command | Storage Device O/M/P | Enclosure O/M/P | Reference spec | Base/Admin reference | Notes |
|---|---|---|---|---|---|---|
| `00h` | Delete I/O Submission Queue | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\00h-delete-io-submission-queue\README.md` | Queue-management command prohibited over OOB MI. |
| `01h` | Create I/O Submission Queue | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\01h-create-io-submission-queue\README.md` | Queue-management command prohibited over OOB MI. |
| `02h` | Get Log Page | M | O | NVMe Base Specification | `..\..\admin-commands-2.0\02h-get-log-page\README.md` | Log page support is further constrained by MI Figure 121. |
| `04h` | Delete I/O Completion Queue | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\04h-delete-io-completion-queue\README.md` | Queue-management command prohibited over OOB MI. |
| `05h` | Create I/O Completion Queue | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\05h-create-io-completion-queue\README.md` | Queue-management command prohibited over OOB MI. |
| `06h` | Identify | M | O | NVMe Base Specification | `..\..\admin-commands-2.0\06h-identify\README.md` | Common low-interference inventory/query command. |
| `08h` | Abort | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\08h-abort\README.md` | Prohibited over OOB MI. |
| `09h` | Set Features | O | O | NVMe Base Specification | `..\..\admin-commands-2.0\09h-set-features\README.md` | Feature support is further constrained by MI Figures 123-125. |
| `0Ah` | Get Features | M | O | NVMe Base Specification | `..\..\admin-commands-2.0\0ah-get-features\README.md` | Feature support is further constrained by MI Figures 123-125. |
| `0Ch` | Asynchronous Event Request | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\0ch-asynchronous-event-request\README.md` | Prohibited over OOB MI. |
| `0Dh` | Namespace Management | O | P | NVMe Base Specification | `..\..\admin-commands-2.0\0dh-namespace-management\README.md` | Enclosure prohibited. |
| `10h` | Firmware Commit | O | O | NVMe Base Specification | `..\..\admin-commands-2.0\10h-firmware-commit\README.md` | Optional over OOB MI. |
| `11h` | Firmware Image Download | O | O | NVMe Base Specification | `..\..\admin-commands-2.0\11h-firmware-image-download\README.md` | Optional over OOB MI. |
| `14h` | Device Self-test | O | O | NVMe Base Specification | `..\..\admin-commands-2.0\14h-device-self-test\README.md` | Optional over OOB MI. |
| `15h` | Namespace Attachment | O | P | NVMe Base Specification | `..\..\admin-commands-2.0\15h-namespace-attachment\README.md` | Enclosure prohibited. |
| `18h` | Keep Alive | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\18h-keep-alive\README.md` | Prohibited over OOB MI. |
| `19h` | Directive Send | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\19h-directive-send\README.md` | Prohibited over OOB MI. |
| `1Ah` | Directive Receive | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\1ah-directive-receive\README.md` | Prohibited over OOB MI. |
| `1Ch` | Virtualization Management | O | O | NVMe Base Specification | `..\..\admin-commands-2.0\1ch-virtualization-management\README.md` | Optional over OOB MI. |
| `1Dh` | NVMe-MI Send | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\1dh-nvme-mi-send\README.md` | In-band tunnel command; prohibited as an OOB Admin-through-MI command. |
| `1Eh` | NVMe-MI Receive | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\1eh-nvme-mi-receive\README.md` | In-band tunnel command; prohibited as an OOB Admin-through-MI command. |
| `20h` | Capacity Management | O | P | NVMe Base Specification | `..\..\admin-commands-2.0\20h-capacity-management\README.md` | Enclosure prohibited. |
| `24h` | Lockdown | O | O | NVMe Base Specification | `..\..\admin-commands-2.0\24h-lockdown\README.md` | Optional over OOB MI. |
| `7Ch` | Doorbell Buffer Config | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\7ch-doorbell-buffer-config\README.md` | Prohibited over OOB MI. |
| `7Fh` | Fabrics Commands | P | P | NVMe Base Specification | `..\..\admin-commands-2.0\7fh-fabrics-commands\README.md` | Prohibited over OOB MI. |
| `80h` | Format NVM | O | P | NVMe Base Specification | `..\..\admin-commands-2.0\80h-format-nvm\README.md` | Enclosure prohibited; sanitize/format interaction also uses MI Figure 122. |
| `81h` | Security Send | O | P | NVMe Base Specification | `..\..\admin-commands-2.0\81h-security-send\README.md` | Enclosure prohibited. |
| `82h` | Security Receive | O | P | NVMe Base Specification | `..\..\admin-commands-2.0\82h-security-receive\README.md` | Enclosure prohibited. |
| `84h` | Sanitize | O | O | NVMe Base Specification | `..\..\admin-commands-2.0\84h-sanitize\README.md` | Optional over OOB MI; command availability during sanitize uses MI Figure 122. |
| `86h` | Get LBA Status | O | P | NVM Command Set Specification | `..\..\admin-commands-2.0\86h-get-lba-status\README.md` | Enclosure prohibited; detailed command semantics are delegated to the NVM command set layer. |
| `C0h`-`FFh` | Vendor Specific | O | O | NVMe Base Specification | `..\..\admin-commands-2.0\c0h-ffh-vendor-specific-admin-commands\README.md` | Requires vendor documentation for exact behavior. |

## Lookup Rule

Use this table for OOB MI support and routing only:

```text
Admin-through-MI support question
-> MI_ADMIN_THROUGH_COMMAND_TABLE.md
-> command-format-reference.md / status-boundary-reference.md for MI wrapper behavior
-> linked admin-commands-2.0 folder for Admin command semantics
```

