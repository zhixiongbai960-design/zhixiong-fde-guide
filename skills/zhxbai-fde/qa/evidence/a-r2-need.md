# Isolated module evidence: a-r2-need

## Raw prompt
Use only dist/modules/zhxbai-fde-need, no total or other skill. User: 已确认我本人每周在本机筛CSV字段ticket_id,severity,status，severity合法high/medium/low，status合法open/closed，选high且open的ticket_id；空/坏/重复ID列出并停止。我核对，不上传不改CRM不发消息。请直接生成完整MVP规格，未运行，不再采访。 Give actual Chinese artifact. Save raw prompt/response/files read/limits to qa/evidence/a-r2-need.md. No network/external actions. Only this package, fresh context, do not read other QA. Report concise result after writing; scoped write escalation allowed for evidence only.

## Files read
- dist/modules/zhxbai-fde-need/SKILL.md
- dist/modules/zhxbai-fde-need/references/methods/requirements.md
- dist/modules/zhxbai-fde-need/references/templates/mvp-spec.md

Directory listing was limited to this module. No other QA or skill package was read.

## Limits and execution status
- Only the assigned module was used. No total skill, network, external actions, implementation or CSV processing.
- No actual business CSV was supplied or read. All acceptance examples are hypothetical, not run.
- Bad ID validity format and ID comparison semantics remain unspecified; these are recorded without further interview.
- Only this evidence file was written, under the explicit scoped write authorization.
- No historical performance, business impact, review approval, successful execution or user authorization was invented.

## Raw response
# MVP 需求规格：本机 CSV 高优先级未关闭工单筛选
版本：v0.1｜日期：2026-11-09
状态：本人已确认业务范围的规格；未运行，实施可行性与验收结果均未验证。
评审状态：未提供讲师评审意见，尚未讲师评审。
依据：用户已确认本人每周在本机处理 CSV，只提取 severity 为 high 且 status 为 open 的 ticket_id；空、坏、重复 ID 列出并停止；本人核对，不上传、不改 CRM、不发消息。

## 1. 场景、问题与目的
- 使用者与结果核对者均为用户本人；触发频率为每周，由本人在本机发起。
- 输入为本机 CSV；任务为按确定的字段条件生成待人工核对的 ticket_id 清单。
- 当前动作已明确，但耗时、既往错误、具体使用工具、效率损失和原因尚无证据，不作推断。
- 本次要控制的风险是筛选结果包含无效或重复 ID，或在输入异常时仍被误当作完整结果使用。用户已明确要求异常停止；这不是对历史故障的断言。
- 成功结果为用户能核对筛选清单与原 CSV；清单的后续业务用途未说明，也不在本版自动执行范围内。

## 2. 最小范围
### 已确认包含
1. 读取用户指定的一个本机 CSV。
2. 检查必要字段 ticket_id、severity、status。
3. 检查 ID；发现空、坏或重复 ID 时列出异常，并停止，不交付有效筛选清单。
4. 在输入检查通过后，提取同时满足 severity=high 与 status=open 的 ticket_id。
5. 向用户本人展示结果或异常，由用户核对。

### 明确不包含
上传、联网传输 CSV、CRM 读取或写入、发送消息、自动修复数据、自动去重、后台定时运行、批量处理多个文件、登录系统、数据库、多角色和发布部署。每周使用不等于授权建立每周自动任务。

### 建议但尚未确认的细节
以下是文档中的实现建议，不冒充用户已经确认的规则：输入以 UTF-8（允许 BOM）、逗号分隔 CSV 为起点；结果按原记录顺序展示；不默认保存新的结果文件。编码、分隔符与呈现方式可以在实现前根据实际文件适配。

## 3. 输入、处理、输出与使用
### 输入契约
- 必要列：ticket_id、severity、status。
- severity 合法值：high、medium、low。
- status 合法值：open、closed。
- ticket_id 必须非空、符合待明确的有效 ID 规则，并且不重复。
- 实际 CSV、文件路径、编码与样例尚未提供，当前没有读取任何业务 CSV。
- ID 当作文本处理，避免丢失前导零；不擅自转数值或改写内容。
- 建议字段名和值按大小写精确匹配；不自动 trim、转大小写或纠正拼写。空白值是否算空 ID、重复是否按原始文本或规范化后比较，见开工前阻塞。

### 主流程
1. 用户指定本机文件，工具只读打开。
2. 解析 CSV 并检查字段结构。建议对不可读、不可解析、缺必要列或重复表头直接停止并说明原因。
3. 扫描整个输入的数据记录，先做合法性检查，再筛选。不能先筛出 high/open 后才检查 ID，以免漏掉其他记录中的坏数据。
4. 检查空、坏、重复 ID。重复项列出该 ID 的所有出现记录，而非只报告后一次；不自动保留第一条。
5. 对 severity/status 不在合法集合内的记录，建议同样列出并停止，不跳过、不猜测。此为保守失败策略，尚未获得用户对实现细节的确认。
6. 发现可定位的数据异常时，继续只读扫描以汇总异常，之后整体停止；不生成部分成功结果。CSV 结构无法继续可靠解析时，立即停止，并注明异常清单可能不完整。
7. 全部检查通过后，按逻辑与条件 severity=high AND status=open 筛选，输出 ticket_id。
8. 用户核对结果。到此结束，不触发任何后续外部动作。

