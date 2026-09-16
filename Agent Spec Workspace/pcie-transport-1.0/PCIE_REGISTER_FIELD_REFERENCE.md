# PCIe Register Field Reference

Status: `COMPLETE`

Source: NVMe over PCIe Transport Specification Revision 1.0 section 3.8 and Figures 10 through 67.

This file records the NVMe-relevant field rules from the PCIe transport layer. PCI and PCIe specifications remain normative for the duplicated PCI/PCIe field definitions; this layer captures the additional NVMe controller requirements and source anchors.

## Register Groups

| Group | Range / base | Figures | Completion level |
|---|---|---|---|
| PCI Header | `00h`-`3Fh` | 10-29 | `COMPLETE` for NVMe-specific requirements and anchors. |
| PCI Power Management Capability | `PMCAP`-`PMCAP+7h` | 30-33 | `COMPLETE` for NVMe-specific requirements and anchors. |
| MSI Capability | `MSICAP`-`MSICAP+14h` | 34-41 | `COMPLETE` for interrupt-mode rules and anchors. |
| MSI-X Capability | `MSIXCAP`-`MSIXCAP+Bh` | 42-46 | `COMPLETE` for interrupt-mode rules and anchors. |
| PCI Express Capability | `PXCAP`-`PXCAP+29h` | 47-57 | `COMPLETE` for NVMe-specific FLR/power/link anchors. |
| Advanced Error Reporting Capability | `AERCAP`-`AERCAP+47h` | 58-67 | `COMPLETE` for error-handling anchors. |

## PCI Header NVMe-Specific Rules

| Symbol | Offset | NVMe-relevant rule |
|---|---:|---|
| `ID` | `00h` | `VID` is PCI-SIG assigned; `DID` is vendor implementation-specific. |
| `CMD` | `04h` | `ID` disables only pin-based INTx, not MSI/MSI-X; `BME` enables bus mastering; `MSE` enables memory-space access to controller registers; `IOSE` controls target I/O space. NVMe shall clear VGA, MWIE, and Special Cycle use. |
| `STS` | `06h` | Capabilities List bit shall indicate capabilities list support; PCI Power Management capability is minimum. `IS` indicates INTx interrupt status. |
| `RID` | `08h` | Hardware stepping; implementation-specific. |
| `CC` | `09h` | Base class `01h`; subclass `08h`; I/O Controllers report PI `02h`; Administrative Controllers report PI `03h`. |
| `CLS` | `0Ch` | Programmed by firmware/OS. |
| `MLT` | `0Dh` | Not applicable to PCIe and hardwired to zero. |
| `HTYPE` | `0Eh` | Header Layout indicates target device layout; MFD indicates multi-function device status. |
| `BIST` | `0Fh` | Optional; if unimplemented, read-only `0h`. |
| `MLBAR` / `BAR0` | `10h` | Lower 32 bits of register memory base address for Controller Properties. Non-prefetchable. |
| `MUBAR` / `BAR1` | `14h` | Upper 32 bits of register memory base address. |
| `BAR2` | `18h` | Optional Index/Data Pair I/O register base if configured as I/O space; vendor-specific if configured as memory space. |
| `BAR3`-`BAR5` | `1Ch`-`27h` | Vendor-specific. |
| `CCPTR` | `28h` | Cleared to zero for NVMe use. |
| `SS` | `2Ch` | Subsystem ID and Subsystem Vendor ID. |
| `EROM` | `30h` | Optional Expansion ROM; if unimplemented, read-only `0h`. |
| `CAP` | `34h` | Points to first PCI capability. |
| `INTR` | `3Ch` | Interrupt Pin and Interrupt Line; ILINE has no hardware action. |
| `MGNT` / `MLAT` | `3Eh` / `3Fh` | Optional legacy timing registers. |

## MSI / MSI-X Rules

| Capability | Field | Rule |
|---|---|---|
| MSI | `MC.PVM` | Indicates per-vector masking support. |
| MSI | `MC.MMC` | Advertises requested number of MSI vectors as power-of-two wrapper. |
| MSI | `MC.MME` | Enables multiple-message MSI count. |
| MSI | `MC.MSIE` | Enables MSI when set. |
| MSI | `MMASK` / `MPEND` | Optional per-vector mask and pending registers. |
| MSI-X | `MXC.MXE` | MSI-X can request service only when MSI Enable is clear. |
| MSI-X | `MXC.FM` | Function Mask prevents MSI-X messages and sets pending state. |
| MSI-X | `MXC.TS` | Table size indicates number of MSI-X vectors minus one. |
| MSI-X | `MTAB` / `MPBA` | Locate MSI-X table and pending bit array using BAR indicator plus offset. |

MSI-X is recommended whenever possible. It is also recommended that the host allocate a unique MSI-X vector for each Completion Queue.

## PCI Express Capability Rules

| Field | Rule |
|---|---|
| `PXCAP.IMN` | Indicates MSI/MSI-X vector used for status-bit interrupts, but this NVMe transport defines no status bits in this capability structure that generate interrupts. |
| `PXDCAP.FLRC` | NVMe controllers shall support Function Level Reset. |
| `PXDC.IFLR` | Write `1` initiates Function Level Reset. |
| `PXDS` | Contains device status including FLR completion-related status. |
| `PXLCAP` / `PXLC` / `PXLS` | Link capability, control, and status fields are PCIe-owned; use this layer as source anchor only. |
| `PXDCAP2` / `PXDC2` | Device Capabilities 2 and Device Control 2 are PCIe-owned; use this layer as source anchor only. |

## AER Rules

| Register | Rule |
|---|---|
| `AERUCES` | Uncorrectable Error Status; sticky behavior is PCIe-defined. |
| `AERUCEM` | Masks uncorrectable errors. Masked errors do not update Header Log or First Error Pointer and are not reported. |
| `AERUCESEV` | Selects severity for uncorrectable errors. |
| `AERCES` | Correctable Error Status. |
| `AERCEM` | Masks correctable errors. |
| `AERCC.FEP` | First Error Pointer indicates first uncorrectable error bit; sticky as described by source. |
| `AERHL` | Header Log. |
| `AERTLP` | Optional TLP Prefix Log. |

## External Normative Boundary

The PCIe transport source duplicates many PCI/PCIe field definitions. For exact PCIe reset semantics, link training, capability-list traversal, MSI/MSI-X table structure details, AER protocol details, and PCIe electrical/protocol behavior, use the PCI Express Base Specification. This markdown is complete for NVMe-over-PCIe transport lookup, not a replacement for the full PCIe base spec.
