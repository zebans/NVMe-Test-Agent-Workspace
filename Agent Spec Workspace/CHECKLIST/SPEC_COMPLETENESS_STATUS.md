# SPEC Completeness Status

This file tracks whether the current SPEC markdown is complete against the local source bundle.

Primary Base source:

```text
NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

## Completeness Labels

| Label | Meaning |
|---|---|
| `COMPLETE` | Relevant command-control or reference facts are captured and external ownership is explicit. |
| `BOUNDARY-COMPLETE` | The local spec only defines the boundary; detailed behavior belongs elsewhere. |
| `COMMAND-INDEX-COMPLETE` | Command-set or layer index is complete enough for routing. |
| `SOURCE-INDEX-COMPLETE` | Source sections/figures/tables are indexed but not necessarily byte-expanded. |
| `BEHAVIOR-INDEXED` | High-value behavior is summarized for token-efficient lookup; exact tables remain in source. |
| `PAYLOAD-INDEXED` | Payload is indexed or routed, but not fully byte-expanded. |
| `PAYLOAD-COMPLETE` | Payload fields are fully expanded or intentionally delegated. |
| `BLOCKED` | Required source is missing, unclear, external, or vendor-specific. |

## Root Files

| Area | Status | Notes |
|---|---|---|
| Root index and source map | `COMPLETE` | `Base_Spec_2_0_Index.md` identifies Base source, major sections, command tables, status figures, command folders, command-set layers, Fabrics, MI, transports, and MCTP layers. |
| Admin command opcode table | `COMPLETE` | `Admin_Command_Spec_Table.md` captures Figure 138 command rows and routes delegated ranges. |
| I/O command opcode table | `COMPLETE` | `IO_Command_Spec_Table.md` captures Figure 390 common I/O command rows and command-set boundaries. |
| Global status references | `COMPLETE` | `Status_Code_Reference.md` captures global status dictionary; per-command applicability remains in command folders. |
| Command-to-status matrix | `COMPLETE` | `Command_Status_Matrix.md` records command/status links explicitly tied to commands by Base Spec. |
| Controller Property index and fields | `COMPLETE` | `controller-properties-2.0` captures Figure 35 applicability plus Figures 36-69 field/bit/value meanings and cross-access routing. |

## Layer Status

| Layer | Status | Notes |
|---|---|---|
| Admin command layer | `COMPLETE` | `admin-commands-2.0` contains canonical folders for Admin opcode table entries and boundary-only delegated ranges. |
| Controller Properties layer | `FIELD-COMPLETE + ROUTING-COMPLETE` | Base 2.0 section 3.1.3 property map and fields are canonical; Fabrics, PCIe, and MI access layers route back without duplicating meanings. |
| Common I/O command layer | `COMPLETE` | `io-commands-2.0` contains canonical folders for Base common I/O commands and vendor-specific boundary. |
| I/O command-set boundary and indexes | `BOUNDARY-COMPLETE + COMMAND-INDEX-COMPLETE` | `io-command-sets-2.0` maps Base handoff points plus NVM 1.0, Key Value 1.0, and ZNS 1.1. |
| NVM detailed command layer | `COMPLETE` | Expands NVM-specific I/O commands, Get LBA Status Admin hook, and shared NVM PI/metadata reference. |
| Key Value detailed command layer | `COMPLETE` | Expands KV Store, Retrieve, List, Delete, and Exist command-control, key/value field, payload, status, ordering, and boundaries. |
| ZNS detailed command layer | `COMPLETE` | Expands ZNS-owned commands and ZNS-modified NVM commands from section 3.3. |
| Fabrics Base layer | `BOUNDARY-COMPLETE + COMMAND-INDEX-COMPLETE + COMMAND-CONTROL-COMPLETE` | Indexes Base Spec 2.0 section 6 Fabrics commands by `OPC=7Fh` plus `FCTYPE`. |
| MI layer | `FRAMEWORK-COMPLETE` | Captures NVMe Management Interface Revision 1.2 source anchors, shared four-byte Message Header, request/response and command-family selectors, CSI/MEB/CIAP, MIC, native MI command-control lookup, status/error values, and in-band/out-of-band boundaries. |
| MI Admin-through-MI layer | `FIELD-COMPLETE + ROUTING-COMPLETE` | Expands MI section 6 Figure 114 Admin command O/M/P support, Figures 115-118 wrapper fields, section 6.2 status boundary, Figures 121-125 support overlays, and links each Admin opcode/range to `admin-commands-2.0`. |
| MI PCIe-through-MI layer | `FIELD-COMPLETE + ROUTING-COMPLETE` | Expands all MI section 7 subsections and Figures 126-144 into source map, Storage Device/Enclosure support, complete MI header/request/response layout, opcode, `CTLID`, `LENGTH`/BAR/`OFFSET`, data, PEL/status, operational restriction, message-identity boundary, and PCIe transport routing references. |
| PCIe transport layer | `COMPLETE` | Captures NVMe over PCIe transport source anchors, registers/capabilities, doorbells, queues, reset, interrupts, power, error, and host-flow behavior. |
| RDMA transport layer | `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE` | Indexes NVMe RDMA Transport Specification Revision 1.0 source sections and figures. |
| TCP transport layer | `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE` | Indexes NVMe TCP Transport Specification Revision 1.0 source sections and figures. |
| MCTP Base layer | `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED + PAYLOAD-COMPLETE` | Captures MCTP Base DSP0236 Version 1.3.1 EID, packet/message, control, routing, discovery, NVMe-MI boundary, common header, and high-priority Control command payload references. |
| MCTP PCIe VDM binding layer | `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED + PAYLOAD-COMPLETE` | Captures MCTP over PCIe VDM DSP0238 Version 1.0.1 encapsulation, routing, discovery, reset/power, Table 1 packet fields, and Table 4 timing references. |
| MCTP SMBus/I2C binding layer | `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE + BEHAVIOR-INDEXED + PAYLOAD-COMPLETE` | Captures MCTP over SMBus/I2C DSP0237 Version 1.1.0 Block Write, slave address, PEC, ARP, NACK/retry/fairness, timing, anti-aliasing, packet fields, and reserved/well-known address references. |

## Residual Gaps

| Area | Status | Reason |
|---|---|---|
| RDMA/TCP behavior references | Optional future expansion | Current layers are source-index/boundary complete; expand if transport-level tests need field/rule lookup without reopening source. |
| Less common MCTP Control command payloads | Optional future expansion | High-priority setup/discovery commands are expanded; less common commands such as routing table, UUID resolution, rate limiting, and transport-specific command bodies remain demand-driven. |
| MCTP SMBus/I2C Table 11 full allocation examples | Optional future expansion | Reserved/well-known address rows are expanded; full recommended computer-system allocation table remains in source until a test needs specific rows. |
| Vendor-specific commands/messages | Blocked without vendor docs | Vendor-specific ranges and message bodies require vendor documentation. |

## Test-Agent Reading Guidance

Test-writing agents should not start with this checklist. They should read the relevant command/reference layer first. Use this file only when deciding whether a markdown layer is complete enough or whether source/audit validation is needed.
