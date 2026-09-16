# Identify - Command Facts

Primary source: NVMe Base Specification 2.0, section 5.17, Figures 269 through 274.

Purpose: define the Identify Admin command itself: opcode, transfer direction, command dwords, selector fields, and command-control rules. Use `field-reference.md` for returned payload fields.

## Command Identity

| Item | Value |
|---|---|
| Command | Identify |
| Opcode | `06h` |
| Command set | Admin |
| Section | 5.17 |
| Queue | Admin Submission Queue / Admin Completion Queue |
| Data transfer | `10b`, controller to host |
| Returned buffer size | 4,096 bytes |
| Returned structure selector | CDW10.CNS |
| Command Set Specific | No, in Figure 138 |

## Purpose

Identify returns information about the NVM subsystem, domain, controller, namespace, namespace lists, or command-set-related structures.

The returned data structure is selected by the Controller or Namespace Structure (`CNS`) field in CDW10. If fewer entries are returned than the selected data structure allows, unused bytes are zero-filled.

## Data Pointer

Source: Figure 269.

| Field | Meaning | Rule |
|---|---|---|
| `DPTR` | Start of the returned 4,096-byte Identify buffer. | If PRPs are used, the Data Pointer shall not point to a PRP List because the data buffer may not cross more than one page boundary. |

## Command Dwords

### CDW10

Source: Figure 270.

| Bits | Field | Meaning | Test/FW Relevance |
|---:|---|---|---|
| `31:16` | `CNTID` | Controller Identifier used by specific CNS values. If unused, host software clears it to `0h` and controller ignores it. Controllers supporting Namespace Management shall support this field. | Controller-list and virtualization-related Identify cases. |
| `15:08` | Reserved | Reserved. | Should be kept cleared by host. |
| `07:00` | `CNS` | Controller or Namespace Structure selector. | Main switch for returned payload and status behavior. See `selector-reference.md`. |

### CDW11

Source: Figure 271.

| Bits | Field | Meaning | Test/FW Relevance |
|---:|---|---|---|
| `31:24` | `CSI` | Command Set Identifier. CNS-specific; used only by CNS values requiring CSI. | Command-set-specific Identify cases; NVM/ZNS/KV boundary. |
| `23:16` | Reserved | Reserved. | Should be kept cleared by host. |
| `15:00` | CNS Specific Identifier | `NVMSETID` for CNS `04h`, `DOMID` for CNS `18h`, `ENDGID` for CNS `19h`. | List start selector and empty-list behavior. |

### CDW12 / CDW13 / CDW15

Reserved / not command-specific.

### CDW14

Source: Figure 272.

| Bits | Field | Meaning | Test/FW Relevance |
|---:|---|---|---|
| `31:07` | Reserved | Reserved. | Should be kept cleared by host. |
| `06:00` | UUID Index | Optional UUID List entry selector when Identify UUID selection is supported. `0h` means no UUID index is specified. | Invalid UUID index and unsupported UUID behavior map to `Invalid Field in Command`. |

## Command Set Identifier Values

Source: Figure 274.

| CSI | Command Set |
|---|---|
| `00h` | NVM Command Set |
| `01h` | Key Value Command Set |
| `02h` | Zoned Namespace Command Set |
| `03h`-`2Fh` | Reserved |
| `30h`-`3Fh` | Vendor specific |
| `40h`-`FFh` | Reserved |

## Command-Control Rules

- Unsupported CNS value shall abort with `Invalid Field in Command`.
- Namespace not associated with an I/O Command Set that supports the specified Identify CNS value shall abort with `Invalid I/O Command Set`.
- Some CNS values return zero-filled data rather than an error when the selected namespace or command set has no in-scope structure; see `selector-reference.md`.
- Some list-returning CNS values use NSID, CNTID, NVMSETID, DOMID, or ENDGID as "start at or after" selectors; see `selector-reference.md` and `payload-reference.md`.
- Some CNS values define "should abort" behavior for NSID `FFFFFFFEh` or `FFFFFFFFh`; see `status-reference.md`.

## Returned Payload Lookup

| Need | Read |
|---|---|
| Which CNS returns which payload | `payload-reference.md` |
| Returned byte/field/bit/value meaning | `field-reference.md` |
| CNS selector and boundary behavior | `selector-reference.md` |
| Completion/status expectation | `status-reference.md` |
| NVM/ZNS/KV/Fabrics/MI ownership boundary | `cross-spec-boundary.md` |

## Compatibility Note

The CNS field was one bit in revision 1.0 and two bits in revision 1.1. Host software should only issue CNS values defined in revision 1.0 to controllers compliant with revision 1.0, and CNS values defined in revision 1.1 to controllers compliant with revision 1.1. Results of issuing other CNS values to those older controllers are indeterminate.

