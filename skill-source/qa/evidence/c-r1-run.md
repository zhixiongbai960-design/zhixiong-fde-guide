# Offline behavioral case, round 1

## Actual request
旧客户每天有人纠错，现在新客户要求无人值守，改名字复用就好。维护费按合同15%是不是一定包所有云费？

## Actual Chinese response
不能只改名字复用，也不能从“维护费15%”推出所有云费都包含。

旧项目的成功条件包括每天人工纠错。新项目取消这道环节，历史记录最多证明“经人工纠正后可用”，不能证明无人值守可靠。当前没有具体版本、纠错记录和新合同范围，结论是候选方案待重新验证。
- 可参考：已获复用许可的通用处理步骤、输入检查、停止条件。
- 需重查：哪些错误原来由人纠正，如何发现业务错误、暂停及升级处理；新客户目标、预算、数据、环境、权限、成本与账号归属。
- 历史未验证：不经人工纠错的准确性、异常恢复及持续运行。没有报错不代表业务可用。

先剥离旧客户名称、事实、字段配置、账号、接口地址和凭据；复用权利不清的组件先不带走。用新客户获准的脱敏样例和缺失/错误输入验证，分别记录首次结果、重试、人工介入与耗时，不能把纠正后的成功当首次成功。客户用自己的授权身份独立完成代表任务，并明确资料更新、规则批准、暂停恢复和续费责任。

15%若确实已写进合同，只说明约定的计价方式，费用包含项仍看合同。指南第30篇的15%本身只是作者年度维护报价参考，不是行业通则。分开核对项目尾款、维护服务费、云/模型调用/平台订阅运行费。维护要区分恢复原承诺能力、新增能力和环境适配；范围期限、响应时段、配合条件、恢复核验以及资源额度和超额费用由双方明确，响应不等于保证修复时间。

最优先下一步：给出旧项目最典型的人工纠错记录及合同中的维护/运行费用条款。先据此划出无人值守能力缺口和费用待确认项，再决定适配范围，不承诺无限云费。依据：本包 operate 方法及指南16、17、30、31篇。

## Files read
- dist/modules/zhxbai-fde-run/SKILL.md
- dist/modules/zhxbai-fde-run/references/methods/operate.md
- dist/modules/zhxbai-fde-run/references/guide-index.md
- dist/modules/zhxbai-fde-run/references/guide/fde_16.md
- dist/modules/zhxbai-fde-run/references/guide/fde_17.md
- dist/modules/zhxbai-fde-run/references/guide/fde_31.md
- dist/modules/zhxbai-fde-run/references/guide/fde_30.md

## Concerns / test boundary
- Offline response-generation test only; no host activation, installation, network, or external mutation. Responses are actual text generated for this case, not tool execution results.
- All six packages were read by the same worker in batched read calls, so package isolation is by selected source attribution, not separate clean model contexts; no total package or QA report/expected answers was read.
- Build source and test plan were not executed, parsed or saved as an installable business Skill. Evidence saving is separate from business execution.
