# NVMe Base Spec 2.0 Reference Guide

這份文件是 `NVMe Spec` 目錄的人類閱讀指南。它說明這一層 markdown 要怎麼用、每個索引檔負責什麼，以及什麼時候要往 command folder 或 I/O command-set layer 展開。

## 這一層負責什麼

SPEC layer 只負責 NVMe specification facts：

- spec 章節、figure、table 的來源定位；
- command opcode、queue type、data transfer direction、NSID 規則；
- CDW、selector、data structure、reserved field、vendor-specific field 的規格定義；
- Base Spec 2.0 明確定義的 expected behavior；
- completion behavior 與 status code；
- Base Spec 2.0 哪些細節交給 NVM / ZNS / Key Value I/O Command Set specification。

SPEC layer 不負責：

- PyNVMe3 API 怎麼呼叫；
- pytest fixture、測試腳本、shell command、執行順序；
- DUT vendor-specific 推測；
- 沒有明確來源的個人經驗補完。

如果需要 PyNVMe3 API 對應，SPEC layer 只指出「這個議題應交給 API layer」。API layer 的入口仍在製作中，因此不是 SPEC layer 的完成條件，也不要在這裡直接寫 API 呼叫。

## 主要來源

Base Spec 2.0 的主要來源是：

```text
..\NVMe Base Spec\2.0\NVMe\NVM-Express-Base-Specification-2_0-2021.06.02-Ratified-5.md
```

I/O Command Set 來源在同一個 `2.0` source bundle：

| Command Set | CSI | 版本 | 來源 |
|---|---:|---|---|
| NVM Command Set | `00h` | 1.0 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-NVM-Command-Set-Specification-2021.06.02-Ratified-1.md` |
| Key Value Command Set | `01h` | 1.0 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-Key-Value-Command-Set-Specification-1.0-2021.06.02-Ratified-1.md` |
| Zoned Namespace Command Set | `02h` | 1.1 | `..\NVMe Base Spec\2.0\NVMe\NVM-Express-Zoned-Namespace-Command-Set-Specification-1.1-2021.06.02-Ratified-1.md` |

目前 local Base 2.0 source bundle 有包含 Key Value Command Set Revision 1.0；如果 Base reference 與 local source 版本描述有差異，請在 command-set index 裡保留版本差異註記。

## 根目錄索引

