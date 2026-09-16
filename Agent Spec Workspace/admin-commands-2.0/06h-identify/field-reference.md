# Identify - Field Reference

Primary source: NVMe Base Specification 2.0, section 5.17, Figures 275 through 290.

Purpose: provide a field lookup reference for Identify returned payloads. Use this when a script, dump, assertion, or question mentions a field name, byte offset, bit, or value and Codex needs the spec meaning without reopening the original specification.

This file is spec-only. It explains fields, values, and relationships. It does not prescribe PyNVMe calls or test-flow steps.

## Reading Model

| Column | Meaning |
|---|---|
| Offset / Bits | Byte offset for returned data structures, or bit range inside the named field. |
| Field | Spec field abbreviation. |
| Full Name | Expanded field name. |
| Meaning | What the field reports or controls. |
| Key Bits / Values | Important bit or value meanings. Use the detailed section when present. |
| Affects | Related command, feature, log page, transport, or command-set behavior. |
| Source | Source figure, section, or table for the field. |

Reserved fields are kept as reserved. They are not expanded unless the Base Spec gives a defined behavior such as "shall be cleared to 0h".

## Figure 275 - Identify Controller Data Structure

CNS: `01h`.

Returned for the controller processing the Identify command. The structure is I/O Command Set independent and is 4,096 bytes.

