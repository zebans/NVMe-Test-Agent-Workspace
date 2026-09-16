# PCIe Transport Behavior Reference

Status: `COMPLETE`

Source: NVMe over PCIe Transport Specification Revision 1.0 sections 3.1 through 3.7 and Annex A.

## Controller Properties And Doorbells

| Topic | Rule |
|---|---|
| BAR mapping | PCIe transport exposes Controller Properties as memory-mapped registers in the address range specified by `MLBAR`/`MUBAR` (`BAR0`/`BAR1`). |
| Register access ordering | Controller registers shall be mapped to memory that supports in-order access and variable access widths. Uncacheable memory is a common way to achieve this. |
| Host access width | Host shall access registers in native width or aligned 32-bit accesses. Violations are undefined behavior. |
| Locked access | Host shall not issue locked accesses to registers. |
| Cross-register access | Accesses targeting portions of two or more registers are not supported. |
| Reserved fields | Reserved registers and reserved bits read as `0h`. |
| Doorbell reads | Host should not read doorbells; returned value is vendor-specific. |
| Non-existent doorbell writes | Writes to non-existent SQ Tail or CQ Head Doorbells have undefined results. |

For the offset, width, applicability, and bit meaning of Base-owned Controller Properties such as `CAP`, `CC`, `CSTS`, `AQA`, and `PMRSTS`, read `..\controller-properties-2.0\README.md`.

## Doorbell Formulas

```text
SQyTDBL = 1000h + ((2y) * (4 << CAP.DSTRD))
CQyHDBL = 1000h + ((2y + 1) * (4 << CAP.DSTRD))
```

| Doorbell | Bits | Meaning |
|---|---|---|
| `SQyTDBL.SQT` | `15:00` | New Submission Queue Tail pointer. The difference from the last SQT write indicates how many commands were added, accounting for rollover. |
| `CQyHDBL.CQH` | `15:00` | New Completion Queue Head pointer. The difference from the last CQH write indicates how many CQ entries are available for controller reuse, accounting for rollover. |

## Queue Model And Command Processing

| Step | PCIe transport behavior |
|---|---|
| 1 | Host places one or more commands in free Submission Queue slots in host memory. |
| 2 | Host writes `SQyTDBL` with new tail pointer. |
| 3 | Controller transfers commands from Submission Queue slots into the controller. Arbitration follows NVMe Base Spec command arbitration. |
| 4 | Controller executes commands; commands may complete out of order. |
| 5 | Controller posts Completion Queue entries and advances the Submission Queue Head pointer in the CQE. Each new CQE inverts Phase Tag relative to previous pass. |
| 6 | Controller may generate an interrupt; interrupt coalescing can suppress per-completion interrupts. |
| 7 | Host consumes CQEs until the Phase Tag indicates no newer entries. |
| 8 | Host writes `CQyHDBL` to indicate processed CQEs. Host may consume multiple entries before updating the head doorbell. |

If a CQE is posted for a command, host software may reuse the command's PRP lists and other resources, except PRP lists for I/O Submission Queues and I/O Completion Queues.

## Create I/O Completion Queue Interrupt Vector

| Field | Rule |
|---|---|
| `CDW11.IV` | PCIe-specific Interrupt Vector for the Completion Queue. |
| MSI-X / multiple MSI | `IV` selects the MSI-X or multiple-message MSI vector. |
| pin-based / single MSI | `IV` shall be `0h`. |
| maximum | MSI-X supports up to 2,048 vectors; value shall not exceed messages supported by `MSICAP.MC.MME` or `MSIXCAP.MXC.TS`. |
| error | If `IV` exceeds supported messages, controller should return `Invalid Interrupt Vector`. |

## Reset Rules

| Reset | PCIe transport behavior |
|---|---|
| Controller Level Reset | In addition to Base Spec reset methods, PCIe Conventional Reset and Function Level Reset initiate Controller Level Reset. |
| PCI register space | In all Controller Level Reset cases except Controller Reset, PCI register space is reset as defined by PCI Express Base Specification. |
| NVM Subsystem Reset | All PCIe links in the NVM Subsystem transition to LTSSM Detect state. |
| FLR support | PCIe Device Capabilities `FLRC` shall indicate Function Level Reset support for NVMe controllers. |

## Interrupt Rules

| Mode | Conditions | Behavior |
|---|---|---|
| Pin-based | MSI disabled and MSI-X disabled | Internal interrupt status drives PCI interrupt line active/inactive. |
| Single MSI | MSI enabled, `MSICAP.MC.MME=000b`, MSI-X disabled | One MSI vector; edge-sensitive MSI message. |
| Multiple MSI | MSI enabled, `MSICAP.MC.MME=001b` through `101b`, MSI-X disabled | Up to 32 MSI vectors; completions aggregate per vector. |
| MSI-X | MSI disabled and MSI-X enabled | Preferred mode; up to 2 KiB vectors; each vector can have unique message data. |

Interrupt status is set when a CQ has unacknowledged entries, the CQ has interrupts enabled, and the relevant interrupt mask is clear. An interrupt for a vector is cleared when host software acknowledges all CQEs for CQs associated with that vector.

Admin Completion Queue interrupts should not be delayed. Interrupt coalescing parameters are provided by NVMe Base Spec Interrupt Coalescing feature; PCIe implementations are required to support Get Features and Set Features for it, but the internal aggregation algorithm is implementation-specific.

For MSI-X, the function mask and vector mask must both be clear before an MSI-X message is generated. If either mask is set, the pending bit is set and the message is generated later after masks clear.

## Power And Error Handling

| Area | Rule |
|---|---|
| Power state selection | Host shall not select a power state consuming more power than PCI Express slot power limit control value from `PXDCAP.CSPLV` and `PXDCAP.CSPLS`. |
| Dynamic Power Allocation | If PCIe DPA is implemented and enabled, maximum NVM subsystem power is the lower of the DPA substate limit and NVMe power state. |
| Error handling | AER support is recommended for robust PCIe error handling. |

## Host Consideration Flow

| Flow | Key points |
|---|---|
| Submit command | Build NVMe SQE using Base Spec Host Annex, write `SQyTDBL`, controller consumes new entries and reports consumed SQ head in completions. |
| Process completion | Use interrupt vector to infer CQ when MSI-X/multiple MSI is active; otherwise inspect CQs. Read CQE, use `DW2.SQID`, `DW3.CID`, and `DW3.SF`, then write `CQyHDBL`. |
| Error completion | If CQE Status Field reports an error, use Base Spec command and queue error handling. |
| Interrupt handling | For pin-based or MSI, host should use `INTMS` in ISR and `INTMC` after deferred CQ processing. |
| MSI masking | During CQ processing, host should mask the CQ's MSI/MSI-X vector to avoid spurious or lost interrupts. |
