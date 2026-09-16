# NVM Get LBA Status Status Reference

## Command Completion Surface

| Surface | Meaning |
|---|---|
| Admin Completion Queue Entry | Controller posts completion status when command completes. |
| Returned `CMPC` field | Successful-command reason for stopping descriptor transfer; not an NVMe CQE status code. |
| LBA Status Descriptor Entry status byte | Per-range information about Write Uncorrectable source and unrecovered-read-risk detection. |

## Explicit NVM-Defined Returned Conditions

| Returned field | Value | Meaning | Follow-up |
|---|---:|---|---|
| `CMPC` | `0h` | No indication of completion condition. | Do not assume completion coverage from `CMPC`. |
| `CMPC` | `1h` | Stopped because the command transferred the amount of data specified by `MNDW`. | Continue querying if full range coverage is required. |
| `CMPC` | `2h` | Stopped because the selected action covered the requested range. | No more entries remain in the specified range. |
| Descriptor status bit | bit `1` set | Range describes LBAs written with Write Uncorrectable. | Treat as Write Uncorrectable-origin risk. |
| Descriptor status bit | bit `0` set | Copy/Read/Verify/Compare to each reported LBA may complete with Unrecovered Read Error. | Recovery or targeted negative test candidate. |

## Invalid / Reserved Selector Conditions

| Condition | Expected status surface |
|---|---|
| `ATYPE` is not `10h` or `11h` | Command should fail as an invalid/reserved command field condition. |
| Reserved command-specific fields are non-zero | Generic invalid field behavior is the relevant status category. |
| `NSID=FFFFFFFFh` | Not supported by the Base opcode boundary for Get LBA Status. |

The NVM section does not define a separate command-specific CQE status table for Get LBA Status beyond the returned descriptor-list fields above. Common Admin, namespace, data-transfer, and controller-state statuses remain applicable through Base/common NVMe rules.
