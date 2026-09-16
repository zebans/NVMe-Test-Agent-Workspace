# Controller Property Index

Status: `COMPLETE`

Source: NVM Express Base Specification Revision 2.0, section 3.1.3, Figure 35.

## Property Map

| Offset / range | Size | I/O Controller | Admin Controller | Discovery Controller | Property | Meaning | Field detail |
|---|---:|---:|---:|---:|---|---|---|
| `00h` | 8 | M | M | M | `CAP` | Controller capabilities exposed to host software. | `CORE_CONTROLLER_PROPERTIES.md` |
| `08h` | 4 | M | M | M | `VS` | NVMe Base specification version implemented by the controller. | `CORE_CONTROLLER_PROPERTIES.md` |
| `0Ch` | 4 | M for memory / R for message | M for memory / R for message | R | `INTMS` | Sets interrupt-vector mask bits for pin-based or MSI interrupts. | `ADMIN_QUEUE_INTERRUPT_PROPERTIES.md` |
| `10h` | 4 | M for memory / R for message | M for memory / R for message | R | `INTMC` | Clears interrupt-vector mask bits for pin-based or MSI interrupts. | `ADMIN_QUEUE_INTERRUPT_PROPERTIES.md` |
| `14h` | 4 | M | M | M | `CC` | Enables/configures controller operation and shutdown. | `CORE_CONTROLLER_PROPERTIES.md` |
| `18h-1Bh` | - | R | R | R | Reserved | No defined property. | This file |
| `1Ch` | 4 | M | M | M | `CSTS` | Reports ready, fatal, shutdown, reset, and paused state. | `CORE_CONTROLLER_PROPERTIES.md` |
| `20h` | 4 | O | O | R | `NSSR` | Requests NVM Subsystem Reset when supported. | `CORE_CONTROLLER_PROPERTIES.md` |
| `24h` | 4 | M for memory / R for message | M for memory / R for message | R | `AQA` | Configures Admin SQ/CQ sizes. | `ADMIN_QUEUE_INTERRUPT_PROPERTIES.md` |
| `28h` | 8 | M for memory / R for message | M for memory / R for message | R | `ASQ` | Configures Admin Submission Queue base address. | `ADMIN_QUEUE_INTERRUPT_PROPERTIES.md` |
| `30h` | 8 | M for memory / R for message | M for memory / R for message | R | `ACQ` | Configures Admin Completion Queue base address. | `ADMIN_QUEUE_INTERRUPT_PROPERTIES.md` |
| `38h` | 4 | O for memory / R for message | O for memory / R for message | R | `CMBLOC` | Locates and qualifies the Controller Memory Buffer. | `MEMORY_REGION_PROPERTIES.md` |
| `3Ch` | 4 | O for memory / R for message | O for memory / R for message | R | `CMBSZ` | Reports CMB size, unit, and supported usages. | `MEMORY_REGION_PROPERTIES.md` |
| `40h` | 4 | O for memory / R for message | O for memory / R for message | R | `BPINFO` | Reports Boot Partition size, status, and active partition. | `MEMORY_REGION_PROPERTIES.md` |
| `44h` | 4 | O for memory / R for message | O for memory / R for message | R | `BPRSEL` | Selects Boot Partition, offset, and read size. | `MEMORY_REGION_PROPERTIES.md` |
| `48h` | 8 | O for memory / R for message | O for memory / R for message | R | `BPMBL` | Supplies Boot Partition destination memory address. | `MEMORY_REGION_PROPERTIES.md` |
| `50h` | 8 | O for memory / R for message | O for memory / R for message | R | `CMBMSC` | Enables CMB memory-space access and sets its controller base address. | `MEMORY_REGION_PROPERTIES.md` |
| `58h` | 4 | O for memory / R for message | O for memory / R for message | R | `CMBSTS` | Reports invalid CMB base address. | `MEMORY_REGION_PROPERTIES.md` |
| `5Ch` | 4 | O for memory / R for message | O for memory / R for message | R | `CMBEBS` | Reports CMB elasticity-buffer size and read-bypass behavior. | `MEMORY_REGION_PROPERTIES.md` |
| `60h` | 4 | O for memory / R for message | O for memory / R for message | R | `CMBSWTP` | Reports CMB sustained write throughput. | `MEMORY_REGION_PROPERTIES.md` |
| `64h` | 4 | O | O | R | `NSSD` | Requests normal or abrupt NVM Subsystem Shutdown. | `CORE_CONTROLLER_PROPERTIES.md` |
| `68h` | 4 | M | M | R | `CRTO` | Reports ready-with-media and ready-independent-of-media timeouts. | `CORE_CONTROLLER_PROPERTIES.md` |
| `6Ch-DFFh` | - | R | R | R | Reserved | No defined Base property. | This file |
| `E00h` | 4 | O for memory / R for message | O for memory / R for message | R | `PMRCAP` | Reports Persistent Memory Region capabilities. | `MEMORY_REGION_PROPERTIES.md` |
| `E04h` | 4 | O for memory / R for message | O for memory / R for message | R | `PMRCTL` | Enables or disables the PMR. | `MEMORY_REGION_PROPERTIES.md` |
| `E08h` | 4 | O for memory / R for message | O for memory / R for message | R | `PMRSTS` | Reports PMR readiness, health, error, and base-address status. | `MEMORY_REGION_PROPERTIES.md` |
| `E0Ch` | 4 | O for memory / R for message | O for memory / R for message | R | `PMREBS` | Reports PMR elasticity-buffer size and read-bypass behavior. | `MEMORY_REGION_PROPERTIES.md` |
| `E10h` | 4 | O for memory / R for message | O for memory / R for message | R | `PMRSWTP` | Reports PMR sustained write throughput. | `MEMORY_REGION_PROPERTIES.md` |
| `E14h` | 4 | O for memory / R for message | O for memory / R for message | R | `PMRMSCL` | Enables PMR memory-space access and supplies lower controller base-address bits. | `MEMORY_REGION_PROPERTIES.md` |
| `E18h` | 4 | O for memory / R for message | O for memory / R for message | R | `PMRMSCU` | Supplies upper controller base-address bits. | `MEMORY_REGION_PROPERTIES.md` |
| `E1Ch-FFFh` | - | R | M | R | Reserved | Figure 35 marks this reserved region mandatory for Admin Controllers; it defines no named field. | This file |
| `1000h-12FFh` | transport-defined | T | T | T | Transport Specific | Base reserves ownership for the applicable transport binding. PCIe uses this area for queue doorbells. | `cross-spec-boundary.md` |
| `1300h+` | vendor-defined | - | - | - | Vendor Specific (Optional) | Meaning requires vendor documentation. | `cross-spec-boundary.md` |

`M`, `O`, `R`, and `T` are Figure 35 applicability classifications. Figure 35 footnotes make `INTMS`, `INTMC`, `AQA`, `ASQ`, `ACQ`, CMB, Boot Partition, and PMR properties available only as shown above for memory-based versus message-based transports.

## Source Discrepancy: INTMC Offset

Figure 35 in the ratified Revision 2.0 PDF prints `Ch` for INTMS and `Fh` for INTMC. Section 3.1.3.3 / Figure 44 define INTMS at `0Ch`; section 3.1.3.4 / Figure 45 define INTMC at `10h`. The canonical routing in this layer uses `0Ch` and `10h` because those offsets are the property-specific definitions and preserve dword alignment. Do not route INTMC to `0Fh`.

