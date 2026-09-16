# SPEC Markdown Self Check Report

Date: 2026-06-23

Last updated: 2026-06-25

Reviewer / Agent: Codex

Scope:

- `NVMe Spec` root SPEC markdown
- `admin-commands-2.0`
- `io-commands-2.0`
- `CHECKLIST\SPEC_MARKDOWN_CHECKLIST.md`
- `CHECKLIST\SPEC_COMPLETENESS_STATUS.md`
- `io-command-sets-2.0`
- `zns-command-set-1.1`
- `io-command-sets-2.0\nvm-command-set-1.0`
- `io-command-sets-2.0\key-value-command-set-1.0`
- `fabrics-base-2.0`
- `mi-1.2`
- `pcie-transport-1.0`
- `rdma-transport-1.0`
- `tcp-transport-1.0`
- `mctp-base-1.3.1`
- `mctp-pcie-vdm-1.0.1`
- `mctp-smbus-i2c-1.1.0`

Validation type:

- Full command-folder structure check
- Command completeness status check
- Boundary keyword scan for API/test-layer leakage
- Representative source-fidelity spot check against Base Spec 2.0 command sections
- Payload coverage boundary check

## Summary

Result: PASS for Base Spec command-control completeness.

All Admin/I/O command folders in scope are now marked `COMPLETE` in `SPEC_COMPLETENESS_STATUS.md`. Each command folder has the canonical command-reference files:

```text
README.md
command-facts.md
field-reference.md
status-reference.md
cross-spec-boundary.md
COMMAND_CONTENT_AUDIT.md
```

The `COMPLETE` label means the Base Spec command-control rules or Base Spec opcode boundary are captured, and external ownership is explicit where Base Spec delegates details to another specification.

Payload lookup is handled by `payload-reference.md` when a command has command data or returned data. Large nested payloads use precise field-family routing and external-owner boundaries instead of copying unrelated tables into every command folder.

The I/O command-set layer is now marked `BOUNDARY-COMPLETE + COMMAND-INDEX-COMPLETE`. It indexes Base Spec 2.0 handoff points plus NVM Command Set 1.0, Key Value Command Set 1.0, and Zoned Namespace Command Set 1.1 command indexes. Expanded detail layers now exist for NVM-specific I/O commands, the NVM-owned Get LBA Status hook, KV Store/Retrieve/List/Delete/Exist, ZNS-owned commands, and ZNS-modified NVM commands.

Root-level source maps, Admin opcode table, I/O opcode table, and global status dictionary are now marked `COMPLETE` in `SPEC_COMPLETENESS_STATUS.md`. They are complete as routing/reference surfaces; command-specific status applicability still lives in per-command `status-reference.md` files.

## File Structure

PASS.

Evidence:

- Admin command folders: 31.
- Common I/O command folders: 6.
- Command folders checked: 37.
- Missing required command-folder files: 0.
- Command-set layer root files checked: 8.
- Expanded NVM command folders checked: 9.
- Expanded KV command folders checked: 5.
- Expanded ZNS command folders checked: 12.

## Command Completeness

PASS.

Evidence from `SPEC_COMPLETENESS_STATUS.md`:

```text
COMPLETE command rows: 37
SKELETON command rows: 0
legacy control-complete label count: 0
```

The status vocabulary now separates command completeness from payload coverage:

- `COMPLETE`: command-control rules or Base Spec opcode boundary are complete.
- `PAYLOAD-INDEXED`: large payload structures are indexed or delegated through a stable owner/routing table.
- `PAYLOAD-COMPLETE`: byte-exact payload fields are fully audited or intentionally delegated.

## Source Fidelity

PASS for command-control scope.

Representative spot checks covered:

- `Identify`
- `Get Log Page`
- `Get Features`
- `Set Features`
- `Format NVM`
- `Sanitize`
- `Namespace Management`
- `Security Send/Receive`
- `Get LBA Status` opcode boundary
- vendor-specific Admin/I/O opcode boundaries
- Base-to-command-set handoff points for CSI, Identify I/O Command Set, I/O Command Set Profile, Namespace Management, Format NVM, Get Log Page, and command-set-specific Features
- NVM / ZNS / Key Value command-set version, CSI, opcode, Identify, feature/log, and Namespace Management indexes
- NVM-specific I/O command detail folders
- KV Store, Retrieve, List, Delete, and Exist command detail folders
- ZNS Zone Management Send, Zone Management Receive, and Zone Append command folders
- ZNS-modified NVM command folders: Flush, Write, Read, Write Uncorrectable, Compare, Write Zeroes, Dataset Management, Verify, Copy

