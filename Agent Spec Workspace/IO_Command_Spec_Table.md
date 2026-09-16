# I/O Command Spec Table - NVMe Base Spec 2.0

This table is a root-level spec index for I/O commands defined for use in all I/O Command Sets by NVMe Base Specification 2.0.

Primary source:

```text
NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

Source anchor: Section 7 and Figure 390, "Opcodes for I/O Commands".

This table is not a test flow and does not define implementation API usage.

## Scope

Section 7 states that an I/O command is submitted to an I/O Submission Queue. Figure 390 lists I/O commands defined for use in all I/O Command Sets.

Base Spec 2.0 also states that user data format, end-to-end protection information, and I/O Command Set-specific commands are defined by the applicable I/O Command Set specification.

## Data Transfer Encoding

Figure 390 note 3 defines command data transfer direction:

| Encoding | Meaning |
|---|---|
| `00b` | No data transfer |
| `01b` | Host to controller |
| `10b` | Controller to host |
| `11b` | Bidirectional |

## NSID Rule

Figure 390 note 2 states that all I/O commands use the NSID field. `FFFFFFFFh` is not supported unless a Figure 390 footnote indicates that a specific command does support it.

## Common I/O Commands

| Opcode | Command | Section | Data Transfer | NSID Usage | Base Spec Notes |
|---|---|---:|---|---|---|
| `00h` | Flush | 7.1 | `00b` no data | Used; `FFFFFFFFh` may be supported | Figure 390 note 4 says this command may support NSID `FFFFFFFFh`. Section 7.1 defines VWC-dependent behavior. |
| `0Dh` | Reservation Register | 7.3 | `01b` host to controller | Used | Uses reservation register data structure. |
| `0Eh` | Reservation Report | 7.5 | `10b` controller to host | Used | Returns reservation status data. |
| `11h` | Reservation Acquire | 7.2 | `01b` host to controller | Used | Uses reservation acquire data structure. |
| `15h` | Reservation Release | 7.4 | `01b` host to controller | Used | Uses reservation release data structure. |
| `80h`-`FFh` | Vendor Specific I/O Commands | Vendor-specific | Vendor-specific / encoded by opcode bits | Used | Vendor-specific definitions are outside Base Spec unless standard vendor-specific format applies. |

## Command-Set-Specific Boundary

Opcodes not listed in Figure 390 are I/O Command Set-specific or reserved. Do not treat NVM Read, Write, Compare, Write Zeroes, ZNS commands, or KV commands as Base Spec-owned definitions unless the applicable I/O Command Set specification is also in scope.

## Common I/O Command Submission Requirements

Section 7 states that commands shall only be submitted when:

- the controller is ready as indicated by `CSTS.RDY`; and
- appropriate I/O Submission Queue(s) and I/O Completion Queue(s) have been created.

The common SQE and CQE structures are defined in section 3.3.3 and section 3.3.3.2.

