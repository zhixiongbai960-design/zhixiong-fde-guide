# 独立模块评审证据：a-r2-doc

## 原始输入

请只评审，不实现。需求已确认本地筛high且open的ticket_id本人核对，不上传/发信/改CRM。设计：本机Python标准库读UTF-8逗号CSV，3列必需；severity合法high/medium/low，status合法open/closed；ticket_id非空且唯一；精确匹配，空/非法/重复/缺列/解析错误列明并停，无候选输出；有效后只终端显示ticket_id或零条。源文件只读，无网络/模型/API。合成测试覆盖全部规则，重开复跑及无外传/源未改待核验。还未写代码。可以进入实现吗？

## 实际评审回复

可以进入这项限定的本地实现与验证。就你提供的设计片段，未发现阻止开工的需求冲突；这不是已实现、已通过测试或可交付的结论。本次只评审，不开始写代码。

- 需求与完整流程已有依据：本地 CSV 输入，筛出 severity 精确为 high 且 status 精确为 open 的 ticket_id，终端展示后由你核对。不上传、不发信、不改 CRM，边界一致。
- 规则已有依据：必需列 ticket_id、severity、status，枚举、非空、唯一、精确匹配及失败停止已明确。应按现有要求先完成全文件校验，再展示候选，避免前几行已输出、后续发现错误。大小写或前后空格不应被静默改成合法枚举。
- 组件与权限边界合适：确定性标准库脚本负责校验和筛选，CSV 提供事实，你负责业务核对。本任务不需要模型、API、数据库或 CRM 权限系统。
- 异常和验收方向明确，但尚未实测：“合成测试覆盖全部规则”现在属于测试计划。后续应保留各规则的输入、预期、实际结果，尤其核对正常命中、合法零命中，以及候选行之后出现错误时仍不输出候选。
- 实施与交接仍有待核验项：确认目标本机 Python 可运行；从实际终端入口重开复跑；检查源文件运行前后未变，核验程序无外传；最后由你核对结果。它们是实现后的验证工作，不是当前设计必须推倒重写的缺口。

建议实现顺序：合成用例与预期 → 只读解析和全量校验 → 校验成功后筛选输出 → 实际入口复跑与边界核验。这里仅给出评审建议，未执行这些步骤。

## 读取文件

读取范围仅限独立模块 dist/modules/zhxbai-fde-doc：

- SKILL.md
- references/guide-index.md
- references/project-navigation.md
- references/methods/product-review.md
- references/guide/fde_09.md
- references/guide/fde_12.md
- references/guide/fde_13.md
- references/guide/fde_14.md
- references/guide/fde_20.md
- references/guide/fde_22.md
- references/guide/fde_23.md

读取目录元数据以定位本模块文件。七篇指南首次合并读取发生输出截断，后单独完整读取 fde_14.md；不能宣称截断部分均已完整查看。

## 限制与实际动作

仅评审用户提供的设计片段，未读取真实 CSV、业务代码或环境配置，未实施、未运行测试。未使用网络，未读总包、其他模块或现有 QA 内容。唯一写入为本证据文件。未将用户的计划或待核验事项表述为已验证事实。
