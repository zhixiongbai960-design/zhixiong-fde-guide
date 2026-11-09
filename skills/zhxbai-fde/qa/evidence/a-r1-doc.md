# doc round 1

## Actual request
需求只本地只读筛工单。设计却上传云模型、猜缺值、直接发客户邮件、加付费登录，演示一次算通过。只评审并给具体修改。

## Actual Chinese response
这份设计片段与“本地、只读、筛工单”明显冲突，暂不建议按它开工。下面只评审你给的片段，未看到完整文档，也不代表整份评审已完成。

1. “上传云模型”：违反本地处理边界，会把工单传出本地。建议替换为：“工单文件仅在本地读取和处理，不调用外部模型或上传服务；筛选采用确定性逻辑。”由需求负责人核对边界，验证时检查实际数据流，而不是只看提示词承诺。
2. “猜缺值”：会把猜测当成工单事实，改变筛选结果。建议替换为：“不推断或补造缺失字段；缺失关键字段或出现无法判定的值时停止，报告行号与字段名，由本人修正源资料后重新运行。”这是建议的保守异常策略，需由你确认；合法值和筛选条件仍待明确。
3. “直接发客户邮件”：新增了原范围没有的对外动作，可能泄露工单资料或误发。建议删除邮件发送组件、凭据和发送步骤，替换为：“结果仅在本地展示给本人核对，不向客户或其他第三方发送。”验收应确认无外发动作。
4. “加付费登录”：未说明服务于哪项原需求，还增加账号、费用与维护负担。建议从本版删除，只保留本地读取入口。若以后确有多人或收费需求，另列新增范围，不占用本次交付。
5. “演示一次算通过”：只能证明一次演示现象，不能覆盖实际任务和失败条件。建议替换为：“用事先核对的样例记录输入、期望结果、实际结果和本人复核结论；至少覆盖正常匹配、无匹配、关键字段缺失及非法值。验证源文件未被改动、无上传和外发。未运行项写未验证。”不凭空添加准确率或商业收益承诺。

七项检查摘要：需求追溯有冲突；完整任务缺少明确输出与人工接手；规则及输入输出有关键缺口；组件责任不合理；资料与授权边界有冲突；异常与验收不足；因此实施交接暂不具备条件。

可以先修正文档，或用合成工单讨论输入到本地结果的链路。进入限定实现前，最少还要明确筛选字段与条件、输出格式，并确认异常策略。修订后的本地方案仍须实测，不能把本次 AI 评审当作验收或上线批准。

## Files read
- dist/modules/zhxbai-fde-doc/SKILL.md
- dist/modules/zhxbai-fde-doc/references/methods/product-review.md
- dist/modules/zhxbai-fde-doc/references/guide-index.md
- dist/modules/zhxbai-fde-doc/references/guide/fde_09.md
- dist/modules/zhxbai-fde-doc/references/guide/fde_12.md
- dist/modules/zhxbai-fde-doc/references/guide/fde_13.md
- dist/modules/zhxbai-fde-doc/references/guide/fde_14.md
- dist/modules/zhxbai-fde-doc/references/guide/fde_20.md
- dist/modules/zhxbai-fde-doc/references/guide/fde_22.md
- dist/modules/zhxbai-fde-doc/references/guide/fde_23.md

## Uncertainty / test limits
文章批量读取返回有截断，部分13/14篇内容未完整进入上下文；核心方法完整读取。只评给定片段，无真实文档版本或页码，无实际运行。未测试宿主安装/技能发现。
