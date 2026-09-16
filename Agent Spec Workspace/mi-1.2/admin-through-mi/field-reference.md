# Admin-Through-MI Field Reference

Status: `FIELD-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 6, Figures 115-118.

## High-Value Fields

| Field | Location | Meaning | Important bits/values | Affects |
|---|---|---|---|---|
| `OPC` | Request byte `04` | NVMe Admin opcode to tunnel through MI. | Must be allowed by Figure 114. | Command routing and prohibited-command checks. |
| `CFLGS` | Request byte `05` | Command flags. | Bits `7:2` reserved; `DOFSTV` and `DLENV` ignored by MI 1.2 endpoints. | Legacy validity handling. |
| `CTLID` | Request bytes `07:06` | Target Controller ID. | Invalid if not implemented in the NVM subsystem. | Target controller selection. |
| `SQEDW1`-`SQEDW5` | Request bytes `11:08` through `27:24` | Admin Submission Queue Entry dwords 1 through 5. | Semantics come from the Base Admin command. | Command-specific inputs. |
| `DOFST` | Request bytes `31:28` | Offset into returned Admin completion data. | Should be zero for no-data or host-to-endpoint data commands; bits `1:0` should be `00b`. | Response data slicing and Invalid Parameter checks. |
| `DLEN` | Request bytes `35:32` | Request or response data length. | No-data commands should use zero; data commands should use non-zero; bits `1:0` should be `00b`; should be <= 4096. | Payload length and Invalid Parameter checks. |
| `SQEDW10`-`SQEDW15` | Request bytes `47:44` through `67:64` | Admin Submission Queue Entry dwords 10 through 15. | Semantics come from the Base Admin command. | Command-specific selectors and fields. |
| NVMe Request Data | Request bytes `N-1:68` | Optional data payload for Admin commands that transfer data to the endpoint. | Replaces PRP/SGL transfer for MI path. | Host-to-endpoint payload. |
| Response `Status` | Response byte `04` | MI response status. | MI-defined; indicates wrapper/request status. | Determines whether NVMe CQE status is meaningful. |
| `CQEDW0` | Response bytes `11:08` | Admin CQE Dword 0. | Defined by Base Admin command. | Command-specific completion value. |
| `CQEDW1` | Response bytes `15:12` | Admin CQE Dword 1. | Defined by Base Admin command. | Command-specific completion value. |
| `CQEDW3` | Response bytes `19:16` | Admin CQE Dword 3. | Contains NVMe Admin status field; Command ID shall be `0h`. | Admin completion status. |
| NVMe Response Data | Response bytes `N-1:20` | Optional Admin command response data. | May be sliced by Admin command offset/length first, then by MI `DOFST`/`DLEN`. | Returned payload fields. |

## Field Ownership

| Field group | Owner |
|---|---|
| MI message header, MIC, wrapper `Status` | NVMe-MI |
| `OPC`, `CTLID`, `DOFST`, `DLEN`, wrapper layout | NVMe-MI section 6 |
| `SQEDW1`-`SQEDW5`, `SQEDW10`-`SQEDW15`, `CQEDW0`, `CQEDW1`, `CQEDW3` semantics | NVM Express Base Specification Admin command definition |
| Log page payload selected by Get Log Page | Base/Admin folder plus command-set, Fabrics, MI, or vendor owner depending on LID |
| Feature payload selected by Get/Set Features | Base/Admin folder plus feature-specific owner |

