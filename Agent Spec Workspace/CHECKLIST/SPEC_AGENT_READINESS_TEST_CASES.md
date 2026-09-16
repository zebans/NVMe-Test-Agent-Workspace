# SPEC Agent Readiness Test Cases

Purpose: verify that Codex Agents can reliably use the NVMe SPEC markdown layer without hitting broken entry points, missing MCTP routing files, malformed markdown tables, broken local references, or unreadable text artifacts.

## How To Run

From the `Agent Spec Workspace` directory:

```powershell
python .\tools\spec_agent_readiness_check.py
```

For machine-readable output:

```powershell
python .\tools\spec_agent_readiness_check.py --json
```

For command source-anchor fidelity:

```powershell
python .\tools\spec_source_fidelity_check.py
```

Pass condition: `Errors: 0`.

Warnings should be reviewed, but they do not fail the gate unless the warning affects agent lookup correctness.

## Test Case 1: Root Agent Entrypoints Exist

Goal: a future Codex Agent can start from the expected root files.

Checks:

- `SPEC_AGENTS.md`
- `SPEC_REFERENCE_GUIDE.md`
- `Base_Spec_2_0_Index.md`
- `Admin_Command_Spec_Table.md`
- `IO_Command_Spec_Table.md`
- `Status_Code_Reference.md`
- `Command_Status_Matrix.md`

Fail examples:

- Missing root index.
- Empty root guide.
- Agent instructions removed or renamed.

## Test Case 2: MCTP Lookup Layer Is Complete

Goal: MCTP, PCIe VDM binding, and SMBus/I2C binding can be routed without opening the full source first.

Checks:

- `mctp-base-1.3.1/README.md`
- `mctp-base-1.3.1/MCTP_BASE_INDEX.md`
- `mctp-base-1.3.1/MCTP_COMMON_HEADER_REFERENCE.md`
- `mctp-base-1.3.1/MCTP_CONTROL_COMMAND_REFERENCE.md`
- `mctp-base-1.3.1/MCTP_TO_NVME_MI_BOUNDARY.md`
- `mctp-pcie-vdm-1.0.1/README.md`
- `mctp-pcie-vdm-1.0.1/MCTP_PCIE_VDM_INDEX.md`
- `mctp-pcie-vdm-1.0.1/MCTP_PCIE_VDM_PACKET_REFERENCE.md`
- `mctp-smbus-i2c-1.1.0/README.md`
- `mctp-smbus-i2c-1.1.0/MCTP_SMBUS_I2C_INDEX.md`
- `mctp-smbus-i2c-1.1.0/MCTP_SMBUS_I2C_PACKET_REFERENCE.md`
- `mctp-smbus-i2c-1.1.0/MCTP_SMBUS_I2C_TIMING_ADDRESS_REFERENCE.md`

Fail examples:

- MCTP Base exists but the NVMe-MI boundary file is missing.
- SMBus/I2C packet reference is missing, forcing agents to guess PEC/address placement.
- PCIe VDM packet reference is missing, forcing agents to mix general PCIe behavior with MCTP VDM behavior.

## Test Case 3: Command Folder Skeleton

Goal: command lookups have the canonical files an agent expects.

Checked command roots:

- `admin-commands-2.0/*`
- `io-commands-2.0/*`
- `fabrics-base-2.0/commands/*`
- `io-command-sets-2.0/nvm-command-set-1.0/admin-commands/*`
- `io-command-sets-2.0/nvm-command-set-1.0/io-commands/*`
- `io-command-sets-2.0/key-value-command-set-1.0/io-commands/*`
- `zns-command-set-1.1/commands/*`
- `zns-command-set-1.1/modified-nvm-commands/*`

Required files:

- `README.md`
- `command-facts.md`
- `field-reference.md`
- `status-reference.md`
- `cross-spec-boundary.md`

Audit evidence:

- `COMMAND_CONTENT_AUDIT.md`

Fail examples:

- Empty command `README.md`.
- Missing `status-reference.md`.
- Missing `cross-spec-boundary.md`, causing source ownership ambiguity.

## Test Case 4: Spec Sources And Layer Entrypoints Exist

Goal: every supported SPEC layer has its authoritative converted source and stable lookup entrypoints.

Checks:

- Base, NVM, Key Value, ZNS, NVMe-MI, PCIe, RDMA, TCP, and MCTP converted source files in the sibling source bundle.
- Command-set, Fabrics, ZNS, MI, PCIe, RDMA, and TCP layer indexes and agent entry files.
- Admin-through-MI and PCIe-through-MI command tables, field references, and cross-spec boundaries.

Fail examples:

- The source bundle was moved and the SPEC agent still points to the old location.
- An MI through-command table is removed while its layer still claims lookup coverage.
- A transport layer has a README but no canonical index.

## Test Case 5: Local References Resolve

Goal: paths that look like concrete local references can be opened by a future agent.

Checks:

- Markdown links that point to concrete local files.
- Inline code paths that include a directory separator and end in `.md` or `.pdf`.
- Root-level known files such as `SPEC_AGENTS.md`.

Ignored:

- Generic model filenames such as `command-facts.md` when used as prose.
- Glob examples such as `*_COMMAND_SET_INDEX.md`.
- External `http`, `https`, and `mailto` links.

Fail examples:

- Source path omits an actual subfolder.
- A guide points to a renamed command folder.
- A cross-layer reference points outside the workspace and no file exists.

## Test Case 6: Markdown Tables Are Structurally Usable

Goal: table-like content can be parsed or scanned reliably.

Checks:

- Header row and separator row.
- Each table body row has the same cell count as the header.

Fail examples:

- A table row accidentally contains an unescaped `|`.
- A row is split or malformed after copy/paste.

## Test Case 7: Mojibake / Replacement Text Review

Goal: agent-facing curated markdown should not contain unreadable encoding artifacts.

Checks:

- Unicode replacement characters.
- Common UTF-8 / CP1252 mojibake sequences.

Notes:

- Original source conversions under `NVMe Base Spec` are not strict-gated for mojibake because PDF-to-markdown source text may contain conversion noise.
- Curated agent guides, checklists, and command references should be readable.

## Test Case 8: Agent Contract Text

Goal: the main agent instructions preserve critical behavioral constraints.

Checks:

- Token-efficient reading protocol remains present.
- The required phrase for missing local Base Spec details remains present.
- MCTP / NVMe-MI transport lookup path remains present.
- MCTP Control and NVMe-MI ownership boundary remains explicit.

Fail examples:

- Agent instructions stop saying how to handle missing facts.
- MCTP packet fields are allowed to overwrite NVMe-MI command payload ownership.
