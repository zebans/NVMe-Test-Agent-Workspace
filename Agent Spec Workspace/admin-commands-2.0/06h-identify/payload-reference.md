# Identify - Payload Reference

Primary source: NVMe Base Specification 2.0, section 5.17, Figures 275 through 290.

Purpose: map each Identify CNS value to its returned payload, ownership, selector rules, and where to look up field meanings.

Use `field-reference.md` when the question is about a specific returned byte/field/bit/value. Use this file when the question is "which payload does this CNS return?" or "which spec owns this payload?"

## Returned Buffer Rule

Identify returns a 4,096-byte data structure selected by CDW10.CNS.

If fewer entries are returned than the selected data structure allows, unused returned bytes are zero-filled.

## CNS To Payload Map

| CNS | Returned Payload | Ownership | Selector Inputs | Field Lookup | Notes |
|---|---|---|---|---|---|
| `00h` | Identify Namespace data structure or common namespace capabilities | Applicable logical-block I/O Command Set, commonly NVM | NSID | Delegated | Base does not define the payload fields. |
| `01h` | Identify Controller data structure, I/O Command Set Independent | Base | None: NSID, CNTID, CSI not used | `field-reference.md`, Figure 275 | Controller capability and identity table. |
| `02h` | Active Namespace ID list | Base common list structure | NSID start-after selector | This file, Base Payload Control Rules | Up to 1,024 active NSIDs in increasing order greater than command NSID. |
| `03h` | Namespace Identification Descriptor list | Base | Active NSID | `field-reference.md`, Figure 277 | Variable-length descriptors; `NIDL=0h` terminates list. |
| `04h` | NVM Set List | Base | CDW11.NVMSETID start-at selector | `field-reference.md`, Figures 278-279 | Ordered by NVM Set Identifier; entries shall not be cleared to `0h`. |
| `05h` | I/O Command Set-specific Identify Namespace data structure | Applicable I/O Command Set | NSID, CSI | Delegated | Inactive NSID returns zero-filled data; unsupported requested structure aborts. |
| `06h` | I/O Command Set-specific Identify Controller data structure | Applicable I/O Command Set | CSI | Delegated | If CSI has no Identify Controller structure, returns zero-filled data; unsupported CSI aborts. |
| `07h` | I/O Command Set-specific Active Namespace ID list | Base selector behavior plus applicable command-set association | NSID, CSI | This file plus command-set layer | Only namespaces associated with CSI are returned. |
| `08h` | I/O Command Set Independent Identify Namespace data structure | Base | NSID | `field-reference.md`, Figure 280 | Active NSID returns namespace data; inactive NSID returns zero-filled data. |
| `10h` | Allocated Namespace ID list | Base common list structure | NSID start-after selector | This file, Base Payload Control Rules | Up to 1,024 allocated NSIDs in increasing order greater than command NSID. |
| `11h` | Identify Namespace data structure for allocated NSID | Applicable logical-block I/O Command Set, commonly NVM | NSID | Delegated | Unallocated NSID returns zero-filled data; non-logical-block association aborts. |
| `12h` | Namespace Attached Controller list | Base common Controller List | NSID, CNTID start-at selector | This file, Base Payload Control Rules | Controllers attached to specified namespace. |
| `13h` | Controller list | Base common Controller List | CNTID start-at selector | This file, Base Payload Control Rules | Controllers in subsystem capable of namespace attachment. |
| `14h` | Primary Controller Capabilities Structure | Base | CNTID | `field-reference.md`, Figure 281 | Virtualization Management capability data. |
| `15h` | Secondary Controller List | Base | CNTID start-at selector | `field-reference.md`, Figures 282-283 | Includes secondary controllers offline due to SR-IOV configuration. |
| `16h` | Namespace Granularity List | Applicable I/O Command Set | CSI | Delegated | Invalid CSI association aborts with `Invalid I/O Command Set`. |
| `17h` | UUID List | Base | None | `field-reference.md`, Figures 284-285 | Requires `CTRATT.UUID List` for required non-zero UUID behavior. |
| `18h` | Domain List | Base | CDW11.DOMID start-at selector | `field-reference.md`, Figures 286-287 | Ordered by Domain Identifier. |
| `19h` | Endurance Group List | Base | CDW11.ENDGID start-at selector | `field-reference.md`, Figure 288 | ENDGID > ENDGIDMAX succeeds with empty list. |
| `1Ah` | I/O Command Set-specific Allocated Namespace ID list | Base selector behavior plus applicable command-set association | NSID, CSI | This file plus command-set layer | Only allocated NSIDs associated with CSI are returned. |
| `1Bh` | I/O Command Set-specific Identify Namespace data for allocated NSID | Applicable I/O Command Set | NSID, CSI | Delegated | Unallocated NSID returns zero-filled data; invalid NSID aborts. |
| `1Ch` | Identify I/O Command Set data structure | Base | CNTID or `FFFFh` for controller processing command | `field-reference.md`, Figures 289-290 | Shall be implemented if `CAP.CSS` bit 6 is set. |

## Payload Ownership Boundaries

Base-owned payloads expanded here:

