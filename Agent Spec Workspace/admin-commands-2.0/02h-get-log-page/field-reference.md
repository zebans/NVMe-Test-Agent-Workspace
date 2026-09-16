# Get Log Page Field Reference

Source: NVMe Base Specification 2.0, section 5.16.1, Figures 203-267.

This file is optimized for field lookup during tests and firmware debugging. It expands common fields and indexes large families so Codex can jump to the right payload without reopening the full Base Spec.

## LID `00h` - Supported Log Pages

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `000h`-`3FFh` | LID Supported and Effects array | 256 entries, one 4-byte entry per LID. | Entry index equals LID value. | Log discovery and index-offset support tests. |
| entry bits `31:16` | LID Specific Field | Per-LID extra capability. | For `0Dh`, bit 0 indicates Establish Context and Read 512 Bytes of Header support. | Persistent Event Log action support. |
| entry bit `1` | `IOS` | Index Offset Supported. | `1` means `OT=1` index offset is supported for that LID. | Offset/index tests. |
| entry bit `0` | `LSUPP` | LID Supported. | `1` means the log page is supported. | Negative tests for unsupported LIDs. |

## LID `01h` - Error Information

Each entry is 64 bytes.

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `07:00` | Error Count | Count of unique error log entries. | Increments per unique error condition. | Error-log ordering and persistence checks. |
| `09:08` | SQID | Submission Queue Identifier of failed command. | Queue source of the error. | Debugging failed command path. |
| `11:10` | CID | Command Identifier of failed command. | Matches CQE/command CID. | Correlating error to command. |
| `13:12` | Status Field | Status returned for failed command. | Includes SCT/SC plus phase information as encoded by status field. | Expected status verification. |
| `15:14` | Parameter Error Location | Byte/bit location for invalid field. | Byte and bit location when available. | Negative tests for invalid command fields. |
| `23:16` | LBA | Command-set specific LBA info. | Meaning depends on command set. | Media/data errors. |
| `27:24` | Namespace | NSID associated with error. | `FFFFFFFFh` may be command-specific. | Namespace-scoped failure triage. |
| `28` | Vendor Specific Information Available | Vendor log page identifier for more info. | `00h` means no vendor info. | Vendor debug path. |
| `29` | TRTYPE | Transport type for transport-related errors. | Same value model as Discovery `TRTYPE`. | Fabrics/transport debugging. |
| `39:32` | Command Specific Information | Extra command-specific info. | Command-owned. | Deep failure analysis. |
| `41:40` | Transport Type Specific Information | Extra transport-specific info. | Transport-owned. | Fabrics/PCIe transport analysis. |

## LID `02h` - SMART / Health Information

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `00` | Critical Warning | Summary health warning. | bit5 PMR unreliable/read-only; bit4 volatile memory backup failed; bit3 media read-only; bit2 reliability degraded; bit1 temperature threshold; bit0 spare below threshold. | Health and async event tests. |
| `02:01` | Composite Temperature | Composite controller temperature in Kelvin. | `0h` if not reported. | Thermal tests. |
| `03` | Available Spare | Remaining spare capacity percentage. | Compared with threshold. | Endurance/health warning. |
| `04` | Available Spare Threshold | Warning threshold. | Critical warning bit0 may depend on this. | Spare threshold tests. |
| `05` | Percentage Used | Vendor estimate of endurance consumed. | May exceed 100. | Wear reporting. |
| `06` | Endurance Group Critical Warning Summary | Endurance-group health summary. | bit3 namespaces read-only; bit2 reliability degraded; bit0 spare below threshold. | Endurance group tests. |
| `47:32` | Data Units Read | 128-bit counter. | Counts units, not raw bytes. | Lifetime read metrics. |
| `63:48` | Data Units Written | 128-bit counter. | Counts units, not raw bytes. | Lifetime write metrics. |
| `79:64` | Host Read Commands | 128-bit counter. | Command count. | Workload accounting. |
| `95:80` | Host Write Commands | 128-bit counter. | Command count. | Workload accounting. |
| `111:96` | Controller Busy Time | Controller busy time. | Unit defined by spec. | Performance/usage metrics. |
| `127:112` | Power Cycles | Power cycle count. | Persistent counter. | Power-cycle tests. |
| `143:128` | Power On Hours | Power-on hour count. | Persistent counter. | Aging tests. |
| `159:144` | Unsafe Shutdowns | Unsafe shutdown count. | Persistent counter. | Power-loss tests. |
| `175:160` | Media and Data Integrity Errors | Error count. | Media/data integrity failures. | Reliability tests. |
| `191:176` | Number of Error Information Log Entries | Count of Error Information log entries. | Tracks Error Information log. | Error-log consistency checks. |
| `195:192` | Warning Composite Temperature Time | Time above warning threshold. | Thermal history. | Thermal threshold tests. |
| `199:196` | Critical Composite Temperature Time | Time above critical threshold. | Thermal history. | Thermal threshold tests. |
| `201:200` ... `215:214` | Temperature Sensor 1-8 | Individual sensor temperatures. | Figure 208; `0h` means not implemented. | Sensor validation. |
| `219:216` | Thermal Management Temperature 1 Transition Count | TMT1 transitions. | Feature-related. | Thermal management tests. |
| `223:220` | Thermal Management Temperature 2 Transition Count | TMT2 transitions. | Feature-related. | Thermal management tests. |
| `227:224` | Total Time For TMT1 | Time at/above TMT1. | Feature-related. | Thermal management tests. |
| `231:228` | Total Time For TMT2 | Time at/above TMT2. | Feature-related. | Thermal management tests. |

