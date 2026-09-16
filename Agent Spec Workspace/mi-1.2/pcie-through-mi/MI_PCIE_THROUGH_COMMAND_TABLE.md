# PCIe-Through-MI Command Table

Status: `COMMAND-CONTROL-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 7 and Figure 128.

Legend:

- `O`: Optional.
- `M`: Mandatory.
- `P`: Prohibited from being supported.
- `-`: Reserved opcode.

All six defined commands are optional for both an NVMe Storage Device and an NVMe Enclosure. An implementation may support a subset. Supported optional commands are reported through the Optionally Supported Command List data structure in Figures 98-99.

| Opcode | Command | Storage Device | Enclosure | Data direction | Command-specific fields | Source |
|---:|---|:---:|:---:|---|---|---|
| `00h` | PCIe Configuration Read | O | O | Endpoint to Management Controller | `LENGTH`, 12-bit `OFFSET` | 7.1, Figures 131-132 |
| `01h` | PCIe Configuration Write | O | O | Management Controller to Endpoint | `LENGTH`, 12-bit `OFFSET`, Request Data | 7.2, Figures 133-134 |
| `02h` | PCIe Memory Read | O | O | Endpoint to Management Controller | `BAR`, `LENGTH`, 64-bit `OFFSET` | 7.5, Figures 139-141 |
| `03h` | PCIe Memory Write | O | O | Management Controller to Endpoint | `BAR`, `LENGTH`, 64-bit `OFFSET`, Request Data | 7.6, Figures 142-144 |
| `04h` | PCIe I/O Read | O | O | Endpoint to Management Controller | `BAR`, `LENGTH`, 32-bit `OFFSET` | 7.3, Figures 135-136 |
| `05h` | PCIe I/O Write | O | O | Management Controller to Endpoint | `BAR`, `LENGTH`, 32-bit `OFFSET`, Request Data | 7.4, Figures 137-138 |
| `06h`-`FFh` | Reserved | - | - | n/a | n/a | Figure 128 |

## Mechanism Rules

| Rule | Meaning |
|---|---|
| Message type | The NVMe-MI Message Type field is `4h`, PCIe Command. |
| Out-of-band only | The PCIe Command Set is applicable only through the out-of-band mechanism. |
| In-band prohibition | Every PCIe Command is prohibited through in-band tunneling. |
| Target boundary | Only PCIe configuration, I/O, and memory addresses mapped to the controller selected by `CTLID` may be accessed. These commands do not directly access host memory. |
| Minimum support dependency | If any PCIe Command Set command is supported, PCIe Configuration Read shall be supported. |
| Support discovery | Read the Optionally Supported Command List and match Command Type `NMIMT=4h` plus the PCIe opcode. |

