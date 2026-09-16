# Identify Content Audit

Primary source:

```text
NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

Audited source range:

- Section 5.17, Identify command
- Section 5.17.2.1 through 5.17.2.21
- Figures 269 through 290

## Current Completeness

Status: `COMPLETE`

Reason:

- Command opcode, fields, selectors, CNS-specific command-control behavior, completion/status rules, and cross-spec boundaries from section 5.17 have been captured.
- Large returned payload structures are indexed and expanded into lookup form for Base-owned Figures 275 through 290 in `field-reference.md` and `payload-reference.md`; no known command-control rule remains missing.

## Command-Control Rules Already Captured

- Opcode `06h`.
- Admin command.
- 4,096-byte returned data buffer.
- Uses Data Pointer, CDW10, CDW11, and CDW14.
- All other command-specific fields are reserved.
- CNS selects returned data structure.
- CSI and CNTID are CNS-specific.
- Unused returned data is zero filled.
- Unsupported CNS aborts with `Invalid Field in Command`.
- Unsupported namespace / I/O Command Set association aborts with `Invalid I/O Command Set`.
- Completion posts a CQE to the Admin Completion Queue.
- Command-set-specific payloads are marked as delegated.

## Current Canonical Files

| File | Role |
|---|---|
| `README.md` | Human/Codex entry point. |
| `command-facts.md` | Opcode, command dwords, and command-control rules. |
| `selector-reference.md` | CNS/CSI/CNTID/NSID selector behavior. |
| `field-reference.md` | Base-owned returned payload field/bit/value lookup. |
| `payload-reference.md` | CNS-to-payload ownership and payload control rules. |
| `status-reference.md` | Completion/status behavior. |
| `cross-spec-boundary.md` | Delegation to NVM/ZNS/KV/Fabrics/MI/transport specs. |
| `COMMAND_CONTENT_AUDIT.md` | Completeness and maintenance checks. |

Retired duplicate files have been removed so future Codex searches are more likely to hit the canonical references above.

## Previously Missing Rules Now Verified

No known command-control rules remain missing from section 5.17.

The items below are now captured in the command folder and retained here as audit evidence. Payload structures remain separate payload-validation material rather than command-control blockers.

### Command Field Rules

- [x] DPTR PRP rule: if using PRPs, DPTR shall not point to a PRP List because the Identify data buffer may not cross more than one page boundary.
- [x] CNTID unused rule: when CNTID is not used, host software shall clear it to `0h` for backwards compatibility and the controller shall ignore it.
- [x] Namespace Management dependency: controllers that support Namespace Management shall support CNTID.
- [x] CSI unused rule: for CNS values that do not use CSI, CDW11.CSI shall be cleared to `0h`.
- [x] CDW11 CNS Specific Identifier rules for NVMSETID, DOMID, and ENDGID are linked from `command-facts.md` and `selector-reference.md`.
- [x] UUID Index support condition references section 8.25 and Figure 477.

### Selector And CNS Rules

- [x] Figure 273 CNS values and notes have a normalized extracted table in `selector-reference.md`.
- [x] CNS `09h`-`0Fh`, `1Dh`-`1Fh`, and `20h`-`FFh` reserved ranges are documented, with the converted-source artifact after `1Ch` called out.
- [x] CNS `10h` Allocated Namespace ID list rules are captured.
- [x] CNS `12h` Controller List attached to specified NSID rules are captured.
- [x] CNS `13h` Controller List in NVM subsystem rules are captured.
- [x] CNS `14h` Primary Controller Capabilities rules are captured.
- [x] CNS `15h` Secondary Controller List rules are captured.
- [x] CNS `17h` UUID List rules are captured.
- [x] CNS `18h` Domain List rules are captured.
- [x] CNS `19h` Endurance Group List rules are captured.
- [x] CNS `1Ah` I/O Command Set-specific Allocated Namespace ID List NSID restrictions are captured.
- [x] CNS `1Bh` allocated namespace behavior and invalid NSID behavior are captured.
- [x] CNS `1Ch` Identify I/O Command Set data structure rules are captured.

### Status And Completion Rules

- [x] Unsupported CNS -> `Invalid Field in Command` is captured and tied to section 5.17.
- [x] Namespace not associated with supporting I/O Command Set -> `Invalid I/O Command Set` is captured and tied to Figure 95 and section 5.17.
- [x] CNS `1Ah` unsupported CSI -> `Invalid Field in Command` is captured.
- [x] CNS `1Ah` NSID `FFFFFFFEh` or `FFFFFFFFh` should abort with `Invalid Namespace or Format` is captured.
- [x] CNS `1Bh` unsupported CSI/structure -> `Invalid Field in Command` is captured.
- [x] CNS `1Bh` invalid NSID or NSID `FFFFFFFFh` should abort with `Invalid Namespace or Format` is captured.
- [x] CNS `16h` invalid Command Set Identifier association -> `Invalid I/O Command Set` is captured.
- [x] Endurance Group List behavior when ENDGID is greater than ENDGIDMAX -> Successful Completion with empty list is captured.

### Payload Structures

These structures are now expanded into lookup form in `field-reference.md` and mapped by CNS in `payload-reference.md`. They are not command-control blockers:

- [x] Figure 275: Identify Controller data structure.
- [x] Figure 276: Power State Descriptor data structure.
- [x] Figure 277: Namespace Identification Descriptor.
- [x] Figure 278: NVM Set List.
- [x] Figure 279: NVM Set Attributes Entry.
- [x] Figure 280: I/O Command Set Independent Identify Namespace data structure.
- [x] Figure 281: Primary Controller Capabilities Structure.
- [x] Figure 282: Secondary Controller List.
- [x] Figure 283: Secondary Controller Entry.
- [x] Figure 284: UUID List.
- [x] Figure 285: UUID List Entry.
- [x] Figure 286: Domain List.
- [x] Figure 287: Domain Attributes Entry.
- [x] Figure 288: Endurance Group List.
- [x] Figure 289: Identify I/O Command Set data structure.
- [x] Figure 290: I/O Command Set Vector.

## Payload Validation Follow-Up

If byte-exact payload validation is needed beyond the lookup tables, validate the new reference tables against the original PDF/source text:

1. Confirm each `field-reference.md` offset and bit range against Base Spec 2.0 Figures 275-290 when doing a formal source audit.
2. Confirm list-entry formulas for Figures 278, 282, 286, 288, and 289.
3. Keep command-set-specific payloads delegated to the applicable I/O Command Set specifications.
