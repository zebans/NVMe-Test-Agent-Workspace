# Admin Queue and Interrupt Properties

Status: `FIELD-COMPLETE`

Source: NVM Express Base Specification Revision 2.0, sections 3.1.3.3 through 3.1.3.4 and 3.1.3.8 through 3.1.3.10, Figures 44-45 and 49-51.

## `INTMS` - Interrupt Mask Set (`0Ch`, 32 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:0` | `IVMS` | RWS / `0h` | Interrupt Vector Mask Set. | Writing `1` masks the corresponding interrupt vector; writing `0` has no effect; reads report current mask state. Applies to pin-based and single/multiple MSI, not MSI-X. |

## `INTMC` - Interrupt Mask Clear (`10h`, 32 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:0` | `IVMC` | RWC / `0h` | Interrupt Vector Mask Clear. | Writing `1` unmasks the corresponding interrupt vector; writing `0` has no effect; reads report current mask state. Applies to pin-based and single/multiple MSI, not MSI-X. |

## `AQA` - Admin Queue Attributes (`24h`, 32 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `31:28` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
| `27:16` | `ACQS` | RW / `0h` | Admin Completion Queue Size, zero based. | Valid queue size is 2 through 4096 entries, encoded as entries minus one. Encoding `0h` means one entry and produces undefined behavior if the controller is then enabled. |
| `15:12` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
| `11:0` | `ASQS` | RW / `0h` | Admin Submission Queue Size, zero based. | Valid queue size is 2 through 4096 entries, encoded as entries minus one. Encoding `0h` means one entry and produces undefined behavior if the controller is then enabled. |

`AQA` is configured while `CC.EN=0`; it is reserved for message-based transports.

## `ASQ` - Admin Submission Queue Base Address (`28h`, 64 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `63:12` | `ASQB` | RW / implementation | Admin Submission Queue Base. | 52 most-significant physical-address bits; address is aligned to the memory page size selected by `CC.MPS`. Configure while `CC.EN=0`. |
| `11:0` | Reserved | RO / `0h` | Reserved. | Write `0h`. |

## `ACQ` - Admin Completion Queue Base Address (`30h`, 64 bits)

| Bits | Field | Type / reset | Meaning | Important values and effects |
|---|---|---|---|---|
| `63:12` | `ACQB` | RW / implementation | Admin Completion Queue Base. | 52 most-significant physical-address bits; address is aligned to `CC.MPS`. This queue uses interrupt vector 0. Configure while `CC.EN=0`. |
| `11:0` | Reserved | RO / `0h` | Reserved. | Write `0h`. |
