# Property Set Restrictions

Status: `COMMAND-CONTROL-COMPLETE`

- Figure 375 marks Property Set as not supported on I/O Queues.
- If a Fabrics command not supported on an I/O Queue is sent on an I/O Queue, it shall be aborted with `Invalid Field in Command`.
- Property size encodings `010b` to `111b` in `ATTRIB` are reserved.
- Property semantics are tied to the Base Spec property definitions in section 3.1.3.

