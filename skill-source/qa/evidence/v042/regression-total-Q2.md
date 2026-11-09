# 0.4.2 合成场景行为验证

本文件为真实模型响应记录。题面均为合成数据，未连接真实客户系统。读取路径仅规范为发布包或合成fixture相对路径，业务题面及答复不改写。

# 当前题面 Q2
这单补充：客户有权负责人刚书面确认报价8000元，交付为方向备忘录、一次评审会和一次修订；修订限同一问题的文字建议、不新增调研。另付资源费300元，付款为签约4000元、完成上述交付并书面确认后4000元。我下周有10小时，双方确认下周五提交。只给三行当前已确认范围、费用付款、排期，不把已确认内容再列待确认，不代表已到账。

# 逐字答案
已确认范围：方向备忘录、一次评审会和一次修订；修订仅限同一问题的文字建议，不新增调研，不含开发。
费用付款：服务费8,000元，签约支付4,000元，完成上述交付并书面确认后支付4,000元；资源费300元由客户另行直接支付，合计8,300元。付款约定已确认，到账情况未核实。
排期：下周可投入10小时，双方已确认下周五提交；此为已确认安排，不代表交付已完成。

# 实际读取清单
本轮未新增读取，沿用同一对话内已实际读取的指定包资料，尤其references/methods/commercial.md。
包根目录：skills/zhxbai-fde
此前累计实际读取：
- SKILL.md
- references/guide-index.md
- references/project-navigation.md
- references/methods/deliver.md
- references/guide/fde_13.md
- references/guide/fde_14.md
- references/methods/progress.md
- references/guide/fde_32.md
- references/methods/coordination.md
- references/guide/fde_18.md
- references/guide/fde_24.md
- references/guide/fde_25.md
- references/methods/operate.md
- references/guide/fde_15.md
- references/methods/commercial.md
- references/guide/fde_08.md
- references/guide/fde_27.md


## 独立审阅

PASS。新确认后准确更新三行范围/价格付款/下周五排期，不再把修订误列未确认，到账和交付仍未证实。

边界：这是加载指定Skill的模型会话行为，不是宿主安装、真实接口或生产验收；宿主约束仍在，未隔离其贡献。