## LID `03h` - Firmware Slot Information

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `00` | Active Firmware Info (`AFI`) | Active and pending firmware slot. | bits6:4 next slot to activate after reset; bits2:0 active slot. | Firmware Commit/Download tests. |
| `15:08` | `FRS1` | Firmware Revision for slot 1. | `0h` if unsupported/invalid. | Slot inventory. |
| `23:16` | `FRS2` | Firmware Revision for slot 2. | `0h` if unsupported/invalid. | Slot inventory. |
| `31:24` ... `63:56` | `FRS3` ... `FRS7` | Firmware Revision for slots 3-7. | `0h` if unsupported/invalid. | Slot inventory. |

## LID `04h` - Changed Namespace List

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `000h` onward | Namespace List | Up to 1,024 changed namespace IDs. | Entries are namespace IDs that changed Identify Namespace data, were added, or were deleted. | Namespace rediscovery after async event or inventory change. |
| entry `0` | Overflow marker | If more than 1,024 namespaces changed, first entry is `FFFFFFFFh`. | Remaining list is zero-filled in overflow case. | Test must treat this as "full rediscovery needed", not as a real NSID. |

## LID `05h` - Commands Supported and Effects

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `000h`-`3FFh` | Admin command effects entries | 256 entries, 4 bytes each, indexed by Admin opcode. | See `Command Effects Entry`. | Command support discovery. |
| `400h`-`7FFh` | I/O command effects entries | 256 entries, 4 bytes each, indexed by I/O opcode. | See `Command Effects Entry`. | I/O command support discovery. |
| entry bits `31:20` | `CSP` | Command Submission and Execution scope. | bit5 NVM subsystem; bit4 Domain; bit3 Endurance Group; bit2 NVM Set; bit1 Controller; bit0 Namespace. | Concurrency and side-effect planning. |
| entry bit `19` | UUID Selection Supported | Command supports UUID selection. | `1` means UUID selection applies. | Vendor/UUID command behavior. |
| entry bits `18:16` | `CSE` | Execution restrictions. | `000` none; `001` no other command to same namespace; `010` no other command to any namespace; others reserved. | Test sequencing. |
| entry bit `4` | `CCC` | Controller capability changed. | Requires host to refresh controller info. | Post-command state refresh. |
| entry bit `3` | `NIC` | Namespace inventory changed. | Namespace list may change. | Namespace rediscovery. |
| entry bit `2` | `NCC` | Namespace capability changed. | Namespace identify data may change. | Identify refresh. |
| entry bit `1` | `LBCC` | LBA format/content changed. | Namespace data format/content may change. | Data destructive/change tests. |
| entry bit `0` | `CSUPP` | Command supported. | `0` means unsupported. | Feature gating. |

## LID `06h` - Device Self-test

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `00` | Current Device Self-test Operation | Current self-test state. | `0` none; `1` short; `2` extended; `Eh` vendor specific; others reserved. | Self-test progress polling. |
| `01` | Current Device Self-test Completion | Completion percentage. | bits6:0 percentage; bit7 reserved. | Timeout/progress checks. |
| `31:04`, repeated | Self-test Result Data Structure | Historical results. | Figure 213. | Self-test history validation. |
| result byte `00` bits `7:4` | Self-test Code | Which test was run. | `1` short; `2` extended; `Eh` vendor. | Result decoding. |
| result byte `00` bits `3:0` | Self-test Result | Outcome. | `0` success; `1` aborted by DST command; `2` reset; `3` namespace removed; `4` Format NVM; `5` fatal/unknown; `6` failed unknown segment; `7` failed indicated segment; `8` unknown abort; `9` sanitize; `F` unused. | Pass/fail interpretation. |
| result byte `01` | Segment Number | Failed segment when available. | Meaningful for indicated segment failure. | Failure localization. |
| result byte `02` | Valid Diagnostic Information | Which result fields are valid. | bit3 SC valid; bit2 SCT valid; bit1 FLBA valid; bit0 NSID valid. | Avoid reading invalid result fields. |

