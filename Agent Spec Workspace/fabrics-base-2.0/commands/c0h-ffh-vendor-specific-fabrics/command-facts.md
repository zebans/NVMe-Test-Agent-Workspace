# Vendor Specific Fabrics Command Facts

Source: NVMe Base Spec 2.0 section 6 and Figure 375.

| Item | Value |
|---|---|
| Command range | Vendor Specific Fabrics Commands |
| Fabrics opcode | `OPC=7Fh` |
| Fabrics command type range | `FCTYPE=C0h`-`FFh` |
| Support | Optional |
| Queue support | Vendor-specific |
| Data direction | Vendor-specific |

## Base-Defined Fact

Base Spec 2.0 defines only the vendor-specific Fabrics command type range. Command semantics, fields, payloads, status behavior, and queue rules require vendor documentation unless otherwise specified by the vendor.
