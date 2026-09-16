# Zone Management Receive Command Facts

Source: ZNS 1.1 section 3.4.2, Figures 31-37, and Figure 12 opcode table.

| Item | Value |
|---|---|
| Command | Zone Management Receive |
| Opcode | `7Ah` |
| Command set | Zoned Namespace Command Set |
| CSI | `02h` |
| Submission queue | I/O Submission Queue |
| Data transfer | Controller to host |
| Support | Mandatory for ZNS controllers |
| Namespace | `NSID` used; `FFFFFFFFh` not supported unless explicitly allowed |
| Main selectors | `ZRA`, Reporting Options, Partial Report |

## Required Command Behavior

| Area | Requirement |
|---|---|
| Purpose | Returns a data buffer containing zone information. |
| Returned information | Zone characteristics, zone state, zone capacity, `ZSLBA`, write pointer, and other Zone Descriptor fields. |
| Data pointer | Points to the controller-to-host result buffer. |
| `SLBA` | Identifies an LBA in the lowest numbered zone that the Zone Receive Action operates on. |
| `NUMD` | Zero-based number of dwords to return. |
| Reserved fields | All non-defined command-specific fields are reserved. |
| Completion | Posts a CQE to the associated I/O Completion Queue. |

## Typical Use

Host software may use this command after:

- Zone Management Send indicates Zone Capacity Changed;
- a Zone Descriptor Changed asynchronous event occurs;
- a test needs to read zone state, capacity, start LBA, or write pointer.
