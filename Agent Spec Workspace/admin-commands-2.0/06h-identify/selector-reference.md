# Identify - Selector Reference

Primary source: NVMe Base Specification 2.0, section 5.17, Figure 273 and Figure 274.

Purpose: describe selector fields that change Identify command behavior and returned payload ownership. Use this when a question mentions CNS, CSI, CNTID, NSID, NVMSETID, DOMID, ENDGID, or UUID Index.

## Selector Fields

| Field | Location | Purpose |
|---|---|---|
| CNS | CDW10 bits 07:00 | Selects the returned Identify data structure. |
| CNTID | CDW10 bits 31:16 | Controller Identifier used by specific CNS values. |
| CSI | CDW11 bits 31:24 | Command Set Identifier used by specific CNS values. |
| CNS Specific Identifier | CDW11 bits 15:00 | NVMSETID, DOMID, or ENDGID for specific CNS values. |
| UUID Index | CDW14 bits 06:00 | Optional vendor-specific UUID selection when supported. |
| NSID | Common command field | Used depending on CNS value. |

## CNS Values

Source: Figure 273.

`Y` and `N` indicate whether NSID, CNTID, or CSI is used.

| CNS | Mandatory / Optional | Returned Information | NSID | CNTID | CSI | Reference / Ownership |
|---|---|---|---|---|---|---|
| `00h` | Mandatory | Identify Namespace data structure for specified NSID or common namespace capabilities for NVM Command Set | Y | N | N | Delegated to NVM Command Set / logical-block command set specification |
| `01h` | Mandatory | Identify Controller data structure for controller processing the command | N | N | N | 5.17.2.1; Figure 275 |
| `02h` | Mandatory | Active Namespace ID list | Y | N | N | 5.17.2.2 |
| `03h` | Mandatory | Namespace Identification Descriptor list for specified NSID | Y | N | N | 5.17.2.3 |
| `04h` | Optional | NVM Set List | N | N | N | 5.17.2.4; uses CDW11.NVMSETID |
| `05h` | Mandatory | I/O Command Set-specific Identify Namespace data structure | Y | N | Y | Delegated to applicable I/O Command Set specification |
| `06h` | Mandatory | I/O Command Set-specific Identify Controller data structure | N | N | Y | Delegated to applicable I/O Command Set specification |
| `07h` | Mandatory | Active Namespace ID list associated with specified I/O Command Set | Y | N | Y | 5.17.2.7 |
| `08h` | Mandatory | I/O Command Set Independent Identify Namespace data structure | Y | N | N | 5.17.2.8; Figure 280 |
| `09h`-`0Fh` | Reserved | Reserved | - | - | - | Reserved |
| `10h` | Optional | Allocated Namespace ID list | Y | N | N | 5.17.2.9 |
| `11h` | Optional | Identify Namespace data structure for allocated NSID | Y | N | N | Delegated to NVM Command Set / logical-block command set specification |
| `12h` | Optional | Controller list of controllers attached to specified NSID | Y | Y | N | 5.17.2.11 |
| `13h` | Optional | Controller list of controllers in NVM subsystem | N | Y | N | 5.17.2.12 |
| `14h` | Optional | Primary Controller Capabilities data structure | N | Y | N | 5.17.2.13 |
| `15h` | Optional | Secondary Controller list associated with primary controller | N | Y | N | 5.17.2.14 |
| `16h` | Optional | Namespace Granularity List | N | N | N | Delegated to NVM Command Set / applicable logical-block command set |
| `17h` | Optional | UUID List | N | N | N | 5.17.2.16 |
| `18h` | Optional | Domain List | N | N | N | 5.17.2.17; uses CDW11.DOMID |
| `19h` | Optional | Endurance Group List | N | N | N | 5.17.2.18; uses CDW11.ENDGID |
| `1Ah` | Optional | I/O Command Set-specific Allocated Namespace ID list | Y | N | Y | 5.17.2.19; command-set-specific association |
| `1Bh` | Optional | I/O Command Set-specific Identify Namespace data structure for allocated NSID | Y | N | Y | 5.17.2.20; delegated payload |
| `1Ch` | Optional | Identify I/O Command Set data structure | N | Y | N | 5.17.2.21; Figure 289 |
| `1Dh`-`1Fh` | Reserved / future definition | Reserved | - | - | - | Converted Figure 273 text is malformed after `1Ch`; undefined values between `1Ch` and `20h` are treated as reserved. |
| `20h`-`FFh` | Reserved | Reserved | - | - | - | Reserved |

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

