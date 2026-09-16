# NVMe 2.0 I/O Command Set Layer

Status: `BOUNDARY-COMPLETE + COMMAND-INDEX-COMPLETE`

This folder records how NVMe Base Specification 2.0 points into local I/O Command Set specifications, and gives a token-efficient command-set index for NVM, Key Value, and Zoned Namespace.

This layer is intentionally not a complete per-command field reference yet. It answers:

- which command set exists in the local Base 2.0 source bundle;
- which Command Set Identifier (CSI) belongs to each command set;
- which local command-set specification version is referenced by Base Spec 2.0;
- which I/O commands, features, log pages, Identify CNS values, and Namespace Management hooks are owned by each command-set specification;
- where Base Spec 2.0 stops and an applicable command-set specification must be read.

## Source Files

| Scope | Local source |
|---|---|
| Base Spec 2.0 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md` |
| NVM Command Set 1.0 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-NVM-Command-Set-Specification-2021.06.02-Ratified-1.md` |
| Zoned Namespace Command Set 1.1 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md` |
| Key Value Command Set 1.0 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-Key-Value-Command-Set-Specification-1.0-2021.06.02-Ratified-1.md` |

## File Index

| File | Purpose |
|---|---|
| `COMMAND_SET_AGENTS.md` | Agent rules for using this I/O command-set layer without mixing in API or test-flow design. |
| `COMMAND_SET_INDEX.md` | Version, CSI, local source, and high-level command-set map. |
| `BASE_TO_COMMAND_SET_BOUNDARY.md` | Base Spec 2.0 locations that delegate behavior to NVM/ZNS/KV command-set specifications. |
| `NVM_COMMAND_SET_INDEX.md` | NVM Command Set 1.0 command, feature, log, Identify, and Namespace Management index. |
| `nvm-command-set-1.0\` | Expanded NVM command detail layer for NVM-specific I/O commands and Admin hooks. |
| `nvm-command-set-1.0\admin-commands\86h-get-lba-status\` | Expanded NVM Get LBA Status Admin hook with CDW fields, `ATYPE`, returned descriptor list, and LBA Status Information log relationship. |
| `ZNS_COMMAND_SET_INDEX.md` | Zoned Namespace Command Set 1.1 command, feature, log, Identify, and Namespace Management index. |
| `KEY_VALUE_COMMAND_SET_INDEX.md` | Key Value Command Set 1.0 command, feature, log, Identify, and Namespace Management index. |
| `key-value-command-set-1.0\` | Expanded Key Value command detail layer for Store, Retrieve, Delete, Exist, and List. |
| `..\zns-command-set-1.1\` | Expanded ZNS detailed command layer for ZNS-owned and ZNS-modified NVM commands. |
| `COMMAND_CONTENT_AUDIT.md` | Completeness status, source coverage, and remaining expansion boundaries. |

## Recommended Reading

Use this order for command-set questions:

```text
1. ..\SPEC_AGENTS.md
2. README.md
3. COMMAND_SET_INDEX.md
4. BASE_TO_COMMAND_SET_BOUNDARY.md
5. One target command-set index file
6. Original command-set source only when a field/layout/status detail is needed
```

If a question asks for exact CDW bits, data-structure offsets, command-specific status conditions, zone state rules, or key/value option semantics, read the original command-set source section referenced by the relevant index file.

## Expanded Command Folders

| Command Set | Command | Folder | Status |
|---|---|---|---|
| NVM | Get LBA Status Admin hook | `nvm-command-set-1.0\admin-commands\86h-get-lba-status` | `COMPLETE` |
| NVM | Expanded NVM I/O command layer | `nvm-command-set-1.0\io-commands` | `COMPLETE` |
| Key Value | Expanded KV I/O command layer | `key-value-command-set-1.0\io-commands` | `COMPLETE` |
| ZNS | Expanded ZNS command layer | `..\zns-command-set-1.1` | `COMPLETE` |
