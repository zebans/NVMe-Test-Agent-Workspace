# PCIe-Through-MI Cross-Spec Boundary

Status: `BOUNDARY-COMPLETE`

## Ownership Matrix

| Fact or question | Owner | Read |
|---|---|---|
| `NMIMT=4h`, PCIe-through-MI opcode, request/response bytes | NVMe-MI 1.2 section 7 | This folder |
| `CTLID`, `NMD0-2`, `LENGTH`, BAR selector, `OFFSET`, data padding | NVMe-MI 1.2 sections 7.1-7.6 | `field-reference.md` |
| MI Response Message Status, PEL, Access Denied, PCIe Inaccessible | NVMe-MI 1.2 sections 4.1.2, 7, 8.1 | `status-and-restrictions-reference.md` |
| PCI Header, BAR register offsets, MSI/MSI-X, PCIe capabilities, AER | NVMe over PCIe Transport 1.0 for NVMe-specific requirements | `..\..\pcie-transport-1.0\PCIE_REGISTER_FIELD_REFERENCE.md` |
| Base Controller Property offset, width, applicability, and bit meaning | NVMe Base 2.0 section 3.1.3 | `..\..\controller-properties-2.0\README.md` |
| Doorbells, property mapping/access, queue/reset/power/interrupt behavior | NVMe over PCIe Transport | `..\..\pcie-transport-1.0\PCIE_TRANSPORT_BEHAVIOR_REFERENCE.md` |
| Full PCIe protocol, TLP, link, electrical, and PCIe-owned capability semantics | PCI Express Base Specification | External normative source |
| MCTP packet/message fields | MCTP Base | `..\..\mctp-base-1.3.1\README.md` |
| MCTP over PCIe VDM framing | MCTP PCIe VDM binding | `..\..\mctp-pcie-vdm-1.0.1\README.md` |
| MCTP over SMBus/I2C framing | MCTP SMBus/I2C binding | `..\..\mctp-smbus-i2c-1.1.0\README.md` |
| Lockdown selector and interface rules | Base Admin Lockdown command | `..\..\admin-commands-2.0\24h-lockdown\README.md` |
| Vendor-specific BAR content or protection mechanism | Vendor documentation | External |

## Three Different PCIe Paths

| Path | What PCIe is doing | Uses NVMe SQ/CQ? | Primary owner |
|---|---|:---:|---|
| Normal NVMe over PCIe | Host submits NVMe Admin/I/O commands and accesses controller registers/doorbells. | Yes | Base Spec + NVMe over PCIe Transport |
| NVMe-MI over MCTP over PCIe VDM | PCIe VDM transports an MCTP packet containing an NVMe-MI message. | No | MCTP PCIe VDM binding + MCTP + NVMe-MI |
| PCIe Command Set through MI | An OOB NVMe-MI command requests access to a target controller's PCIe configuration, I/O, or memory space. | No | NVMe-MI section 7, with PCIe transport used to interpret the target |

## Boundary Rules

- PCIe-through-MI is out-of-band only and is prohibited through the NVMe-MI in-band tunneling mechanism.
- The `STATUS` byte is an NVMe-MI Response Message Status, not an NVMe command `SCT/SC`.
- A BAR selector chooses an address-space owner; it does not define the contents of that BAR.
- Configuration-space `OFFSET` is defined by NVMe-MI, while the register at that offset is interpreted using the PCIe transport or PCI Express specification.
- OOB host-coordination policy and vendor access controls must remain explicit external boundaries.
