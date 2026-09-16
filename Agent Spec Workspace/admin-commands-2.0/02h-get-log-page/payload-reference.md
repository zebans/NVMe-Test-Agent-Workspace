# Get Log Page Payload Reference

Source: NVMe Base Specification 2.0, section 5.16.1, Figures 203-267.

This file maps each `LID` to the returned payload. Use [field-reference.md](field-reference.md) for byte/bit lookup of Base-owned fields and descriptor layouts.

| LID | Payload | Main figures | Payload ownership |
|---|---|---|---|
| `00h` | Supported Log Pages | Figures 203-205 | Base |
| `01h` | Error Information entries | Figure 206 | Base plus command/transport-specific fields |
| `02h` | SMART / Health Information | Figures 207-208 | Base |
| `03h` | Firmware Slot Information | Figure 209 | Base |
| `04h` | Changed Namespace List | 5.16.1.5 | Base |
| `05h` | Commands Supported and Effects | Figures 210-211 | Base |
| `06h` | Device Self-test | Figures 212-213 | Base |
| `07h` | Telemetry Host-Initiated | Figure 215 | Base command path; telemetry contents may be vendor/log-area specific |
| `08h` | Telemetry Controller-Initiated | Figure 216 | Base command path; telemetry contents may be vendor/log-area specific |
| `09h` | Endurance Group Information | Figure 217 | Base |
| `0Ah` | Predictable Latency Per NVM Set | Figure 218 | Base |
| `0Bh` | Predictable Latency Event Aggregate | Figure 219 | Base |
| `0Ch` | Asymmetric Namespace Access | Figures 220-222 | Base |
| `0Dh` | Persistent Event Log | Figures 223-246 | Base header/event framework; several event payloads mirror other commands/features |
| `0Eh` | I/O Command Set specific log | Figure 202 | External I/O command set spec |
| `0Fh` | Endurance Group Event Aggregate | Figure 247 | Base |
| `10h` | Media Unit Status | Figures 248-249 | Base |
| `11h` | Supported Capacity Configuration List | Figures 250-254 | Base |
| `12h` | Feature Identifiers Supported and Effects | Figures 255-256 | Base |
| `13h` | NVMe-MI Commands Supported and Effects | Figures 257-258 | Base plus NVMe-MI command definitions |
| `14h` | Command and Feature Lockdown | Figures 259-260 | Base plus lockdown set by NVMe-MI |
| `15h` | Boot Partition | Figures 261-262 | Base |
| `16h` | Rotational Media Information | Figure 263 | Base |
| `70h` | Discovery Log Page | Figures 264-265 | Base discovery payload; transport fields may require Fabrics/transport specs |
| `80h` | Reservation Notification | Figure 266 | Base plus Reservation feature/commands |
| `81h` | Sanitize Status | Figure 267 | Base plus Sanitize command behavior |
| `82h`-`BFh` | I/O Command Set specific logs | Figure 202 | External I/O command set specs |
| `C0h`-`FFh` | Vendor specific logs | Figure 202 | Vendor |

## Payload Selection Pattern

| Step | What to check | Why |
|---|---|---|
| 1 | `LID` in [selector-reference.md](selector-reference.md) | Determines payload family. |
| 2 | Scope for the selected `LID` | Determines whether `NSID`, Domain ID, Endurance Group ID, or NVM Set ID is meaningful. |
| 3 | `LSP` and Log Specific Identifier | Some payloads require an action/subselector. |
| 4 | `NUMD` and offset | Determines partial vs full payload read. |
| 5 | `field-reference.md` | Decodes bytes/bits in the returned payload. |

## Precision Contract

| Question type | Canonical lookup |
|---|---|
| Which payload is returned for a `LID`? | Use the `LID` table in this file first. |
| What does a Base-owned returned byte/bit mean? | Use `field-reference.md`; it contains the test/FW-oriented offset and descriptor table. |
| What if the returned structure contains nested descriptors or events? | Use the LID section in `field-reference.md`; nested Base-owned descriptor families such as ANA, Media Unit Status, Supported Capacity Configuration, and Persistent Event headers are expanded there. |
| What if `LID` is I/O Command Set specific? | Do not infer from Base; route to the selected command-set spec. |
| What if `LID` is vendor specific? | Do not infer from Base; use vendor documentation or device-specific expectation. |