## LID `07h` / `08h` - Telemetry Logs

| LID | Offset | Field | Meaning | Important bits | Affects |
|---|---:|---|---|---|---|
| `07h` | `00` | Log Identifier | Telemetry Host-Initiated log identifier. | Shall be `07h`. | Payload sanity check. |
| `08h` | `00` | Log Identifier | Telemetry Controller-Initiated log identifier. | Shall be `08h`. | Payload sanity check. |
| `07h`/`08h` | `07:05` | IEEE OUI Identifier | Vendor OUI that can interpret telemetry data. | `0h` means no IEEE OUI present. | Vendor decode routing. |
| `07h`/`08h` | `09:08` | Data Area 1 Last Block | Last block for telemetry area 1. | `0h` means area has no data. | Telemetry transfer size. |
| `07h`/`08h` | `11:10` | Data Area 2 Last Block | Last block for telemetry area 2. | Must be >= Area 1 Last Block when non-zero. | Telemetry parser bounds. |
| `07h`/`08h` | `13:12` | Data Area 3 Last Block | Last block for telemetry area 3. | Must be >= Area 2 Last Block when non-zero. | Telemetry parser bounds. |
| `07h`/`08h` | `19:16` | Data Area 4 Last Block | Last block for telemetry area 4. | Used when Log Page Attributes bit 6 / ETDAS support allows area 4. | Extended telemetry size. |
| `07h` | `381` | Host-Initiated Data Generation Number | Increments when controller captures internal state for host-initiated log. | Rolls over from `FFh` to `00h`. | Detecting fresh capture. |
| `08h` | `382` | Controller-Initiated Data Available | Whether saved controller-initiated telemetry exists. | `0` unavailable; `1` available; cleared after successful read with `RAE=0`. | AER/event clear behavior. |
| `08h` | `383` | Controller-Initiated Data Generation Number | Increments when controller initiates capture. | Persistent across power cycles. | Detecting fresh capture. |
| `07h`/`08h` | `511:384` | Reason Identifier | Vendor-specific reason for capture. | Vendor-specific. | Debug routing. |
| `07h`/`08h` | `1023:512` onward | Telemetry Data Blocks | 512-byte telemetry data blocks. | If transfer is not multiple of 512 bytes, controller returns Invalid Field in Command. | Telemetry buffer sizing tests. |

## LID `09h` - Endurance Group Information

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `00` | Critical Warning | Endurance group health warning. | bit3 read-only; bit2 reliability degraded; bit0 spare below threshold. | Endurance group AER/health tests. |
| `01` | `EGFEAT` | Endurance Group features. | bit0 `EGRMEDIA` indicates rotational media storage. | Rotational media behavior. |
| `03` | Available Spare | Endurance group spare percentage. | Compared with threshold. | Health warnings. |
| `04` | Available Spare Threshold | Spare warning threshold. | Threshold for bit0. | Health warnings. |
| `05` | Percentage Used | Endurance consumed estimate. | May exceed 100. | Wear reporting. |
| `07:06` | Domain Identifier | Domain associated with the endurance group. | Domain scope. | Domain tests. |
| `47:32` | Endurance Estimate | Estimated endurance remaining/usage. | 128-bit value. | Endurance metrics. |
| `63:48` | Data Units Read | Read counter. | 128-bit value. | Workload accounting. |
| `79:64` | Data Units Written | Write counter. | 128-bit value. | Workload accounting. |
| `95:80` | Media Units Written | Media write counter. | 128-bit value. | Media wear metrics. |
| `111:96` | Host Read Commands | Host read command count. | 128-bit value. | Workload accounting. |
| `127:112` | Host Write Commands | Host write command count. | 128-bit value. | Workload accounting. |
| `143:128` | Media and Data Integrity Errors | Error count. | 128-bit value. | Reliability tests. |
| `159:144` | Number of Error Information Log Entries | Error log count. | 128-bit value. | Error-log consistency. |
| `175:160` | `TEGCAP` | Total Endurance Group Capacity. | Capacity value. | Capacity tests. |
| `191:176` | `UEGCAP` | Unallocated Endurance Group Capacity. | Capacity value. | Capacity allocation tests. |

## LID `0Ah` / `0Bh` - Predictable Latency Logs