| Offset | Field | Full Name | Meaning | Key Bits / Values | Affects | Source |
|---|---|---|---|---|---|---|
| `01:00` | `VID` | PCI Vendor ID | PCI SIG vendor identifier. | Same as PCIe ID register. | PCIe identity, vendor matching. | Figure 275 |
| `03:02` | `SSVID` | PCI Subsystem Vendor ID | PCI SIG subsystem vendor identifier. | Same as PCIe SS register. | PCIe subsystem identity. | Figure 275 |
| `23:04` | `SN` | Serial Number | Vendor-assigned NVM subsystem serial number ASCII string. | Unique identifier rules in section 4.5.1. | Device identity. | Figure 275 |
| `63:24` | `MN` | Model Number | Vendor-assigned NVM subsystem model number ASCII string. | ASCII string rules apply. | Device identity. | Figure 275 |
| `71:64` | `FR` | Firmware Revision | Currently active firmware revision for the domain. | Also available through Get Log Page firmware slot info. | Firmware validation. | Figure 275 |
| `72` | `RAB` | Recommended Arbitration Burst | Recommended Arbitration Burst size in commands, encoded as `2^n`. | Same units as arbitration burst size. | Arbitration behavior. | Figure 275 |
| `75:73` | `IEEE` | IEEE OUI Identifier | IEEE/RAC assigned OUI for controller vendor. | Big-endian OUI. | Vendor identity. | Figure 275 |
| `76` | `CMIC` | Controller Multi-Path I/O and Namespace Sharing Capabilities | Reports ANA, SR-IOV VF association, multiple controllers, and multiple subsystem ports. | See `CMIC` bit table. | ANA, multipath, namespace sharing, SR-IOV. | Figure 275 |
| `77` | `MDTS` | Maximum Data Transfer Size | Maximum host-memory-to-controller data transfer size. | Units are `CAP.MPSMIN`, encoded as `2^n`; `0h` means no maximum. | Data-transfer commands; over-limit command aborts with `Invalid Field in Command`. | Figure 275 |
| `79:78` | `CNTLID` | Controller ID | NVM subsystem unique controller identifier. | Controller-specific identity. | Controller lists, CNTID selectors. | Figure 275 |
| `83:80` | `VER` | Version | Value reported in Version property. | NVMe 1.2+ compliant implementations report non-zero. | Version-gated behavior. | Figure 275 |
| `87:84` | `RTD3R` | RTD3 Resume Latency | Expected latency to resume from Runtime D3 in microseconds. | `0h` means not reported. | Power management. | Figure 275 |
| `91:88` | `RTD3E` | RTD3 Entry Latency | Typical latency to enter Runtime D3 in microseconds. | `0h` means not reported. | Power management. | Figure 275 |
| `95:92` | `OAES` | Optional Asynchronous Events Supported | Optional async events the controller can send after host enables them. | See `OAES` bit table. | Asynchronous Event Request, log change notices. | Figure 275 |
| `99:96` | `CTRATT` | Controller Attributes | Controller and subsystem attributes such as NVM Sets, Endurance Groups, UUID List, MDS, capacity management. | See `CTRATT` bit table. | Identify lists, Capacity Management, UUID, domains, NVM Sets, Endurance Groups. | Figure 275 |
| `101:100` | `RRLS` | Read Recovery Levels Supported | Supported Read Recovery Levels if read recovery is supported. | Bits `0`-`15` map to Read Recovery Level 0-15. | Read Recovery Level feature. | Figure 275 |
| `110:102` | - | Reserved | Reserved. | Reserved. | None. | Figure 275 |
| `111` | `CNTRLTYPE` | Controller Type | Reports controller type. | `1h` I/O, `2h` Discovery, `3h` Administrative; `0h` reserved for NVMe 1.4+. | Controller role handling. | Figure 275 |
| `127:112` | `FGUID` | FRU Globally Unique Identifier | 128-bit identifier unique for a Field Replaceable Unit. | `0h` if not implemented. | NVMe-MI FRU identity. | Figure 275 |
| `129:128` | `CRDT1` | Command Retry Delay Time 1 | Retry delay if CQE `CRD=01b` and `DNR=0`. | Units are 100 ms. | Command retry behavior. | Figure 275 |
| `131:130` | `CRDT2` | Command Retry Delay Time 2 | Retry delay if CQE `CRD=10b` and `DNR=0`. | Units are 100 ms. | Command retry behavior. | Figure 275 |
| `133:132` | `CRDT3` | Command Retry Delay Time 3 | Retry delay if CQE `CRD=11b` and `DNR=0`. | Units are 100 ms. | Command retry behavior. | Figure 275 |
| `239:134` | - | Reserved | Reserved. | Reserved. | None. | Figure 275 |
| `252:240` | - | Reserved for NVMe-MI | Reserved for NVMe Management Interface. | See NVMe-MI specification. | NVMe-MI boundary. | Figure 275 |
| `253` | `NVMSR` | NVM Subsystem Report | Reports NVM subsystem information associated with NVMe-MI. | Bit 1 NVMe enclosure, bit 0 NVMe storage device. | NVMe-MI inventory. | Figure 275 |
| `254` | `VWCI` | VPD Write Cycle Information | Reports remaining VPD write cycles when valid. | Bit 7 valid; bits `6:0` remaining write cycles in 256-byte units. | NVMe-MI VPD Write. | Figure 275 |
| `255` | `MEC` | Management Endpoint Capabilities | Reports management endpoints in NVM subsystem. | Bit 1 PCIe management endpoint; bit 0 SMBus/I2C management endpoint. | NVMe-MI transport boundary. | Figure 275 |
| `257:256` | `OACS` | Optional Admin Command Support | Optional Admin commands and features supported by the controller. | See `OACS` bit table. | Admin command availability. | Figure 275 |
| `258` | `ACL` | Abort Command Limit | Max concurrently executing Abort commands, zero-based. | Recommended minimum is four concurrent Abort commands. | Abort. | Figure 275 |
| `259` | `AERL` | Asynchronous Event Request Limit | Max concurrently outstanding AER commands, zero-based. | Recommended minimum is four outstanding AER commands. | Asynchronous Event Request. | Figure 275 |
| `260` | `FRMW` | Firmware Updates | Firmware slot and activation behavior. | See `FRMW` bit table. | Firmware Commit / Firmware Image Download. | Figure 275 |
| `261` | `LPA` | Log Page Attributes | Optional Get Log Page attributes. | See `LPA` bit table. | Get Log Page. | Figure 275 |
| `262` | `ELPE` | Error Log Page Entries | Maximum number of Error Information log entries, zero-based. | Used by Error Information log page. | Get Log Page Error Information. | Figure 275 |
| `263` | `NPSS` | Number of Power States Support | Number of supported power states, zero-based. | At least power state 0, up to 31 additional states. | Power State Descriptors, power management. | Figure 275 |
| `264` | `AVSCC` | Admin Vendor Specific Command Configuration | Vendor-specific Admin command format selection. | Bit 0 set means Figure 88 format. | Vendor-specific Admin commands. | Figure 275 |
| `265` | `APSTA` | Autonomous Power State Transition Attributes | Reports APST feature support. | Bit 0 APST supported. | Autonomous Power State Transition feature. | Figure 275 |
| `267:266` | `WCTEMP` | Warning Composite Temperature Threshold | Warning temperature threshold in Kelvins. | `0h` means not reported. | SMART / Health, thermal management. | Figure 275 |
| `269:268` | `CCTEMP` | Critical Composite Temperature Threshold | Critical temperature threshold in Kelvins. | `0h` means not reported. | SMART / Health, thermal management. | Figure 275 |
| `271:270` | `MTFA` | Maximum Time for Firmware Activation | Max temporary command stop time for firmware activation. | 100 ms units; valid if activation without reset is supported. | Firmware Commit. | Figure 275 |
| `275:272` | `HMPRE` | Host Memory Buffer Preferred Size | Preferred Host Memory Buffer allocation size. | Units are 4 KiB; non-zero means HMB supported. | Host Memory Buffer feature. | Figure 275 |
| `279:276` | `HMMIN` | Host Memory Buffer Minimum Size | Minimum requested HMB size. | `0h` means allocate any amount up to HMPRE. | Host Memory Buffer feature. | Figure 275 |
| `295:280` | `TNVMCAP` | Total NVM Capacity | Total NVM capacity accessible by the controller, in bytes. | Required if Namespace Management is supported. | Namespace Management, Capacity Management. | Figure 275 |
| `311:296` | `UNVMCAP` | Unallocated NVM Capacity | Unallocated NVM capacity accessible by the controller, in bytes. | Required if Namespace Management is supported. | Namespace Management, Capacity Management. | Figure 275 |
| `315:312` | `RPMBS` | Replay Protected Memory Block Support | RPMB count, authentication, total size, and access size. | Non-zero units require Security Send/Receive support. | Security Send / Security Receive, RPMB. | Figure 275 |
| `317:316` | `EDSTT` | Extended Device Self-test Time | Nominal extended self-test time in minutes. | Reserved if Device Self-test command unsupported. | Device Self-test. | Figure 275 |
| `318` | `DSTO` | Device Self-test Options | Device self-test operation concurrency behavior. | Bit 0 set means only one self-test per NVM subsystem. | Device Self-test. | Figure 275 |
| `319` | `FWUG` | Firmware Update Granularity | Firmware Image Download granularity and alignment. | 4 KiB units; `0h` no info; `FFh` no restriction. | Firmware Image Download. | Figure 275 |
| `321:320` | `KAS` | Keep Alive Support | Keep Alive Timer granularity in 100 ms units. | `0h` means Keep Alive unsupported; required for Fabrics. | Keep Alive, NVMe-oF. | Figure 275 |
| `323:322` | `HCTMA` | Host Controlled Thermal Management Attributes | Reports HCTM support. | Bit 0 supported; requires Set/Get Features FID `10h`. | Thermal Management feature. | Figure 275 |
| `325:324` | `MNTMT` | Minimum Thermal Management Temperature | Minimum host-requestable thermal management temperature. | `0h` means not reported or HCTM unsupported. | Thermal Management feature. | Figure 275 |
| `327:326` | `MXTMT` | Maximum Thermal Management Temperature | Maximum host-requestable thermal management temperature. | `0h` means not reported or HCTM unsupported. | Thermal Management feature. | Figure 275 |
| `331:328` | `SANICAP` | Sanitize Capabilities | Supported sanitize operations and No-Deallocate behavior. | See `SANICAP` bit table. | Sanitize. | Figure 275 |
| `335:332` | `HMMINDS` | HMB Minimum Descriptor Entry Size | Minimum usable HMB descriptor entry size. | 4 KiB units; `0h` means no limitation reported. | Host Memory Buffer. | Figure 275 |
| `337:336` | `HMMAXD` | HMB Maximum Descriptor Entries | Max usable HMB descriptor entries. | `0h` means no maximum reported. | Host Memory Buffer. | Figure 275 |
| `339:338` | `NSETIDMAX` | NVM Set Identifier Maximum | Maximum valid NVM Set Identifier. | Number of NVM Sets <= NSETIDMAX. | NVM Set List, NVM Set aware commands. | Figure 275 |
| `341:340` | `ENDGIDMAX` | Endurance Group Identifier Maximum | Maximum valid Endurance Group Identifier. | Number of Endurance Groups <= ENDGIDMAX. | Endurance Group List, Endurance Group logs. | Figure 275 |
| `342` | `ANATT` | ANA Transition Time | Max ANA transition or change-state reporting time in seconds. | Non-zero if ANA Reporting supported; `0h` otherwise. | ANA. | Figure 275 |
| `343` | `ANACAP` | ANA Capabilities | Supported ANA states and ANAGRPID behavior. | Bits 0-4 report ANA states; bit 6 ANAGRPID immutability; bit 7 non-zero ANAGRPID in Namespace Management. | ANA, Namespace Management. | Figure 275 |
| `347:344` | `ANAGRPMAX` | ANA Group Identifier Maximum | Maximum valid ANA Group Identifier. | Non-zero if ANA Reporting supported. | ANA. | Figure 275 |
| `351:348` | `NANAGRPID` | Number of ANA Group Identifiers | Number of ANA groups supported by controller. | Non-zero and <= ANAGRPMAX if ANA Reporting supported. | ANA. | Figure 275 |
| `355:352` | `PELS` | Persistent Event Log Size | Maximum reportable Persistent Event Log size. | 64 KiB units; reserved if log unsupported. | Persistent Event Log. | Figure 275 |
| `357:356` | - | Domain Identifier | Domain containing this controller. | Non-zero if `CTRATT.MDS=1`; `0h` for single-domain subsystem. | Domain List, multi-domain systems. | Figure 275 |
| `367:358` | - | Reserved | Reserved. | Reserved. | None. | Figure 275 |
| `383:368` | `MEGCAP` | Max Endurance Group Capacity | Maximum capacity of a single Endurance Group. | `0h` means not reported. | Capacity Management, Endurance Groups. | Figure 275 |
| `511:384` | - | Reserved | Reserved. | Reserved. | None. | Figure 275 |
| `512` | `SQES` | Submission Queue Entry Size | Required and maximum I/O SQ entry size. | Upper nibble max; lower nibble required; required value is `6` for 64 bytes. | I/O queue setup. | Figure 275 |
| `513` | `CQES` | Completion Queue Entry Size | Required and maximum I/O CQ entry size. | Upper nibble max; lower nibble required; required value is `4` for 16 bytes. | I/O queue setup. | Figure 275 |
| `515:514` | `MAXCMD` | Maximum Outstanding Commands | Max commands controller processes at one time for a queue. | Mandatory for Fabrics, optional for PCIe; `0h` if unused. | Queue sizing, Fabrics. | Figure 275 |
| `519:516` | `NN` | Number of Namespaces | Maximum valid NSID for the NVM subsystem. | See `MNAN` for maximum supported namespaces. | Namespace enumeration. | Figure 275 |
| `521:520` | `ONCS` | Optional NVM Command Support | Optional I/O commands and features supported by the controller. | See `ONCS` bit table. | I/O command availability, Reservations, Features. | Figure 275 |
| `523:522` | `FUSES` | Fused Operation Support | Fused operations supported. | Bit 0 Compare and Write fused operation. | Fused Compare + Write. | Figure 275 |
| `524` | `FNA` | Format NVM Attributes | Format NVM scope and secure erase behavior. | See `FNA` bit table. | Format NVM. | Figure 275 |
| `525` | `VWC` | Volatile Write Cache | Volatile write cache presence and Flush broadcast behavior. | See `VWC` bit table. | Flush, Set/Get Features Volatile Write Cache. | Figure 275 |
| `527:526` | `AWUN` | Atomic Write Unit Normal | Atomic write unit for logical-block command sets. | Cleared for namespaces not associated with logical-block command sets. | Write atomicity. | Figure 275 |
| `529:528` | `AWUPF` | Atomic Write Unit Power Fail | Atomic write unit under power fail for logical-block command sets. | Cleared for namespaces not associated with logical-block command sets. | Write atomicity. | Figure 275 |
| `530` | `ICSVSCC` | I/O Command Set Vendor Specific Command Configuration | Vendor-specific I/O command format selection. | Bit 0 set means Figure 88 format. | Vendor-specific I/O commands. | Figure 275 |
| `531` | `NWPC` | Namespace Write Protection Capabilities | Namespace write-protection states supported. | Bits 0-2 define write protection capabilities. | Namespace Write Protection. | Figure 275 |
| `533:532` | `ACWU` | Atomic Compare & Write Unit | Compare and Write atomicity for logical-block command sets. | Cleared for non-logical-block command sets. | Compare and Write. | Figure 275 |
| `535:534` | - | Optional Copy Formats Supported | Copy format support. | Bit 0 Copy Format 0h; bit 1 Copy Format 1h. | Copy command. | Figure 275 |
| `539:536` | `SGLS` | SGL Support | Supported SGL types, alignment, threshold, and metadata behavior. | See `SGLS` bit table. | Data pointer, SGL descriptors, Fabrics. | Figure 275 |
| `543:540` | `MNAN` | Maximum Number of Allowed Namespaces | Maximum namespaces supported by NVM subsystem. | `0h` means max <= `NN`; non-zero if ANA supported. | Namespace enumeration and limits. | Figure 275 |
| `559:544` | `MAXDNA` | Maximum Domain Namespace Attachments | Max sum of namespaces attached to each I/O controller in the Domain. | `0h` means no maximum specified. | Namespace Attachment. | Figure 275 |
| `563:560` | `MAXCNA` | Maximum I/O Controller Namespace Attachments | Max namespaces attachable to this I/O controller. | `0h` means no maximum specified. | Namespace Attachment. | Figure 275 |
| `767:564` | - | Reserved | Reserved. | Reserved. | None. | Figure 275 |
| `1023:768` | `SUBNQN` | NVM Subsystem NVMe Qualified Name | UTF-8 null-terminated NQN string. | Mandatory for revision 1.2.1+ support. | NVM subsystem identity, Fabrics discovery. | Figure 275 |
| `1791:1024` | - | Reserved | Reserved. | Reserved. | None. | Figure 275 |
| `1795:1792` | `IOCCSZ` | I/O Queue Command Capsule Supported Size | Maximum I/O command capsule size in 16-byte units. | Min value 4, meaning 64 bytes. | NVMe over Fabrics. | Figure 275 |
| `1799:1796` | `IORCSZ` | I/O Queue Response Capsule Supported Size | Maximum I/O response capsule size in 16-byte units. | Min value 1, meaning 16 bytes. | NVMe over Fabrics. | Figure 275 |
| `1801:1800` | `ICDOFF` | In Capsule Data Offset | Offset where data starts within an I/O capsule. | 16-byte units from end of SQE; Admin Queue uses `0h`. | NVMe over Fabrics. | Figure 275 |
| `1802` | `FCATT` | Fabrics Controller Attributes | NVMe-oF controller model attributes. | Bit 0 clear dynamic model, set static model. | NVMe over Fabrics. | Figure 275 |
| `1803` | `MSDBD` | Maximum SGL Data Block Descriptors | Max SGL data block or keyed SGL data block descriptors in a capsule. | `0h` means no limit. | NVMe over Fabrics SGL handling. | Figure 275 |
| `1805:1804` | `OFCS` | Optional Fabric Commands Support | Optional Fabrics command support. | Bit 0 Disconnect command supported. | Fabrics Disconnect. | Figure 275 |
| `2047:1806` | - | Reserved | Reserved. | Reserved. | None. | Figure 275 |
| `2079:2048` | `PSD0` | Power State 0 Descriptor | Power state 0 characteristics. | Format is Figure 276; power state 0 mandatory. | Power management. | Figure 275 / 276 |
| `3071:2080` | `PSD1`-`PSD31` | Power State 1-31 Descriptors | Optional power state characteristics. | Each descriptor is 32 bytes using Figure 276. | Power management. | Figure 275 / 276 |
| `4095:3072` | - | Vendor Specific | Vendor-specific area. | Optional/vendor-defined. | Vendor-specific interpretation. | Figure 275 |

