# NVM Write Zeroes Restrictions

| Condition | Rule / expected behavior |
|---|---|
| Namespace is write protected | Return Namespace is Write Protected. |
| Range contains read-only blocks | Return Attempted Write to Read Only Range, unless caused by namespace write-protection state. |
| `PRCHK` is non-zero | Invalid field / invalid PI behavior; `PRCHK` shall be cleared. |
| `STC` is set | Invalid field / invalid PI behavior; `STC` shall be cleared. |
| `WZSL` non-zero and ONCS bit 3 clear, and range exceeds limit | Abort with Invalid Field in Command. |
| `WZSL` non-zero and ONCS bit 3 set, and range exceeds recommendation | Command can encounter processing delays. |
| `DEAC=1` and namespace supports zero reads from deallocated LBAs | Controller should deallocate while preserving zero read behavior. |
| Namespace uses ZNS (`CSI=02h`) | Apply ZNS overlay rules for zone boundary, write pointer, zone state, and active/open resources. |