| LID | Offset | Field | Meaning | Important bits | Affects |
|---|---:|---|---|---|---|
| `0Ah` | `00` | Status | Current window state. | bits2:0: `000` not used, `001` DTWIN, `010` NDWIN. | Predictable latency state. |
| `0Ah` | `03:02` | Event Type | Latency event flags. | bit0 DTWIN reads warning; bit1 DTWIN writes warning; bit2 DTWIN time warning; bit14 typical/max exceeded; bit15 deterministic excursion. | Event handling. |
| `0Ah` | `39:32` | DTWIN Reads Typical | Typical deterministic read count. | NVM Set specific. | Latency model. |
| `0Ah` | `47:40` | DTWIN Writes Typical | Typical deterministic write count. | NVM Set specific. | Latency model. |
| `0Ah` | `55:48` | DTWIN Time Max | Max deterministic time window. | NVM Set specific. | Timing tests. |
| `0Ah` | `151:128` | Estimates | Read/write/time estimates. | DTWIN estimates. | Runtime prediction checks. |
| `0Bh` | `07:00` | Number of Entries | Count of NVM Set ID entries. | Entries are 2-byte NVM Set IDs. | Event aggregate parsing. |

## LID `0Ch` - Asymmetric Namespace Access

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| CDW10 bit `8` | `RGO` | Return Groups Only. | When set, ANA descriptors return zero NSID count. | ANA partial-read tests. |
| `07:00` | Change Count | ANA state change counter. | Incremented on ANA changes. | Change detection. |
| `09:08` | Number of ANA Group Descriptors | Descriptor count. | Determines parsing length. | ANA parser. |
| descriptor `03:00` | ANA Group ID | ANA group identifier. | Matches namespace ANA group. | Namespace path state. |
| descriptor `07:04` | Number of NSID Values | Number of NSIDs in descriptor. | May be zero when `RGO=1`. | Namespace membership. |
| descriptor `15:08` | Change Count | Per-group change count. | Detects group changes. | ANA change tests. |
| descriptor `16` | ANA State | Current ANA state. | `01h` optimized; `02h` non-optimized; `03h` inaccessible; `04h` persistent loss; `0Fh` change. | Multipath/path selection. |
| descriptor `35:32` onward | NSID list | Namespace IDs in this ANA group. | 4 bytes each. | Namespace membership. |

## LID `0Dh` - Persistent Event Log

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| CDW10 bits `09:08` | Action | Persistent Event Log action. | `00` Read Log Data; `01` Establish Context and Read Log Data; `10` Release Context; `11` Establish Context and Read 512 Bytes Header. | Context lifecycle and error tests. |
| `00` | Log Identifier | Persistent Event Log identifier. | `0Dh`. | Payload sanity check. |
| `07:04` | `TNEV` | Total number of events. | Event count. | Parser loop bound. |
| `15:08` | `TLL` | Total log length. | Length of log. | Transfer sizing. |
| `16` | Log Revision | Persistent Event Log revision. | Base 2.0 uses revision value from Figure 224. | Version handling. |
| `19:18` | Log Header Length | Header size. | Start of event records. | Parser offset. |
| `27:20` | Timestamp | Event-log timestamp. | Timestamp format from Base. | Time correlation. |
| `43:28` | Power On Hours | Power-on hours snapshot. | Persistent counter. | Event context. |
| `51:44` | Power Cycle Count | Power cycle count snapshot. | Persistent counter. | Event context. |
| `53:52` | VID | PCI Vendor ID. | Controller identity. | Vendor matching. |
| `55:54` | SSVID | PCI Subsystem Vendor ID. | Controller identity. | Vendor matching. |
| `75:56` | SN | Serial Number. | Controller identity. | Device matching. |
| `115:76` | MN | Model Number. | Controller identity. | Device matching. |
| `371:116` | SUBNQN | Subsystem NQN. | NVM subsystem identity. | Fabrics/subsystem matching. |
| event byte `00` | Event Type | Type of persistent event. | Figure 226. | Event payload dispatch. |
| event byte `01` | Event Type Revision | Revision of event data. | Event-specific. | Parser versioning. |
| event byte `02` | Event Header Length | Header length for this event. | Start of event data. | Parser offset. |
| event byte `03` | Event Header Additional Info | Additional header flags. | bits1:0 `PIT`. | Timestamp/power-state interpretation. |
| event bytes `05:04` | Controller Identifier | Controller associated with event. | Controller scope. | Multi-controller debugging. |
| event bytes `13:06` | Event Timestamp | Timestamp for event. | Event time. | Ordering/correlation. |
| event bytes `15:14` | `PELPID` | Persistent Event Log Page Identifier. | Event source. | Event correlation. |
| event bytes `21:20` | `VSIL` | Vendor Specific Information Length. | Size of vendor-specific info. | Parser skip length. |
| event bytes `23:22` | `EL` | Event Length. | Size of event data. | Parser length. |

