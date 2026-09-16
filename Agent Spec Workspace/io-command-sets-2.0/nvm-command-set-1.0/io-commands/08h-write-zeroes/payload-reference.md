# NVM Write Zeroes Payload Reference

Write Zeroes has no host data payload. The command effect is visible through later reads.

| Result surface | Meaning |
|---|---|
| User data after success | Reads return all bytes cleared to `0h` until a write occurs to the LBA range. |
| Non-PI metadata | All bytes cleared to `0h`. |
| Protection information | Updated according to `CDW12.PRINFO`; if `PRACT=0`, PI written to media is all zeroes. |
| `DEAC=1` with compatible `DLFEAT` | Controller should deallocate the logical blocks and still return zero data/metadata values on reads. |

No command-specific returned data buffer is defined for successful Write Zeroes completion.
