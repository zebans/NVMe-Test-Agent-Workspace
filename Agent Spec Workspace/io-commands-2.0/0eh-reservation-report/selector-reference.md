# Reservation Report Selector Reference

## `CDW10.NUMD`

| Selector | Meaning | Test / FW impact |
|---|---|---|
| `NUMD` | Zero-based number of dwords to transfer. | Drives truncation or full-structure transfer behavior. |

| Requested length | Required behavior |
|---|---|
| Less than Reservation Status structure length | Controller transfers only the specified portion of the structure. |
| Greater than Reservation Status structure length | Controller transfers the complete structure and no additional data. |

## `CDW11.EDS`

| Host Identifier format | `EDS` | Returned structure / status |
|---|---:|---|
| 64-bit Host Identifier | `0` | Valid; return Figure 404 Reservation Status data structure. |
| 64-bit Host Identifier | `1` | Invalid; return `Host Identifier Inconsistent Format`. |
| 128-bit Host Identifier | `0` | Invalid; return `Host Identifier Inconsistent Format`. |
| 128-bit Host Identifier | `1` | Valid; return Figure 405 Extended Reservation Status data structure. |

## High-Signal Rule

`EDS` is not just an output-format preference. It is coupled to the controller Host Identifier format. Tests that change Host Identifier format should verify Reservation Report with both `EDS=0` and `EDS=1`.