### CMIC Bits

| Bit | Meaning | Affects |
|---:|---|---|
| `3` | ANA Reporting supported when set. | ANA log/behavior, `ANATT`, `ANACAP`, `ANAGRPMAX`, `NANAGRPID`. |
| `2` | Controller is associated with an SR-IOV Virtual Function when set. | SR-IOV / secondary controller context. |
| `1` | NVM subsystem may contain two or more controllers when set. | Multipath, namespace sharing. |
| `0` | NVM subsystem may contain more than one NVM subsystem port when set. | Multipath / port topology. |

### OAES Bits

| Bit | Meaning | Affects |
|---:|---|---|
| `31` | Discovery Log Page Change Notifications. | Discovery log, AER. |
| `27` | Zone Descriptor Changed Notices and Changed Zone List log. | ZNS boundary. |
| `15` | Normal NVM Subsystem Shutdown event. | AER. |
| `14` | Endurance Group Event Aggregate Log Page Change Notices. | Endurance Group logs. |
| `13` | LBA Status Information Notices. | NVM command set boundary. |
| `12` | Predictable Latency Event Aggregate Log Change Notices. | Predictable Latency logs. |
| `11` | ANA Change Notices. | ANA. |
| `9` | Firmware Activation Notices. | Firmware Commit / AER. |
| `8` | Namespace Attribute Notices and Changed Namespace List log. | Namespace Management / AER. |

