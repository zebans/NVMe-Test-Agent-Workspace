# Base To Command Set Boundary

Status: `BOUNDARY-COMPLETE`

This file records where NVMe Base Specification 2.0 explicitly points to an applicable I/O Command Set specification.

## Core Boundary

Base Spec 2.0 defines common command-set selection and routing. NVM, Key Value, and Zoned Namespace specifications define command-set-specific behavior.

| Base topic | Base source anchor | Boundary fact |
|---|---|---|
| I/O Command Set specific definitions | Sections 1.6 and 1.7 | Terms such as User Data Format and User Data In/Out/Read Access commands are defined in each I/O Command Set specification. LBA examples come from the NVM Command Set specification. |
| Types of NVMe Command Sets | Figure 5 | Base shows Admin, NVM, Key Value, and Zoned Namespace command-set relationship. |
| Namespace command-set association | Section 3.2.1.7 | A namespace is associated with exactly one I/O Command Set. The I/O Command Set for an I/O command is determined by the submission queue association and selected command set. |
| CAP.CSS / CC.CSS | Controller register definitions | `CAP.CSS` reports supported command-set selection modes. `CC.CSS=000b` selects NVM when supported. `CC.CSS=110b` selects all supported I/O Command Sets when `CAP.CSS` bit 6 is set. |
| Command Set Identifiers | Figure 274 | `00h=NVM`, `01h=Key Value`, `02h=Zoned Namespace`. |
| Identify I/O Command Set data structure | Section 5.17.2.21, Figures 289-290 | Implemented when `CAP.CSS` bit 6 is set. It lists supported I/O Command Set combinations and vector bits. |
| I/O Command Set Profile | Section 5.27.1.21, Figures 354-355 | FID `19h` selects an I/O Command Set Combination Index when `CC.CSS=110b`. Unsupported combinations may complete with I/O Command Set Combination Rejected. |
| Identify CNS command-set hooks | Figure 273, sections 5.17.2.5 through 5.17.2.7 and 5.17.2.19 through 5.17.2.21 | CNS `05h`, `06h`, `07h`, `1Ah`, `1Bh`, and `1Ch` use command-set-specific or command-set-selection behavior. |
| Namespace Management create | Section 5.23, Figures 297-300 | CDW11.CSI selects the I/O Command Set for namespace creation. Create data structure fields at bytes `511:384` are command-set-specific and defined by the applicable command-set specification. |
| Format NVM | Section 5.14, Figure 189 | Format fields such as User Data Format selection, PIL, PI, MSET, and command-set-specific format data structure are delegated to the applicable I/O Command Set specification. |
| Get Log Page command | Section 5.16.1, Figure 202 | LID `0Eh` and LID range `82h` to `BFh` include I/O Command Set specific log pages. When `CC.CSS=110b`, CDW14.CSI selects the command set. |
| Get Features / Set Features | Section 5.27, Figure 316 | FID `20h` is Command Set Specific. FID `19h` is the Base-defined I/O Command Set Profile feature. |
| Get LBA Status Admin command | Admin opcode table Figure 138, NVM/ZNS command-set specs | Base lists opcode `86h` as applicable to NVM and ZNS. Details are command-set-specific. |
| Asynchronous events | Base AER / AEC definitions | LBA Status Information Alert and Zone Descriptor Changed are command-set-specific and refer to NVM and ZNS sources respectively. |
| Status values | Base status figures | Some values are explicitly command-set-specific, including I/O Command Set Not Supported, I/O Command Set Not Enabled, I/O Command Set Combination Rejected, Invalid I/O Command Set, and range `80h` to `BFh` for I/O Command Set Specific status codes. |

## Practical Reading Rules

Read Base first when the question is about:

- whether a command set is supported, selected, enabled, or simultaneously usable;
- `CAP.CSS`, `CC.CSS`, `CSI`, `CNS`, `FID 19h`, or Identify I/O Command Set combinations;
- common Admin command routing, NSID rules, or data-pointer shape;
- whether a behavior is delegated.

Read the applicable command-set source when the question is about:

- exact command opcode behavior for NVM, ZNS, or Key Value commands;
- command-set-specific Identify Namespace or Identify Controller data structures;
- command-set-specific Namespace Management create payload fields;
- command-set-specific features or log pages;
- command-specific status values in the `80h` to `BFh` range;
- zone state rules, KV key/value semantics, or NVM logical block semantics.

## Boundary Complete Definition

`BOUNDARY-COMPLETE` means the Base-to-command-set handoff points above have been identified and indexed. It does not mean every command-set-specific field, bit, status condition, or data-structure offset has been expanded.
