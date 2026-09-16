# Sanitize Command Facts

Source: NVMe Base Specification 2.0, section 5.24, Figures 303-305.

## Command Identity

| Item | Value |
|---|---|
| Command | Sanitize |
| Admin opcode | `84h` |
| Data transfer | No data |
| Data pointer | Not used |
| NSID | Not used |
| Primary selector | `CDW10.SANACT` |

## Command Dwords

| Dword | Bits | Field | Meaning | Test/FW impact |
|---|---:|---|---|---|
| CDW10 | 09 | `NDAS` | No-Deallocate After Sanitize. | May prevent deallocation if Identify `SANICAP.NDI=0`; ignored for Exit Failure Mode. |
| CDW10 | 08 | `OIPBP` | Overwrite Invert Pattern Between Passes. | Used only for Overwrite. |
| CDW10 | 07:04 | `OWPASS` | Overwrite Pass Count. | Used only for Overwrite; `0h` means 16 passes. |
| CDW10 | 03 | `AUSE` | Allow Unrestricted Sanitize Exit. | Controls unrestricted vs restricted completion mode; ignored for Exit Failure Mode. |
| CDW10 | 02:00 | `SANACT` | Sanitize Action. | Selects Exit Failure Mode, Block Erase, Overwrite, or Crypto Erase. |
| CDW11 | 31:00 | `OVRPAT` | Overwrite Pattern. | Used only for Overwrite sanitize operation. |

## Completion

If a sanitize operation is started, the Sanitize command completes with Successful Completion after the Sanitize Status log has been updated. The sanitize operation itself continues in the background.