### CTRATT Bits

| Bit | Meaning | Affects |
|---:|---|---|
| `15` | Extended LBA Formats Supported. | Command-set-specific protection information formats. |
| `14` | Delete NVM Set supported. | Capacity Management. |
| `13` | Delete Endurance Group supported. | Capacity Management. |
| `12` | Variable Capacity Management supported. | Capacity Management. |
| `11` | Fixed Capacity Management supported. | Capacity Management. |
| `10` | Multi-Domain Subsystem supported. | Domain List, Domain Identifier. |
| `9` | UUID List supported. | CNS `17h`, UUID Index. |
| `8` | SQ Associations supported. | SQ Associations. |
| `7` | Namespace Granularity reporting supported. | CNS `16h`. |
| `6` | Traffic Based Keep Alive Support. | Keep Alive. |
| `5` | Predictable Latency Mode supported. | Predictable Latency. |
| `4` | Endurance Groups supported. | CNS `19h`, Endurance Group logs. |
| `3` | Read Recovery Levels supported. | `RRLS`, Read Recovery Level feature. |
| `2` | NVM Sets supported. | CNS `04h`, NVM Set aware commands. |
| `1` | Non-Operational Power State Permissive Mode supported. | Power management feature. |
| `0` | 128-bit Host Identifier supported. | Host Identifier feature. |

### OACS Bits

| Bit | Meaning | Affects |
|---:|---|---|
| `10` | Command and Feature Lockdown supported. | Lockdown. |
| `9` | Get LBA Status capability supported. | NVM command set boundary. |
| `8` | Doorbell Buffer Config supported. | Doorbell Buffer Config. |
| `7` | Virtualization Management supported. | Virtualization Management, primary/secondary controller structures. |
| `6` | NVMe-MI Send and NVMe-MI Receive supported. | NVMe-MI Send / Receive. |
| `5` | Directives supported. | Directive Send / Receive. |
| `4` | Device Self-test supported. | Device Self-test, `EDSTT`, `DSTO`. |
| `3` | Namespace Management supported. | Namespace Management / Attachment, several Identify CNS behaviors. |
| `2` | Firmware Commit and Firmware Image Download supported. | Firmware commands. |
| `1` | Format NVM supported. | Format NVM. |
| `0` | Security Send and Security Receive supported. | Security commands, RPMB. |

