# NVM Copy Status Reference

| Value / status | Meaning | Test/FW interpretation |
|---|---|---|
| `81h` Invalid Protection Information | `PRINFOR`, `PRINFOW`, `ILBRT`, or source `EILBRT` invalid for namespace PI format. | Check source/destination PI settings. |
| `82h` Attempted Write to Read Only Range | Destination LBA range contains read-only blocks, excluding namespace write-protection-state cases. | Destination write blocked. |
| `83h` Command Size Limit Exceeded | `NR`, `MSSRL`, or `MCL` processing limit exceeded. | Check Identify Namespace Copy limits. |
| `87h` Deallocated or Unwritten Logical Block | Copy failed due to source range containing deallocated/unwritten logical block. | Source data is not readable for copy under current DULBE behavior. |

If Copy fails, CQE Dword 0 contains the lowest numbered Source Range entry that was not successfully copied. If no data was written to destination LBAs, CQE Dword 0 is `0h`.
