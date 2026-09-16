# MCTP PCIe VDM Transport Binding 1.0.1 Layer

Status: `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED`

This folder records the local MCTP PCIe VDM Transport Binding Specification as an independent MCTP transport binding layer.

Primary source:

```text
..\NVMe Base Spec\2.0\MCTP\MCTP-PCIe-VDM-Transport-Binding-Specification.md
```

Version signal:

```text
Document Number: DSP0238
Version: 1.0.1
```

## File Index

| File | Purpose |
|---|---|
| `MCTP_PCIE_VDM_AGENTS.md` | Agent rules for using this transport binding layer. |
| `MCTP_PCIE_VDM_INDEX.md` | Source and table map for token-efficient reading. |
| `MCTP_PCIE_VDM_BEHAVIOR_REFERENCE.md` | High-value PCIe VDM encapsulation, routing, discovery, reset, and timing behavior. |
| `MCTP_PCIE_VDM_PACKET_REFERENCE.md` | Expanded PCIe VDM packet fields, routing values, fixed field values, and timing table. |
| `COMMAND_CONTENT_AUDIT.md` | Current coverage and remaining expansion boundaries. |

## Scope

This layer owns MCTP over PCIe VDM transport binding behavior:

- MCTP packet encapsulation in PCIe Type 1 VDMs with data.
- PCIe medium-specific fields used for MCTP.
- PCIe routing requirements for MCTP messages.
- PCIe bus owner discovery flow.
- Discovery Notify, full endpoint discovery, partial endpoint discovery, and timing requirements.

This layer does not define NVMe Admin/I/O queue behavior and does not define NVMe-MI command payload semantics.

## Complete Definition

`PAYLOAD-COMPLETE` applies to the PCIe VDM packet/timing fields expanded in `MCTP_PCIE_VDM_PACKET_REFERENCE.md`.
