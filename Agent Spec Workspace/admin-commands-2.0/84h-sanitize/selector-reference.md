# Sanitize Selector Reference

Source: NVMe Base Specification 2.0, section 5.24, Figure 303.

## Sanitize Action (`SANACT`)

| SANACT | Action | Meaning | Test/FW use |
|---|---|---|---|
| `000b` | Reserved | Invalid. | Negative test. |
| `001b` | Exit Failure Mode | Recover from failed sanitize state when allowed. | Failure recovery tests. |
| `010b` | Start Block Erase | Starts Block Erase sanitize operation. | Operation support depends on Identify `SANICAP`. |
| `011b` | Start Overwrite | Starts Overwrite sanitize operation. | Uses `OWPASS`, `OIPBP`, and `OVRPAT`. |
| `100b` | Start Crypto Erase | Starts Crypto Erase sanitize operation. | Operation support depends on Identify `SANICAP`. |
| `101b`-`111b` | Reserved | Invalid. | Negative test. |

## Modifier Selectors

| Field | Applies to | Meaning |
|---|---|---|
| `NDAS` | Block Erase, Overwrite, Crypto Erase | Requests no deallocation after sanitize when not inhibited. |
| `OIPBP` | Overwrite only | Invert overwrite pattern between passes. |
| `OWPASS` | Overwrite only | Number of overwrite passes; `0h` means 16. |
| `AUSE` | Start actions | Selects unrestricted completion mode when set. |
| `OVRPAT` | Overwrite only | 32-bit overwrite pattern. |
