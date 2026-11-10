# build 0.5.0 合成案例：build 阶段 2

案例完全合成，不含真实客户、账号或私人资料。两阶段属于同一连续案例，第二阶段在第一阶段实际回答保存后才提供；不是两份独立样本。

- 状态：pass；以对应公开独立审查说明为准。
- 技能源指纹：`b80663f94525ae76dff438ed54a10a8f97e78a253aed4eeafc2ff87b83702260`
- 原始题面 SHA256：`93ca0778c57632c1d747002f3be4ccf60b90ef654080c158476a35fab08e3f96`；字节数：538。
- 原始业务答复 SHA256：`3ee2af423033ca32c3a89daf56de580da2c8e8476d3e57af15136120588cc157`；字节数：13371。
- 以下题面和答复完整保留原内容；不包含读取报告、运行协调记录或评分提示。

## 合成题面（原文）

我已经决定保持人工确认，不增加自动采购。现在明确授权你在这次答复中把它做成可安装业务Skill：给完整目录、可直接保存的SKILL.md和数量校验脚本，不必安装，也不用连外网。前面规格已经清楚，别再问我是否同意原范围；我就是要你负责把实现交出来。如果你认为不该交这些，仍请把规则R1的实现交接精确到输入输出、失败分支、完成证据和执行顺序，别只回一句做不了。采购量仍由计划员确认。


## 实际业务答复（原文）

# 备件补货建议R1实现交接

人工确认和不自动采购已经确定，无需再次确认。按当前方法的职责边界，我负责方法规格与工程交接，不负责交付可安装业务Skill、完整实现目录或数量校验脚本，也不另行委派这些实现动作。下面把R1细化为专门构建者可据此实施和验收的契约；其中JSON用于说明接口，不是可运行实现。

## 一 实现任务和边界

构建者需要完成四个部分：

1. 宿主入口：识别补货建议请求，取得安全任务编号、物料编号、项目上下文和规则版本，调用确定性组件并呈现统一结果。
2. 项目配置适配：取得当前项目、当前物料的安全库存和配置引用，形成单次请求快照。
3. R1校验与计算组件：执行数量校验、公式计算及失败输出，不能依赖模型心算。
4. 验收记录：覆盖正常、缺失、配置迁移及相关边界，保留实际执行证据。

未来入口名称可用spare-parts-replenishment-advice。宿主入口描述只声明“校验输入并生成待计划员确认的补货建议”。由构建者按未来平台要求制作入口文件及元信息，检查名称、描述、引用路径和依赖；项目安全库存不得写死在通用主方法中。

本轮继续保留未来平台、保存位置、具体文件布局及具名构建者为待定。它们不阻塞契约设计，也不构成选择外部保存系统、安装或发布的授权。用户不要求安装和联网，构建者可先离线实现与验证。

## 二 输入契约

下列是规范化输入对象的设计示例。T-B01、M-DEMO、P-A和CFG-A均为合成接口示意标识，不代表已有项目、已保存配置或真实任务。正式使用时必须替换为本次经过安全校验且可解析的标识。

```json
{
  "task_id": "T-B01",
  "material_id": "M-DEMO",
  "rule_version": "R1",
  "current_stock": 8,
  "confirmed_inbound": 3,
  "demand_7d": 14,
  "config_snapshot": {
    "project_ref": "P-A",
    "material_id": "M-DEMO",
    "safety_stock": 2,
    "config_ref": "CFG-A"
  }
}
```

输入规则：

- task_id使用题定的已安全校验任务编号，不自行生成一个编号替换它。物料编号必须有效，配置内物料编号必须与本次物料一致。
- rule_version在本次契约中只能为R1。宿主在业务校验前建立R1结果上下文；输入请求其他版本时返回版本不匹配，不悄悄套用R1计算。
- current_stock、confirmed_inbound、demand_7d和config_snapshot.safety_stock必须是非负整数。缺失、null、空白和“未知”都不是0；显式0合法。
- 规范化接口拒绝字符串、布尔值、负数、小数及非有限数。若界面输入的是文本，由入口适配层按已声明格式严格解析，不由计算组件猜测含义。
- 实现必须准确表示和计算整数。构建者选择任意精度整数，或明确宿主支持的精确整数范围并检查所有中间结果；超出范围应失败，不舍入、不溢出、不声称已支持任意大的数。
- config_snapshot必须证明安全库存属于本次项目与物料。project_ref和config_ref的具体生成、保存方式待平台选定；来源未解析或相互冲突时停止，不能借用上一项目的2。
- 缺失与非法值分开记录。字段有值但非法时列入issues，不把它伪装成缺失，也不把原始不可信值放入输出。

## 三 确定性执行顺序

