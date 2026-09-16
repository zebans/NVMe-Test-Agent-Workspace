# NVMe Base 2.0 Controller Properties

Status: `FIELD-COMPLETE + ROUTING-COMPLETE`

This is the canonical lookup layer for the Controller Property space defined by NVM Express Base Specification Revision 2.0 section 3.1.3, Figures 35 through 69.

## Fast Routing

| Question | Read |
|---|---|
| Which property is at an offset and which controller types support it? | `CONTROLLER_PROPERTY_INDEX.md` |
| What do `CAP`, `VS`, `CC`, `CSTS`, or `NSSR` fields mean? | `CORE_CONTROLLER_PROPERTIES.md` |
| What do `INTMS`, `INTMC`, `AQA`, `ASQ`, or `ACQ` fields mean? | `ADMIN_QUEUE_INTERRUPT_PROPERTIES.md` |
| What do CMB, Boot Partition, or PMR fields mean? | `MEMORY_REGION_PROPERTIES.md` |
| How do Fabrics, PCIe transport, and MI access these properties? | `cross-spec-boundary.md` |
| Is this layer source-complete? | `COMMAND_CONTENT_AUDIT.md` |

## Ownership Rule

Base Spec 2.0 owns property identity, offset, size, field meaning, access type, reset value, and controller-type applicability. Transport layers own the access mechanism. Fabrics Property Get/Set and MI PCIe-through-MI are access wrappers; they do not redefine a property's meaning.

## Universal Access Rules

- A property is a dword or qword controller attribute.
- Software accesses the exact property width beginning at its defined offset unless an applicable transport specification explicitly permits another form.
- An access that spans any portion of two or more properties is unsupported.
- Reserved bits return `0h`, and host software writes reserved bits and reserved properties as `0h`.
- Message-based transports use Fabrics Property Get and Property Set.
- Memory-based transports use the applicable transport binding's register access rules.
- A property-level `M`, `O`, `R`, or `T` in Figure 35 means Mandatory, Optional, Reserved, or Transport Specific for that controller/transport model. It is not a field access type such as `RO` or `RW`.

## Source

Primary source: NVM Express Base Specification Revision 2.0, section 3.1.3, Figure 35 and Figures 36-69.

