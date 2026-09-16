# Reservation Release Field Reference

Source: NVMe Base Specification 2.0, section 7.4, Figures 398-400.

| Location | Field | Meaning | Important bits | Affects |
|---|---|---|---|---|
| DPTR | Data Pointer | Host data buffer containing Reservation Release data structure. | PRP1/PRP2 or SGL1. | Key transfer. |
| CDW10 bits `15:08` | `RTYPE` | Reservation Type. | For `RRELA=Release`, shall match current reservation type. | Release validity. |
| CDW10 bit `03` | `IEKEY` | Ignore Existing Key. | Must be cleared; if set, invalid field. | Negative tests. |
| CDW10 bits `02:00` | `RRELA` | Reservation Release Action. | Release or Clear. | Reservation state transition. |
| Data bytes `07:00` | `CRKEY` | Current Reservation Key. | Checked when `IEKEY=0`. | Key validation. |
