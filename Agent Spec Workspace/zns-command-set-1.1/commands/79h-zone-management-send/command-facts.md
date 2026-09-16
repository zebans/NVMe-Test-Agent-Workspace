# Zone Management Send Command Facts

Source: ZNS 1.1 section 3.4.3, Figures 38-41, and Figure 12 opcode table.

| Item | Value |
|---|---|
| Command | Zone Management Send |
| Opcode | `79h` |
| Command set | Zoned Namespace Command Set |
| CSI | `02h` |
| Submission queue | I/O Submission Queue |
| Data transfer | Host to controller |
| Support | Mandatory for ZNS controllers |
| Namespace | `NSID` used; `FFFFFFFFh` not supported unless explicitly allowed |
| Main selectors | `ZSA`, Select All |

## Required Command Behavior

| Area | Requirement |
|---|---|
| Purpose | Requests a zone action on one or more zones. |
| Target zone | If Select All is clear, `SLBA` shall specify the lowest logical block of the target zone. |
| Select All | If set, `SLBA` is ignored and the action applies to all zones matching the action criteria. |
| Data pointer | Used only when the action transfers Zone Descriptor Extension data. |
| Reserved fields | All non-defined command-specific fields are reserved. |
| Completion | Posts a CQE to the associated I/O Completion Queue. |

## State-Changing Effects

Successful Zone Management Send may change:

- zone state;
- Zone Descriptor Extension data;
- Zone Descriptor Extension Valid zone attribute bit;
- write pointer for Reset Zone;
- zone capacity, signaled through CQE Dword 0 bit 0.
