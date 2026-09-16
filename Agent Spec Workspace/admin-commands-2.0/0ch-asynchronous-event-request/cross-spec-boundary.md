# Asynchronous Event Request Cross-Spec Boundary

## This Folder Owns

- Base Spec 2.0 AER command semantics.
- AER CQE DW0 field meanings.
- Base event information values from Figures 144-148.
- Event retention, masking, and log-page clearing rules stated by Base Spec.

## This Folder Does Not Own

- PyNVMe API call syntax.
- Detailed Get Log Page payload structures.
- I/O Command Set specific event definitions such as LBA Status or Zone Descriptor Changed.
- NVMe over Fabrics future AEN definitions.
- Test harness wait/poll implementation.

