# Firmware Image Download Selector Reference

| Selector | Location | Meaning |
|---|---|---|
| Data Pointer | `DPTR` | Start of host data buffer containing image portion. |
| Number of Dwords | `CDW10.NUMD` | Number of dwords to transfer, encoded as a zero-based value. |
| Offset | `CDW11.OFST` | Dword offset from start of firmware image. The first piece has `OFST=0h`. |
| Firmware Update Granularity | Identify Controller `FWUG` | Alignment/granularity requirement for `NUMD` and `OFST`. |

