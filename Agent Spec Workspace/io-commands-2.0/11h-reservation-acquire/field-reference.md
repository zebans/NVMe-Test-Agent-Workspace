# Reservation Acquire Field Reference

Source: NVMe Base Specification 2.0, section 7.2, Figures 391-393.

| Location | Field | Meaning | Important bits | Affects |
|---|---|---|---|---|
| DPTR | Data Pointer | Host data buffer containing Reservation Acquire data structure. | PRP1/PRP2 or SGL1. | Key transfer. |
| CDW10 bits `15:08` | `RTYPE` | Reservation Type to create/preempt. | Values from Figure 394. | Reservation permission model. |
| CDW10 bit `03` | `IEKEY` | Ignore Existing Key. | Must be cleared; if set, invalid field. | Negative tests. |
| CDW10 bits `02:00` | `RACQA` | Reservation Acquire Action. | Acquire, Preempt, Preempt and Abort. | Reservation state transition. |
| Data bytes `07:00` | `CRKEY` | Current Reservation Key. | Checked when `IEKEY=0`. | Key validation. |
| Data bytes `15:08` | `PRKEY` | Preempt Reservation Key. | Used only for Preempt actions. | Preempt target key. |
