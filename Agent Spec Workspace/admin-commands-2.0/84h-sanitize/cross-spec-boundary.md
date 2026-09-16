# Sanitize Cross-Spec Boundary

Source: NVMe Base Specification 2.0, sections 5.24 and 8.21.

## Base-Owned

| Area | Base ownership |
|---|---|
| Opcode and command dwords | `84h`, CDW10, CDW11. |
| Sanitize action selector | `SANACT`. |
| Command acceptance restrictions | PMR, firmware activation, unsupported action, domains, CMB support. |
| Command completion semantics | CQE indicates command accepted/rejected, not operation completion. |
| Command-specific status values | Figure 305 and related global status definitions. |

## Related Base Material

| Area | Boundary |
|---|---|
| Sanitize operation behavior | Section 8.21 owns operation progress, allowed/disallowed command restrictions, and failure behavior details. |
| Sanitize Status Log | Get Log Page `LID=81h` owns progress and final operation status fields. |
| Identify Controller `SANICAP` | Identify owns operation support and no-deallocate capability fields. |
| Set Features Sanitize Config | `FID=17h` owns `NODRM` behavior. |

## API Boundary

This folder does not define PyNVMe call syntax. Use it for expected spec behavior, then use the API layer for command invocation and log parsing.
