# Memory Region and Boot Partition Properties

Status: `FIELD-COMPLETE`

Source: NVM Express Base Specification Revision 2.0, sections 3.1.3.11 through 3.1.3.19 and 3.1.3.22 through 3.1.3.28, Figures 52-60 and 63-69.

## Controller Memory Buffer

### `CMBLOC` - Controller Memory Buffer Location (`38h`)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:12` | `OFST` | RO / implementation | CMB offset from the BAR selected by `BIR`. | Unit is selected by `CMBSZ.SZU`. |
| `11:9` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `8` | `CQDA` | RO / implementation | CMB Queue Dword Alignment. | `1`: a CMB queue address may be dword aligned when Create Queue `PC=1`; `0`: normal PRP1 alignment applies. |
| `7` | `CDMMMS` | RO / implementation | CMB Data Metadata Mixed Memory Support. | `1`: section 8.5's data/metadata mixed-memory restriction is not enforced; `0`: it is enforced. |
| `6` | `CDPCILS` | RO / implementation | CMB Data Pointer and Command Independent Locations Support. | `1`: PRP/SGL lists may be in CMB even when their command is outside CMB; `0`: that restriction is enforced. |
| `5` | `CDPMLS` | RO / implementation | CMB Data Pointer Mixed Locations Support. | `1`: memory associated with one PRP list/SGL may be split across CMB and non-CMB memory; `0`: it must reside wholly in one location class. |
| `4` | `CQPDS` | RO / implementation | CMB Queue Physically Discontiguous Support. | `1`: queues in CMB need not be physically contiguous; `0`: they must be physically contiguous. |
| `3` | `CQMMS` | RO / implementation | CMB Queue Mixed Memory Support. | `1`: memory for one queue may span CMB and non-CMB memory; `0`: a queue placed in CMB resides wholly in CMB. |
| `2:0` | `BIR` | RO / implementation | Base Indicator Register containing the CMB. | Valid encodings are `000b`, `010b`, `011b`, `100b`, and `101b`. |

### `CMBSZ` - Controller Memory Buffer Size (`3Ch`)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:12` | `SZ` | RO / implementation | CMB size in units selected by `SZU`. | `0h` means CMB not supported. |
| `11:8` | `SZU` | RO / implementation | CMB size unit. | `0`: 4 KiB; `1`: 64 KiB; `2`: 1 MiB; `3`: 16 MiB; `4`: 256 MiB; `5`: 4 GiB; `6`: 64 GiB; `7h-Fh` reserved. |
| `7:5` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `4` | `WDS` | RO / implementation | Write data supported in CMB. | CMB usage capability. |
| `3` | `RDS` | RO / implementation | Read data supported in CMB. | CMB usage capability. |
| `2` | `LISTS` | RO / implementation | PRP/SGL lists supported in CMB. | CMB usage capability. |
| `1` | `CQS` | RO / implementation | Completion Queues supported in CMB. | CMB usage capability. |
| `0` | `SQS` | RO / implementation | Submission Queues supported in CMB. | CMB usage capability. |

### `CMBMSC` - CMB Memory Space Control (`50h`)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `63:12` | `CBA` | RW / `0h` | Controller Base Address for CMB memory-space access. | Must not overflow the address space or overlap PMR. |
| `11:2` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
| `1` | `CMSE` | RW / `0b` | CMB Memory Space Enable. | Enables host-supplied addresses to reference CMB at a valid `CBA`; has no effect if `CRE=0`. |
| `0` | `CRE` | RW / `0b` | Capabilities Registers Enabled. | `1`: `CMBLOC` and `CMBSZ` are defined; `0`: both properties are cleared to `0h`. |

`CMBMSC` is not reset by Controller Reset or Function Level Reset; other controller-level reset types reset it.

### `CMBSTS`, `CMBEBS`, and `CMBSWTP`

| Property | Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|---|
| `CMBSTS` (`58h`) | `31:1` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `CMBSTS` | `0` | `CBAI` | RO / `0b` | Controller Base Address Invalid. | Set when `CRE=1`, `CMSE=1`, and `CBA` is invalid; otherwise clear. |
| `CMBEBS` (`5Ch`) | `31:8` | `CMBWBZ` | RO / implementation | CMB write buffer size value. | Scale by `CMBSZU`. |
| `CMBEBS` | `7:5` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `CMBEBS` | `4` | Read Bypass Behavior | RO / implementation | Reports read-bypass behavior. | Qualifies elasticity-buffer behavior. |
| `CMBEBS` | `3:0` | `CMBSZU` | RO / implementation | CMB elasticity-buffer size unit. | `0`: bytes; `1`: KiB; `2`: MiB; `3`: GiB; `4h-Fh` reserved. |
| `CMBSWTP` (`60h`) | `31:8` | `CMBSWTV` | RO / implementation | CMB sustained write-throughput value. | Scale by `CMBSWTU`. |
| `CMBSWTP` | `7:4` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `CMBSWTP` | `3:0` | `CMBSWTU` | RO / implementation | Throughput unit. | `0`: bytes/s; `1`: KiB/s; `2`: MiB/s; `3`: GiB/s; `4h-Fh` reserved. |

## Boot Partition

