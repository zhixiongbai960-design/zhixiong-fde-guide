# Standalone client-module evidence

## Raw prompt

客户已有开发团队，能开发，但想让我判断该做培训系统还是先用现成工具；他愿意安排业务负责人聊真实流程，预算等范围明确。我需要卖什么服务、先拿什么信息，是否必须先给完整免费方案？

## Raw response

你现在最适合卖的是**付费的方向咨询：判断现成工具能否满足需求、哪些部分值得自建，以及先验证哪一段**。客户缺的主要是取舍依据，不是开发人手。业务对象是“培训系统”，不代表你应当卖“工具培训”；只有员工确实不会用现成工具时，培训陪跑才是另一项服务。

这条机会值得推进。愿意安排业务负责人、讨论真实流程、明确预算和范围，都是积极信号，但还不能据此保证成交。建议先做一次有边界的需求沟通，再确认付费评估的范围，不必直接接整套系统开发。

**先拿这些信息，最好让业务负责人拿最近一次真实培训走一遍：**

1. 为什么现在要改？谁提出的，哪些人使用，现在哪里最费时或最容易出错？希望改善什么，怎样判断有用？
2. 目前从材料准备、员工学习、练习、测试到主管查看结果，分别由谁做、用什么工具、产生什么记录？请提供可用于评估的脱敏材料和典型例子，不用一开始索取全部数据。
3. 哪些能力是必须的？例如员工身份、学习进度保存、中断后续学、测试记录、主管看板、权限和异常处理。区分“必须有”与“以后再说”，不要仅凭“想做个智能体”确定交付物。
4. 已有工具、账号、系统和接口是什么？能否满足使用入口、数据保存与权限要求？若要接现有小程序或内部系统，客户团队负责哪部分？数据可否发送到外部模型，谁负责后续维护？
5. 核实预算覆盖的是咨询、采购还是开发与长期维护，期望时间，以及谁推动、谁拍板、谁签约付款、谁确认结果。范围明确也要落实到这些具体责任。

**把咨询卖成一个明确的小项目。**

可以约定：围绕一个培训流程，访谈业务与技术负责人，检查现有材料和约束，比较“现成工具”“现成工具加少量集成”“独立开发”三条路线，交付一份可供决策的建议。说明每条路线满足哪些需求、有哪些缺口、成本与维护负担如何、哪些结论仍需验证，以及推荐的首个试点和验收方式。工具能力和接口未经检查，不能写成已经可用；成本估计也要标明依据和假设。

是否做小样或验证，应由关键不确定性决定，并写进范围和费用。例如只验证“员工退出后能否按身份恢复进度”，而不是顺手免费开发整套培训系统。你的承诺是提供有依据的选择建议，不是保证业务效果或替客户承担全部实施风险。如果缺少相关实施经验，要说明边界，不冒充做过同类项目。

**不必先给完整免费方案。**

普通售前可以给：你理解的问题、需要哪些材料、评估方法、拟交付什么、服务范围及报价。深入流程诊断、工具适配验证、详细路线方案、定制 Demo 等，可作为付费工作。是否免费初谈、时长多长，由你决定并提前说清；不要让“先聊一下”无限扩大成完整交付。后续若需要培训或实施，再单独确认范围，不必捆绑销售。

你可以这样跟客户说：

“你们已经有开发能力，这次我主要帮你们判断哪些需求用现成工具就能满足，哪些确实值得自建。我们先请业务负责人带着一个真实培训流程和现有材料聊一轮，同时请技术负责人说明现有系统和约束。之后我给出一个范围明确的咨询提案，约定评估内容、交付物、时间和费用。深入评估后再建议是否开发，避免在方向没验证前投入整套系统。”

下一步由客户安排业务和技术负责人、准备一个流程样例；你负责发出简短材料清单，并确认首次沟通的时长与边界。沟通后先复述已确认事实、列出缺口，再提交付费咨询提案。

## Reads

Only the standalone package `dist/modules/zhxbai-fde-client` was inspected.

- Directory listing and file discovery within that package.
- `SKILL.md`, `references/guide-index.md`, `references/methods/engage.md` in full.
- Keyword search across package guide articles 01–06 including 05 extra; output included matching source excerpts.
- Focused original passages: `fde_01.md` lines 40–60; `fde_02.md` 50–108; `fde_03.md` 30–142; `fde_05.md` 74–108; `fde_06.md` 18–88.

## Limits

- No total package, sibling module, existing QA evidence, network source, or outreach was accessed.
- No external action was taken; the proposed client wording is an unsent draft.
- No customer facts beyond the prompt, tool capabilities, price, conversion rate, implementation history, or guaranteed outcome were invented.
- This answer does not decide build versus buy before inspecting the customer's real process and constraints. The only write is this requested evidence artifact.