| File / Folder | 用途 |
|---|---|
| `SPEC_AGENTS.md` | 給 agent 的 spec-layer 行為規則。 |
| `SPEC_REFERENCE_GUIDE.md` | 這份人類閱讀指南。 |
| `Base_Spec_2_0_Index.md` | Base Spec 2.0 source 與章節 / figure 閱讀地圖。 |
| `Admin_Command_Spec_Table.md` | Base Spec 2.0 Admin command opcode table。 |
| `IO_Command_Spec_Table.md` | Base Spec 2.0 common I/O command opcode table。 |
| `Status_Code_Reference.md` | 全域 status code 類別與值。 |
| `Command_Status_Matrix.md` | Base Spec 明確綁定 command 與 status 的對照。 |
| `controller-properties-2.0\` | Base 2.0 Controller Properties 的 canonical database：offset、size、controller applicability、bit/field/value、access path 與跨規格邊界。 |
| `admin-commands-2.0\` | Admin command folders。 |
| `io-commands-2.0\` | Base common I/O command folders。 |
| `io-command-sets-2.0\` | NVM / ZNS / Key Value I/O command-set 邊界與 command index。 |
| `zns-command-set-1.1\` | ZNS 1.1 詳細 command layer，包含 ZNS-owned commands 與 ZNS-modified NVM commands。 |
| `fabrics-base-2.0\` | Base Spec 2.0 section 6 的 Fabrics Command Set layer，使用 `OPC=7Fh` + `FCTYPE` 當 command identity。 |
| `mi-1.2\` | NVMe Management Interface 1.2 的獨立 source / command index。 |
| `pcie-transport-1.0\` | NVMe over PCIe Transport Specification 1.0 的獨立 source / register index。 |
| `rdma-transport-1.0\` | NVMe RDMA Transport Specification 1.0 的獨立 source index。 |
| `tcp-transport-1.0\` | NVMe TCP Transport Specification 1.0 的獨立 source index。 |
| `mctp-base-1.3.1\` | MCTP Base DSP0236 1.3.1：EID、packet/message、message type、tag、routing、discovery、MCTP Control。 |
| `mctp-pcie-vdm-1.0.1\` | MCTP over PCIe VDM DSP0238 1.0.1：PCIe VDM 封裝、routing、discovery、timing。 |
| `mctp-smbus-i2c-1.1.0\` | MCTP over SMBus/I2C DSP0237 1.1.0：Block Write、slave address、PEC、ARP、NACK/retry/fairness、timing。 |
| `CHECKLIST\SPEC_MARKDOWN_CHECKLIST.md` | 自檢 checklist。 |
| `CHECKLIST\SPEC_COMPLETENESS_STATUS.md` | command folder completeness 狀態。 |

## Command Folder

每個 command folder 的核心檔案通常是：

```text
README.md
command-facts.md
status-reference.md
```

複雜 command 可能追加：

```text
selector-reference.md
field-reference.md
payload-reference.md
restrictions.md
cross-spec-boundary.md
COMMAND_CONTENT_AUDIT.md
```

先讀 `README.md` 和 `command-facts.md`。只有在需要精確 selector、payload ownership、field/bit/value lookup、status、限制條件、跨 spec 邊界時，才展開其他 reference 檔案。

新的 command folder 不應該固定長出一整組檔案；應該依 command 複雜度增減。目標是讓 Codex 之後能精準命中測試與 FW 解讀真正需要的欄位，例如 `ONCS bit 5`、`OACS bit 6`、`SANICAP.NDI`、`RESCAP bit 3` 這類 field lookup。

## Controller Properties Layer

`controller-properties-2.0\` 負責 Base Spec 2.0 section 3.1.3 的 Controller Property 空間。問 `CAP.DSTRD`、`CC.EN`、`CSTS.RDY`、`AQA.ASQS`、`CMBLOC.BIR`、`PMRSTS.HSTS`，或某個 property offset 代表什麼時，先讀這層，不必回原始大份 spec。

| File | 用途 |
|---|---|
| `README.md` | 閱讀入口、ownership 與通用 access rule。 |
| `CONTROLLER_PROPERTY_INDEX.md` | Figure 35 的 offset、size、I/O/Admin/Discovery applicability、名稱與 detail routing。 |
| `CORE_CONTROLLER_PROPERTIES.md` | `CAP`、`VS`、`CC`、`CSTS`、`NSSR`、`NSSD`、`CRTO` 欄位。 |
| `ADMIN_QUEUE_INTERRUPT_PROPERTIES.md` | `INTMS`、`INTMC`、`AQA`、`ASQ`、`ACQ` 欄位。 |
| `MEMORY_REGION_PROPERTIES.md` | CMB、Boot Partition、PMR 欄位。 |
| `cross-spec-boundary.md` | Base field meaning 與 Fabrics、PCIe、MI access wrapper 的分界。 |

同一個 property 可以有不同存取路徑：NVMe-oF 用 Fabrics Property Get/Set；NVMe over PCIe 用 BAR memory-mapped access；out-of-band MI 可用 PCIe-through-MI Memory Read/Write。三者最後都回到這層解釋 property 本身的欄位意義。

## I/O Command-Set Layer

`io-command-sets-2.0\` 是 Base Spec 與 NVM / ZNS / Key Value I/O Command Set 規格之間的橋。

這層目前完成：

- `BOUNDARY-COMPLETE`：Base 哪些地方把內容交給 command set 已經索引；
- `COMMAND-INDEX-COMPLETE`：NVM / ZNS / Key Value 的版本、CSI、I/O command、feature、log、Identify、Namespace Management hook 已經建表。

重要檔案：

| File | 用途 |
|---|---|
| `io-command-sets-2.0\COMMAND_SET_INDEX.md` | 三個 I/O command set 的版本、CSI、來源總表。 |
| `io-command-sets-2.0\BASE_TO_COMMAND_SET_BOUNDARY.md` | Base Spec 2.0 何時停止，何時要讀 command-set spec。 |
| `io-command-sets-2.0\NVM_COMMAND_SET_INDEX.md` | NVM Command Set 1.0 index。 |
| `io-command-sets-2.0\ZNS_COMMAND_SET_INDEX.md` | Zoned Namespace Command Set 1.1 總索引。 |
| `zns-command-set-1.1\ZNS_COMMAND_SET_INDEX.md` | ZNS 詳細 command index：Zone Append / Zone Management，以及 ZNS 修改過的 NVM commands。 |
| `io-command-sets-2.0\KEY_VALUE_COMMAND_SET_INDEX.md` | Key Value Command Set 1.0 index。 |

這層的目標是避免每次都直接讀完整 command-set specification。若後續要寫 ZNS Zone Append 測試，應該先從這裡找到 Zone Append 的 CDW、status、restriction、zone state 規則，再決定是否讀原始 spec section。

## Fabrics Base Layer

`fabrics-base-2.0\` 是獨立 layer，但它的來源仍然是 Base Spec 2.0 section 6。

特別標註：

- Fabrics Command Set 本體在 Base Spec 2.0 裡，不是另外一份 PDF。
- 它獨立出來，是因為所有 Fabrics commands 都使用 `OPC=7Fh`，真正 command identity 是 `FCTYPE`。

重要檔案：

| File | 用途 |
|---|---|
| `fabrics-base-2.0\FABRICS_COMMAND_SET_INDEX.md` | Fabrics `FCTYPE` command index。 |
| `fabrics-base-2.0\BASE_TO_FABRICS_BOUNDARY.md` | Base-owned Fabrics facts 與相關 source ownership。 |
| `fabrics-base-2.0\FABRICS_STATUS_REFERENCE.md` | Figure 97 Fabrics command-specific status。 |
| `fabrics-base-2.0\commands\` | Property Set、Connect、Property Get、Authentication Send/Receive、Disconnect、Vendor Specific folders。 |

## Transport Layers

`pcie-transport-1.0\`、`rdma-transport-1.0\` 與 `tcp-transport-1.0\` 是獨立 source layer。PCIe 已經補成完整 transport reference；RDMA / TCP 目前負責讓 agent 快速找到 transport-specific setup、queue、data transfer、keep alive、error handling、PDU / private data 等來源位置。

目前狀態：

| Folder | 狀態 | 用途 |
|---|---|---|
| `pcie-transport-1.0\` | `COMPLETE` | PCIe transport section / figure / register map、doorbell、queue、reset、interrupt、power、error、host-flow reference。 |
| `rdma-transport-1.0\` | `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE` | RDMA transport section / figure map。 |
| `tcp-transport-1.0\` | `BOUNDARY-COMPLETE + SOURCE-INDEX-COMPLETE` | TCP transport section / figure map。 |

## MI Layer

`mi-1.2\` 是 NVMe Management Interface Revision 1.2 的獨立 layer。Base Spec 2.0 只定義 `NVMe-MI Send` / `NVMe-MI Receive` 這兩個 Admin command opcode 邊界；真正的 MI message、out-of-band / in-band tunneling、Management Interface Command Set、MI Admin tunneling、PCIe Command Set、VPD / enclosure / reset 等內容在 `mi-1.2\`。

目前狀態：

| File | 用途 |
|---|---|
| `mi-1.2\MI_SOURCE_INDEX.md` | MI source section / figure map。 |
| `mi-1.2\MI_COMMAND_SET_INDEX.md` | Management Interface Command Set index。 |
| `mi-1.2\MI_MESSAGE_HEADER_REFERENCE.md` | 共用 4-byte MI header、request/response、`NMIMT` command selector、`CSI`、`CIAP`、`MEB`、message identity boundary 與 MIC。 |
| `mi-1.2\MI_COMMAND_REFERENCE.md` | MI opcode、support、field、payload direction、command-control rules。 |
| `mi-1.2\admin-through-mi\README.md` | Out-of-band Admin-through-MI 的入口。 |
| `mi-1.2\admin-through-mi\MI_ADMIN_THROUGH_COMMAND_TABLE.md` | MI Figure 114：Admin command O/M/P support，並連回 Base Admin command folder。 |
| `mi-1.2\admin-through-mi\command-format-reference.md` | MI Figures 115-118：Admin-through-MI request/response wrapper bytes。 |
| `mi-1.2\admin-through-mi\support-overlays-reference.md` | MI Figures 121-125：Get Log Page、Feature、sanitize/format support overlays。 |
| `mi-1.2\admin-through-mi\status-boundary-reference.md` | MI wrapper status 與 tunneled NVMe Admin completion status 的分界。 |
| `mi-1.2\pcie-through-mi\README.md` | Out-of-band PCIe Command Set through MI 的入口。 |
| `mi-1.2\pcie-through-mi\SECTION_7_SOURCE_MAP.md` | 完整 Section 7 subsection、Figures 126-144 與原文 source routing；同時釐清 Figure 122 並非 PCIe support table。 |
| `mi-1.2\pcie-through-mi\MI_PCIE_THROUGH_COMMAND_TABLE.md` | MI Figure 128：Configuration、I/O、Memory Read/Write opcode 與 optional support。 |
| `mi-1.2\pcie-through-mi\command-format-reference.md` | MI Figures 126-130：PCIe-through-MI 共用 request/response bytes。 |
| `mi-1.2\pcie-through-mi\field-reference.md` | MI Figures 131-144：`LENGTH`、BAR、12/32/64-bit `OFFSET` 與 data 規則。 |
| `mi-1.2\pcie-through-mi\status-and-restrictions-reference.md` | PEL、range check、Access Denied、PCIe Inaccessible 與 operational restrictions。 |
| `mi-1.2\MI_STATUS_AND_ERROR_REFERENCE.md` | MI Response Message Status 與常見 error mapping。 |
| `mi-1.2\MI_INBAND_OUTOFBAND_BOUNDARY.md` | in-band / out-of-band mechanism ownership。 |

## MCTP Layers

MCTP 是 NVMe-MI 常見的 out-of-band transport substrate。它不是 NVMe Admin/I/O queue，也不是 PyNVMe API。它負責把管理訊息包成 MCTP packet/message，再透過 SMBus/I2C 或 PCIe VDM 這類 binding 傳送。

最重要的分層：

```text
NVMe-MI command / response payload
  inside MCTP message
    inside MCTP packet
      over SMBus/I2C Block Write
      or over PCIe VDM
