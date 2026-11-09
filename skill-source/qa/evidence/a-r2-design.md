# a-r2-design evidence

## Raw input

需求确认员工用本地离线资料按固定规则算金额，我核对后手动录入系统，不准上传。我同事建议为了三层架构先上云数据库、网页和自动API写回。请给最小方案及建议是否采纳，具体金额规则尚未提供。

## Reads

- Listed only dist/modules/zhxbai-fde-design and its references file names.
- Read dist/modules/zhxbai-fde-design/SKILL.md.
- Read dist/modules/zhxbai-fde-design/references/methods/design.md.
- No other package, total skill, QA evidence, network, or business operations read or performed.

## Actual output

建议不采纳当前“先上云数据库、网页和自动 API 写回”的方案。云数据库违反“不准上传”，自动写回改变了“你核对后手动录入”的已确认流程；网页也不是实现三层架构的必要条件。三层可以是本机程序的逻辑分层，不必变成三个在线服务。

最小候选方案：本地资料 → 员工选择资料并检查必填项 → 本机确定性程序按已确认规则计算 → 生成本地核对清单 → 你核对 → 你手动录入现有系统。

- 输入层：只读取获准的本地文件，字段映射待确认，不改原文件。
- 规则层：用确定性代码计算和校验，固定规则无需让模型猜金额。规则单独保存版本；当前批次输入、参考资料和计算结果分开放置。
- 输出层：本地清单列记录标识、来源定位、计算依据、规则版本、计算过程、金额及异常标记，供你逐笔核对。实际业务字段、金额精度和舍入方式尚未确定。
- 人员分工：员工选取资料、处理缺项；规则负责人确认规则和样例；你核对并手动录入。规则维护责任人待指定。

不新增云数据库、在线文档、系统 API、RAG 或多 Agent。若已有完全离线且获准的 Agent，可仅辅助组织步骤，Skill 只提供方法和边界；二者都不是计算所必需。没有本地模型也能用本地脚本完成。任何工具输出、日志及模型上下文都不能把私有原文或结果传出本机，不能仅以“不上传附件”代替这个限制。

实现顺序：先确认规则及合成样例，再核对输入字段，之后实现本地计算和清单，最后由你用预期结果验收。现阶段只是设计，不能称为已具备准确计算或生产使用条件。

验证计划（仅设计推演，未运行或处理真实数据）：
- 正常样例：用合成输入走完整流程，逐步对照人工给出的预期金额。
- 边界样例：确认金额精度、舍入以及规则阈值两侧的结果。
- 缺字段、格式错误、规则冲突或来源冲突：停止该条计算并列明待核对项，不默认为零、不猜结果。
- 重复记录或重复运行：提示核对，不覆盖原始资料；输出失败就停下，不转用云端，也不自动重试系统录入。
- 数据边界：检查依赖、日志和工具调用是否存在外传路径；不能确认离线边界时，只用合成或明确获准的脱敏样例验证。

当前阻塞是金额规则缺失，最先要验证的是规则能否从现有本地字段唯一确定金额。能否提供一份不含私有资料的金额规则说明，包含适用条件、精度/舍入和一个合成输入及预期金额？

## Limits

- Design only. No private source materials or amounts were processed.
- No formula, actual fields, API, connectivity, or numerical results were invented.
- No external connections, uploads, writes to a business system, or implementation occurred.
- Only the explicitly scoped evidence file was written.
