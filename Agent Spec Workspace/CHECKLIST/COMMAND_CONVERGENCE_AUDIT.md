# Command Convergence Audit

Date: 2026-06-24

Scope:

- Root reference files: `Base_Spec_2_0_Index.md`, `Admin_Command_Spec_Table.md`, `IO_Command_Spec_Table.md`, `Status_Code_Reference.md`
- `admin-commands-2.0`
- `io-commands-2.0`
- `fabrics-base-2.0/commands`
- `io-command-sets-2.0/key-value-command-set-1.0`
- `zns-command-set-1.1/commands`
- `zns-command-set-1.1/modified-nvm-commands`
- `mctp-base-1.3.1`
- `mctp-pcie-vdm-1.0.1`
- `mctp-smbus-i2c-1.1.0`

## Current Result

| Check | Result |
|---|---|
| Empty command markdown files | PASS |
| Missing command `COMMAND_CONTENT_AUDIT.md` | PASS |
| Empty command `COMMAND_CONTENT_AUDIT.md` | PASS |
| Missing non-empty `Status:` line in command audit | PASS |
| Broken local `.md` links inside command folders | PASS |
| Legacy expansion wording in command README files | PASS |
| Root source map and opcode/status reference status | PASS |

## Structure Generations

| Generation | Commands | Meaning |
|---|---|---|
| Canonical command reference | All command folders currently present in `admin-commands-2.0`, `io-commands-2.0`, `fabrics-base-2.0/commands`, `io-command-sets-2.0/nvm-command-set-1.0`, `io-command-sets-2.0/key-value-command-set-1.0`, `zns-command-set-1.1/commands`, and `zns-command-set-1.1/modified-nvm-commands` | Uses `command-facts.md`, `selector-reference.md` when useful, `field-reference.md`, `payload-reference.md`, `status-reference.md`, `restrictions.md` when useful, `cross-spec-boundary.md`, and `COMMAND_CONTENT_AUDIT.md` as needed. |
| Boundary-only canonical references | Base Get LBA Status opcode folder, NVMe-MI Send/Receive, Admin `7Fh` Fabrics opcode, vendor-specific Admin/I/O ranges | Intentionally thin command references because Base Spec identifies the opcode/range but delegates detailed semantics to another spec or vendor documentation. Get LBA Status now has an NVM-owned detailed folder. |
| Complete but legacy naming | None in the command folders covered by this audit | Old compact layouts have been removed from the current command-folder scope. |

## Root Reference Convergence

| File | Result | Notes |
|---|---|---|
| `Base_Spec_2_0_Index.md` | COMPLETE | Identifies the Base Spec source, major sections, command/status figures, active command folders, command-set layers, Fabrics, MI, and transport layers. |
| `Admin_Command_Spec_Table.md` | COMPLETE | Captures Figure 138 Admin opcode rows, data-transfer encoding, NSID notes, command-set-specific flags, and boundaries for Fabrics, Get LBA Status, and vendor-specific commands. |
| `IO_Command_Spec_Table.md` | COMPLETE | Captures Figure 390 common I/O opcode rows, data-transfer encoding, NSID rule, vendor-specific range, and I/O command-set-specific boundary. |
| `Status_Code_Reference.md` | COMPLETE | Captures Figures 92-99 as a global status dictionary. Per-command applicability remains in each command folder's `status-reference.md`. |

## Fixed During This Audit

