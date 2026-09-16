# TCP Transport Agent Rules

You are reading the NVMe TCP Transport Specification Revision 1.0 layer.

This layer owns TCP-specific transport facts:

- TCP setup and initialization.
- queue model instantiation.
- data transfer model.
- keep alive model.
- error handling model.
- transport-specific content.
- NVMe/TCP PDU structures.

Do not put Base Spec section 6 Fabrics command identity here. For `OPC=7Fh` and `FCTYPE`, use `..\fabrics-base-2.0\README.md`.

Do not write API calls, test-flow steps, or executable scripts.

Use the original source only when `TCP_TRANSPORT_INDEX.md` does not contain the needed source anchor.