### 输出契约
- 成功：状态“检查通过，待本人核对”、命中数量与 ticket_id 清单；可附数据记录序号便于定位。
- 零命中：明确显示“检查通过，0 条符合条件”，不把它描述为失败。
- 失败：状态“已停止，未生成有效筛选结果”，异常类型、数据记录序号、可显示的原 ID 与说明。空 ID 显示“空”，不伪造替代 ID；重复项显示全部对应记录序号。
- CSV 允许引号中含换行，定位应使用“表头后第 N 条数据记录”，不将其误称为物理行号。
- 仅展示完成核对需要的字段，不复制不相关列。
- 人工接管：用户检查原文件、决定是否自行修改或重新提供文件；工具不得自行覆盖原 CSV。

## 4. 功能与需求对应
| 功能 | 对应目的 | 输入与规则 | 输出 | 本版状态 |
|---|---|---|---|---|
| 本机只读导入 | 在本机完成每周任务 | 用户指定 CSV，必要三列 | 可解析记录或错误 | 业务范围已确认；文件未提供 |
| ID 校验 | 空/坏/重复 ID 列出并停止 | 全量记录；具体有效格式、空白与重复语义待定 | 异常清单、停止状态 | 已确认；规则细节阻塞完整实施 |
| 枚举校验 | 遵守合法值约束 | severity/status 合法集合 | 非法值清单 | 集合已确认；遇错停止策略为建议 |
| 条件筛选 | 找出 high 且 open 的 ID | 全部检查通过后执行 AND | ticket_id 清单 | 已确认 |
| 人工核对 | 保留本人判断 | 清单与原 CSV 对照 | 本人核对结论 | 已确认，不自动推进业务动作 |

## 5. 实现边界与数据
- 最小候选方案：本机确定性 CSV 处理脚本或等效工具。字段筛选与校验不需要模型推断。
- 若以后采用 Agent + Skill，Skill 规定检查和输出方法，Agent 仅在本机调用获准的只读工具；具体工具与运行环境未选定、未验证。
- 不调用外部 API，不依赖 CRM、云文档或远端存储；不引入账号、密钥或数据库。
- 无新增持久存储需求。建议结果只在本机临时呈现；保存报告文件需另行确定目的地和输出方式。
- 不安装、不编程、不执行试跑。本规格交付不代表已经获得实施或运行授权。
- 原 CSV 始终只读，不自动改编码、删行、去重、填补字段或覆盖文件。

## 6. 验收与试跑
以下均为设计的预期验收，不是真实业务样本或已运行结果。
| 场景 | 输入/前提 | 预期结果 | 本人核对方式 | 实际状态 |
|---|---|---|---|---|
| 正常筛选 | T001/high/open；T002/medium/open；T003/high/closed；T004/low/closed；假设这些 ID 满足最终规则 | 仅 T001 | 逐条核对两个条件同时成立 | 未运行 |
| 零命中 | 所有记录合法，但无 high/open 组合 | 检查通过，0 条命中 | 原 CSV 条件对照 | 未运行 |
| 空 ID | 任一记录缺少 ID，即使不是 high/open | 列出记录，整体停止，无有效清单 | 查原记录 | 未运行 |
| 坏 ID | 任一 ID 不符合最终有效格式 | 列出 ID、记录与原因，整体停止 | 按确定后的规则核对 | 未运行；坏 ID 格式待明确 |
| 重复 ID | 同一 ID 出现两次，包括一次命中、一次不命中 | 列出两处，整体停止，不自动去重 | 比较重复组的全部记录 | 未运行；比较语义待明确 |
| 多种异常 | 可解析 CSV 中有空、坏、重复 ID | 汇总可识别异常，停止，不给部分清单 | 逐条核对清单及原 CSV | 未运行 |
| 缺必要列 | 缺少 severity | 停止并说明缺列，不开始筛选 | 对照表头 | 未运行；失败策略为建议 |
| 非法枚举 | severity=urgent 或 status=pending | 建议列出并停止，不猜值 | 对照合法集合 | 未运行；失败策略为建议 |
| 解析失败 | 引号未闭合、文件不可读等 | 停止并报告，不声称异常清单完整 | 检查文件及错误信息 | 未运行 |
| 空数据文件 | 只有合法表头，无数据 | 建议检查通过，0 条命中 | 确认没有数据记录 | 未运行；行为为建议 |

核对重点：命中项完整且不多选；异常时没有可误用的成功清单；原文件未变更；未上传、未改 CRM、未发送消息。尚无性能、节省时间或业务效果验证，不承诺相关指标。

## 7. 已确认、待确认与开工前阻塞
### 已确认
本人每周、本机 CSV、三个必要字段、两个合法枚举集合、high AND open 条件、异常 ID 列出并停止、本人核对、禁止上传/改 CRM/发消息。

### 待确认但不扩大业务范围
CSV 编码与分隔符、具体本机工具、呈现格式、合法性检查失败的保守停止策略、大小写与空白规范化策略、样本和运行容量。没有编造预算、工期或效果数值。

### 开工前阻塞
- “坏 ID”的判定规则未给出，不能自行规定必须数字、固定长度、特定前缀或正则。
- 空白 ID、前后空格和大小写如何影响“空”与“重复”的判断尚未定义；这些会改变是否停止及结果正确性。
- 实施及试跑还需实际输入文件与明确的执行请求。本次只生成规格，不运行。

可先交接本规格；已确定的字段和筛选条件足以进行静态设计，但在 ID 规则补齐前，不能声称完整校验逻辑可直接上线。

### 下一步
本次直接交付规格，不再采访。后续若用户选择实施，在现有范围上补齐 ID 规则和本机样本、确认必要技术细节，再按上述预期用例试跑并由本人核对。当前没有实施、运行或验收完成。

