# Reservation Register Payload Reference

Source: NVMe Base Specification 2.0, section 7.3, Figure 397.

## Reservation Register Data Structure

| Bytes | Field | Meaning | Used when |
|---:|---|---|---|
| `07:00` | `CRKEY` | Current Reservation Key. | Used for Unregister and Replace; reserved for Register; ignored when `IEKEY=1`. |
| `15:08` | `NRKEY` | New Reservation Key. | Used for Register and Replace; reserved for Unregister. |