### FRMW Bits

| Bits | Meaning | Affects |
|---:|---|---|
| `5` | Support Multiple Update Detection. | Firmware image update sequences. |
| `4` | Firmware Activation Without Reset. | Firmware Commit. |
| `3:1` | Number of Firmware Slots, values 1-7. | Firmware Commit / Firmware Slot log. |
| `0` | First Firmware Slot Read Only. | Firmware Commit. |

### LPA Bits

| Bit | Meaning | Affects |
|---:|---|---|
| `6` | Telemetry Data Area 4 supported. | Telemetry logs. |
| `5` | Supported Log Pages log, command scope in Commands Supported and Effects log, Feature Identifiers Supported and Effects log, NVMe-MI Commands Supported and Effects log behavior. | Get Log Page. |
| `4` | Persistent Event Log supported. | Persistent Event Log. |
| `3` | Telemetry Host/Controller Initiated logs and Telemetry Log Notices supported. | Telemetry logs, AER. |
| `2` | Extended data for Get Log Page supported, including extended NUMD and Log Page Offset. | Get Log Page command fields. |
| `1` | Commands Supported and Effects log supported. | Get Log Page LID `05h`. |
| `0` | SMART / Health Information log per-namespace supported. | Get Log Page SMART / Health. |

### ONCS Bits

| Bit | Meaning | Affects |
|---:|---|---|
| `8` | Copy command supported. | Copy. |
| `7` | Verify command supported and `VSL` indicates recommended max Verify data size. | Verify. |
| `6` | Timestamp feature supported. | Get/Set Features Timestamp. |
| `5` | Reservations supported. Reservation Register, Report, Acquire, and Release shall be supported. | Reservation commands. |
| `4` | Save in Set Features and non-zero Select in Get Features supported. | Set Features / Get Features. |
| `3` | Write Zeroes supported and `WZSL` indicates recommended max Write Zeroes data size. | Write Zeroes. |
| `2` | Dataset Management supported; `DMRL`, `DMSL`, `DMRSL` define Dataset Management limits. | Dataset Management. |
| `1` | Write Uncorrectable supported and `WUSL` indicates recommended max data size. | Write Uncorrectable. |
| `0` | Compare supported. | Compare. |

### FNA Bits

| Bit | Meaning | Affects |
|---:|---|---|
| `3` | If set, Format NVM does not support NSID `FFFFFFFFh`; bits 1 and 0 shall be cleared. | Format NVM broadcast behavior. |
| `2` | Cryptographic erase supported as part of secure erase. | Format NVM secure erase. |
| `1` | Secure erase applies to all namespaces when set; otherwise per namespace. | Format NVM secure erase scope. |
| `0` | Format operation applies to all namespaces when set; otherwise per namespace. | Format NVM format scope. |

### VWC Bits

| Bits | Meaning | Affects |
|---:|---|---|
| `2:1` | Flush command behavior for NSID `FFFFFFFFh`: `10b` not supported and fails with `Invalid Namespace or Format`; `11b` supported. | Flush. |
| `0` | Volatile write cache present when set. | Flush, Volatile Write Cache feature. |

### SANICAP Bits

| Bits | Meaning | Affects |
|---:|---|---|
| `31:30` | No-Deallocate Modifies Media After Sanitize. | Sanitize completion/event behavior. |
| `29` | No-Deallocate Inhibited. | Sanitize No-Deallocate After Sanitize handling. |
| `2` | Overwrite sanitize operation supported. | Sanitize. |
| `1` | Block Erase sanitize operation supported. | Sanitize. |
| `0` | Crypto Erase sanitize operation supported. | Sanitize. |

### SGLS Bits

| Bits | Meaning | Affects |
|---:|---|---|
| `21` | Transport SGL Data Block descriptor supported. | Fabrics SGL. |
| `20` | Address field offset in SGL Data Block / Segment / Last Segment supported. | SGL descriptors. |
| `19` | MPTR containing one qword-aligned SGL Descriptor supported. | Metadata pointer. |
| `18` | Data/metadata SGL length larger than transfer amount supported. | SGL validation. |
| `17` | Byte-aligned contiguous metadata buffer supported when `PSDT=01b`. | Metadata alignment. |
| `16` | SGL Bit Bucket descriptor supported. | SGL descriptors. |
| `15:8` | Recommended maximum number of SGL descriptors. | SGL descriptor count. |
| `2` | Keyed SGL Data Block descriptor supported. | SGL descriptors. |
| `1:0` | SGL support and alignment: `00b` unsupported, `01b` supported with no data-block alignment/granularity, `10b` supported with dword alignment/granularity. | SGL use. |

## Figure 276 - Power State Descriptor

Each descriptor is 32 bytes. Figure 275 contains `PSD0` through `PSD31`; `PSD0` is mandatory and the others are optional based on `NPSS`.

