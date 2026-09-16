# Connect Field Reference

Source: Base Spec 2.0 section 6.3, Figure 380.

| Bytes | Field | Meaning | Important values / rules | Affects |
|---:|---|---|---|---|
| `00` | `OPC` | Fabrics command opcode. | Set to `7Fh`. | Fabrics command dispatch. |
| `01` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `03:02` | `CID` | Command Identifier. | Identifies the command. | Completion matching. |
| `04` | `FCTYPE` | Fabrics Command Type. | Set to `01h` for Connect. | Command type dispatch. |
| `23:05` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `39:24` | `SGL1` | SGL descriptor for transfer. | Transport SGL Data Block or Keyed SGL Data Block descriptor. | Connect data transfer. |
| `41:40` | `RECFMT` | Record format. | This definition uses `0h`. | Capsule format compatibility. |
| `43:42` | `QID` | Queue Identifier. | `0h` Admin Queue; `1`-`65,534` I/O Queue. | Queue type / sequence rules. |
| `45:44` | `SQSIZE` | Submission Queue size. | `0h` or larger than supported returns `Connect Invalid Parameters`. | Queue sizing. |
| `46` | `CATTR` | Connect Attributes. | Delete individual I/O queue support, SQ flow control disable request, priority class. | Queue behavior. |
| `47` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
| `51:48` | `KATO` | Keep Alive Timeout. | Admin Queue Connect only; reserved for I/O Queue Connect. | Keep Alive behavior. |
| `63:52` | Reserved | Reserved. | Host should clear. | Reserved-field validation. |
