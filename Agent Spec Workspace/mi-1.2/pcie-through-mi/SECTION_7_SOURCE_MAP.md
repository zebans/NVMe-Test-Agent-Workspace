# NVMe-MI Section 7 Source Map

Status: `SOURCE-COMPLETE`

Authoritative local source:

```text
..\..\..\NVMe Base Spec\2.0\NVMe\NVM-Express-Management-Interface-1.2-2021.06.02-Ratified.md
```

The original Section 7 text remains authoritative and is not duplicated wholesale in this derived layer. This map provides direct coverage of every Section 7 subsection and figure so an agent can audit exact source wording without searching the full specification.

## Section And Figure Coverage

| Source | Subject | Derived reference |
|---|---|---|
| Section 7 opening text | Scope, target-controller address spaces, `NMIMT=4h`, OOB-only rule, Lockdown, host-interference warning | `README.md`, `cross-spec-boundary.md`, `status-and-restrictions-reference.md` |
| Figures 126-127 | PCIe Command Request format and byte descriptions | `command-format-reference.md` |
| Figure 128 | Opcode plus Storage Device / Enclosure O/M/P support | `MI_PCIE_THROUGH_COMMAND_TABLE.md` |
| Figures 129-130 | PCIe Command Response format and byte descriptions | `command-format-reference.md` |
| Section 7 common error text | Blocked ranges, Access Denied, PCIe Inaccessible, well-formed request conditions | `status-and-restrictions-reference.md` |
| Section 7.1, Figures 131-132 | PCIe Configuration Read | `field-reference.md` |
| Section 7.2, Figures 133-134 | PCIe Configuration Write | `field-reference.md` |
| Section 7.3, Figures 135-136 | PCIe I/O Read | `field-reference.md` |
| Section 7.4, Figures 137-138 | PCIe I/O Write | `field-reference.md` |
| Section 7.5, Figures 139-141 | PCIe Memory Read | `field-reference.md` |
| Section 7.6, Figures 142-144 | PCIe Memory Write | `field-reference.md` |
| Section 8.1, Figure 145 follow-up | Controller/reset/power/link states that may return PCIe Inaccessible | `status-and-restrictions-reference.md` |
| Section 3.1, Figures 17-18 dependency | Shared NVMe-MI Message Header, request type, `NMIMT`, `CSI`, `CIAP`, `MEB`, MIC | `..\MI_MESSAGE_HEADER_REFERENCE.md` |
| Section 5.7, Figures 90-99 dependency | Optionally Supported Command List discovery | `status-and-restrictions-reference.md` |

## Figure Number Correction

Figure 122 is not the PCIe Command support table. In NVMe-MI 1.2:

| Figure | Actual subject |
|---:|---|
| 122 | Command Messages allowed during sanitize and Format NVM processing; belongs to Admin-through-MI support overlays. |
| 126-127 | PCIe Command request format and fields. |
| 128 | PCIe Command opcode and Storage Device / Enclosure O/M/P support table. |
| 129-130 | PCIe Command response format and fields. |
| 131-144 | Command-specific Configuration, I/O, and Memory Read/Write field definitions. |

## Completeness Boundary

This map covers every rule in MI Section 7 and the shared dependencies required to interpret and construct the request. It does not claim that MI Section 7 defines a PCIe transaction-width field: it defines `LENGTH` in bytes and command-specific offset widths, while lower-level PCIe transaction sizing, Byte Enables, splitting, and TLP behavior remain PCIe-owned.