### Persistent Event Types

| Event type | Event | Support | Test/FW use |
|---|---|---|---|
| `01h` | SMART / Health Log Snapshot | Conditional | Captures SMART/Health snapshot event data. |
| `02h` | Firmware Commit | Mandatory | Firmware commit history. |
| `03h` | Timestamp Change | Mandatory | Timestamp update history. |
| `04h` | Power-on or Reset | Mandatory | Reset/power cycle history. |
| `05h` | NVM Subsystem Hardware Error | Mandatory | Hardware error history. |
| `06h` | Change Namespace | Conditional | Namespace management history. |
| `07h` | Format NVM Start | Conditional | Format operation start record. |
| `08h` | Format NVM Completion | Conditional | Format operation completion record. |
| `09h` | Sanitize Start | Conditional | Sanitize start record. |
| `0Ah` | Sanitize Completion | Conditional | Sanitize completion record. |
| `0Bh` | Set Feature | Optional | Feature change history. |
| `0Ch` | Telemetry Log Created | Optional | Telemetry creation history. |
| `0Dh` | Thermal Excursion | Optional | Thermal excursion history. |
| `DEh` | Vendor Specific Event | Optional | Vendor-owned event payload. |
| `DFh` | TCG Defined | Optional | TCG-owned event payload. |

## LID `0Fh` - Endurance Group Event Aggregate

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `07:00` | Number of Entries | Count of Endurance Group Identifier entries. | Entries are 2-byte Endurance Group IDs. | Event aggregate parsing. |

## LID `10h` - Media Unit Status

Source: Figures 248-249.

### Media Unit Status Log

| Offset | Field | Meaning | Important bits / rules | Affects |
|---:|---|---|---|---|
| `01:00` | `NMU` | Number of Media Unit Status Descriptors. | `0h` means no descriptors are reported. | Parser loop bound. |
| `03:02` | `CCHANS` | Number of Channels accessible by the controller. | `0h` means the number of Channels is not reported. | Channel topology discovery. |
| `05:04` | Selected Configuration | Configuration Identifier selected by the most recent successful Capacity Management Select Capacity Configuration operation. | `0h` means no Configuration Identifier is selected. A non-zero value may exist by default if no select operation completed. | Capacity configuration state. |
| `15:06` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `16...` | Media Unit Status Descriptor list | `NMU` descriptors follow the header. | Descriptors may be different lengths; listed in ascending Media Unit Identifier order. | Media unit parsing. |

If Selected Configuration is `0h`, each Media Unit Status Descriptor shall clear `ENDGID`, `NVMSETID`, Capacity Adjustment Factor, and `MUCS` to `0h`.

### Media Unit Status Descriptor

| Descriptor offset | Field | Meaning | Important bits / rules | Affects |
|---:|---|---|---|---|
| `01:00` | Media Unit Identifier | Identifier of the Media Unit. | Values begin at `0h` and increase sequentially. | Descriptor identity. |
| `03:02` | Domain Identifier | Domain containing this Media Unit. | `0h` means not reported; cleared to `0h` if multiple domains are not supported. | Domain-scoped parsing. |
| `05:04` | `ENDGID` | Endurance Group containing this Media Unit. | Must be <= Identify Controller Endurance Group Identifier Maximum; `0h` means not part of an Endurance Group. | Endurance group mapping. |
| `07:06` | `NVMSETID` | NVM Set containing this Media Unit. | Must be <= Identify Controller NVM Set Identifier Maximum; clear to `0h` if NVM Sets are not supported. | NVM Set mapping. |
| `09:08` | Capacity Adjustment Factor | Capacity adjustment factor for the Endurance Group. | `FFFFh` means that value and all higher values; `0h` means not reported. Same `ENDGID` descriptors shall report same value. | Capacity Management. |
| `10` | Available Spare | Normalized remaining spare percentage for the Media Unit. | Relationship to Endurance Group Information spare is outside Base scope. | Media unit health. |
| `11` | Percentage Used | Vendor estimate of life used for the Media Unit. | May exceed 100; values greater than 254 represented as 255; updated once per power-on hour when not sleeping. | Media unit endurance. |
| `12` | `MUCS` | Number of Channels attached to this Media Unit. | `0h` means no Channel Identifiers are reported. | Channel list parsing. |
| `13` | `CIO` | Offset of the Channel 0 Identifier from descriptor start. | Shall be non-zero and a multiple of 16. | Locate channel ID list. |
| `CIO-1:14` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `CIO+1:CIO` | Channel Identifier 0 | First Channel attached to this Media Unit, if any. | Channel Identifiers are listed ascending; each appears only once. | Channel topology. |

