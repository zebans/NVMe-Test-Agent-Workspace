# ZNS Expanded Layer Content Audit

Audit date: 2026-06-24

Status: `COMPLETE`

## Layer Role

This folder is the expanded command-control detail layer for ZNS 1.1.

The command-set level index remains:

```text
..\io-command-sets-2.0\ZNS_COMMAND_SET_INDEX.md
```

This folder should not duplicate the full command-set overview. It should provide the detailed per-command markdown that the higher-level index links to.

## Covered Source

| Source area | Coverage |
|---|---|
| ZNS Figure 12 | Opcode ownership and data transfer direction for ZNS-owned commands. |
| ZNS section 3.3 | All ZNS-modified NVM commands expanded into folders. |
| ZNS section 3.4 | All ZNS-owned I/O commands expanded into folders. |
| ZNS Figures 13-21 | ZNS command-specific status values for modified NVM commands captured. |
| ZNS Figures 22-41 | ZNS-owned command field/completion/status details captured or indexed. |
| ZNS Figure 37, Figure 48, Figure 49, sections 5.3-5.6 | Shared command-control model facts captured in `zns-model.md`. |

## Expanded Folders

| Group | Count | Complete for command-control use |
|---|---:|---|
| ZNS-owned commands | 3 | Yes |
| ZNS-modified NVM commands | 9 | Yes |

## File Model Check

| Folder type | Required files | Status |
|---|---|---|
| ZNS-owned commands | `README.md`, `command-facts.md`, `selector-reference.md`, `field-reference.md`, `payload-reference.md`, `status-reference.md`, `restrictions.md`, `cross-spec-boundary.md`, `COMMAND_CONTENT_AUDIT.md` | Present |
| ZNS-modified NVM commands | `README.md`, `command-facts.md`, `selector-reference.md`, `field-reference.md`, `payload-reference.md`, `status-reference.md`, `restrictions.md`, `cross-spec-boundary.md`, `COMMAND_CONTENT_AUDIT.md` | Present |

## Delegated / Out Of Scope

- Full NVM command field definitions for modified NVM commands. Those remain owned by the NVM Command Set specification.
- ZNS model sections that do not affect command-control behavior.
- Full ZNS Identify Namespace byte-for-byte payload validation beyond command-control fields captured in `zns-model.md`.
- PyNVMe API mapping.
- Test-flow setup, ordering, cleanup, or pass/fail script design.

## Completion Notes

The current layer is complete for ZNS command-control and status/restriction lookup. If later tests require byte-for-byte validation of payloads beyond command-control fields, add focused payload files without changing this layer's command-control completeness status.
