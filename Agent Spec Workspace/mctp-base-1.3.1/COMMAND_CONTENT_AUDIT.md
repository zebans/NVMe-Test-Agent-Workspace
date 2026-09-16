# MCTP Base Content Audit

Status: `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED`

## Source

```text
..\NVMe Base Spec\2.0\MCTP\MCTP-Base-Specification.md
```

## Captured

| Area | Evidence |
|---|---|
| Source identity | `DSP0236`, Version `1.3.1`. |
| Source index | Major sections, tables, and MCTP Control command families are indexed. |
| Behavior reference | EID, endpoint, bus owner, bridge, packet/message fields, message assembly, Control Protocol, routing/discovery are summarized. |
| Common header expansion | `MCTP_COMMON_HEADER_REFERENCE.md` expands Table 1 fields. |
| Control command expansion | `MCTP_CONTROL_COMMAND_REFERENCE.md` expands Control common fields, completion codes, Set/Get Endpoint ID, Get UUID, Get MCTP Version Support, Get Message Type Support, Prepare/Endpoint Discovery, Discovery Notify, and Transport Specific boundary. |
| Boundary | NVMe-MI, SMBus/I2C, PCIe VDM, and vendor-defined ownership are separated. |

## Not Expanded

| Area | Reason |
|---|---|
| Less common MCTP Control command byte fields | Indexed but not byte-expanded; expand only when a test/FW task needs exact payload bytes. |
| Vendor-defined message body | Vendor documentation required. |
| Transport-specific command bodies | Owned by the transport binding identified by the command. |

## Token-Efficient Use

Use `MCTP_COMMON_HEADER_REFERENCE.md` and `MCTP_CONTROL_COMMAND_REFERENCE.md` before opening the full source for common packet/control questions. Open the full source only for less common control commands or unresolved source-fidelity checks.