Channel Identifier values begin at `0h` and increase sequentially. With multiple domains, values are unique within the specified domain; otherwise they are unique within the NVM subsystem.

## LID `11h` - Supported Capacity Configuration List

Source: Figures 250-254.

### Supported Capacity Configuration List

| Offset | Field | Meaning | Important bits / rules | Affects |
|---:|---|---|---|---|
| `00` | `SCCN` | Number of Supported Capacity Configuration Descriptors. | `0h` means no Capacity Configuration Descriptors are reported. | Parser loop bound. |
| `15:01` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `16...` | Capacity Configuration Descriptor list | `SCCN` descriptors follow the header. | Descriptors may be different lengths. | Capacity configuration parsing. |

### Capacity Configuration Descriptor

| Descriptor offset | Field | Meaning | Important bits / rules | Affects |
|---:|---|---|---|---|
| `01:00` | Capacity Configuration Identifier | Identifier for this capacity configuration. | Used by Capacity Management Select Capacity Configuration. | Configuration selection. |
| `03:02` | Domain Identifier | Domain containing the described Endurance Group configurations. | `0h` means not reported; cleared to `0h` if multiple domains are not supported. | Domain-scoped configuration. |
| `05:04` | `EGCN` | Number of Endurance Group Configuration Descriptors. | `0h` means no Endurance Group Configuration Descriptors are reported. | Parser loop bound. |
| `31:06` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `32...` | Endurance Group Configuration Descriptor list | `EGCN` descriptors follow. | Listed ascending by Endurance Group Identifier; each ENDGID appears only once. | Endurance group layout. |

### Endurance Group Configuration Descriptor

| Descriptor offset | Field | Meaning | Important bits / rules | Affects |
|---:|---|---|---|---|
| `01:00` | `ENDGID` | Endurance Group described by this descriptor. | Value is `>=1h` and <= Identify Controller Endurance Group Identifier Maximum. | Endurance group identity. |
| `03:02` | Capacity Adjustment Factor | Capacity adjustment factor for this Endurance Group. | `FFFFh` means that value and all higher values; `0h` means not reported. | Capacity Management. |
| `15:04` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `31:16` | `TEGCAP` | Total Endurance Group Capacity in bytes. | `0h` means total capacity is not reported. | Capacity validation. |
| `47:32` | `SEGCAP` | Spare Endurance Group Capacity in bytes. | `0h` means spare/unallocated capacity is not reported. | Spare capacity validation. |
| `63:48` | Endurance Estimate | Estimated total bytes writable over lifetime with write amplification of 1. | Unit is billions of bytes; `FFFF...FFFFh` means that value and higher; `0h` means not reported. | Endurance planning. |
| `79:64` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `81:80` | `EGSETS` | Number of NVM Set Identifiers in this descriptor. | `0h` means no NVM Set Identifiers are reported. | NVM Set list parsing. |
| `83:82` onward | NVM Set Identifier list | NVM Set IDs assigned to this Endurance Group. | Listed ascending; each NVM Set Identifier appears only once. | NVM Set mapping. |
| `(EGSETS*2)+83 : (EGSETS*2)+82` | `EGCHANS` | Number of Channel Configuration Descriptors in this Endurance Group Configuration Descriptor. | `0h` means no Channel Configuration Descriptors are reported. | Channel descriptor parsing. |
| after `EGCHANS` | Channel Configuration Descriptor list | `EGCHANS` descriptors follow. | Listed ascending by Channel Identifier; each Channel Identifier appears only once. | Channel topology. |

### Channel Configuration Descriptor

| Descriptor offset | Field | Meaning | Important bits / rules | Affects |
|---:|---|---|---|---|
| `01:00` | Channel Identifier | Identifier of this Channel. | `FFFFh` means Channel Identifier is not specified. | Channel identity. |
| `03:02` | `CHMUS` | Number of Media Units attached to this Channel. | `0h` means no Media Unit Configuration Descriptors are reported. | Media unit list parsing. |
| `04...` | Media Unit Configuration Descriptor list | `CHMUS` descriptors follow. | Listed ascending by Media Unit Identifier; each Media Unit Identifier appears only once. | Media unit topology. |

### Media Unit Configuration Descriptor

| Descriptor offset | Field | Meaning | Important bits / rules | Affects |
|---:|---|---|---|---|
| `01:00` | Media Unit Identifier | Identifier of this Media Unit. | Identifies the Media Unit attached to the Channel. | Media unit identity. |
| `05:02` | Reserved | Reserved. | Do not assign meaning. | Reserved-field checks. |
| `07:06` | `MUDL` | Media Unit Descriptor Length. | Total descriptor length in bytes is `MUDL + 8`; Base 2.0 says this field shall be cleared to `0h`. | Descriptor length parsing. |

