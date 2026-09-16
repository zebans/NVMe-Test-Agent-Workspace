# Base to Fabrics Boundary

Status: `BOUNDARY-COMPLETE`

This file records the Base Spec 2.0 source anchors for Fabrics behavior and the related external source owners for non-Base details.

## Base-Owned Fabrics Facts

| Area | Source | Base-owned facts |
|---|---|---|
| Command type category | Section 2 / Figure 5 context | Fabrics is a command type distinct from Admin and I/O commands. |
| Fabrics command capsule | Section 3.3.2.1.1, Figure 80 | `OPC=7Fh`, `FCTYPE`, command identifier, reserved fields, type-specific bytes. |
| Fabrics response capsule | Section 3.3.2.1.2, Figure 82 | CQE layout, SQHD behavior, CID, status field. |
| Fabrics command processing | Section 6 | Fabrics commands create queues and initialize a controller; they are processed regardless of `CC.EN`. |
| Command type list | Figure 375 | Property Set, Connect, Property Get, Authentication Send/Receive, Disconnect, Vendor Specific. |
| Fabrics status | Figure 97 | Incompatible Format, Controller Busy, Connect Invalid Parameters, Connect Restart Discovery, Connect Invalid Host, Invalid Queue Type, Discover Restart, Authentication Required, transport-specific range. |

## Related Source Owners

| Area | Owner |
|---|---|
| RDMA transport | `NVM-Express-RDMA-Transport-Specification-2021.06.02-Ratified-1.md`; see `..\rdma-transport-1.0\README.md`. |
| TCP transport | `NVM-Express-TCP-Transport-Specification-2021.06.02-Ratified-1.md`; see `..\tcp-transport-1.0\README.md`. |
| FC-NVMe transport binding | External INCITS FC-NVMe-2 source; not present locally yet. |
| Security protocol payload details for Authentication Send/Receive | SPC-5, as referenced by sections 6.1 and 6.2. |
| Transport-specific status values `B0h` to `BFh` | Applicable NVMe Transport binding specification. |

## Boundary Rule

Use Base Fabrics files for `OPC=7Fh`, `FCTYPE`, queue support, capsule fields, response fields, and Figure 97 status applicability.

Use each related source when the question asks for behavior owned by that source.
