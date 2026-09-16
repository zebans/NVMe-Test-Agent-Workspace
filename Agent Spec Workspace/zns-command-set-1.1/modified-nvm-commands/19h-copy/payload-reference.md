# ZNS-Modified Copy Payload Reference

The base NVM Command Set owns Copy command fields, Source Range Entry structure, base completion, and base copy semantics.

ZNS adds no new payload structure. ZNS adds source/destination zone restrictions and status values based on:

- whether any Source Range Entry crosses zone boundaries;
- whether the destination LBA range crosses zone boundaries;
- source/destination zone state;
- destination write pointer;
- active/open zone resource availability.