## CNS Specific Identifier Values

Source: Figure 271.

| CNS | CDW11 bits 15:00 meaning |
|---|---|
| `04h` | NVM Set Identifier (`NVMSETID`) |
| `18h` | Domain Identifier (`DOMID`) |
| `19h` | Endurance Group Identifier (`ENDGID`) |

## CNS Behavior Rules

These rules summarize command-control behavior from sections 5.17.2.1 through 5.17.2.21. Base-owned payload field layouts are in `field-reference.md`; CNS-to-payload mapping is in `payload-reference.md`.

| CNS | Behavior Rules | Status / Boundary Rules |
|---|---|---|
| `00h` | Returns an Identify Namespace data structure for the specified NSID or common namespace capabilities for the NVM Command Set. | Payload is delegated to the NVM Command Set or applicable logical-block command set. |
| `01h` | Returns the Identify Controller data structure for the controller processing the command. | Base Spec-owned payload index is in `payload-reference.md`; detailed payload fields are in `field-reference.md`. |
| `02h` | Returns up to 1,024 active NSIDs in increasing order greater than the command NSID. NSID may be `0h` to start from NSID `1h`. | Controller should abort with `Invalid Namespace or Format` if NSID is `FFFFFFFEh` or `FFFFFFFFh`. |
| `03h` | Returns Namespace Identification Descriptor structures for the namespace specified by NSID if it is active. | If NSID does not specify an active NSID, use section 3.2.1.5 for returned status. Descriptor list rules are in `payload-reference.md` and field layout is in `field-reference.md`. |
| `04h` | Returns an NVM Set List sorted by NVM Set Identifier, starting at the first NVM Set ID greater than or equal to CDW11.NVMSETID and accessible by the controller. | NVM Set List shall not contain an entry cleared to `0h`. |
| `05h` | Returns I/O Command Set-specific Identify Namespace data for the specified active NSID and CSI. Inactive NSID returns a zero-filled data structure. If Namespace Management is supported, requested CSI is enabled, and NSID is `FFFFFFFFh`, returns common namespace capabilities for that I/O Command Set. | If namespace's I/O Command Set does not support the requested structure, abort with `Invalid Field in Command`. If Namespace Management is not supported and NSID is `FFFFFFFFh`, abort with `Invalid Namespace or Format`. Payload is delegated. |
| `06h` | Returns I/O Command Set-specific Identify Controller data for the controller processing the command and CSI. If the specified I/O Command Set has no Identify Controller data structure, returns a zero-filled data structure. | If host requests data for an I/O Command Set the controller does not support, abort with `Invalid Field in Command`. Payload is delegated. |
| `07h` | Returns up to 1,024 active NSIDs in increasing order greater than NSID and associated with the CSI value. NSID may be `0h` to start from NSID `1h`. | If CSI is not supported or not enabled, abort with `Invalid Field in Command`. Controller should abort with `Invalid Namespace or Format` if NSID is `FFFFFFFEh` or `FFFFFFFFh`. |
| `08h` | Returns I/O Command Set Independent Identify Namespace data for an active NSID. Inactive NSID returns a zero-filled data structure. If Namespace Management is supported and NSID is `FFFFFFFFh`, returns common controller capabilities. | If Namespace Management is not supported and NSID is `FFFFFFFFh`, abort with `Invalid Namespace or Format`. |
| `10h` | Returns up to 1,024 allocated NSIDs in increasing order greater than NSID. NSID may be `0h` to start from NSID `1h`. | Controller should abort with `Invalid Namespace or Format` if NSID is `FFFFFFFEh` or `FFFFFFFFh`. |
| `11h` | Returns Identify Namespace data for the allocated NSID. Unallocated NSID returns a zero-filled data structure. | If namespace is not associated with an I/O Command Set that specifies logical blocks, abort with `Invalid I/O Command Set`. Invalid NSID aborts with `Invalid Namespace or Format`. NSID `FFFFFFFFh` should abort with `Invalid Namespace or Format`. Payload is delegated. |
| `12h` | Returns up to 2,047 controller identifiers attached to the specified namespace, starting at the first controller ID greater than or equal to CDW10.CNTID. | If NSID is `FFFFFFFFh`, controller should abort with `Invalid Field in Command`. |
| `13h` | Returns up to 2,047 controller identifiers in the NVM subsystem that are capable of being attached to namespaces, starting at CDW10.CNTID. | Uses CNTID; no NSID. |
| `14h` | Returns Primary Controller Capabilities Structure for the specified primary controller. | The payload is Base Spec-owned; detailed resource fields are payload-level. |
| `15h` | Returns up to 127 secondary controllers associated with the primary controller processing the command, starting at CDW10.CNTID. Includes secondary controllers offline due to SR-IOV configuration. | Uses CNTID; no NSID. |
| `16h` | Returns Namespace Granularity List if supported. | Details are delegated to the applicable I/O Command Set. If CSI is not associated with an I/O Command Set that supports Namespace Granularity List, abort with `Invalid I/O Command Set`. |
| `17h` | Returns UUID List. Each UUID List entry is `0h`, NVMe Invalid UUID, or a valid UUID. If CTRATT.UUID List is set, UUID List shall contain at least one valid UUID, UUID 1 shall be non-zero, and a UUID field cleared to `0h` indicates end of list. List may be in any order. | UUID List payload is Base Spec-owned. |
| `18h` | Returns Domain List ordered by Domain Identifier starting at the first Domain ID greater than or equal to CDW11.DOMID and accessible by the controller. | Uses CDW11.DOMID. |
| `19h` | Returns up to 2,047 Endurance Group Identifiers in increasing order greater than or equal to CDW11.ENDGID and accessible by the controller. | If ENDGID is greater than ENDGIDMAX, complete successfully and return an empty Endurance Group List. |
| `1Ah` | Returns up to 1,024 allocated NSIDs in increasing order greater than NSID and associated with CSI. NSID may be `0h` to start from NSID `1h`. | If CSI is not supported, abort with `Invalid Field in Command`. Controller should abort with `Invalid Namespace or Format` if NSID is `FFFFFFFEh` or `FFFFFFFFh`. |
| `1Bh` | Returns I/O Command Set-specific Identify Namespace data for an allocated NSID. Unallocated NSID returns a zero-filled data structure. | If namespace's I/O Command Set does not support the requested CSI structure, abort with `Invalid Field in Command`. Invalid NSID aborts with `Invalid Namespace or Format`. NSID `FFFFFFFFh` should abort with `Invalid Namespace or Format`. Payload is delegated. |
| `1Ch` | Returns Identify I/O Command Set data for CDW10.CNTID if CNTID is not `FFFFh`; if CNTID is `FFFFh`, returns data for the controller processing the command. Shall be implemented if `CAP.CSS` bit 6 is set. | Only I/O Command Sets enabled in the selected I/O Command Set Combination may be used; all others are treated as unsupported I/O Command Sets. |

## Selector-Derived Validation Implications

- CNS `01h` is the basic Identify Controller selector and does not use NSID, CNTID, or CSI.
- CNS values using NSID may require active, allocated, invalid, or broadcast NSID distinctions.
- CNS values using CSI require checking command-set support, command-set enablement, and applicable payload ownership.
- Reserved CNS or unsupported CNS values are tied to `Invalid Field in Command`.
- Unsupported namespace/command-set association is tied to `Invalid I/O Command Set`.
- Large returned payload field validation uses `field-reference.md` for Base-owned payloads plus the applicable command-set specification for delegated payloads.
