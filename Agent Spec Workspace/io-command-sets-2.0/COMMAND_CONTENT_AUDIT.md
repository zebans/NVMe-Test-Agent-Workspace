# I/O Command Set Layer Content Audit

Audit date: 2026-06-23

Status: `BOUNDARY-COMPLETE + COMMAND-INDEX-COMPLETE`

## Audited Sources

| Source | Audited for this layer |
|---|---|
| Base Spec 2.0 | Command-set references, CSI map, CAP.CSS/CC.CSS selection, Identify I/O Command Set structure, I/O Command Set Profile, Namespace Management CSI handoff, Format NVM handoff, Get Log Page handoff, Set/Get Features handoff, status boundary. |
| NVM Command Set 1.0 | CSI, opcode table, feature table, log page table, Identify CNS table, expanded Get LBA Status hook, and expanded NVM-specific I/O commands. |
| Zoned Namespace Command Set 1.1 | CSI, command support requirements, opcode table, Zone Append snapshot, ZNS Admin behavior hooks, Changed Zone List log page, Identify CNS table, and link to expanded `..\zns-command-set-1.1` layer. |
| Key Value Command Set 1.0 | CSI, mandatory command support, opcode table, expanded KV commands, KV status values, feature table, log page statement, Identify CNS table, Namespace Management hook. |

## Completion Meaning

`BOUNDARY-COMPLETE` means:

- Base-to-command-set handoff points are identified.
- Command-set selection mechanisms are indexed.
- Delegation points are explicit enough for a future test-flow layer to know when to read Base versus NVM/ZNS/KV.

`COMMAND-INDEX-COMPLETE` means:

- Each local command set has a version row.
- Each local command set has a CSI row.
- Each local command set has an I/O command table.
- Each local command set has key Admin hooks: Identify, feature/log page, and Namespace Management where applicable.
- ZNS-owned commands `79h`, `7Ah`, and `7Dh` have expanded command folders in `..\zns-command-set-1.1\commands`.
- ZNS-modified NVM commands have expanded folders in `..\zns-command-set-1.1\modified-nvm-commands`.
- NVM Get LBA Status has an expanded Admin hook folder in `nvm-command-set-1.0\admin-commands\86h-get-lba-status`.
- NVM-specific I/O commands have expanded folders in `nvm-command-set-1.0\io-commands`.
- KV-specific I/O commands have expanded folders in `key-value-command-set-1.0\io-commands`.

## Expanded Command Folder Status

| Command Set | Command | Status | Notes |
|---|---|---|---|
| NVM | Get LBA Status Admin hook (`86h`) | `COMPLETE` | `SLBA`, `MNDW`, `ATYPE`, `RL`, descriptor list, `CMPC`, and LBA Status Information log relationship captured. |
| NVM | Write (`01h`) | `COMPLETE` | `SLBA`, `NLB`, PI fields, `FUA`, `LR`, Directives, DSM hints, and status captured. |
| NVM | Read (`02h`) | `COMPLETE` | `SLBA`, `NLB`, PI fields, `FUA`, `LR`, DSM hints, read payload, and status captured. |
| NVM | Write Uncorrectable (`04h`) | `COMPLETE` | `SLBA`, `NLB`, `WUSL`, and Unrecovered Read Error aftermath captured. |
| NVM | Compare (`05h`) | `COMPLETE` | Comparison payload, PI fields, Compare Failure, and DULBE interaction captured. |
| NVM | Write Zeroes (`08h`) | `COMPLETE` | `DEAC`, zero readback behavior, `WZSL`, PI restrictions, and status captured. |
| NVM | Dataset Management (`09h`) | `COMPLETE` | Range descriptors, context attributes, processing limits, and deallocated/unwritten behavior captured. |
| NVM | Verify (`0Ch`) | `COMPLETE` | No-transfer integrity check, `VSL`, PI fields, and read-like status captured. |
| NVM | Copy (`19h`) | `COMPLETE` | Source range entries, descriptor formats, copy limits, CQE Dword 0 failure reporting, and status captured. |
| Key Value | Store (`01h`) | `COMPLETE` | `VS`, `SO`, `KL`, key bytes, value payload, atomicity, and Store statuses captured. |
| Key Value | Retrieve (`02h`) | `COMPLETE` | `HBS`, `RO`, `KL`, returned value size in CQE Dword 0, partial retrieval, and statuses captured. |
| Key Value | List (`06h`) | `COMPLETE` | `HBS`, starting key, returned key list structure, ordering/stability boundary, and statuses captured. |
| Key Value | Delete (`10h`) | `COMPLETE` | `KL`, key bytes, atomic delete, `EDNEK` boundary, and statuses captured. |
| Key Value | Exist (`14h`) | `COMPLETE` | `KL`, key bytes, success-as-exists, and absence status semantics captured. |
| ZNS | Zone Management Send (`79h`) | `COMPLETE + STATUS-MATRIX-COMPLETE` | ZSA, Select All, transition matrix summary, CQE bit, and status values captured. |
| ZNS | Zone Management Receive (`7Ah`) | `COMPLETE + DATA-STRUCTURE-COMPLETE` | ZRA, reporting options, Report Zones / Extended Report Zones, and Zone Descriptor key fields captured. |
| ZNS | Zone Append (`7Dh`) | `COMPLETE` | ZSLBA, PI remap, ALBA completion, and status values captured. |
| ZNS-modified NVM | Section 3.3 commands | `COMPLETE` | Compare, Copy, Dataset Management, Flush, Read, Verify, Write, Write Uncorrectable, and Write Zeroes captured. |

## Expanded Coverage

The former command-set gaps are now covered by canonical detailed references:

- NVM per-command fields, payloads, restrictions, and command-specific statuses are under `nvm-command-set-1.0\admin-commands\` and `nvm-command-set-1.0\io-commands\`.
- NVM logical block format, metadata, and protection information are routed through `nvm-command-set-1.0\NVM_PI_METADATA_REFERENCE.md` and the applicable command folder.
- Key Value per-command fields, key/value payloads, restrictions, and statuses are under `key-value-command-set-1.0\io-commands\`.
- ZNS command data structures, statuses, zone-state rules, and modified NVM behavior are under `..\zns-command-set-1.1\`.

This boundary/index layer remains concise by design; detailed facts are owned by those linked command folders rather than duplicated here.

## Self Check

| Check | Result |
|---|---|
| Uses local Base 2.0 bundle only | Pass |
| Identifies NVM/ZNS/KV source versions | Pass |
| Identifies CSI values | Pass |
| Separates Base-owned behavior from command-set-owned behavior | Pass |
| Avoids PyNVMe API calls | Pass |
| Avoids test-flow design | Pass |
| Provides future expansion boundaries | Pass |
