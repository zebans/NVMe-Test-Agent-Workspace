# MCTP PCIe VDM Packet Reference

Status: `PAYLOAD-COMPLETE`

Source: MCTP PCIe VDM Transport Binding DSP0238 Version 1.0.1 Figure 1, Table 1, and Table 4.

This file expands the PCIe medium-specific fields for carrying MCTP packets in PCIe VDMs.

## Packet Position

```text
PCIe medium-specific header / trailer
  contains MCTP transport header
    contains MCTP packet payload
```

This binding defines where MCTP common fields sit when carried in PCIe Vendor Defined Messages.

## PCIe Medium-Specific Fields

| Field | Rule / value | Meaning | Important rule |
|---|---|---|---|
| `Fmt[2]` | PCIe 2.1: `0b` | PCIe format extension bit. | PCIe 1.1/2.0 treat corresponding bit as reserved. |
| `Fmt` | `11b` | 4 dword header with data. | Required for MCTP over PCIe VDM. |
| `Type[4:3]` | `10b` | PCIe message. | Required for MCTP over PCIe VDM. |
| `Type[2:0]` | `000b` / `010b` / `011b` | PCI message routing. | `000b` Route to Root Complex; `010b` Route by ID; `011b` Broadcast from Root Complex. Other routing values are not supported for MCTP. |
| `TC` | `000b` | Traffic Class. | Set to zero for all MCTP over PCIe VDM. |
| `Attr[2]` / `TH` | `0b` where present | PCIe 2.1 fields. | Set to zero for MCTP over PCIe VDM. |
| `TD` | `0b` | TLP Digest. | Set to zero for all MCTP over PCIe VDM. |
| `EP` | `0b` | Error Present. | Set to zero for all MCTP over PCIe VDM. |
| `Attr` | `00b` or `01b` | PCIe attributes. | Allowed values for MCTP over PCIe VDM. |
| `AT` | `00b` | PCIe Address Type. | Set to zero where present. |
| `Length` | Dword count | Length of PCIe VDM data in dwords. | Must support MCTP baseline transmission unit. 64-byte baseline requires up to 16 dwords of PCIe VDM data. |
| PCI Requester ID | Bus/device/function | Managed endpoint sending the message. | Used as PCIe physical source identity. |
| `Pad Len` | 0 to 3, 1-based count | Number of `00h` pad bytes added to dword-align packet. | Non-`EOM` packets are already full transfer unit and should have `Pad Len=00b`. |
| MCTP VDM Code | `0000b` | Identifies MCTP messages among DMTF VDMs. | Fixed for this mapping. |
| Message Code | `7Fh` | PCIe Type 1 VDM. | Fixed for this mapping. |
| PCI Target ID | Bus/device/function | Physical address of target endpoint for Route By ID. | Ignored for Broadcast and Route to Root Complex. |
| Vendor ID | `1AB4h` | DMTF VDM Vendor ID. | Source states decimal `6836`, hex `0x1AB4`; MSB in byte 10, LSB in byte 11. |
| MCTP reserved | 4 bits | Reserved for MCTP. | Set to zero on transmit; ignore on receive. |
| `Hdr Version` | `0001b` | MCTP header version for this binding. | Other values reserved for future expansion. |
| `PAD` | 0 to 3 bytes of `00h` | Dword alignment pad. | Only needed when packet with `EOM=1b` is shorter than transfer unit. |

## Supported Routing Values

| Routing bits | Name | Use |
|---:|---|---|
| `000b` | Route to Root Complex | Used for Discovery Notify and access to PCIe VDM bus owner functionality. |
| `010b` | Route by ID | Uses PCI Target ID as target physical address. |
| `011b` | Broadcast from Root Complex | Used by bus owner for broadcast discovery flows. |
| Other | Not supported for MCTP | Do not use for this binding. |

## Timing Requirements

Source: Table 4.

| Symbol | Name | Min | Max | Meaning |
|---|---|---:|---:|---|
| `TRECLAIM` | Endpoint ID reclaim | none | 5 sec | Max interval a hot-plug endpoint may be non-responsive before bus owner can reclaim EID. |
| `MN1` | Number of request retries | 2 | See description | Total of three tries minimum: original plus two retries; retries must occur within `MT4` max. |
| `MT1` | Request-to-response time | none | 120 ms | Responder interval from end of request reception to beginning of response transmission. |
| `MT2` | Time-out waiting for response | `MT1 max + 6 ms` | `MT4 min` | Requester minimum wait before retrying. |
| `MT4` | Instance ID expiration interval | 5 sec | 6 sec | Interval after which response Instance ID expires and becomes reusable. |

## Boundary

- MCTP common fields are expanded in `..\mctp-base-1.3.1\MCTP_COMMON_HEADER_REFERENCE.md`.
- NVMe-MI payload/status semantics belong to `..\mi-1.2`.
- This path is not NVMe SQ/CQ, doorbell, or DMA command submission.