| Bits | Field | Full Name | Meaning | Key Bits / Values | Affects | Source |
|---|---|---|---|---|---|---|
| `255:184` | - | Reserved | Reserved. | Reserved. | None. | Figure 276 |
| `183:182` | `APS` | Active Power Scale | Scale for `ACTP`. | `00b` not reported, `01b` 0.0001 W, `10b` 0.01 W. | Power calculation. | Figure 276 |
| `178:176` | `APW` | Active Power Workload | Workload used to calculate active power. | Shall not be No Workload unless `ACTP=0h`. | Power calculation. | Figure 276 |
| `175:160` | `ACTP` | Active Power | Largest average power over 10 seconds for APW workload. | `0h` not reported. | Power management. | Figure 276 |
| `151:150` | `IPS` | Idle Power Scale | Scale for `IDLP`. | `00b` not reported, `01b` 0.0001 W, `10b` 0.01 W. | Power calculation. | Figure 276 |
| `143:128` | `IDLP` | Idle Power | Typical idle power over 30 seconds after 10 seconds idle. | `0h` not reported. | Power management. | Figure 276 |
| `124:120` | `RWL` | Relative Write Latency | Relative write latency for this power state. | Lower means lower latency; value < supported power states. | Power/performance selection. | Figure 276 |
| `116:112` | `RWT` | Relative Write Throughput | Relative write throughput for this power state. | Lower means higher throughput; value < supported power states. | Power/performance selection. | Figure 276 |
| `108:104` | `RRL` | Relative Read Latency | Relative read latency for this power state. | Lower means lower latency; value < supported power states. | Power/performance selection. | Figure 276 |
| `100:96` | `RRT` | Relative Read Throughput | Relative read throughput for this power state. | Lower means higher throughput; value < supported power states. | Power/performance selection. | Figure 276 |
| `95:64` | `EXLAT` | Exit Latency | Max exit latency in microseconds. | `0h` not reported. | Power state transition. | Figure 276 |
| `63:32` | `ENLAT` | Entry Latency | Max entry latency in microseconds. | `0h` not reported. | Power state transition. | Figure 276 |
| `25` | `NOPS` | Non-Operational State | Whether controller processes I/O in this power state. | `0` processes I/O, `1` does not process I/O. | Power state command eligibility. | Figure 276 |
| `24` | `MXPS` | Max Power Scale | Scale for `MP`. | `0` 0.01 W, `1` 0.0001 W. | Power calculation. | Figure 276 |
| `15:00` | `MP` | Maximum Power | Sustained maximum power for this power state. | `0h` not reported. | Power management. | Figure 276 |

## Figure 277 - Namespace Identification Descriptor

CNS: `03h`.

| Offset | Field | Full Name | Meaning | Key Bits / Values | Affects | Source |
|---|---|---|---|---|---|---|
| `00` | `NIDT` | Namespace Identifier Type | Type of data in `NID`. | See NIDT value table. | Namespace identity. | Figure 277 |
| `01` | `NIDL` | Namespace Identifier Length | Length in bytes of `NID`. Total descriptor length is `NIDL + 4`. | `0h` means end of descriptor list. | Descriptor parsing. | Figure 277 |
| `03:02` | - | Reserved | Reserved. | Reserved. | None. | Figure 277 |
| `(NIDL+3):04` | `NID` | Namespace Identifier | Globally unique namespace identifier of the type indicated by `NIDT`. | Fixed for life of namespace. | Namespace identity. | Figure 277 |

| NIDT | NIDL | Meaning | Rule |
|---|---:|---|---|
| `0h` | - | Reserved. | Not valid as a descriptor type. |
| `1h` | `8h` | IEEE Extended Unique Identifier. | Copies EUI64 from applicable Identify Namespace; do not report if EUI64 unsupported or `0h`. |
| `2h` | `10h` | Namespace Globally Unique Identifier. | Copies NGUID; do not report if NGUID unsupported or `0h`. |
| `3h` | `10h` | Namespace UUID. | Required if namespace supports neither EUI64 nor NGUID. |
| `4h` | `1h` | Command Set Identifier. | NID contains CSI from Figure 274; required if `CAP.CSS` bit 6 is set. |
| `5h`-`FFh` | - | Reserved. | Reserved. |

## Figure 278 / 279 - NVM Set List And Attributes Entry

CNS: `04h`.

| Structure | Offset | Field | Full Name | Meaning | Affects | Source |
|---|---|---|---|---|---|---|
| NVM Set List | `00` | `N` | Number of Identifiers | Number of NVM Set Attributes Entries, up to 31. `0h` means no entries. | List parsing. | Figure 278 |
| NVM Set List | `127:01` | - | Reserved | Reserved. | None. | Figure 278 |
| NVM Set List | `N*128+255:N*128+128` | Entry N | NVM Set Attributes Entry | N+1th entry, if present. | NVM Set attributes. | Figure 278 |
| NVM Set Attributes Entry | `01:00` | `NVMSETID` | NVM Set Identifier | Identifier of the NVM Set. | NVM Set aware commands. | Figure 279 |
| NVM Set Attributes Entry | `03:02` | `ENDGID` | Endurance Group Identifier | Endurance Group for this NVM Set. | Endurance Group association. | Figure 279 |
| NVM Set Attributes Entry | `11:08` | - | Random 4 KiB Read Typical | Typical 4 KiB random read completion time in 100 ns units during Predictable Latency deterministic window. | Predictable Latency. | Figure 279 |
| NVM Set Attributes Entry | `15:12` | - | Optimal Write Size | Optimal write size in bytes. `0h` means none specified. | Write sizing. | Figure 279 |
| NVM Set Attributes Entry | `31:16` | - | Total NVM Set Capacity | Total NVM capacity in this NVM Set, in bytes. | Capacity reporting. | Figure 279 |
| NVM Set Attributes Entry | `47:32` | - | Unallocated NVM Set Capacity | Unallocated NVM capacity in this NVM Set, in bytes. | Capacity reporting. | Figure 279 |

## Figure 280 - I/O Command Set Independent Identify Namespace Data Structure

CNS: `08h`.

