# Reservation Register Field Reference

Source: NVMe Base Specification 2.0, section 7.3, Figures 395-397.

| Location | Field | Meaning | Important bits | Affects |
|---|---|---|---|---|
| DPTR | Data Pointer | Host data buffer containing Reservation Register data structure. | PRP1/PRP2 or SGL1. | Key transfer. |
| CDW10 bits `31:30` | `CPTPL` | Change Persist Through Power Loss state. | `00b` no change; `10b` clear; `11b` set; `01b` reserved. | Reservation persistence. |
| CDW10 bit `03` | `IEKEY` | Ignore Existing Key. | If set, actions that use `CRKEY` succeed regardless of `CRKEY`. | Key-check behavior. |
| CDW10 bits `02:00` | `RREGA` | Reservation Register Action. | Register, Unregister, Replace. | Registrant key state. |
| Data bytes `07:00` | `CRKEY` | Current Reservation Key. | Used for Unregister/Replace unless ignored. | Key validation. |
| Data bytes `15:08` | `NRKEY` | New Reservation Key. | Used for Register/Replace. | New registrant key. |
