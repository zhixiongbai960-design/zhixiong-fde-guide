# Standalone scope test evidence

## Raw prompt

原范围是一份本地报表，只给我看，金额字段叫总额。现在我只想把显示标题改为本月合计，不改任何公式、输入、数据流、收件人、接口或验收口径。这算必须重新报价的大变更吗？先帮我判断，不修改。

## Actual output

按你描述，这属于显示文案的小调整，不是必须重新报价的大变更。

- 原范围：本地报表，仅供你查看，金额字段显示为“总额”。
- 新请求：只把显示标题改成“本月合计”。
- 影响：只改展示文字，目标、公式、输入、数据流、收件人、接口和验收口径均保持不变，不据此增加“按月筛选或汇总”的工作。
- 取舍：可按这个小调整处理；如果原数据并非本月范围，“本月合计”可能让人误解，但这只是标题准确性提醒，不代表你已要求修改计算逻辑。

以上判断依据是你的描述，尚未检查报表实现或原报价约定。是否另收费要看双方原约定，不能仅凭换标题认定必须重新报价。若有交付方，可由你与交付方确认这是一项仅改文案的小调整；没有第三方就无需额外引入审批。

我没有修改报表，也没有作出价格或工期承诺。

## Reads

- Listed only dist/modules/zhxbai-fde-scope and files to depth 2.
- Read dist/modules/zhxbai-fde-scope/SKILL.md.
- Read dist/modules/zhxbai-fde-scope/references/methods/scope.md.

## Limits

- Used only the standalone scope package. No total skill, other packages, existing QA, network, report implementation, or contract read.
- No report modification, external communication, price commitment, or execution action.
- This evidence file is the only requested write.
- Classification is conditional on the user's expressly stated unchanged behavior, not independently verified implementation facts.