| Property | Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|---|
| `BPINFO` (`40h`) | `31` | `ABPID` | RO / implementation | Active Boot Partition ID. | Identifies active partition. |
| `BPINFO` | `30:26` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `BPINFO` | `25:24` | `BRS` | RO / implementation | Boot Read Status. | `00b` no request; `01b` in progress; `10b` complete; `11b` error. |
| `BPINFO` | `23:15` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `BPINFO` | `14:0` | `BPSZ` | RO / implementation | Boot Partition size. | Unit is 128 KiB. |
| `BPRSEL` (`44h`) | `31` | `BPID` | RW / implementation | Boot Partition ID selected for read. | Selects partition. |
| `BPRSEL` | `30` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
| `BPRSEL` | `29:10` | `BPROF` | RW / implementation | Boot Partition read offset. | Unit is 4 KiB. |
| `BPRSEL` | `9:0` | `BPRSZ` | RW / implementation | Boot Partition read size. | Unit is 4 KiB. |
| `BPMBL` (`48h`) | `63:12` | `BMBBA` | RW / implementation | Boot Partition Memory Buffer base address. | Destination memory address for the Boot Partition read. |
| `BPMBL` | `11:0` | Reserved | RO / `0h` | Reserved. | Write `0h`. |

## Persistent Memory Region

### `PMRCAP` - Persistent Memory Capabilities (`E00h`)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:25` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `24` | `CMSS` | RO / implementation | Controller Memory Space Supported. | Qualifies PMR controller memory-space behavior and `WDS/RDS`. |
| `23:16` | `PMRTO` | RO / implementation | PMR enable timeout value. | Scale by `PMRTU`. |
| `15:14` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `13:10` | `PMRWBM` | RO / implementation | PMR write-barrier mechanisms supported. | bit 0 memory-read persistence; bit 1 `PMRSTS`-read persistence; bits 3:2 reserved; at least one supported bit is set. |
| `9:8` | `PMRTU` | RO / implementation | PMR timeout unit. | `00b`: 500 ms; `01b`: minutes; `10b-11b` reserved. |
| `7:5` | `BIR` | RO / implementation | Base Indicator Register for PMR. | Valid encodings are `010b`, `011b`, `100b`, and `101b`. |
| `4` | `WDS` | RO / implementation | Write data supported. | Reports `0` when `CMSS=0`. |
| `3` | `RDS` | RO / implementation | Read data supported. | Reports `0` when `CMSS=0`. |
| `2:0` | Reserved | RO / `0h` | Reserved. | Read `0h`. |

### `PMRCTL` and `PMRSTS`

| Property | Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|---|
| `PMRCTL` (`E04h`) | `31:1` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
| `PMRCTL` | `0` | `EN` | RW / `0` | PMR Enable. | Enables or disables PMR. |
| `PMRSTS` (`E08h`) | `31:13` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `PMRSTS` | `12` | `CBAI` | RO / implementation | Controller Base Address Invalid. | `1` means the programmed PMR base is invalid. |
| `PMRSTS` | `11:9` | `HSTS` | RO / implementation | PMR Health Status. | `000b` normal; `001b` restore error; `010b` read-only; `011b` unreliable; `100b-111b` reserved. |
| `PMRSTS` | `8` | `NRDY` | RO / implementation | Not Ready. | `1` means PMR is not ready for access. |
| `PMRSTS` | `7:0` | `ERR` | RO / implementation | Vendor-specific PMR error. | Nonzero is an error; sticky until PCI Function reset. Meaning requires vendor documentation. |

### `PMREBS`, `PMRSWTP`, `PMRMSCL`, and `PMRMSCU`

| Property | Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|---|
| `PMREBS` (`E0Ch`) | `31:8` | `PMRWBZ` | RO / implementation | PMR write buffer size value. | Scale by `PMRSZU`. |
| `PMREBS` | `7:5` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `PMREBS` | `4` | Read Bypass Behavior | RO / implementation | Reports read-bypass behavior. | Qualifies elasticity-buffer behavior. |
| `PMREBS` | `3:0` | `PMRSZU` | RO / implementation | PMR elasticity-buffer size unit. | `0`: bytes; `1`: KiB; `2`: MiB; `3`: GiB; `4h-Fh` reserved. |
| `PMRSWTP` (`E10h`) | `31:8` | `PMRSWTV` | RO / implementation | PMR sustained write-throughput value. | Scale by `PMRSWTU`. |
| `PMRSWTP` | `7:4` | Reserved | RO / `0h` | Reserved. | Read `0h`. |
| `PMRSWTP` | `3:0` | `PMRSWTU` | RO / implementation | Throughput unit. | `0`: bytes/s; `1`: KiB/s; `2`: MiB/s; `3`: GiB/s; Figure 67 explicitly reserves `7h-Fh` but does not assign `4h-6h`, so do not infer those values. |
| `PMRMSCL` (`E14h`) | `31:12` | `CBA` lower | RW / `0h` | Lower 20 bits of the 52-bit PMR Controller Base Address field. | Address must not overflow or overlap CMB. Access as aligned 32 bits. |
| `PMRMSCL` | `11:2` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
| `PMRMSCL` | `1` | `CMSE` | RW / `0b` | Controller Memory Space Enable. | Enables PMR memory-space mapping when the base address is valid. |
| `PMRMSCL` | `0` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
| `PMRMSCU` (`E18h`) | `31:0` | `CBA` upper | RW / `0h` | Upper 32 bits of the 52-bit PMR Controller Base Address field. | Access as aligned 32 bits. |

`PMRMSCL` and `PMRMSCU` are not reset by Controller Reset. Their exact reset behavior for other reset types follows the Base property definitions and controller reset rules.
