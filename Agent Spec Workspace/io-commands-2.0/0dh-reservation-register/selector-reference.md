# Reservation Register Selector Reference

Source: NVMe Base Specification 2.0, section 7.3, Figure 396.

## Reservation Register Action (`RREGA`)

| RREGA | Action | Meaning |
|---|---|---|
| `000b` | Register Reservation Key | Register `NRKEY`. |
| `001b` | Unregister Reservation Key | Unregister using `CRKEY`. |
| `010b` | Replace Reservation Key | Replace `CRKEY` with `NRKEY`. |
| `011b`-`111b` | Reserved | Invalid. |

## Change Persist Through Power Loss (`CPTPL`)

| CPTPL | Meaning |
|---|---|
| `00b` | No change to PTPL state |
| `01b` | Reserved |
| `10b` | Clear PTPL state: reservations are released and registrants are cleared on power on |
| `11b` | Set PTPL state: reservations and registrants persist across power loss |
