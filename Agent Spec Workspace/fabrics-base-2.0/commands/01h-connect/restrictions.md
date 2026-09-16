# Connect Restrictions

Status: `COMMAND-CONTROL-COMPLETE`

Source: Base Spec 2.0 section 6.3.

- The host shall establish an association with a controller and enable the controller before establishing an I/O Queue connection.
- If the host sends Connect for a Queue ID that has already been created, `Command Sequence Error` is returned.
- For dynamic controller model Admin Queue Connect, `CNTLID` shall be `FFFFh`; otherwise `Connect Invalid Parameters` is returned.
- For static controller model Admin Queue Connect, `CNTLID=FFFFh` returns `Connect Invalid Parameters`; `CNTLID=FFFEh` requests any Controller ID.
- `HOSTID` cleared to `0h` causes `Connect Invalid Parameters`.
- I/O Queue Connect parameters must match the associated Admin Queue association values as specified by section 6.3.
- SQ flow control is disabled only if `CATTR` bit 2 is set and the response `SQHD` is `FFFFh`.
- SQ flow control is enabled if `CATTR` bit 2 is cleared or response `SQHD` is not `FFFFh`.
- If SQ flow control is disabled, `SQHD` is reserved in later Fabrics response capsules for that queue pair.