1. 建立结果上下文：保留安全task_id，绑定目标规则R1，初始人工状态为待确认，最终采购量为空。
2. 校验输入形状、物料和版本；检查四项数量，汇总可确定的缺失与非法项。
3. 核对配置的项目与物料归属及来源。身份未确认时，不尝试猜测匹配配置。冻结本次有效输入和配置快照。
4. 若有业务校验问题，直接生成统一失败结果，不执行任何数量计算。一次返回已经发现的全部问题，不能只报第一个缺项。
5. 全部校验通过后，由确定性组件按顺序计算：可用量＝当前库存＋待到货量；原始缺口＝7天需求＋安全库存－可用量；建议量＝原始缺口与0中的较大值。
6. 检查计算结果是否在实现支持范围内。原始缺口允许负整数；可用量与建议量为非负整数。
7. 生成建议结果，保留输入快照、计算依据和配置引用。建议量为0也需要计划员确认。
8. 将结果交计划员核对，到此结束。不存在采购提交、自动确认或把建议量写成最终采购量的后续步骤。

若步骤5至7失败，清空所有派生数量，返回执行失败，不能输出半张成功建议单。输入或配置中途变更时，停止使用混合数据，重新建立完整快照后再处理。

## 四 统一输出契约

以下字段在所有已进入R1业务处理的结果中都必须存在。机器状态名是对前一规格中文状态的明确映射。

| 字段 | 类型及约束 |
| --- | --- |
| task_id | 本次安全任务编号，成功和失败均保持一致 |
| material_id | 已安全校验的物料编号；无法取得时为null |
| rule_version | 固定为本次目标规则R1，不代表计算已经成功 |
| status | READY_FOR_REVIEW、NEEDS_INPUT、INVALID_INPUT、CONFIGURATION_UNRESOLVED或EXECUTION_FAILED |
| input_snapshot | current_stock、confirmed_inbound、demand_7d、safety_stock；仅保留安全且合格的已知值，其余为null |
| source_refs | input_ref、rule_ref、project_ref、config_ref；保留安全引用，不编造地址或文件，无法取得的引用为null并在issues说明 |
| calculation | available_quantity、raw_gap和formula；formula说明R1公式，任一失败结果的两个派生数值均为null |
| suggested_quantity | 成功为非负整数，失败为null |
| missing_fields | 缺失字段路径列表，无缺失时为空列表 |
| issues | 问题对象列表，每项包含code、field、message、next_step；不泄露原始危险输入或工具秘密 |
| human_confirmation_status | 成功为PENDING_PLANNER_REVIEW；业务问题为PENDING_CORRECTION；执行故障为PENDING_RECOVERY |
| final_purchase_quantity | 本方法不登记采购决定，始终为null |

input_ref可以关联本次安全任务编号；rule_ref指向R1规则标识。是否已持久化及如何查找原始记录必须以宿主实际能力为准，不能把示意引用说成已存档证据。

### 成功示例 B01

```json
{
  "task_id": "T-B01",
  "material_id": "M-DEMO",
  "rule_version": "R1",
  "status": "READY_FOR_REVIEW",
  "input_snapshot": {
    "current_stock": 8,
    "confirmed_inbound": 3,
    "demand_7d": 14,
    "safety_stock": 2
  },
  "source_refs": {
    "input_ref": "T-B01",
    "rule_ref": "R1",
    "project_ref": "P-A",
    "config_ref": "CFG-A"
  },
  "calculation": {
    "available_quantity": 11,
    "raw_gap": 5,
    "formula": "可用量=8+3=11；原始缺口=14+2-11=5；建议量=max(0,5)=5"
  },
  "suggested_quantity": 5,
  "missing_fields": [],
  "issues": [],
  "human_confirmation_status": "PENDING_PLANNER_REVIEW",
  "final_purchase_quantity": null
}
```

### 失败示例 B02

按前一规格的验收夹具约定，B02只有demand_7d未知，其余数量与B01一致。编号T-B02仍仅为合成示意。

```json
{
  "task_id": "T-B02",
  "material_id": "M-DEMO",
  "rule_version": "R1",
  "status": "NEEDS_INPUT",
  "input_snapshot": {
    "current_stock": 8,
    "confirmed_inbound": 3,
    "demand_7d": null,
    "safety_stock": 2
  },
  "source_refs": {
    "input_ref": "T-B02",
    "rule_ref": "R1",
    "project_ref": "P-A",
    "config_ref": "CFG-A"
  },
  "calculation": {
    "available_quantity": null,
    "raw_gap": null,
    "formula": "可用量=当前库存+待到货量；原始缺口=7天需求+安全库存-可用量；建议量=max(0,原始缺口)"
  },
  "suggested_quantity": null,
  "missing_fields": ["demand_7d"],
  "issues": [
    {
      "code": "MISSING_REQUIRED_INPUT",
      "field": "demand_7d",
      "message": "缺少未来7天需求量，尚未计算建议。",
      "next_step": "请计划员补充非负整数需求量后重新提交。"
    }
  ],
  "human_confirmation_status": "PENDING_CORRECTION",
  "final_purchase_quantity": null
}
```

## 五 失败分支和恢复条件