| Path | Fix |
|---|---|
| `admin-commands-2.0/08h-abort` | Replaced compact legacy reference with canonical command identity, fields, behavior, and status facts. |
| `admin-commands-2.0/7fh-fabrics-commands` | Replaced compact legacy reference with canonical Base Admin opcode boundary facts. |
| `zns-command-set-1.1/modified-nvm-commands/09h-dataset-management/README.md` | Filled empty README with ZNS modification scope and read path. |
| `zns-command-set-1.1/modified-nvm-commands/19h-copy/COMMAND_CONTENT_AUDIT.md` | Filled empty audit with source, captured facts, and boundary notes. |
| Admin command README files | Replaced old legacy expansion wording with canonical expansion note. |
| `admin-commands-2.0/09h-set-features` | Converted from compact legacy layout to canonical command reference with FID selector, payload, field, status, and boundary files. |
| `admin-commands-2.0/0ah-get-features` | Converted from compact legacy layout to canonical command reference with FID/SEL selector, payload, returned-field, status, and boundary files. |
| `admin-commands-2.0/0dh-namespace-management` | Converted to canonical command reference with create/delete selector, create buffer, completion, status, restriction, and command-set boundary files. |
| `admin-commands-2.0/15h-namespace-attachment` | Converted to canonical command reference with attach/detach selector, Controller List payload, first-failure reporting, status, restriction, and boundary files. |
| `admin-commands-2.0/80h-format-nvm` | Converted from compact legacy layout to canonical command reference with destructive scope, field, restriction, status, and boundary files. |
| `admin-commands-2.0/84h-sanitize` | Converted from compact legacy layout to canonical command reference with sanitize action, field, restriction, status, and section 8.21 boundary files. |
| `io-commands-2.0/0dh-reservation-register` | Converted to canonical command reference with `RREGA`, `CPTPL`, `IEKEY`, key payload, status, and boundary files. |
| `io-commands-2.0/0eh-reservation-report` | Converted to canonical command reference with `NUMD`, `EDS`, Host Identifier format rules, returned payload fields, status, and boundary files. |
| `io-commands-2.0/11h-reservation-acquire` | Converted to canonical command reference with `RACQA`, `RTYPE`, `IEKEY`, key payload, status, and boundary files. |
| `io-commands-2.0/15h-reservation-release` | Converted to canonical command reference with `RRELA`, `RTYPE`, `IEKEY`, key payload, status, and boundary files. |
| `fabrics-base-2.0/commands/00h-property-set` | Converted to canonical command reference with `ATTRIB`, `OFST`, `VALUE`, completion, status, restriction, and boundary files. |
| `fabrics-base-2.0/commands/01h-connect` | Converted to canonical command reference with `RECFMT`, `QID`, `SQSIZE`, `CATTR`, Connect data/response, status, restriction, and boundary files. |
| `fabrics-base-2.0/commands/04h-property-get` | Converted to canonical command reference with `ATTRIB`, `OFST`, response `VALUE`, completion, status, restriction, and boundary files. |
| `fabrics-base-2.0/commands/05h-authentication-send` | Converted to canonical command reference with `SECP`, `SPSP0/1`, `TL`, security payload boundary, status, restriction, and boundary files. |
| `fabrics-base-2.0/commands/06h-authentication-receive` | Converted to canonical command reference with `SECP`, `SPSP0/1`, `AL`, returned payload boundary, status, retention, and boundary files. |
| `fabrics-base-2.0/commands/08h-disconnect` | Converted to canonical command reference with `RECFMT`, I/O Queue-only behavior, completion ordering, status, restriction, and boundary files. |
| `fabrics-base-2.0/commands/c0h-ffh-vendor-specific-fabrics` | Converted to canonical boundary reference for the vendor-specific `FCTYPE=C0h`-`FFh` range. |
| `zns-command-set-1.1/commands/79h-zone-management-send` | Converted to canonical command reference with `ZSA`, Select All, action/state matrix, payload, status, and boundary files. |
| `zns-command-set-1.1/commands/7ah-zone-management-receive` | Converted to canonical command reference with `ZRA`, Reporting Options, Partial Report, Zone Descriptor payload, status, and boundary files. |
| `zns-command-set-1.1/commands/7dh-zone-append` | Converted to canonical command reference with `ZSLBA`, `NLB`, `PIREMAP`, `ALBA`, status, and boundary files. |
| `zns-command-set-1.1/modified-nvm-commands/01h-write` | Converted to canonical ZNS overlay reference with zone boundary, write pointer, zone state, active/open resource, status, and boundary files. |
| `zns-command-set-1.1/modified-nvm-commands/08h-write-zeroes` | Converted to canonical ZNS overlay reference with zone boundary, write pointer, deallocation boundary, zone state, status, and boundary files. |
| `zns-command-set-1.1/modified-nvm-commands/19h-copy` | Converted to canonical ZNS overlay reference with source/destination zone boundary, destination write pointer, status, and boundary files. |
| `zns-command-set-1.1/modified-nvm-commands/00h-flush` | Converted to canonical ZNS overlay reference for the Offline zone status condition. |
| `zns-command-set-1.1/modified-nvm-commands/02h-read` | Converted to canonical ZNS overlay reference with Zone Boundary Error and Zone Is Offline status conditions. |
| `zns-command-set-1.1/modified-nvm-commands/04h-write-uncorrectable` | Converted to canonical ZNS overlay reference with zone boundary, write pointer, zone state, active/open resource, status, and boundary files. |
| `zns-command-set-1.1/modified-nvm-commands/05h-compare` | Converted to canonical ZNS overlay reference with ZNS status surface and NVM ownership boundary files. |
| `zns-command-set-1.1/modified-nvm-commands/09h-dataset-management` | Converted to canonical ZNS overlay reference for the Offline zone status condition and NVM payload boundary. |
| `zns-command-set-1.1/modified-nvm-commands/0ch-verify` | Converted to canonical ZNS overlay reference with Zone Boundary Error and Zone Is Offline status conditions. |
| `admin-commands-2.0/00h-delete-io-submission-queue` | Converted to canonical command reference with `QID`, Admin SQ exclusion, completion ordering, deleted-SQ completion behavior, status, and boundary files. |
| `admin-commands-2.0/01h-create-io-submission-queue` | Converted to canonical command reference with `PRP1`, `QSIZE`, `QID`, `CQID`, `QPRIO`, `PC`, `NVMSETID`, status, restriction, and boundary files. |
| `admin-commands-2.0/04h-delete-io-completion-queue` | Converted to canonical command reference with `QID`, Admin CQ exclusion, associated-SQ deletion ordering, status, restriction, and boundary files. |
| `admin-commands-2.0/05h-create-io-completion-queue` | Converted to canonical command reference with `PRP1`, `QSIZE`, `QID`, `IV`, `IEN`, `PC`, status, restriction, and boundary files. |
| `admin-commands-2.0/08h-abort` | Converted to canonical command reference with `SQID`, `CID`, `ACL`, Abort CQE DW0 bit 0, completion ordering, status, and boundary files. |
| `admin-commands-2.0/0ch-asynchronous-event-request` | Converted to canonical command reference with `AERL`, CQE DW0 fields, event type values, Figures 144-148 event information, status, and boundary files. |
| `admin-commands-2.0/10h-firmware-commit` | Converted to canonical command reference with `FS`, `CA`, `BPID`, Firmware Commit CQE DW0 `MUD`, status, restriction, and boundary files. |
| `admin-commands-2.0/11h-firmware-image-download` | Converted to canonical command reference with `DPTR`, `NUMD`, `OFST`, `FWUG`, image piece rules, status, restriction, and boundary files. |
| `admin-commands-2.0/14h-device-self-test` | Converted to canonical command reference with `NSID`, `STC`, command processing matrix, `DSTO`, Device Self-test Log interaction, status, and boundary files. |
| `admin-commands-2.0/18h-keep-alive` | Converted to canonical command reference with `KAS`, `TBKAS`, `KATO`, timer restart behavior, status boundary, and boundary files. |
| `admin-commands-2.0/19h-directive-send` | Converted to canonical command reference with `DPTR`, `NUMD`, `DSPEC`, `DTYPE`, `DOPER`, conditional `CDW12/CDW13`, status boundary, and boundary files. |
| `admin-commands-2.0/1ah-directive-receive` | Converted to canonical command reference with `DPTR`, `NUMD`, `DSPEC`, `DTYPE`, `DOPER`, receive length behavior, status, and boundary files. |
| `admin-commands-2.0/1dh-nvme-mi-send` | Converted to canonical boundary reference with opcode, data direction, Identify support-bit relationship, MI spec boundary, and audit files. |
| `admin-commands-2.0/1eh-nvme-mi-receive` | Converted to canonical boundary reference with opcode, data direction, Identify support-bit relationship, MI spec boundary, and audit files. |
| `admin-commands-2.0/1ch-virtualization-management` | Converted to canonical command reference with `CNTLID`, `RT`, `ACT`, `NR`, CQE `NRM`, status, restriction, and boundary files. |
| `admin-commands-2.0/20h-capacity-management` | Converted to canonical command reference with `Operation`, `Element Identifier`, `Capacity Lower/Upper`, operation effects, status, restriction, and boundary files. |
| `admin-commands-2.0/24h-lockdown` | Converted to canonical command reference with `OFI`, `IFC`, `PRHBT`, `SCP`, UUID Index, status, restriction, and boundary files. |
| `admin-commands-2.0/7ch-doorbell-buffer-config` | Converted to canonical command reference with `PRP1`, `PRP2`, Shadow Doorbell/EventIdx buffer layout, status, restriction, and boundary files. |
| `admin-commands-2.0/7fh-fabrics-commands` | Converted to canonical boundary reference for Admin opcode `7Fh` and routing to `fabrics-base-2.0/commands`. |
| `admin-commands-2.0/81h-security-send` | Converted to canonical command reference with `DPTR`, `SECP`, `SPSP`, `NSSF`, `TL`, Security Protocol `EAh`, status, and boundary files. |
| `admin-commands-2.0/82h-security-receive` | Converted to canonical command reference with `DPTR`, `SECP`, `SPSP`, `NSSF`, `AL`, Security Protocol `00h`/`EAh`, retention rule, status, and boundary files. |
| `admin-commands-2.0/86h-get-lba-status` | Converted to canonical boundary reference with opcode, data direction, NSID boundary, capability note, and NVM/ZNS command-set ownership. |
| `io-command-sets-2.0/nvm-command-set-1.0/admin-commands/86h-get-lba-status` | Added NVM-owned canonical detail folder with `SLBA`, `MNDW`, `ATYPE`, `RL`, returned descriptor list, `CMPC`, descriptor status bits, and LBA Status Information log relationship. |
| `io-command-sets-2.0/nvm-command-set-1.0/io-commands` | Added NVM-owned canonical detail folders for Write, Read, Write Uncorrectable, Compare, Write Zeroes, Dataset Management, Verify, and Copy. |
| `io-command-sets-2.0/key-value-command-set-1.0/io-commands` | Added KV-owned canonical detail folders for Store, Retrieve, List, Delete, and Exist, including key layout, value/buffer semantics, statuses, ordering rules, and command-set boundaries. |
| Root reference files | Marked root source map, Admin opcode table, I/O opcode table, and global status dictionary complete after aligning them to the current command-set, Fabrics, MI, PCIe, RDMA, and TCP layer layout. |
| `admin-commands-2.0/02h-get-log-page` | Expanded Base-owned LID payload lookup, including Media Unit Status and Supported Capacity Configuration nested descriptor offsets. |
| `admin-commands-2.0/09h-set-features` and `admin-commands-2.0/0ah-get-features` | Expanded high-value feature data-buffer layouts for Timestamp, Host Behavior Support, Host Metadata, and Host Identifier. |
| `admin-commands-2.0/0dh-namespace-management` | Expanded Base create buffer plus NVM, KV, and ZNS namespace-create field ownership and byte offsets. |
| `io-commands-2.0/0eh-reservation-report` | Expanded normal and extended registered-controller data structures from Figures 406-407. |
| `io-command-sets-2.0/*_COMMAND_SET_INDEX.md` | Added high-value command-set-specific Identify, feature, and Namespace Management field snapshots for NVM, ZNS, and KV. |
| `io-command-sets-2.0/nvm-command-set-1.0/NVM_PI_METADATA_REFERENCE.md` | Added shared NVM Protection Information and metadata reference covering `PRINFO`, `PRACT`, `PRCHK`, `STC`, `PIF`, `STS`, `LBSTM`, metadata placement, Storage Tag / Reference Tag split, command routing, and PI status mapping. |
| `mctp-base-1.3.1` | Added MCTP Base DSP0236 1.3.1 token-efficient source index, behavior reference, NVMe-MI boundary map, agent rules, and audit. |
| `mctp-pcie-vdm-1.0.1` | Added MCTP PCIe VDM DSP0238 1.0.1 token-efficient source index, behavior reference, agent rules, and audit. |
| `mctp-smbus-i2c-1.1.0` | Added MCTP SMBus/I2C DSP0237 1.1.0 token-efficient source index, behavior reference, agent rules, and audit. |
| `mctp-base-1.3.1/MCTP_COMMON_HEADER_REFERENCE.md` | Expanded MCTP Base Table 1 common packet/message fields for direct field lookup. |
| `mctp-base-1.3.1/MCTP_CONTROL_COMMAND_REFERENCE.md` | Expanded MCTP Control common fields, completion codes, Set/Get Endpoint ID, Get UUID, Get MCTP Version Support, Get Message Type Support, Prepare/Endpoint Discovery, Discovery Notify, and Transport Specific boundary. |
| `mctp-pcie-vdm-1.0.1/MCTP_PCIE_VDM_PACKET_REFERENCE.md` | Expanded PCIe VDM Table 1 packet fields, supported routing values, fixed field values, and Table 4 timing requirements. |
| `mctp-smbus-i2c-1.1.0/MCTP_SMBUS_I2C_PACKET_REFERENCE.md` | Expanded SMBus/I2C packet byte placement, command code `0x0F`, source/destination slave address, PEC, and bridge behavior. |
| `mctp-smbus-i2c-1.1.0/MCTP_SMBUS_I2C_TIMING_ADDRESS_REFERENCE.md` | Expanded SMBus/I2C packet/control timing, retry values, and reserved/well-known slave address rules. |
| `admin-commands-2.0/c0h-ffh-vendor-specific-admin-commands` | Converted to canonical boundary reference for vendor-specific Admin opcode range. |
| `io-commands-2.0/00h-flush` | Converted to canonical command reference with `NSID`, `VWC[2:1]`, volatile write cache behavior, status, and boundary files. |
| `io-commands-2.0/80h-ffh-vendor-specific-io-commands` | Converted to canonical boundary reference for vendor-specific I/O opcode range. |

## Recommended Next Priority

| Priority | Area | Why |
|---|---|---|
| 1 | RDMA/TCP behavior reference only when NVMe-oF transport testing needs it | RDMA/TCP currently have source-index and boundary layers; expand to behavior references if transport-level tests need field/rule lookup without reopening source. |
| 2 | Vendor-specific command folders only when vendor documentation exists | Vendor-specific ranges are intentionally boundary-only without vendor docs. |

## Boundary

This audit checks command-folder readability and structure health for the command folders currently present in scope. Boundary-only folders are marked complete when they accurately state the Base Spec boundary and refuse to invent fields, payloads, statuses, or behavior that belong to another specification or vendor documentation.