| Offset | Field | Full Name | Meaning | Key Bits / Values | Affects | Source |
|---|---|---|---|---|---|---|
| `00` | `NSFEAT` | Common Namespace Features | Namespace features independent of I/O Command Set. | Bit 4 rotational media storage; bit 3 UID reuse guarantee; bit 0 associated with rotational media. | Namespace identity, rotational media, UID reuse. | Figure 280 |
| `01` | `NMIC` | Namespace Multi-path I/O and Namespace Sharing Capabilities | Namespace sharing capability. | Bit 0 set means namespace may be attached to two or more controllers concurrently. | Namespace sharing, Namespace Attachment. | Figure 280 |
| `02` | `RESCAP` | Reservation Capabilities | Reservation types supported by the namespace. | See `RESCAP` bit table. | Reservation commands. | Figure 280 |
| `03` | `FPI` | Format Progress Indicator | Format progress status. | Bit 7 valid; bits `6:0` percentage remaining. | Format NVM. | Figure 280 |
| `07:04` | `ANAGRPID` | ANA Group Identifier | ANA group of the namespace. | Valid if controller supports ANA; cleared if ANA unsupported. | ANA. | Figure 280 |
| `08` | `NSATTR` | Namespace Attributes | Namespace attributes. | Bit 0 set means namespace currently write protected. | Write commands, namespace write protection. | Figure 280 |
| `09` | - | Reserved | Reserved. | Reserved. | None. | Figure 280 |
| `11:10` | `NVMSETID` | NVM Set Identifier | NVM Set associated with the namespace. | Cleared if NVM Sets unsupported. | NVM Set aware behavior. | Figure 280 |
| `13:12` | `ENDGID` | Endurance Group Identifier | Endurance Group associated with the namespace. | Cleared if Endurance Groups unsupported. | Endurance Group behavior. | Figure 280 |
| `14` | `NSTAT` | Namespace Status | Namespace readiness status. | Bit 0 `NRDY`, set means ready, clear means not ready. | Namespace readiness. | Figure 280 |
| `4095:15` | - | Reserved | Reserved. | Reserved. | None. | Figure 280 |

### RESCAP Bits

| Bit | Meaning | Affects |
|---:|---|---|
| `7` | Ignore Existing Key definition version. Set for NVMe 1.3+ behavior. | Reservation Register / Acquire / Release. |
| `6` | Exclusive Access - All Registrants supported. | Reservation type availability. |
| `5` | Write Exclusive - All Registrants supported. | Reservation type availability. |
| `4` | Exclusive Access - Registrants Only supported. | Reservation type availability. |
| `3` | Write Exclusive - Registrants Only supported. | Reservation type availability. |
| `2` | Exclusive Access supported. | Reservation type availability. |
| `1` | Write Exclusive supported. | Reservation type availability. |
| `0` | Persist Through Power Loss capability supported. | Reservation persistence. |

## Figure 281 - Primary Controller Capabilities Structure

CNS: `14h`.

| Offset | Field | Full Name | Meaning | Key Bits / Values | Affects | Source |
|---|---|---|---|---|---|---|
| `01:00` | `CNTLID` | Controller Identifier | Primary controller identifier. | Primary controller selected by CNTID. | Virtualization Management. | Figure 281 |
| `03:02` | `PORTID` | Port Identifier | NVM subsystem port associated with primary controller. | PCIe Port ID unique within subsystem; may match NVMe-MI Controller Information. | PCIe / NVMe-MI boundary. | Figure 281 |
| `04` | `CRT` | Controller Resource Types | Supported controller resource types. | Bit 1 VI, bit 0 VQ. | Virtualization resources. | Figure 281 |
| `35:32` | `VQFRT` | VQ Resources Flexible Total | Total VQ Flexible Resources. | Primary + secondary controllers. | Virtualization Management. | Figure 281 |
| `39:36` | `VQRFA` | VQ Resources Flexible Assigned | Total VQ Flexible Resources assigned to secondary controllers. | Resource allocation state. | Virtualization Management. | Figure 281 |
| `41:40` | `VQRFAP` | VQ Resources Flexible Allocated to Primary | VQ Flexible Resources allocated to primary controller. | May change after certain resets. | Virtualization Management. | Figure 281 |
| `43:42` | `VQPRT` | VQ Resources Private Total | Total VQ Private Resources for primary. | Resource capacity. | Virtualization Management. | Figure 281 |
| `45:44` | `VQFRSM` | VQ Resources Flexible Secondary Maximum | Max VQ Flexible Resources assignable to a secondary. | Resource limit. | Virtualization Management. | Figure 281 |
| `47:46` | `VQGRAN` | VQ Flexible Resource Preferred Granularity | Preferred granularity for assigning/removing VQ resources. | Minimizes wasted implementation resources. | Virtualization Management. | Figure 281 |
| `67:64` | `VIFRT` | VI Resources Flexible Total | Total VI Flexible Resources. | Primary + secondary controllers. | Virtualization Management. | Figure 281 |
| `71:68` | `VIRFA` | VI Resources Flexible Assigned | Total VI Flexible Resources assigned to secondary controllers. | Resource allocation state. | Virtualization Management. | Figure 281 |
| `73:72` | `VIRFAP` | VI Resources Flexible Allocated to Primary | VI Flexible Resources allocated to primary controller. | May change after certain resets. | Virtualization Management. | Figure 281 |
| `75:74` | `VIPRT` | VI Resources Private Total | Total VI Private Resources for primary. | Resource capacity. | Virtualization Management. | Figure 281 |
| `77:76` | `VIFRSM` | VI Resources Flexible Secondary Maximum | Max VI Flexible Resources assignable to a secondary. | Resource limit. | Virtualization Management. | Figure 281 |
| `79:78` | `VIGRAN` | VI Flexible Resource Preferred Granularity | Preferred granularity for assigning/removing VI resources. | Minimizes wasted implementation resources. | Virtualization Management. | Figure 281 |

## Figure 282 / 283 - Secondary Controller List And Entry

CNS: `15h`.

| Structure | Offset | Field | Full Name | Meaning | Affects | Source |
|---|---|---|---|---|---|---|
| Secondary Controller List | `00` | `N` | Number of Identifiers | Number of Secondary Controller Entries, up to 127. `0h` means no entries. | List parsing. | Figure 282 |
| Secondary Controller List | `31:01` | - | Reserved | Reserved. | None. | Figure 282 |
| Secondary Controller List | `N*32+63:N*32+32` | Entry N | Secondary Controller Entry | N+1th entry, if present. | Secondary controller topology. | Figure 282 |
| Secondary Controller Entry | `01:00` | `SCID` | Secondary Controller Identifier | Controller Identifier of the secondary controller. | Virtualization Management. | Figure 283 |
| Secondary Controller Entry | `03:02` | `PCID` | Primary Controller Identifier | Associated primary controller identifier. | Virtualization Management. | Figure 283 |
| Secondary Controller Entry | `04` | `SCS` | Secondary Controller State | Bit 0 set means Online; clear means Offline. | Secondary controller state. | Figure 283 |
| Secondary Controller Entry | `09:08` | `VFN` | Virtual Function Number | SR-IOV VF number if secondary controller is an SR-IOV VF; otherwise `0h`. | SR-IOV. | Figure 283 |
| Secondary Controller Entry | `11:10` | `NVQ` | Number of VQ Flexible Resources Assigned | VQ resources assigned to the secondary controller. | Virtualization resources. | Figure 283 |
| Secondary Controller Entry | `13:12` | `NVI` | Number of VI Flexible Resources Assigned | VI resources assigned to the secondary controller. | Virtualization resources. | Figure 283 |