```

三個 MCTP folder 的角色：

| Folder | 負責內容 |
|---|---|
| `mctp-base-1.3.1\` | MCTP 共用邏輯：EID、endpoint、bus owner、bridge、message type、SOM/EOM、packet sequence、TO、message tag、MCTP Control commands、routing、discovery。 |
| `mctp-pcie-vdm-1.0.1\` | PCIe VDM transport binding：MCTP packet 怎麼放進 PCIe Type 1 VDM、DMTF Vendor ID、VDM code、Route-to-Root Complex、PCIe endpoint discovery、timing。 |
| `mctp-smbus-i2c-1.1.0\` | SMBus/I2C transport binding：MCTP packet 怎麼放進 SMBus Block Write、`Command Code=0x0F`、source/destination slave address、PEC、SMBus ARP、NACK/retry/fairness/timing。 |

MCTP 常用 lookup 檔案：

| File | 用途 |
|---|---|
| `mctp-base-1.3.1\MCTP_COMMON_HEADER_REFERENCE.md` | MCTP common packet/message 欄位：Destination EID、Source EID、`SOM/EOM`、packet sequence、`TO`、message tag、`IC`、message type。 |
| `mctp-base-1.3.1\MCTP_CONTROL_COMMAND_REFERENCE.md` | MCTP Control common fields、completion codes、Set/Get Endpoint ID、Get UUID、Get MCTP Version Support、Get Message Type Support、Prepare/Endpoint Discovery、Discovery Notify。 |
| `mctp-pcie-vdm-1.0.1\MCTP_PCIE_VDM_PACKET_REFERENCE.md` | PCIe VDM packet fields、routing values、DMTF Vendor ID、MCTP VDM code、timing。 |
| `mctp-smbus-i2c-1.1.0\MCTP_SMBUS_I2C_PACKET_REFERENCE.md` | SMBus/I2C packet byte placement、`0x0F` command code、source/destination slave address、PEC、bridge behavior。 |
| `mctp-smbus-i2c-1.1.0\MCTP_SMBUS_I2C_TIMING_ADDRESS_REFERENCE.md` | SMBus/I2C retry/timing、control timing、reserved/well-known slave addresses、ARP/address assignment notes。 |

常見混淆：

| 路徑 | 是否使用 NVMe SQ/CQ | 是否使用 MCTP | 是否使用 PCIe VDM |
|---|---:|---:|---:|
| 一般 NVMe over PCIe Admin/I/O | Yes | No | No |
| NVMe-MI over MCTP over PCIe VDM | No | Yes | Yes |
| NVMe-MI over MCTP over SMBus/I2C | No | Yes | No |

所以同樣看起來都可能碰到 PCIe，但一般 NVMe over PCIe 是 queue/doorbell/DMA 路徑；NVMe-MI over PCIe VDM 是 PCIe message/VDM 路徑。
## 建議閱讀路徑

查 Base Admin command：

```text
SPEC_AGENTS.md
Base_Spec_2_0_Index.md
Admin_Command_Spec_Table.md
admin-commands-2.0\<opcode-command>\README.md
admin-commands-2.0\<opcode-command>\command-facts.md
admin-commands-2.0\<opcode-command>\field-reference.md   # 如果要查 payload 欄位 / bit / value
```

查 Base common I/O command：

```text
SPEC_AGENTS.md
Base_Spec_2_0_Index.md
IO_Command_Spec_Table.md
io-commands-2.0\<opcode-command>\README.md
io-commands-2.0\<opcode-command>\command-facts.md
```

查 NVM / ZNS / Key Value I/O command set：

```text
SPEC_AGENTS.md
io-command-sets-2.0\README.md
io-command-sets-2.0\COMMAND_SET_INDEX.md
io-command-sets-2.0\BASE_TO_COMMAND_SET_BOUNDARY.md
io-command-sets-2.0\<target>_COMMAND_SET_INDEX.md
zns-command-set-1.1\ZNS_COMMAND_SET_INDEX.md    # 如果 target 是 ZNS
```

查 Fabrics command：

```text
SPEC_AGENTS.md
fabrics-base-2.0\README.md
fabrics-base-2.0\FABRICS_COMMAND_SET_INDEX.md
fabrics-base-2.0\commands\<target-fctype-command>\README.md
fabrics-base-2.0\commands\<target-fctype-command>\command-facts.md
fabrics-base-2.0\FABRICS_STATUS_REFERENCE.md    # 如果需要 status
```

查 RDMA / TCP transport：

```text
SPEC_AGENTS.md
rdma-transport-1.0\README.md 或 tcp-transport-1.0\README.md
rdma-transport-1.0\RDMA_TRANSPORT_INDEX.md 或 tcp-transport-1.0\TCP_TRANSPORT_INDEX.md
```

查 PCIe transport：

```text
SPEC_AGENTS.md
pcie-transport-1.0\README.md
pcie-transport-1.0\PCIE_TRANSPORT_INDEX.md
pcie-transport-1.0\PCIE_TRANSPORT_BEHAVIOR_REFERENCE.md      # 如果需要 doorbell / queue / reset / interrupt / power / error
pcie-transport-1.0\PCIE_REGISTER_FIELD_REFERENCE.md          # 如果需要 register / capability field rules
```

查 NVMe-MI：

```text
SPEC_AGENTS.md
mi-1.2\README.md
mi-1.2\MI_SOURCE_INDEX.md
mi-1.2\MI_COMMAND_SET_INDEX.md
mi-1.2\MI_MESSAGE_HEADER_REFERENCE.md                      # 如果要查 request type / command selector / CSI / message identity / MIC
mi-1.2\MI_COMMAND_REFERENCE.md
mi-1.2\admin-through-mi\README.md                            # 如果問題是 out-of-band Admin-through-MI
mi-1.2\admin-through-mi\MI_ADMIN_THROUGH_COMMAND_TABLE.md     # 如果要查 Admin opcode O/M/P support 與 Base Admin routing
mi-1.2\admin-through-mi\command-format-reference.md           # 如果要查 Admin-through-MI request/response wrapper bytes
mi-1.2\admin-through-mi\support-overlays-reference.md         # 如果要查 Log Page / Feature / sanitize/format support overlays
mi-1.2\admin-through-mi\status-boundary-reference.md          # 如果要分清楚 MI status / NVMe Admin completion status
mi-1.2\pcie-through-mi\README.md                              # 如果問題是 out-of-band PCIe Command Set through MI
mi-1.2\pcie-through-mi\SECTION_7_SOURCE_MAP.md                 # 如果要核對完整 Section 7 原文與 Figure 126-144
mi-1.2\pcie-through-mi\MI_PCIE_THROUGH_COMMAND_TABLE.md       # 如果要查 Configuration / I/O / Memory opcode 與 optional support
mi-1.2\pcie-through-mi\command-format-reference.md            # 如果要查共用 MI request/response wrapper
mi-1.2\pcie-through-mi\field-reference.md                     # 如果要查 LENGTH / BAR / OFFSET / Request Data / Response Data
mi-1.2\pcie-through-mi\status-and-restrictions-reference.md   # 如果要查 PEL / range / Access Denied / PCIe Inaccessible
mi-1.2\MI_STATUS_AND_ERROR_REFERENCE.md
mi-1.2\MI_INBAND_OUTOFBAND_BOUNDARY.md
```

查 MCTP / NVMe-MI transport substrate：

```text
SPEC_AGENTS.md
mctp-base-1.3.1\README.md
mctp-base-1.3.1\MCTP_BASE_INDEX.md
mctp-base-1.3.1\MCTP_COMMON_HEADER_REFERENCE.md
mctp-base-1.3.1\MCTP_CONTROL_COMMAND_REFERENCE.md
mctp-base-1.3.1\MCTP_TO_NVME_MI_BOUNDARY.md       # 如果要分清楚 MI / MCTP / transport ownership
mctp-pcie-vdm-1.0.1\MCTP_PCIE_VDM_PACKET_REFERENCE.md                    # 如果走 PCIe VDM
mctp-smbus-i2c-1.1.0\MCTP_SMBUS_I2C_PACKET_REFERENCE.md                  # 如果走 SMBus/I2C
mctp-smbus-i2c-1.1.0\MCTP_SMBUS_I2C_TIMING_ADDRESS_REFERENCE.md          # 如果查 timing / address / PEC / retry
```
只有 index 不夠時，才打開原始 specification 的特定 section 或 figure。

## 跟其他 Layer 的邊界

| Layer | 負責內容 |
|---|---|
| SPEC layer | spec facts、field、status、expected behavior、cross-spec boundary。 |
| API layer | PyNVMe3 API 怎麼正確呼叫。 |
| Test-flow layer | 測試目的、前置條件、步驟、驗證順序、cleanup、風險處理。 |
| Script-style layer | 最終腳本格式、命名、檔案慣例。 |

SPEC layer 可以說「這個議題應該去 API layer 找實作方式」，但不要直接寫 API 呼叫。
