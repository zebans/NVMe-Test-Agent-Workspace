# NVM Dataset Management Selector Reference

| Selector | Location | Values | Meaning |
|---|---|---|---|
| Range count | `CDW10.NR` | Zero-based | Selects how many 16-byte range descriptors are provided. |
| Deallocate request | `CDW11.AD` | `0` no deallocate attribute; `1` deallocate attribute | Requests deallocation of provided ranges. |
| Integral write/read | `CDW11.IDW` / `CDW11.IDR` | Boolean | Advisory integral dataset hints. |
| Range descriptor | Payload | Starting LBA + one-based length | Selects affected LBA ranges. |
| Context attributes | Payload | Access size, WP/SW/SR, latency, frequency | Advisory optimization hints. |

All combinations of attributes in `CDW11` are supported when Dataset Management is supported.
