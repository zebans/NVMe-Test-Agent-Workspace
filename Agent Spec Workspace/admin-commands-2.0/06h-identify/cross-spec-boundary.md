# Identify - Cross-Spec Boundary

Primary source: NVMe Base Specification 2.0, section 5.17 and Figure 273.

This file marks Identify content that Base Spec 2.0 delegates to another specification or does not expand in this pass.

## Delegated To NVM Command Set Or Logical-Block Command Sets

| CNS | Topic |
|---|---|
| `00h` | Identify Namespace data structure for specified NSID or common namespace capabilities for the NVM Command Set. |
| `11h` | Identify Namespace data structure for an allocated NSID. |
| `16h` | Namespace Granularity List, when applicable to NVM or logical-block command sets. |

## Delegated To Applicable I/O Command Set Specification

| CNS | Topic |
|---|---|
| `05h` | I/O Command Set-specific Identify Namespace data structure. |
| `06h` | I/O Command Set-specific Identify Controller data structure. |
| `1Ah` | I/O Command Set-specific Allocated Namespace ID list. |
| `1Bh` | I/O Command Set-specific Identify Namespace data structure for an allocated NSID. |

## Command Set Identifier Boundary

Figure 274 defines CSI values:

- `00h`: NVM Command Set
- `01h`: Key Value Command Set
- `02h`: Zoned Namespace Command Set
- reserved and vendor-specific ranges

This Base Spec-only pass records the CSI values but does not expand command-set-specific payload layouts.

## Not Expanded In This Pass

- NVM Identify Namespace data structure field layout.
- ZNS Identify Namespace or Controller data structure field layout.
- KV Identify Namespace or Controller data structure field layout.
- Command-set-specific validation rules beyond the Base Spec selector behavior.

## Test-Flow Boundary

If downstream validation needs payload fields for delegated CNS values, it should request the applicable command set specification layer before generating validation details.
