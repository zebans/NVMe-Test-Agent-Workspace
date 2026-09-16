# ZNS Expanded Command Folder Index

Status: `COMPLETE`

This file indexes detailed ZNS command folders. It is not the command-set level index. For CSI, version check, ZNS Admin behavior, log page, Identify, and Namespace Management summaries, read:

```text
..\io-command-sets-2.0\ZNS_COMMAND_SET_INDEX.md
```

## Identity

| Item | Value |
|---|---|
| Command Set | Zoned Namespace Command Set |
| CSI | `02h` |
| Revision | 1.1 |
| Source | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md` |
| Detailed folder role | Per-command command-control details for ZNS section 3.3 and 3.4. |

## ZNS-Owned Commands

These commands are defined by ZNS section 3.4.

| Opcode | Command | Section | Folder | Status | Read when |
|---:|---|---|---|---|---|
| `79h` | Zone Management Send | 3.4.3 | `commands\79h-zone-management-send` | `COMPLETE + CANONICAL` | Need ZSA, Select All, zone transitions, capacity-changed CQE bit, or Zone Management Send statuses. |
| `7Ah` | Zone Management Receive | 3.4.2 | `commands\7ah-zone-management-receive` | `COMPLETE + CANONICAL` | Need ZRA, Report Zones, Extended Report Zones, Zone Descriptor, zone state/capacity/WP reporting. |
| `7Dh` | Zone Append | 3.4.1 | `commands\7dh-zone-append` | `COMPLETE + CANONICAL` | Need ZSLBA, ALBA completion, Zone Append PI remap, or Zone Append statuses. |

## ZNS-Modified NVM Commands

These commands remain NVM commands for base fields and base semantics. ZNS section 3.3 adds zone-specific restrictions and status values.

| Opcode | Command | ZNS section | Folder | ZNS delta |
|---:|---|---|---|---|
| `00h` | Flush | 3.3.4 | `modified-nvm-commands\00h-flush` | `COMPLETE + CANONICAL`; adds Zone Is Offline condition when volatile write cache conditions apply. |
| `01h` | Write | 3.3.7 | `modified-nvm-commands\01h-write` | `COMPLETE + CANONICAL`; adds zone boundary, zone state, write pointer, and active/open resource status behavior. |
| `02h` | Read | 3.3.5 | `modified-nvm-commands\02h-read` | `COMPLETE + CANONICAL`; adds Zone Boundary Error and Zone Is Offline behavior. |
| `04h` | Write Uncorrectable | 3.3.8 | `modified-nvm-commands\04h-write-uncorrectable` | `COMPLETE + CANONICAL`; adds zone boundary, zone state, write pointer, and active/open resource status behavior. |
| `05h` | Compare | 3.3.1 | `modified-nvm-commands\05h-compare` | `COMPLETE + CANONICAL`; adds zone type requirements and ZNS command-specific status values. |
| `08h` | Write Zeroes | 3.3.9 | `modified-nvm-commands\08h-write-zeroes` | `COMPLETE + CANONICAL`; adds zone boundary, zone state, write pointer, active/open resource status behavior, and deallocation-related boundary note. |
| `09h` | Dataset Management | 3.3.3 | `modified-nvm-commands\09h-dataset-management` | `COMPLETE + CANONICAL`; adds Zone Is Offline abort condition. |
| `0Ch` | Verify | 3.3.6 | `modified-nvm-commands\0ch-verify` | `COMPLETE + CANONICAL`; adds Zone Boundary Error and Zone Is Offline behavior. |
| `19h` | Copy | 3.3.2 | `modified-nvm-commands\19h-copy` | `COMPLETE + CANONICAL`; adds source/destination zone boundary, destination write pointer, and source/destination zone state behavior. |

## Detail File Model

Shared ZNS command-control model facts are centralized in:

```text
zns-model.md
```

Canonical ZNS-owned command folders start with:

```text
README.md
command-facts.md
selector-reference.md
field-reference.md
payload-reference.md
status-reference.md
cross-spec-boundary.md
restrictions.md
COMMAND_CONTENT_AUDIT.md
```

ZNS-modified NVM command folders also use the canonical overlay layout:

```text
README.md
command-facts.md
selector-reference.md
field-reference.md
payload-reference.md
status-reference.md
cross-spec-boundary.md
restrictions.md
COMMAND_CONTENT_AUDIT.md
```

## Boundary Rule

For ZNS-modified NVM commands:

- NVM owns base command fields, base data structures, and base command behavior.
- ZNS owns only the additional zone requirements, restrictions, and command-specific status values listed in ZNS section 3.3.
- If a downstream task needs exact NVM CDW fields, read the NVM Command Set source or NVM command index first, then apply the ZNS folder as an overlay.
