# Fabrics Command Set Index

Status: `COMMAND-INDEX-COMPLETE`

Source:

```text
..\NVMe Base Spec\2.0\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

Primary anchors:

| Topic | Source |
|---|---|
| Fabrics command capsule SQE | Section 3.3.2.1.1, Figure 80 |
| Fabrics response capsule CQE | Section 3.3.2.1.2, Figure 82 |
| Fabrics command types | Section 6, Figure 375 |
| Fabrics command-specific status values | Figure 97 |

## Command Identity Model

All Fabrics commands use:

| Field | Value | Meaning |
|---|---|---|
| `OPC` | `7Fh` | Indicates a Fabrics command. |
| `FCTYPE` | command-specific | Selects the specific Fabrics command type. |

Do not model these commands as separate opcodes. The command identity is `OPC=7Fh + FCTYPE`.

## Command Type Index

| FCTYPE | Command | Mandatory / Optional | I/O Queue Support | Data Direction | Folder | Status |
|---:|---|---|---|---|---|---|
| `00h` | Property Set | Mandatory | No | No data transfer | `commands\00h-property-set` | `COMMAND-CONTROL-COMPLETE + CANONICAL` |
| `01h` | Connect | Mandatory | Yes | Host to controller | `commands\01h-connect` | `COMMAND-CONTROL-COMPLETE + CANONICAL` |
| `04h` | Property Get | Mandatory | No | Controller to host | `commands\04h-property-get` | `COMMAND-CONTROL-COMPLETE + CANONICAL` |
| `05h` | Authentication Send | Optional | Yes | Host to controller | `commands\05h-authentication-send` | `COMMAND-CONTROL-COMPLETE + CANONICAL` |
| `06h` | Authentication Receive | Optional | Yes | Controller to host | `commands\06h-authentication-receive` | `COMMAND-CONTROL-COMPLETE + CANONICAL` |
| `08h` | Disconnect | Optional | Yes | No data transfer | `commands\08h-disconnect` | `COMMAND-CONTROL-COMPLETE + CANONICAL` |
| `C0h`-`FFh` | Vendor Specific | Optional | Command-specific | Vendor-specific | `commands\c0h-ffh-vendor-specific-fabrics` | `BOUNDARY-COMPLETE + CANONICAL` |

Reserved values:

- FCTYPE values not listed in Figure 375 are reserved.
- If `FCTYPE` is set to a reserved value, Figure 80 says the command should be aborted with `Invalid Field in Command`.

## Queue Rule Snapshot

Figure 375 notes:

- All Fabrics commands other than Disconnect may be submitted on the Admin Queue.
- I/O Queue support is command-specific as listed above.
- If a Fabrics command not supported on an I/O Queue is sent on an I/O Queue, the command shall be aborted with `Invalid Field in Command`.
- Connect is submitted and completed on the same queue that the Connect command creates.

## Transport Boundary

Base Spec 2.0 section 6 defines Base Fabrics command behavior. Transport-specific status values `B0h` to `BFh` are owned by the applicable NVMe Transport binding specification.

## Completion Depth

`COMMAND-CONTROL-COMPLETE` means the Base section 6 command identity, fields, queue support, completion/status behavior, restrictions, and source ownership are captured.

`COMPLETE` should be used only after any intentionally delegated structures, security protocol payloads, transport-specific status values, and related property semantics required by the target task are either fully expanded or explicitly declared out of scope for that task.
