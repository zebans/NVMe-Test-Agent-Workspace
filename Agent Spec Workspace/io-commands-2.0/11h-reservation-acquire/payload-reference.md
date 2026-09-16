# Reservation Acquire Payload Reference

Source: NVMe Base Specification 2.0, section 7.2, Figure 393.

## Reservation Acquire Data Structure

| Bytes | Field | Meaning | Used when |
|---:|---|---|---|
| `07:00` | `CRKEY` | Current Reservation Key associated with the host. | Checked when `IEKEY=0`. |
| `15:08` | `PRKEY` | Preempt Reservation Key. | Used when `RACQA=001b` Preempt or `010b` Preempt and Abort; reserved otherwise. |