- Figure 275: Identify Controller data structure.
- Figure 276: Power State Descriptor data structure.
- Figure 277: Namespace Identification Descriptor.
- Figure 278: NVM Set List.
- Figure 279: NVM Set Attributes Entry.
- Figure 280: I/O Command Set Independent Identify Namespace data structure.
- Figure 281: Primary Controller Capabilities Structure.
- Figure 282: Secondary Controller List.
- Figure 283: Secondary Controller Entry.
- Figure 284: UUID List.
- Figure 285: UUID List Entry.
- Figure 286: Domain List.
- Figure 287: Domain Attributes Entry.
- Figure 288: Endurance Group List.
- Figure 289: Identify I/O Command Set data structure.
- Figure 290: I/O Command Set Vector.

Delegated payloads:

- CNS `00h`: Identify Namespace data structure for logical-block command sets.
- CNS `05h`: I/O Command Set-specific Identify Namespace data structure.
- CNS `06h`: I/O Command Set-specific Identify Controller data structure.
- CNS `11h`: Identify Namespace data structure for allocated NSID.
- CNS `16h`: Namespace Granularity List.
- CNS `1Ah`: I/O Command Set-specific Allocated Namespace ID list.
- CNS `1Bh`: I/O Command Set-specific Identify Namespace data for allocated NSID.

## Lookup Examples

| If You See | Read |
|---|---|
| `ONCS bit 5` | `field-reference.md`, Figure 275 `ONCS` bit table. |
| `OACS bit 6` | `field-reference.md`, Figure 275 `OACS` bit table. |
| `RESCAP bit 3` | `field-reference.md`, Figure 280 `RESCAP` bit table. |
| `UUID Index` failure | `selector-reference.md` and `field-reference.md`, Figures 284-285. |
| `ENDGIDMAX` or empty Endurance Group List | `field-reference.md`, Figure 275 `ENDGIDMAX` and Figure 288. |
| `I/O Command Set Vector bit 2` | `field-reference.md`, Figure 290. |
| `PSD0.NOPS` | `field-reference.md`, Figure 276. |

## Base Payload Control Rules

| CNS / Structure | Control Rules |
|---|---|
| `02h` Active Namespace ID list | Contains up to 1,024 active NSIDs in increasing order greater than command NSID; returned structure is a Namespace List from section 4.4.2. |
| `03h` Namespace Identification Descriptor list | Contains variable-length descriptors that fit in the 4,096-byte Identify payload. Remaining bytes after descriptors should be cleared to `0h`; host shall treat NIDL `0h` as end of list. Host should ignore unsupported NIDT values. Controller shall not return multiple descriptors with same NIDT. Controller shall return at least one namespace-identifying descriptor: NIDT `1`, `2`, or `3`. If `CAP.CSS` bit 6 is set, NIDT `4` shall be returned. |
| `04h` NVM Set List | Ordered by NVM Set Identifier starting at the first NVM Set ID greater than or equal to CDW11.NVMSETID and accessible by the controller. The list shall not contain an entry cleared to `0h`. |
| `08h` I/O Command Set Independent Identify Namespace | Active NSID returns data for that namespace. Inactive NSID returns zero-filled data. If Namespace Management is supported and NSID is `FFFFFFFFh`, returns common controller namespace capabilities. |
| `10h` Allocated Namespace ID list | Contains up to 1,024 allocated NSIDs in increasing order greater than command NSID; returned structure is a Namespace List from section 4.4.2. |
| `12h` Namespace Attached Controller list | Contains up to 2,047 controller IDs attached to the specified namespace, greater than or equal to CDW10.CNTID; returned structure is Controller List from section 4.4.1. |
| `13h` Controller list | Contains up to 2,047 controller IDs in the NVM subsystem capable of being attached to namespaces, greater than or equal to CDW10.CNTID. |
| `14h` Primary Controller Capabilities | Returned for the specified primary controller. Payload fields describe controller resource capabilities. |
| `15h` Secondary Controller list | Contains up to 127 secondary controllers associated with the primary controller processing the command, greater than or equal to CDW10.CNTID; includes secondary controllers offline due to SR-IOV configuration. |
| `17h` UUID List | Each UUID List entry is `0h`, NVMe Invalid UUID, or a valid UUID. If CTRATT.UUID List is set, list shall contain at least one valid UUID, UUID 1 shall be non-zero, and a UUID field cleared to `0h` indicates end of list. UUID 127 shall be cleared to `0h`. |
| `18h` Domain List | Ordered by Domain Identifier starting at the first Domain ID greater than or equal to CDW11.DOMID and accessible by the controller; contains up to 31 Domain Attribute Entries. |
| `19h` Endurance Group List | Contains up to 2,047 Endurance Group Identifiers in increasing order greater than or equal to CDW11.ENDGID and accessible by the controller. If CDW11.ENDGID is greater than ENDGIDMAX, command completes successfully and returns an empty list. |
| `1Ch` Identify I/O Command Set | Array of I/O Command Set Vectors. Combination index is indicated by I/O Command Set Profile Feature. If an I/O Command Set Combination entry is cleared to `0h`, no further combinations are supported and subsequent combinations shall be `0h`. |

## Compatibility Note

This file does not replace selector/status rules:

- Use `selector-reference.md` for CNS-specific command inputs and invalid selector behavior.
- Use `status-reference.md` for expected status behavior.
- Use `cross-spec-boundary.md` before interpreting command-set-specific Identify payloads.