## LID `12h` - Feature Identifiers Supported and Effects

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `000h`-`3FFh` | FID effects entries | 256 entries, 4 bytes each, indexed by Feature Identifier. | See FID Effects Entry. | Feature support discovery. |
| entry bits `31:20` | `FSP` | Feature scope. | bit fields mirror command scope style. | Scope and side-effect planning. |
| entry bit `19` | UUID Selection Supported | Feature supports UUID selection. | `1` means UUID selection applies. | UUID feature behavior. |
| entry bit `4` | `CCC` | Controller capability changed. | Refresh controller data. | Post-feature state. |
| entry bit `3` | `NIC` | Namespace inventory changed. | Refresh namespace list. | Namespace rediscovery. |
| entry bit `2` | `NCC` | Namespace capability changed. | Refresh namespace identify data. | Identify refresh. |
| entry bit `1` | `UDCC` | User data content changed. | Data may be affected. | Destructive/change tests. |
| entry bit `0` | `FSUPP` | Feature supported. | `0` means unsupported. | Feature gating. |

## LID `13h` - NVMe-MI Commands Supported and Effects

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `000h`-`3FFh` | NVMe-MI command effects entries | 256 entries, 4 bytes each, indexed by MI opcode. | Figure 258. | MI command support discovery. |
| entry bits `31:20` | `CSP` | Command scope. | Same role as command effects scope. | MI sequencing. |
| entry bit `4` | `CCC` | Controller capability changed. | Refresh controller data. | Post-MI state. |
| entry bit `3` | `NIC` | Namespace inventory changed. | Refresh namespace list. | Namespace rediscovery. |
| entry bit `2` | `NCC` | Namespace capability changed. | Refresh namespace identify data. | Identify refresh. |
| entry bit `1` | `UDCC` | User data content changed. | Data may be affected. | Destructive/change tests. |
| entry bit `0` | `CSUPP` | MI command supported. | `0` means unsupported. | MI feature gating. |

## LID `14h` - Command and Feature Lockdown

| Field | Meaning | Important bits | Affects |
|---|---|---|---|
| CDW10 `CNTTS` | Contents selector. | `00` supported to prohibit; `01` prohibited by Admin SQ; `10` prohibited out-of-band; `11` reserved. | Which lockdown view is returned. |
| CDW10 `SCP` | Scope selector. | `0` Admin opcodes; `2` Feature IDs; `3` MI command opcodes; `4` PCIe command set opcodes. | Which identifier space is listed. |
| Lockdown log payload | Bitmap/table of prohibited or supported identifiers. | Interpretation depends on `CNTTS` and `SCP`. | Negative tests for prohibited operations. |

## LID `15h` / `16h` - Boot Partition and Rotational Media

| LID | Offset | Field | Meaning | Important bits | Affects |
|---|---:|---|---|---|---|
| `15h` | CDW10 bit `08` | Boot Partition Identifier | Selects which boot partition to return. | Other LSP bits reserved. | Boot partition selection. |
| `15h` | `00` | Log Identifier | Boot Partition log identifier. | Shall be `15h`. | Payload sanity check. |
| `15h` | `07:04` bit `31` | `ABPID` | Active Boot Partition ID. | Active boot partition. | Boot partition state checks. |
| `15h` | `07:04` bits `14:00` | `BPSZ` | Boot Partition Data size in multiples of 128 KiB. | Determines data length. | Buffer sizing. |
| `15h` | `BPSZ*128KiB + 15:16` | Boot Partition Data | Contents of selected boot partition. | Read-only through this log. | Boot partition content tests. |
| `16h` | `01:00` | Endurance Group Identifier | Endurance Group selected by CDW11 Log Specific Identifier. | Must match requested Endurance Group. | Rotational media scope. |
| `16h` | `03:02` | Number of Actuators | Actuator count in endurance group. | Count value. | Rotational media geometry. |
| `16h` | `05:04` | Nominal Rotational Speed | Rotational speed in RPM. | `0000h` not reported; `0001h` prohibited; `FFFFh` reserved. | Rotational media feature tests. |
| `16h` | `11:08` | Spinup Count | Successful spinup event count. | Saturates at `FFFFFFFFh`. | Power-state transition history. |
| `16h` | `15:12` | Failed Spinup Count | Failed spinup event count. | Saturates at `FFFFFFFFh`. | Media reliability. |
| `16h` | `19:16` | Load Count | Successful actuator load event count. | Saturates at `FFFFFFFFh`. | Actuator state history. |
| `16h` | `23:20` | Failed Load Count | Failed actuator load event count. | Saturates at `FFFFFFFFh`. | Actuator failure history. |

