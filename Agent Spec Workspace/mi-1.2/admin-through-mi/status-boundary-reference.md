# Admin-Through-MI Status Boundary Reference

Status: `FIELD-COMPLETE`

Source: NVM Express Management Interface Revision 1.2 section 6.2 and Figures 117-118.

An Admin-through-MI response may contain two different status locations:

| Status location | Owner | Meaning | When to use |
|---|---|---|---|
| Response byte `04` | NVMe-MI | MI response status for the Admin-through-MI request message. | Use for malformed wrapper, invalid opcode not listed in Figure 114, invalid CTLID, invalid command size, or invalid input data size. |
| Response `CQEDW3` Status Field | NVMe Base / I/O Command Set | Status associated with the tunneled NVMe Admin command. | Use when the Admin-through-MI request message is well formed and the command was processed as an NVMe Admin command. |

## Well-Formed Request Rule

An NVMe Admin Command Request Message is not well formed if it contains:

| Error class | Example from MI section 6.2 | Status owner |
|---|---|---|
| Invalid Opcode | Opcode not listed in Figure 114. | MI response status. |
| Invalid Parameter | Controller ID specifies a Controller ID not implemented in the NVM subsystem. | MI response status. |
| Invalid Command Size | Request Message does not contain a complete command. | MI response status. |
| Invalid Command Input Data Size | Request Data field is larger than the size specified in `DLEN`. | MI response status. |

If the Admin-through-MI Request Message is well formed, the response message status is Success and the NVMe Admin command status is reported in `CQEDW3`.

## Prohibited Command Rule

If an NVMe Admin command is issued in a Request Message that is prohibited by Figure 114, the Management Endpoint returns an Invalid Parameter Error Response. The Parameter Error Location (`PEL`) indicates the NVMe opcode.

## Completion Data Rule

For Admin commands that return data, the Admin command may first apply its own offset and length. Then MI `DOFST` and `DLEN` select the portion carried in the Response Data field. Data outside the selected portion is discarded by the Management Endpoint.

## Command ID Rule

In the response mapping, `CQEDW3` is defined by the NVM Express Base Specification, but the Command ID field shall be cleared to `0h`.