Observed pattern:

- Commands with full Base Spec sections capture fields, selectors/actions, required behavior, completion, status, and cross-spec boundaries.
- Commands delegated by Base Spec, such as `NVMe-MI Send`, `NVMe-MI Receive`, `Get LBA Status`, and vendor-specific ranges, explicitly state the external owner instead of inventing behavior.

## Payload Coverage

PASS for boundary clarity.

Known payload handling:

- `Identify`: large returned structures are indexed and linked to Figures 275-290; byte-exact expansion remains payload-validation work.
- `Get Log Page`: Base-owned LID payloads are expanded in `field-reference.md` for direct test/FW field lookup; command-set-specific, vendor-specific, and transport-owned payload portions remain explicitly delegated.
- `Get/Set Features`: high-value data-buffer payloads are expanded for Timestamp, Host Behavior Support, Host Metadata, and Host Identifier; remaining feature behavior is routed by FID and command-set/vendor ownership.
- `Reservation Report`: EDS behavior, Host Identifier format relationship, Reservation Status layout, and normal/extended registered-controller structures are expanded in the command folder.
- command-set-specific, vendor-specific, MI, security protocol, and Fabrics payloads are explicitly delegated.
- `io-command-sets-2.0` records I/O command-set indexes and routes into expanded NVM, KV, and ZNS detail folders.
- `zns-command-set-1.1` expands ZNS-owned commands and ZNS-modified NVM commands.
- NVM-specific and KV-specific I/O commands are expanded into per-command folders. Command-set-specific Identify, feature, and Namespace Management create field snapshots are now present in the command-set indexes; command-set-specific log pages remain routed by command-set ownership.
- NVM Protection Information and metadata behavior is centralized in `io-command-sets-2.0\nvm-command-set-1.0\NVM_PI_METADATA_REFERENCE.md` for direct lookup of `PRINFO`, `PRACT`, `PRCHK`, `STC`, `PIF`, `STS`, `LBSTM`, metadata placement, tag split, and PI status mapping.
- MCTP Base, MCTP PCIe VDM, and MCTP SMBus/I2C are now indexed as independent transport substrate layers for NVMe-MI routing. Common MCTP header fields, high-priority MCTP Control commands, PCIe VDM packet/timing fields, and SMBus/I2C packet/PEC/timing/address fields are expanded for direct lookup.

## Boundary Check

PASS.

Boundary scan over command folders and completeness status found no concrete implementation-layer leakage:

- no `PyNVMe`
- no `pytest`
- no `fixture`
- no `.waitdone()`
- no `ioworker`
- no `nvme0` / `nvme0n1`
- no flow-hint/test-case wording in command folders

## Residual Risk

The markdown is now suitable as a Base Spec command-reference layer for downstream script generation.

Residual risk is limited to byte-exact payload validation and details that Base Spec explicitly delegates to:

- applicable I/O Command Set specifications
- NVMe-MI specification
- Fabrics command set details
- security protocol specifications such as SPC-5 / ACS-4 / RPMB material
- vendor-specific documentation

For command-set and transport work, residual risk is now limited to deeper behavior that is intentionally not pulled into every lookup table: command-set-specific log page details not already expanded, transport behavior for RDMA/TCP, less common MCTP Control command payloads, SMBus/I2C Table 11 full allocation examples, and vendor-specific documentation.

## Next Recommended Validation

When payload-level tests are needed, expand only the relevant payload structures instead of expanding every payload globally. Good first payload candidates:

1. Identify Controller / Namespace structures.
2. Command-set-specific log pages when a test flow targets them, such as ZNS Changed Zone List or NVM LBA Status Information.
3. RDMA/TCP transport behavior when NVMe-oF transport tests need field/rule lookup.
4. Less common MCTP Control commands such as routing-table, UUID resolution, rate-limit, and transport-specific bodies when tests need byte/value-level assertions.
5. Vendor-specific structures only after vendor documentation is added.