## Figure 284 / 285 - UUID List And Entry

CNS: `17h`.

| Structure | Offset | Field | Full Name | Meaning | Key Bits / Values | Affects | Source |
|---|---|---|---|---|---|---|
| UUID List | `31:00` | - | Reserved | Reserved. | Reserved. | None. | Figure 284 |
| UUID List | `63:32` | UUID 1 | UUID List Entry 1 | First UUID List Entry. | Shall be non-zero if `CTRATT.UUID List=1`. | UUID Index. | Figure 284 |
| UUID List | `4063:64` | UUID 2-126 | UUID List Entries 2-126 | Additional UUID entries, if present. | `0h` entry indicates end of list. | UUID Index. | Figure 284 |
| UUID List | `4095:4064` | UUID 127 | UUID List Entry 127 | Last entry. | Shall be cleared to `0h`. | UUID Index. | Figure 284 |
| UUID Entry | `00` | - | UUID List Entry Header | Reports association between UUID and vendor identity. | Bits `1:0` association; bits `7:2` reserved. | UUID interpretation. | Figure 285 |
| UUID Entry | `15:01` | - | Reserved | Reserved. | Reserved. | None. | Figure 285 |
| UUID Entry | `31:16` | UUID | Universally Unique Identifier | 128-bit UUID as specified in RFC 4122. | Non-zero and not NVMe Invalid UUID means valid UUID. | UUID Index. | Figure 285 |

| Header Bits `1:0` | Meaning |
|---|---|
| `00b` | No association reported. |
| `01b` | UUID associated with vendor in `VID`. |
| `10b` | UUID associated with vendor in `SSVID`. |
| `11b` | Reserved. |

## Figure 286 / 287 - Domain List And Domain Attributes Entry

CNS: `18h`.

| Structure | Offset | Field | Full Name | Meaning | Affects | Source |
|---|---|---|---|---|---|---|
| Domain List | `00` | `N` | Number of Identifiers | Number of Domain Attributes Entries, up to 31. `0h` means no entries. | List parsing. | Figure 286 |
| Domain List | `127:01` | - | Reserved | Reserved. | None. | Figure 286 |
| Domain List | `N*128+255:N*128+128` | Entry N | Domain Attributes Entry | N+1th entry, if present. | Domain attributes. | Figure 286 |
| Domain Attributes Entry | `01:00` | - | Domain Identifier | Identifier of accessible Domain described by this entry. | Domain selection. | Figure 287 |
| Domain Attributes Entry | `31:16` | - | Total Domain Capacity | Total NVM capacity in this Domain, in bytes. | Capacity reporting. | Figure 287 |
| Domain Attributes Entry | `47:32` | - | Unallocated Domain Capacity | Unallocated NVM capacity in this Domain, in bytes. | Capacity reporting. | Figure 287 |
| Domain Attributes Entry | `63:48` | - | Max Endurance Group Domain Capacity | Max capacity of a single Endurance Group in this Domain. `0h` means not reported. | Capacity Management. | Figure 287 |

## Figure 288 - Endurance Group List

CNS: `19h`.

| Offset | Field | Full Name | Meaning | Affects | Source |
|---|---|---|---|---|---|
| `01:00` | `N` | Number of Identifiers | Number of Endurance Group Identifiers in the list, up to 2,047. `0h` means no identifiers. | List parsing. | Figure 288 |
| `03:02` | Identifier 0 | Endurance Group Identifier 0 | First identifier, if any. | Endurance Group selection. | Figure 288 |
| `N*2+1:N*2` | Identifier N-1 | Endurance Group Identifier N-1 | Last identifier. | Endurance Group selection. | Figure 288 |

If CDW11.ENDGID is greater than `ENDGIDMAX`, the command completes successfully and returns an empty Endurance Group List.

## Figure 289 / 290 - Identify I/O Command Set Data Structure And Vector

CNS: `1Ch`.

| Structure | Offset / Bits | Field | Full Name | Meaning | Affects | Source |
|---|---|---|---|---|---|---|
| Identify I/O Command Set | `7:0` | Combination 0 | I/O Command Set Combination 0 | First I/O Command Set Vector. If only one I/O Command Set is supported, only one bit is set. | I/O Command Set Profile. | Figure 289 |
| Identify I/O Command Set | `15:8` | Combination 1 | I/O Command Set Combination 1 | Second vector if supported; `0h` means no further combinations. | I/O Command Set Profile. | Figure 289 |
| Identify I/O Command Set | `4095:4088` | Combination 511 | I/O Command Set Combination 511 | Last vector position. | I/O Command Set Profile. | Figure 289 |
| I/O Command Set Vector | `63:3` | - | Reserved | Reserved. | None. | Figure 290 |
| I/O Command Set Vector | `2` | ZNS | Zoned Namespace Command Set | Set if Zoned Namespace Command Set is selected. | ZNS command set. | Figure 290 |
| I/O Command Set Vector | `1` | KV | Key Value Command Set | Set if Key Value Command Set is selected. | Key Value command set. | Figure 290 |
| I/O Command Set Vector | `0` | NVM | NVM Command Set | Set if NVM Command Set is selected. | NVM command set. | Figure 290 |

Only I/O Command Sets with a bit set in the vector selected by the I/O Command Set Profile Feature may be used. Other I/O Command Sets are treated as unsupported.
