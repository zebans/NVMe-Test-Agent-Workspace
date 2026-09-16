# Identify Command - Opcode 06h

This folder contains the Base Spec 2.0-only reference for the Identify Admin command.

Primary source:

```text
NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

## Command Identity

| Item | Value |
|---|---|
| Command | Identify |
| Opcode | `06h` |
| Command set | Admin |
| Section | 5.17 |
| Queue | Admin Submission Queue / Admin Completion Queue |
| Data transfer | `10b`, controller to host |
| Data structure size | 4,096 bytes |
| NSID usage | Depends on CNS value, per Figure 273 |
| Command Set Specific | No, in Figure 138 |

## Summary

The Identify command returns a data buffer that describes information about the NVM subsystem, domain, controller, namespace, namespace lists, or command-set-related structures. The returned data structure is selected by the Controller or Namespace Structure (`CNS`) field in CDW10.

## Files

- [command-facts.md](command-facts.md) - opcode, command dwords, command-control rules, and reading map.
- [selector-reference.md](selector-reference.md) - CNS, CSI, CNTID, NSID, and UUID selector behavior.
- [field-reference.md](field-reference.md) - field/bit/value lookup for Base-owned Identify payloads, including Figures 275-290.
- [payload-reference.md](payload-reference.md) - CNS-to-payload map and payload ownership boundaries.
- [status-reference.md](status-reference.md) - completion, status code, and UUID Index status behavior.
- [cross-spec-boundary.md](cross-spec-boundary.md) - command-set-specific boundaries.
- [COMMAND_CONTENT_AUDIT.md](COMMAND_CONTENT_AUDIT.md) - completeness and self-check status.

## Retired File Policy

Older split or combined files were removed after their content was merged into the files above. Prefer the names in this README for future agent workflows.

## Base Spec Boundaries

This pass does not expand NVM, ZNS, or KV command-set-specific Identify payloads. When Figure 273 delegates a returned data structure to an applicable I/O Command Set specification, this folder marks it as delegated.

## Key Figures

| Figure | Topic |
|---|---|
| Figure 269 | Identify Data Pointer |
| Figure 270 | Identify Command Dword 10 |
| Figure 271 | Identify Command Dword 11 |
| Figure 272 | Identify Command Dword 14 |
| Figure 273 | CNS values |
| Figure 274 | Command Set Identifiers |
| Figure 275 | Identify Controller data structure, I/O Command Set Independent |
| Figure 276 | Power State Descriptor data structure |
| Figure 277 | Namespace Identification Descriptor |
| Figure 278 | NVM Set List |
| Figure 279 | NVM Set Attributes Entry |
| Figure 280 | I/O Command Set Independent Identify Namespace data structure |
| Figure 281 | Primary Controller Capabilities Structure |
| Figure 282 | Secondary Controller List |
| Figure 283 | Secondary Controller Entry |
| Figure 284 | UUID List |
| Figure 285 | UUID List Entry |
| Figure 286 | Domain List |
| Figure 287 | Domain Attributes Entry |
| Figure 288 | Endurance Group List |
| Figure 289 | Identify I/O Command Set data structure |
| Figure 290 | I/O Command Set Vector |
