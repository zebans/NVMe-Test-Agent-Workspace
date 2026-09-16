# MI Source Index

Status: `COMPLETE`

Primary source:

```text
..\..\NVMe Base Spec\2.0\NVMe\NVM-Express-Management-Interface-1.2-2021.06.02-Ratified.md
```

## Section Map

| Topic | Section |
|---|---|
| Introduction, overview, scope | 1 |
| Out-of-band theory of operation | 1.3.1 |
| In-band theory of operation | 1.3.2 |
| Architectural models | 1.4-1.6 |
| Definitions / keywords / byte relationships / references | 1.8-1.11 |
| Physical layer | 2 |
| PCI Express physical layer | 2.1 |
| SMBus/I2C physical layer | 2.2 |
| Error handling | 2.3 |
| Message transport | 3 |
| NVMe-MI messages | 3.1 |
| Common NVMe-MI Message Header and fields | 3.1.1, Figures 17-18 |
| Message Integrity Check | 3.1.1.1, Figures 19-22 |
| Out-of-band message transport | 3.2 |
| In-band tunneling message transport | 3.3 |
| Message servicing model | 4 |
| Request / response messages | 4.1 |
| Out-of-band message servicing model | 4.2 |
| In-band tunneling message servicing model | 4.3 |
| NVMe-MI Send command mapping | 4.3.1 |
| NVMe-MI Receive command mapping | 4.3.2 |
| Management Interface Command Set | 5 |
| NVM Express Admin Command Set through MI | 6 |
| Optional PCIe Command Set | 7 |
| PCIe Configuration Read / Write | 7.1 / 7.2 |
| PCIe I/O Read / Write | 7.3 / 7.4 |
| PCIe Memory Read / Write | 7.5 / 7.6 |
| Management architecture | 8 |
| Out-of-band operational times | 8.1 |
| Vital Product Data | 8.2 |
| Reset | 8.3 |
| Security | 8.4 |

## High-Value Figure Groups

| Figures | Topic |
|---|---|
| 17-22 | NVMe-MI message and MCTP packet fields |
| 23-32 | Message taxonomy, response messages, status, command servicing |
| 33-43 | Control primitives |
| 44-54 | NVMe-MI Send / Receive in-band mapping |
| 55-61 | MI command request/response formats and opcode table |
| 62-113 | Management Interface Command Set commands and data structures |
| 114-125 | NVM Express Admin Command Set through MI |
| 126-130 | PCIe Command Set through MI common format, opcode, and response |
| 131-144 | PCIe Configuration, I/O, and Memory Read/Write command fields |
| 145-173 | Management architecture and VPD structures |
| 174-178 | Appendix examples and subsystem management data |
