# Admin-Through-MI Command Format Reference

Status: `FIELD-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 6, Figures 115-118.

## Request Message Layout

| Bytes | Field | Meaning | Important rules | Affects |
|---|---|---|---|---|
| `03:00` | NVMe-MI Message Header | Common MI message header. | See MI section 3.1. | Message routing and integrity behavior. |
| `04` | `OPC` | NVMe Admin command opcode. | Must be listed and allowed by Figure 114. | Selects tunneled Admin command. |
| `05` | `CFLGS` | Command Flags. | Bits `7:2` reserved; bit `1` DOFSTV ignored after MI 1.1; bit `0` DLENV ignored after MI 1.1. | Legacy validity flags; mostly ignored in MI 1.2. |
| `07:06` | `CTLID` | Controller ID target. | Must identify an implemented Controller ID in the NVM subsystem. | Selects target controller. |
| `11:08` | `SQEDW1` | Admin SQE Dword 1. | Defined by Base Admin command. | Admin command semantics. |
| `15:12` | `SQEDW2` | Admin SQE Dword 2. | Defined by Base Admin command. | Admin command semantics. |
| `19:16` | `SQEDW3` | Admin SQE Dword 3. | Defined by Base Admin command. | Admin command semantics. |
| `23:20` | `SQEDW4` | Admin SQE Dword 4. | Defined by Base Admin command. | Admin command semantics. |
| `27:24` | `SQEDW5` | Admin SQE Dword 5. | Defined by Base Admin command. | Admin command semantics. |
| `31:28` | `DOFST` | Data Offset. | For no-data or host-to-endpoint data commands, should be `0h`; for endpoint-to-host response data, selects returned data start offset. Bits `1:0` should be `00b`. | Response data slicing. |
| `35:32` | `DLEN` | Data Length. | No-data commands should use `0h`; data commands should use non-zero length; bits `1:0` should be `00b`; should be <= 4096. | Request/response data length. |
| `43:36` | Reserved | Reserved bytes. | Do not assign command semantics. | Reserved-field checks. |
| `47:44` | `SQEDW10` | Admin SQE Dword 10. | Defined by Base Admin command. | Admin command selectors/fields. |
| `51:48` | `SQEDW11` | Admin SQE Dword 11. | Defined by Base Admin command. | Admin command selectors/fields. |
| `55:52` | `SQEDW12` | Admin SQE Dword 12. | Defined by Base Admin command. | Admin command selectors/fields. |
| `59:56` | `SQEDW13` | Admin SQE Dword 13. | Defined by Base Admin command. | Admin command selectors/fields. |
| `63:60` | `SQEDW14` | Admin SQE Dword 14. | Defined by Base Admin command. | Admin command selectors/fields. |
| `67:64` | `SQEDW15` | Admin SQE Dword 15. | Defined by Base Admin command. | Admin command selectors/fields. |
| `N-1:68` | NVMe Request Data | Optional Admin command data. | Used instead of PRP lists or SGL segments. | Host-to-endpoint Admin payload. |
| `N+3:N` | MIC | Message Integrity Check. | See MI section 3.1. | Message integrity. |

## Response Message Layout

| Bytes | Field | Meaning | Important rules | Affects |
|---|---|---|---|---|
| `03:00` | NVMe-MI Message Header | Common MI message header. | See MI section 3.1. | Response routing and integrity. |
| `04` | Status | MI-defined response status. | See MI section 4.1.2 and `status-boundary-reference.md`. | Indicates wrapper/request validity. |
| `07:05` | Reserved | Reserved bytes. | Do not assign command semantics. | Reserved-field checks. |
| `11:08` | `CQEDW0` | Admin CQE Dword 0. | Defined by Base Admin command. | Command-specific completion result. |
| `15:12` | `CQEDW1` | Admin CQE Dword 1. | Defined by Base Admin command. | Command-specific completion result. |
| `19:16` | `CQEDW3` | Admin CQE Dword 3. | Defined by Base Admin command; Command ID field shall be cleared to `0h`. | NVMe Admin status field and phase/status bits. |
| `N-1:20` | NVMe Response Data | Optional Admin command response data. | Carries selected Admin completion data after any Admin command offset/length and MI `DOFST`/`DLEN` slicing. | Endpoint-to-management-controller payload. |
| `N+3:N` | MIC | Message Integrity Check. | See MI section 3.1. | Message integrity. |

## Data Transfer Rules

| Case | `DOFST` rule | `DLEN` rule | Payload rule |
|---|---|---|---|
| Admin command transfers no data | Should be `0h`. | Should be `0h`. | No NVMe Request Data or Response Data. |
| Management Controller to Management Endpoint | Should be `0h`. | Length of Request Data. | Data is carried in Request Data. |
| Management Endpoint to Management Controller | Starting byte offset into Admin completion data. | Length of returned portion. | Data is carried in Response Data. |

For endpoint-to-controller response data, `DLEN + DOFST` should be less than or equal to the size of the Admin command completion data. `DOFST` and `DLEN` low two bits should be cleared to `00b`.

