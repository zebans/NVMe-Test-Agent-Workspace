# Format NVM Cross-Spec Boundary

Source: NVMe Base Specification 2.0, section 5.14.

## Base-Owned

| Area | Base ownership |
|---|---|
| Opcode and command dword layout | `80h`, `NSID`, `CDW10`. |
| Secure erase selector | `SES`. |
| FNA/NSID destructive scope rules | Base section 5.14 with Identify Controller `FNA`. |
| Completion semantics | CQE posted when media format is complete. |
| Base command-specific status | `Invalid Format`. |

## External Or Shared Ownership

| Area | Boundary |
|---|---|
| `PIL`, `PI`, `MSET`, LBA format details | Applicable I/O Command Set spec and Identify Namespace structures. |
| Extended LBA formats | Host Behavior Support `LBAFEE` and command-set-specific Identify data. |
| Security denial behavior | Security / TCG-related specifications may define access denial details. |
| API usage | PyNVMe call syntax belongs to API layer documentation, not this spec folder. |
