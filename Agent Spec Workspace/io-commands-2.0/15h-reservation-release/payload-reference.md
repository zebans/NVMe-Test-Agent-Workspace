# Reservation Release Payload Reference

Source: NVMe Base Specification 2.0, section 7.4, Figure 400.

## Reservation Release Data Structure

| Bytes | Field | Meaning | Used when |
|---:|---|---|---|
| `07:00` | `CRKEY` | Current Reservation Key associated with the host. | Checked when `IEKEY=0`. |
