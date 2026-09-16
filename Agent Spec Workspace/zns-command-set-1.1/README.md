# ZNS Command Set 1.1 Expanded Layer

Status: `COMPLETE`

This folder is the detailed command-control layer for the local Zoned Namespace Command Set 1.1 source.

For the ZNS command-set level summary, version check, CSI, Admin hooks, log page hooks, Identify hooks, and Namespace Management hook, read:

```text
..\io-command-sets-2.0\ZNS_COMMAND_SET_INDEX.md
```

Use this folder when the question needs exact ZNS command folders, ZNS-modified NVM command deltas, ZNS command-specific status values, or ZNS command restrictions.

## Primary Source

```text
..\NVMe Base Spec\2.0\NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md
```

## Scope

This detailed layer owns:

- ZNS-owned I/O commands defined by ZNS section 3.4.
- NVM Command Set I/O commands modified by ZNS section 3.3.
- ZNS command-specific status values from Figures 13-21, 30, and 40.
- ZNS command restrictions: zone boundary, write pointer, zone state, active/open resources, Select All, and Zone Descriptor Extension command-control behavior.

This detailed layer does not own:

- Base command-set selection (`CAP.CSS`, `CC.CSS`, `CSI`, I/O Command Set Profile).
- ZNS Admin/log/Identify/Namespace Management overview tables; those live in `..\io-command-sets-2.0\ZNS_COMMAND_SET_INDEX.md`.
- PyNVMe API usage.
- Test-flow design.

## Folder Index

| Folder | Purpose |
|---|---|
| `commands\` | ZNS-owned I/O command folders: Zone Management Send, Zone Management Receive, Zone Append. |
| `modified-nvm-commands\` | NVM commands whose behavior/status is modified by ZNS section 3.3. |
| `zns-model.md` | Shared ZNS command-control model facts used by multiple commands. |

## Command Folder Status

| Group | Count | Status |
|---|---:|---|
| ZNS-owned commands | 3 | `COMPLETE` or better |
| ZNS-modified NVM commands | 9 | `COMPLETE` |

## Recommended Reading

For a ZNS-owned command:

```text
1. README.md
2. ZNS_COMMAND_SET_INDEX.md
3. zns-model.md when shared zone model facts are needed
4. commands\<opcode-command>\command-facts.md
5. commands\<opcode-command>\selector-reference.md
6. commands\<opcode-command>\field-reference.md / payload-reference.md / status-reference.md / restrictions.md as needed
```

For a ZNS-modified NVM command:

```text
1. README.md
2. ZNS_COMMAND_SET_INDEX.md
3. zns-model.md when shared zone model facts are needed
4. modified-nvm-commands\<opcode-command>\command-facts.md
5. modified-nvm-commands\<opcode-command>\selector-reference.md
6. modified-nvm-commands\<opcode-command>\status-reference.md
7. NVM Command Set source only when base NVM command fields or base behavior are needed
```

Open the original ZNS source only when the extracted markdown does not contain the needed detail or when exact source wording is required.
