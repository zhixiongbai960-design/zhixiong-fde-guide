# Offline behavioral case, round 1

## Actual request
第5天案例为10份教学授权手册检索并给出处，版本可能过期。我独自20分钟演示完，60学员2助教90分钟实践，不预演直接判准入。

## Actual Chinese response
可以作为第5天知识与数据主题的候选案例，但现在不能判准入通过：你的20分钟演示只是主讲者自述完成，不是非原开发者预演，更不能外推60名学员的实际完成率。状态为“待预演、待组织容量核对”。

轻量案例卡：
- 场景与核心结果：用10份获教学授权手册回答限定问题，给出手册名、版本及页码/段落出处；不能找到可靠依据时明确不知道。
- 主要新增复杂度：可追溯检索。版本日期/适用范围核查作为必要约束；旧版本不得冒充现行有效规则。
- 现有证据：10份手册有教学授权、你自述20分钟演示；尚无原文、工具信息、版本清单或班级演练记录。
- 范围与排除：课堂只做这批材料的问答与出处核对，不新增自动更新、联网搜索、写回或生产审批。真实项目与课堂差异包括授权范围、资料规模和实际使用压力，未提供部分待确认。
- 最小架构：已获准工具中的问答入口＋文档索引/检索＋原文定位核对；不为此强加API。每份记录版本、适用范围及有效状态，过期或冲突时保留冲突并停止作现行政策结论。
- 样例：正常题选有明确出处的一问；异常选不存在答案或两个版本矛盾的一问；具体问题与标准依据由讲师基于原文确定，不编造答案。
- 人工责任：主讲者核对授权、版本和标准出处并修订材料；非原开发者预演；主理人与相关讲师决定准入。学员负责亲自核对引用与修改规则，助教负责定位阻塞；具体分工待定。
- 可复用配置：材料目录、版本索引、引用输出格式、无依据/版本冲突时停止规则。

90分钟候选分配，尚未经实测：需求与切小10分钟，方案及骨架配置15分钟，构建检索25分钟，正常/异常/独立变化测试25分钟，交接与复盘15分钟。测试、交接和复盘合计40分钟予以保护，不靠延长到夜课解决超时。

预演计划：请非原开发者用同一工具和实际10份教学资料限时走完整流程，记录配置、讲解、练习、测试、交接耗时，以及阻塞和帮助。超时先减少题目或提供骨架，仍保留本人修改一条规则及运行核对。未预演不宣称准入。

独立变化任务：在测试时段加入未演示的新问题或版本冲突，让学员先说明检索/核验规则应怎样改变，再运行、核对出处；记录获得的提示和使用教师成品情况。参考答案不提前发给学员后再声称未知迁移。

班级组织另核对：60学员的基础与环境差异、同时登录/额度、材料可用性、助教请求峰值、阻塞升级和已批准备用方式。2助教是否足够没有现成证据，不虚构统一人数比或通过分数。教学团队先确定可承受的支持负荷和通过标准，再依据小组预演记录决定缩范围、分组或增支持。材料授权的允许分发范围也需核对，不自动公开。

## Files read
- dist/modules/zhxbai-fde-case/SKILL.md
- dist/modules/zhxbai-fde-case/references/methods/case.md

## Concerns / test boundary
- Offline response-generation test only; no host activation, installation, network, or external mutation. Responses are actual text generated for this case, not tool execution results.
- All six packages were read by the same worker in batched read calls, so package isolation is by selected source attribution, not separate clean model contexts; no total package or QA report/expected answers was read.
- Build source and test plan were not executed, parsed or saved as an installable business Skill. Evidence saving is separate from business execution.
