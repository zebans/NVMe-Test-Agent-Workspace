# Connect Cross-Spec Boundary

## Owned By Fabrics Base / This Folder

| Area | Covered here |
|---|---|
| Capsule fields | `OPC`, `FCTYPE`, `RECFMT`, `QID`, `SQSIZE`, `CATTR`, `KATO`. |
| Connect data | `HOSTID`, `CNTLID`, `SUBNQN`, `HOSTNQN`. |
| Connect response | `CNTLID`, `AUTHREQ`, `SQHD`, status code specific dword. |
| Connect status | Connect-specific status values and failed-Connect rules. |
| Queue sequence | Admin Queue association before I/O Queue connection. |

## Delegated Outside This Folder

| Area | Owner |
|---|---|
| Transport-specific SGL and connection mechanics | Applicable NVMe transport binding. |
| Authentication protocol details | Authentication Send/Receive and security protocol references. |
| Keep Alive feature details | Keep Alive Timeout feature reference. |
| PyNVMe API call syntax | API layer such as `API_AGENTS.md`. |

## Boundary Rule

This folder defines Connect command fields and Base Fabrics behavior. It does not define RDMA/TCP/PCIe transport binding mechanics or PyNVMe calls.