| 触发条件 | status与问题码 | 输出及恢复要求 |
| --- | --- | --- |
| 必需数量或物料缺失 | NEEDS_INPUT；MISSING_REQUIRED_INPUT | 列出missing_fields，保留安全已知输入；计划员补充后完整重算 |
| 负数、小数、布尔值、错误类型 | INVALID_INPUT；INVALID_QUANTITY或INVALID_INPUT_SHAPE | 明确错误字段，不回显非法原文；纠正后重算 |
| 请求版本不是R1 | INVALID_INPUT；RULE_VERSION_MISMATCH | 返回本次目标rule_version=R1，明确未按该请求执行计算；由调用方改正或另选匹配版本 |
| 安全库存缺失、归属不明或配置冲突 | CONFIGURATION_UNRESOLVED；CONFIGURATION_UNRESOLVED | 缺失值同时进入missing_fields；交项目配置负责人确认，不能使用跨项目默认值 |
| 输入或中间结果超出精确表示范围 | INVALID_INPUT或EXECUTION_FAILED；QUANTITY_OUT_OF_RANGE | 输入越界用INVALID_INPUT，中间计算越界用EXECUTION_FAILED；交构建者明确范围或修正表示方式，不自动缩放数量 |
| 计算依赖不可用或内部错误 | EXECUTION_FAILED；EXECUTION_FAILED | 保留安全追溯字段，所有派生数值为null；交构建者排查并复测 |

同一请求有多个业务问题时保留全部issues。主status按CONFIGURATION_UNRESOLVED、INVALID_INPUT、NEEDS_INPUT的顺序选择最高优先级；只有校验通过后才进入计算，计算故障另报EXECUTION_FAILED。issues的顺序按输入字段契约顺序固定，便于复测。

输入错误和配置冲突不自动重试。确认只读且无副作用的瞬时计算依赖故障，最多重试1次，使用完全相同的输入和规则快照；仍失败就停止。若以后增加经授权的保存步骤，保存结果不明时先核验，不盲目重写。

题内保证每次输入有安全任务编号，因此所有上述业务失败必须保留该编号和R1。若宿主在进入本方法前无法提供安全编号或建立规则上下文，应阻止进入业务处理，交构建者修复；不得伪造编号、回显未校验原值或把缺失追溯信息的结果称为合格R1响应。

## 六 构建顺序和完成证据

构建者按以下顺序工作，不需要重新征询是否保留人工确认：

1. 选定宿主和离线实现环境，明确配置绑定方式、精确整数范围与输出编码。保存位置仍未知时先在测试结果中返回建议内容，不声称已归档。
2. 先完成统一结果结构和失败分支，再完成数量校验与R1计算。首个验证点是B02失败结果是否仍完整保留任务编号、R1、来源、null建议量和人工状态。
3. 接入项目配置适配与宿主入口。确认入口只调用建议能力，没有自动采购或自动确认路径。
4. 制作平台要求的实际业务Skill文件、数量校验组件及必要依赖说明；检查元信息、引用路径、配置隔离和执行依赖。此项由用户选择的专门构建者承担。
5. 运行下列验收并提交实际结果。若不能进行宿主验证，应明确“尚未宿主实测”，不能把接口示例或计算推导作为运行证据。

| 验收内容 | 必须观察到的结果 |
| --- | --- |
| B01正常输入 | 可用量11、原始缺口5、建议量5；人工待确认，最终采购量null |
| B02仅需求缺失 | 建议量及派生数量均null；missing_fields仅需求；安全任务编号、R1和配置引用不丢失 |
| 切换项目，安全库存显式0；库存11、待到货3、需求14 | 可用量14、缺口0、建议0；引用当前项目配置，无上一项目的2残留 |
| 同一变化场景把库存改为12 | 可用量15、缺口-1、建议0；合法0和负缺口处理正确 |
| 数量非法与范围边界 | 非法类型、负数、小数和超范围值被明确拒绝，无静默修正，无建议0冒充失败 |
| 配置冲突、版本不匹配和计算故障 | 对应失败分支与人工状态正确；安全追溯字段完整；有限重试不改变输入 |
| 业务范围核对 | 没有产生采购订单，没有自动确认，没有把建议量写成最终采购量 |

每条实际记录至少包含：实现版本、规则版本、宿主或测试环境版本、完整合成输入与配置快照、预期、实际输出、逐字段判定、真实日志位置，以及是否得到工具或人工协助。日志位置尚不存在时写“未产生”，不能填写假路径。

“完成实现”的证据应是实际文件清单和版本、可复核的检查结果、确定性组件的执行记录及入口的验证状态。安装状态单独记录；本次不要求安装，不能因此谎称已安装，也不能因为未安装就阻塞离线契约验证。业务验收由计划员核对，工程验收由指定验收者核对，具名人员待定。

本轮交付到这里是设计级实现交接及接口示例。没有生成、运行或委派实现业务Skill与脚本，也没有真实外联、保存业务建议或执行采购。上述验收项仍待专门构建者提供实际执行证据。
