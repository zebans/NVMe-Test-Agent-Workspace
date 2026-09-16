# PCIe-Through-MI Status and Restrictions Reference

Status: `STATUS-COMPLETE + RESTRICTION-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 sections 4.1.2, 7, 7.1-7.6, 8.1; Figures 26 and 126-145.

## Applicable MI Response Status

| Value | Status | Applies when | PEL / result |
|---:|---|---|---|
| `00h` | Success | The PCIe Command completed successfully. | Read data, when applicable, is returned in `RESPD`. |
| `01h` | More Processing Required | The Management Endpoint needs additional time to finish the command. | Uses the section 4.1.2.3 response with `MPRT`; a later response contains the result. |
| `02h` | Internal Error | A vendor-specific internal error prevents processing. | Generic Error Response. |
| `03h` | Invalid Command Opcode | Opcode is reserved or an optional PCIe command is not implemented. | Generic Error Response. |
| `04h` | Invalid Parameter | A defined field has a reserved/unimplemented value, `CTLID` is invalid, BAR/type is invalid, or the requested range is outside the target space. | Invalid Parameter Error Response includes PEL. |
| `05h` | Invalid Command Size | The PCIe Command message body is incomplete or otherwise has the wrong command size, excluding Request Data sizing. | Generic Error Response. |
| `06h` | Invalid Command Input Data Size | A Write command has too much or too little Request Data. | Generic Error Response. |
| `07h` | Access Denied | A vendor protection mechanism or Command and Feature Lockdown prohibits the access, or an implementation blocks the requested address range. | Command is aborted. |
| `21h` | PCIe Inaccessible | PCIe functionality for the target controller is unavailable in the current controller/reset/power/link state. | Command is aborted. |

The PCIe Command response contains MI `STATUS` at response byte `04`. It does not return an NVMe Completion Queue Entry and does not use Base Spec `SCT/SC` completion status.

## Parameter Error Location

For `04h Invalid Parameter`, the Error Response contains the 24-bit Parameter Error Location:

| PEL bits | Meaning |
|---:|---|
| `23:08` | Byte offset of the least-significant byte of the invalid request parameter. If the error is beyond byte 65,535, this field reports 65,535. |
| `07:03` | Reserved. |
| `02:00` | Least-significant bit position, `0`-`7`, within that request byte. |

## Command-Specific Invalid Parameter Matrix

| Command family | Invalid condition | Status | PEL indicates |
|---|---|---:|---|
| All PCIe Commands | `CTLID` names a controller not implemented in the NVM Subsystem. | `04h` | `CTLID` |
| Configuration Read/Write | `OFFSET + LENGTH` falls outside the 4 KiB PCIe configuration space. | `04h` | `OFFSET` |
| I/O Read/Write | `BAR` does not identify an implemented I/O BAR for the selected controller. | `04h` | `BAR` |
| I/O Read/Write | `OFFSET + LENGTH` falls outside the selected I/O BAR range. | `04h` | `OFFSET` |
| Memory Read/Write | `BAR` is unimplemented or its address range is not a memory region. | `04h` | `BAR` |
| Memory Read/Write | 64-bit `OFFSET + LENGTH` falls outside the selected memory BAR range. | `04h` | `OFFSET` |
| Any command | A reserved field or reserved selector value is supplied. | `04h` | The invalid field |

## Data-Length Rules

| Rule | Expected behavior |
|---|---|
| Read response sizing | `RESPD` is `LENGTH` rounded up to the next dword. |
| Read padding | Bytes beyond `LENGTH` in the final response dword are cleared to `0h`. |
| Write request sizing | `REQD` is `LENGTH` rounded up to the next dword. |
| Write padding | Bytes beyond `LENGTH` in the final request dword are discarded. |
| Wrong Write data size | Too much or too little Request Data returns `06h Invalid Command Input Data Size`. |

## Access and State Restrictions

| Restriction | Spec behavior |
|---|---|
| Address ownership | Only configuration, I/O, and memory addresses mapped to the controller selected by `CTLID` may be accessed. The command does not directly access host memory. |
| Blocked ranges | A supported command may still be denied for selected address ranges; return `07h Access Denied`. |
| Configuration BAR reads | If any PCIe Command is supported, Configuration Read is mandatory. Reading BAR offsets through Configuration Read shall not return `Access Denied`; correct BAR data is returned. |
| Command and Feature Lockdown | Lockdown may prevent PCIe Command Set processing and produce `07h Access Denied`. |
| Controller/reset/link state | Implementations may decline processing during Controller Level Reset, disabled SR-IOV VF, PCIe Conventional Reset, FLR, non-D0 state, or when the link is not in `DL_Active`; return `21h PCIe Inaccessible`. |
| Other controller states | Supported PCIe Commands are required to be processed outside the listed inaccessible states. |
| ASPM | Processing may temporarily cause a low-power PCIe link to exit its low-power state. |
| Host interference | OOB PCIe commands may interfere with host software. The Management Controller should coordinate with the host or use non-interfering commands such as Configuration Read. Coordination policy is outside NVMe-MI scope. |

## Support Discovery

Support is not inferred from Figure 128 alone because every defined PCIe Command is optional. Use the native `00h Read NVMe-MI Data Structure` command with `DTYP=04h` to obtain the Optionally Supported Command List:

| Field | Meaning |
|---|---|
| `DTYP=04h` | Selects the Optionally Supported Command List. |
| `CTRLID` | Ignored for list entries whose Command Type has `NMIMT` other than `02h`; therefore it does not select PCIe Command Set support. |
| `NUMCMD` | Number of optional command entries. |
| Command Type `NMIMT` | Must be `4h` for PCIe Command Set entries. |
| Opcode | Match `00h`-`05h` from `MI_PCIE_THROUGH_COMMAND_TABLE.md`. |
