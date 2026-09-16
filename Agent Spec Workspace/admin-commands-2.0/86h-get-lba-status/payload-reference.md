# Get LBA Status Payload Reference

Base Spec 2.0 does not define the Get LBA Status returned payload layout. This file exists as the canonical routing point so Codex does not stop at the Admin opcode boundary or invent Base-owned fields.

## Payload Ownership

| Payload surface | Owner | What to look for |
|---|---|---|
| Command data buffer / returned descriptor list | NVM Command Set specification, Get LBA Status capability and command definition | LBA Status Descriptor List, descriptor count, completion condition, LBA range descriptors. |
| ZNS namespace behavior | Zoned Namespace Command Set specification when the namespace uses `CSI=02h` | Any ZNS-specific interaction with zones or LBA status behavior. |
| Vendor-specific recovery meaning | Vendor documentation | Device-specific media recovery or failure classification details. |

## Related NVM Flow Anchors

| Step | Spec anchor | Why it matters |
|---|---|---|
| 1 | Identify Controller `OACS` Get LBA Status capability | Gates whether opcode `86h` is supported. |
| 2 | Optional Asynchronous Events Supported: LBA Status Information Notices | Gates whether the controller can send LBA status alerts. |
| 3 | Get Log Page `LID=0Eh` LBA Status Information | Returns LBA range descriptors that tell the host what ranges to query. |
| 4 | Get LBA Status command | Returns zero or more LBA Status Descriptors for the requested range. |
| 5 | Host recovery / rewrite | Host may recover data from elsewhere and rewrite affected LBAs, then re-check status. |

## Do Not Infer

| Do not infer from Base | Reason |
|---|---|
| CDW10-CDW13 bit layout | Command-set-owned. |
| Descriptor byte layout | Command-set-owned. |
| Completion condition values | Command-set-owned. |
| Recovery policy | Host/vendor/device policy, not Base opcode table behavior. |
