# PCIe-Through-MI Field Reference

Status: `FIELD-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 sections 7.1-7.6, Figures 131-144.

## Access Tuple Mapping

| Requested element | Section 7 representation | Completion status |
|---|---|---|
| Operation | `OPC` byte `04`: Configuration, Memory, or I/O Read/Write | Complete |
| Target | `CTLID` bytes `07:06` | Complete |
| Base / address space | Target controller's 4 KiB Configuration Space, or BAR selector in `NMD0[18:16]` for I/O/Memory | Complete as a selector; the MI command does not carry the resolved physical BAR base address |
| Offset | `NMD1` or `NMD2:NMD1`, depending on command | Complete |
| Width | No independent access-width field exists | Not defined by MI Section 7; do not substitute offset width or infer PCIe transaction width |
| Transfer byte count | `LENGTH=NMD0[15:0]` | Complete; number of bytes requested |
| Data | `REQD` for Write; `RESPD` for Read | Complete for MI message placement |

`LENGTH` is a transfer byte count, not proof of one PCIe transaction of that width. The 12-bit/32-bit/64-bit values below describe the size of the `OFFSET` field, not the access width.

## Field Matrix

| Opcode / Command | Location | Field | Bits | Meaning | Important checks | Affects |
|---|---|---|---:|---|---|---|
| `00h` Configuration Read | `NMD0` | `LENGTH` | `15:0` | Number of configuration-space bytes to read. | `OFFSET + LENGTH` must remain within the 4 KiB configuration space. | Response Data size and range validation. |
| `00h` Configuration Read | `NMD1` | `OFFSET` | `11:0` | Starting byte offset in the selected controller's 4 KiB PCIe configuration space. | `NMD1[31:12]` reserved; out-of-range sum returns `04h` with PEL indicating `OFFSET`. | Which PCIe configuration register is returned. |
| `00h` Configuration Read | `NMD2` | Reserved | `31:0` | Not used. | Must remain reserved. | Request validity. |
| `01h` Configuration Write | `NMD0` | `LENGTH` | `15:0` | Number of configuration-space bytes to write. | `OFFSET + LENGTH` must remain within 4,096 bytes. | Request Data size and range validation. |
| `01h` Configuration Write | `NMD1` | `OFFSET` | `11:0` | Starting byte offset in the selected controller's PCIe configuration space. | `NMD1[31:12]` reserved; out-of-range sum returns `04h` with PEL indicating `OFFSET`. | Which PCIe configuration register is modified. |
| `01h` Configuration Write | `NMD2` | Reserved | `31:0` | Not used. | Must remain reserved. | Request validity. |
| `02h` Memory Read | `NMD0` | `LENGTH` | `15:0` | Number of bytes to read from PCIe memory space. | Selected BAR must exist and describe memory space; requested range must fit. | Response Data size. |
| `02h` Memory Read | `NMD0` | `BAR` | `18:16` | Selects the PCI BAR whose memory region is accessed. | Values `0h`-`5h` map to BAR offsets `10h`-`24h`; `6h`-`7h` reserved. For a 64-bit BAR, select its least-significant BAR. | Address-space owner and `Invalid Parameter` checks. |
| `02h` Memory Read | `NMD1` | `OFFSET[31:0]` | `31:0` | Low 32 bits of byte offset into the selected BAR. | Combined with `NMD2`; `OFFSET + LENGTH` must fit the BAR range. | Starting memory byte. |
| `02h` Memory Read | `NMD2` | `OFFSET[63:32]` | `31:0` | High 32 bits of byte offset into the selected BAR. | Combined 64-bit offset is used for range validation. | Starting memory byte. |
| `03h` Memory Write | `NMD0` | `LENGTH` | `15:0` | Number of bytes to write to PCIe memory space. | Request Data size is rounded up to a dword; selected range must fit. | Request Data size. |
| `03h` Memory Write | `NMD0` | `BAR` | `18:16` | Selects the PCI BAR whose memory region is accessed. | Same BAR encoding and memory-region checks as Memory Read. | Address-space owner and `Invalid Parameter` checks. |
| `03h` Memory Write | `NMD1` | `OFFSET[31:0]` | `31:0` | Low 32 bits of byte offset into the selected BAR. | Combined with `NMD2`; `OFFSET + LENGTH` must fit the BAR range. | Starting memory byte. |
| `03h` Memory Write | `NMD2` | `OFFSET[63:32]` | `31:0` | High 32 bits of byte offset into the selected BAR. | Combined 64-bit offset is used for range validation. | Starting memory byte. |
| `04h` I/O Read | `NMD0` | `LENGTH` | `15:0` | Number of bytes to read from PCIe I/O space. | Selected BAR must be an implemented I/O BAR; requested range must fit. | Response Data size. |
| `04h` I/O Read | `NMD0` | `BAR` | `18:16` | Selects the PCI BAR whose I/O region is accessed. | Values `0h`-`5h` map to BAR offsets `10h`-`24h`; `6h`-`7h` reserved. | Address-space owner and `Invalid Parameter` checks. |
| `04h` I/O Read | `NMD1` | `OFFSET` | `31:0` | Starting byte offset into the selected I/O BAR. | `OFFSET + LENGTH` must fit the BAR range. | Starting I/O-space byte. |
| `04h` I/O Read | `NMD2` | Reserved | `31:0` | Not used. | Must remain reserved. | Request validity. |
| `05h` I/O Write | `NMD0` | `LENGTH` | `15:0` | Number of bytes to write to PCIe I/O space. | Request Data size is rounded up to a dword; requested range must fit. | Request Data size. |
| `05h` I/O Write | `NMD0` | `BAR` | `18:16` | Selects the PCI BAR whose I/O region is accessed. | Same BAR encoding and I/O-region checks as I/O Read. | Address-space owner and `Invalid Parameter` checks. |
| `05h` I/O Write | `NMD1` | `OFFSET` | `31:0` | Starting byte offset into the selected I/O BAR. | `OFFSET + LENGTH` must fit the BAR range. | Starting I/O-space byte. |
| `05h` I/O Write | `NMD2` | Reserved | `31:0` | Not used. | Must remain reserved. | Request validity. |

For all I/O and Memory command `NMD0` values, bits `31:19` are reserved.

## Offset Width Summary

| Command family | Offset width | Location |
|---|---:|---|
| Configuration Read/Write | 12-bit | `NMD1[11:0]` |
| I/O Read/Write | 32-bit | `NMD1[31:0]` |
| Memory Read/Write | 64-bit | `NMD2[31:0]` is `OFFSET[63:32]`; `NMD1[31:0]` is `OFFSET[31:0]` |

## BAR Selector

| `BAR` value | PCI Configuration Space BAR offset | PCIe transport name / use |
|---:|---:|---|
| `0h` | `10h` | `BAR0` / `MLBAR`; lower 32 bits of the Controller Properties memory base. |
| `1h` | `14h` | `BAR1` / `MUBAR`; normally the upper 32 bits paired with BAR0. |
| `2h` | `18h` | `BAR2`; optional Index/Data Pair I/O register base when implemented as I/O space, otherwise vendor-specific memory use. |
| `3h` | `1Ch` | `BAR3`; vendor-specific. |
| `4h` | `20h` | `BAR4`; vendor-specific. |
| `5h` | `24h` | `BAR5`; vendor-specific. |
| `6h`-`7h` | Reserved | Invalid defined-field value. |

For a 64-bit BAR, the selector corresponds to the BAR containing the least-significant 32 bits. Selecting a BAR does not by itself prove that it is implemented or that it has the address-space type required by the command.

## Target Interpretation

| Access | MI field tells Codex | Follow-up reference |
|---|---|---|
| Configuration Read/Write | Exact byte offset in the target controller's 4 KiB PCIe configuration space. | `..\..\pcie-transport-1.0\PCIE_REGISTER_FIELD_REFERENCE.md` for PCI Header and NVMe-specific capability rules. |
| I/O Read/Write | BAR selector plus byte offset into an implemented I/O BAR. | PCIe transport BAR field rules; vendor documentation when the selected I/O region is vendor-specific. |
| Memory Read/Write | BAR selector plus 64-bit byte offset into an implemented memory BAR. | PCIe transport controller-property/register references for BAR0/BAR1; vendor documentation for vendor-specific BAR regions. |
