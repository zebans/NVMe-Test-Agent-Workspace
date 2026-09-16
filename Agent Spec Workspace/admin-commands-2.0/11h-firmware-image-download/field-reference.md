# Firmware Image Download Field Reference

| Location | Field | Meaning | Important values / rules | Affects |
|---|---|---|---|---|
| `DPTR` | Data Pointer | Host buffer containing firmware/Boot Partition image data. | Points to data transferred from host to controller. | Image content transfer. |
| `CDW10` bits 31:00 | `NUMD` | Number of dwords to transfer. | Zero-based; should meet `FWUG` requirement. | Transfer size and `Invalid Field in Command` / overlap behavior. |
| `CDW11` bits 31:00 | `OFST` | Dword offset from start of image. | First piece has `OFST=0h`; should meet `FWUG` requirement. | Image piece placement. |
| Identify Controller | `FWUG` | Firmware Update Granularity. | Defines alignment/granularity for image portions. | Alignment validation. |
| Other command fields | Reserved | No command-specific meaning. | Host should clear. | Reserved-field validation. |

