# ZNS-Modified Write Payload Reference

Write data payload, metadata, protection information, and base completion payload are owned by the NVM Command Set.

ZNS adds no new payload structure for Write. ZNS adds restrictions and status values based on the target zone state, write pointer, range boundary, and active/open resources.
