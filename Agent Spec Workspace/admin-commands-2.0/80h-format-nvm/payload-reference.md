# Format NVM Payload Reference

Source: NVMe Base Specification 2.0, section 5.14.

Format NVM has no data buffer payload. All command parameters are carried in `NSID` and `CDW10`.

## Post-Command Readback

| Need | Read back with |
|---|---|
| Selected LBA format and metadata settings | Identify Namespace / command-set-specific Identify data. |
| Protection information state | Identify Namespace and applicable I/O Command Set spec. |
| Whether previous user data is inaccessible | Read/verify behavior according to test design and command-set rules. |
