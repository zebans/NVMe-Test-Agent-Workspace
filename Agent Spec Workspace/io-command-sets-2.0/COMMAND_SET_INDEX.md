# Command Set Index

Status: `COMMAND-INDEX-COMPLETE`

Base Spec 2.0 references these local I/O Command Set specifications in section 1.8 references.

| Command Set | CSI | Base referenced revision | Local source | Index |
|---|---:|---|---|---|
| NVM Command Set | `00h` | Revision 1.0 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-NVM-Command-Set-Specification-2021.06.02-Ratified-1.md` | `NVM_COMMAND_SET_INDEX.md` |
| Key Value Command Set | `01h` | Revision 1.0 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-Key-Value-Command-Set-Specification-1.0-2021.06.02-Ratified-1.md` | `KEY_VALUE_COMMAND_SET_INDEX.md` |
| Zoned Namespace Command Set | `02h` | Revision 1.1 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md` | `ZNS_COMMAND_SET_INDEX.md` |

## Version Check

| Command Set | Base reference | Local file version signal | Difference found? |
|---|---|---|---|
| NVM | `NVM Express NVM Command Set Specification, Revision 1.0` | Local NVM Command Set source is the 2021.06.02 ratified command-set source and assigns CSI `00h`. | No local Base 2.0 bundle difference found. |
| Key Value | `NVM Express Key Value Command Set Specification, Revision 1.0` | Local Key Value filename and content identify Key Value Command Set 1.0 and assign CSI `01h`. | No local Base 2.0 bundle difference found. |
| Zoned Namespace | `NVM Express Zoned Namespace Command Set Specification, Revision 1.1` | Local ZNS filename and content identify Zoned Namespace Command Set revision 1.1 and assign CSI `02h`. | No local Base 2.0 bundle difference found. |

## CSI Map

Base Spec 2.0 Figure 274 defines:

| CSI | Command Set | Referenced specification |
|---:|---|---|
| `00h` | NVM Command Set | NVM Command Set Specification |
| `01h` | Key Value Command Set | Key Value Command Set Specification |
| `02h` | Zoned Namespace Command Set | Zoned Namespace Command Set Specification |

Base Spec 2.0 Figure 290 defines the I/O Command Set Vector bits:

| Bit | Command Set |
|---:|---|
| 2 | Zoned Namespace Command Set |
| 1 | Key Value Command Set |
| 0 | NVM Command Set |

## Command Ownership Summary

| Command Set | Command model |
|---|---|
| NVM | Defines logical-block I/O commands such as Write, Read, Compare, Dataset Management, Verify, Write Zeroes, Write Uncorrectable, and NVM-specific Admin behavior such as Get LBA Status. |
| Key Value | Defines key/value I/O commands: Store, Retrieve, Delete, Exist, and List. Expanded command folders live under `key-value-command-set-1.0`. It does not use LBA command semantics for those commands. |
| Zoned Namespace | Builds on NVM command semantics, modifies several NVM commands with zone rules, and defines Zone Management Send, Zone Management Receive, and Zone Append. |

## Use In Later Layers

For future test-flow generation, this table should answer which command-set source has authority before a flow asks for exact field values or expected status behavior.

For API mapping, this file is only a spec selector. Concrete API calls belong to the separately maintained API layer, whose entry point is not a prerequisite for SPEC-layer completion.
