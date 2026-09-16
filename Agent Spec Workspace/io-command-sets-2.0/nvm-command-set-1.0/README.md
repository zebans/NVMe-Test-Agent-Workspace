# NVM Command Set 1.0 Detail Layer

This folder contains expanded command references for NVM Command Set-specific commands and Admin hooks.

## Source

```text
..\..\NVMe Base Spec\2.0\NVM-Express-NVM-Command-Set-Specification-2021.06.02-Ratified-1.md
```

## Expanded Folders

| Area | Folder | Scope |
|---|---|---|
| Admin hook | `admin-commands\86h-get-lba-status` | NVM-specific Get LBA Status fields, descriptor list, `ATYPE`, and LBA Status Information log relationship. |
| I/O commands | `io-commands\01h-write` | NVM Write command fields, payload, PI, DSM hints, and status. |
| I/O commands | `io-commands\02h-read` | NVM Read command fields, payload, PI, DSM hints, and status. |
| I/O commands | `io-commands\04h-write-uncorrectable` | NVM Write Uncorrectable command fields and read-after-mark behavior. |
| I/O commands | `io-commands\05h-compare` | NVM Compare command fields, comparison payload, and Compare Failure behavior. |
| I/O commands | `io-commands\08h-write-zeroes` | NVM Write Zeroes command fields, zero/deallocate behavior, and status. |
| I/O commands | `io-commands\09h-dataset-management` | NVM Dataset Management ranges, context attributes, limits, and deallocated/unwritten behavior. |
| I/O commands | `io-commands\0ch-verify` | NVM Verify command fields, no-transfer behavior, VSL, and read-like status surface. |
| I/O commands | `io-commands\19h-copy` | NVM Copy command fields, source range descriptors, processing limits, and copy status. |

## Shared References

| File | Use when you need |
|---|---|
| `NVM_PI_METADATA_REFERENCE.md` | Shared NVM Protection Information and metadata semantics: `PRINFO`, `PRACT`, `PRCHK`, `STC`, `PIF`, `STS`, `LBSTM`, metadata placement, and PI status mapping. |

## Boundary

Base common I/O commands such as Flush and Reservations remain in `..\..\io-commands-2.0`. ZNS overlays remain in `..\..\zns-command-set-1.1`.
