# RDMA Transport Agent Rules

You are reading the NVMe RDMA Transport Specification Revision 1.0 layer.

This layer owns RDMA-specific transport facts:

- RDMA command list.
- setup and initialization.
- queue model instantiation.
- data transfer model.
- keep alive model.
- error handling model.
- transport-specific content.

Do not put Base Spec section 6 Fabrics command identity here. For `OPC=7Fh` and `FCTYPE`, use `..\fabrics-base-2.0\README.md`.

Do not write API calls, test-flow steps, or executable scripts.

Use the original source only when `RDMA_TRANSPORT_INDEX.md` does not contain the needed source anchor.