## LID `70h` - Discovery Log Page

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| log `07:00` | `GENCTR` | Generation counter. | Changes when discovery info changes. | Discovery cache invalidation. |
| log `15:08` | `NUMREC` | Number of records. | Number of discovery entries. | Parser loop bound. |
| log `17:16` | `RECFMT` | Record format. | Base value `0`. | Parser versioning. |
| entry `00` | `TRTYPE` | Transport type. | `01h` RDMA; `02h` FC; `03h` TCP; other values reserved/vendor as defined. | Transport dispatch. |
| entry `01` | `ADRFAM` | Address family. | `01h` IPv4; `02h` IPv6; `03h` InfiniBand; `04h` FC. | Address parser. |
| entry `02` | `SUBTYPE` | Subsystem type. | `01h` discovery referral; `02h` NVM subsystem. | Connection target handling. |
| entry `03` | `TREQ` | Transport requirements. | bit2 SQ flow control disable capable; bits1:0 secure channel requirement. | Connection policy. |
| entry `05:04` | `PORTID` | Port identifier. | Transport port. | Connection endpoint. |
| entry `07:06` | `CNTLID` | Controller ID. | May be `FFFFh` for dynamic allocation. | Controller binding. |
| entry `09:08` | `ASQSZ` | Admin SQ size. | Queue sizing. | Fabrics connection setup. |
| entry `63:32` | `TRSVCID` | Transport service identifier. | Port/service string. | Connection address. |
| entry `511:256` | `SUBNQN` | Subsystem NQN. | NVM subsystem identity. | Target selection. |
| entry `767:512` | `TRADDR` | Transport address. | Address string. | Connection address. |
| entry `1023:768` | `TSAS` | Transport-specific address subtype. | Transport-owned. | RDMA/TCP/FC details. |

## LID `80h` - Reservation Notification

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `07:00` | Log Page Count | Reservation notification log count. | Incrementing counter. | Event tracking. |
| `08` | Reservation Notification Type | Type of reservation event. | `0` empty; `1` registration preempted; `2` reservation released; `3` reservation preempted. | Reservation event handling. |
| `09` | Number of Available Log Pages | Count of available reservation notification log pages. | Queue depth of notifications. | Event drain logic. |
| `15:12` | Namespace ID | Namespace associated with event. | NSID. | Reservation scope. |

## LID `81h` - Sanitize Status

| Offset | Field | Meaning | Important bits | Affects |
|---:|---|---|---|---|
| `01:00` | `SPROG` | Sanitize Progress. | Fraction complete over 65536; `FFFFh` when status is not in-progress as defined. | Sanitize progress polling. |
| `03:02` | `SSTAT` | Sanitize Status. | bit8 Global Data Erased; bits7:3 completed overwrite passes; bits2:0 status. | Sanitize pass/fail interpretation. |
| `03:02` bits `2:0` | Sanitize operation status | Current or final sanitize state. | `000` never sanitized; `001` completed success; `010` in progress; `011` failed; `100` completed success with deallocation for NDAS; others reserved. | Sanitize state machine. |
| `07:04` | `SCDW10` | Command Dword 10 from sanitize operation. | Captures sanitize parameters. | Operation reconstruction. |
| `11:08` | Estimated Time For Overwrite | Estimated overwrite time. | Operation-specific estimate. | Timeout planning. |
| `15:12` | Estimated Time For Block Erase | Estimated block erase time. | Operation-specific estimate. | Timeout planning. |
| `19:16` | Estimated Time For Crypto Erase | Estimated crypto erase time. | Operation-specific estimate. | Timeout planning. |
| `23:20` | Estimated Time For Overwrite With No-Deallocate Media Modification | NDAS/NODMMAS-related estimate. | Operation-specific estimate. | Timeout planning. |
| `27:24` | Estimated Time For Block Erase With No-Deallocate Media Modification | NDAS/NODMMAS-related estimate. | Operation-specific estimate. | Timeout planning. |
| `31:28` | Estimated Time For Crypto Erase With No-Deallocate Media Modification | NDAS/NODMMAS-related estimate. | Operation-specific estimate. | Timeout planning. |

## Reserved And External Ranges

| Range | Meaning | Test/FW rule |
|---|---|---|
| `17h`-`6Fh`, `71h`-`7Fh` | Reserved LID ranges. | No Base-defined payload; do not assign meaning. |
| `0Eh`, `82h`-`BFh` | I/O Command Set specific logs. | Use command-set spec for payload fields. |
| `C0h`-`FFh` | Vendor specific logs. | Use vendor documentation or device-specific expectation. |
