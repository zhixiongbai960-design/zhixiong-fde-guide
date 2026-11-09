# 0.4.2 合成场景行为验证

本文件为真实模型响应记录。题面均为合成数据，未连接真实客户系统。读取路径仅规范为发布包或合成fixture相对路径，业务题面及答复不改写。

# 当前题面 X4
现在回到最初那个只读员工排班项目A，不是刚才新合成项目的A/B子任务。原范围和隔离测试授权未改，刚发现员工A刷新时短暂看到B的班次。项目负责人只批准暂停这个试点入口，没批准停其他系统。请给三条最小处理动作，不要真的执行。

# 逐字答案
回到原只读员工排班项目A。短暂看到他人班次也属于权限边界失效，先按阻断问题处理。以下三条仅为建议，未执行：

1. **止住暴露：**由获授权人员按负责人批准暂停这个试点入口，并核对入口确已暂停；向负责人报告刷新时发生跨员工班次泄露。不停其他系统，不扩大暂停范围。
2. **留证定位：**保留最少必要的发生时间、版本、A的登录状态、刷新步骤及脱敏截图/请求日志，交给负责排查的人。沿页面展示、缓存/会话和后端查询权限核对，确认B的班次从哪里进入A的结果；不要预判只是显示问题，也不靠继续暴露真实数据复现。后续复现仅用原已授权的隔离测试A、B。
3. **修复后再决定恢复：**修复方案经确认后处理，在隔离环境复测原刷新路径、A/B各查本人及互查拒绝，核对页面和接口全程不返回他人班次、排班数据未改。保留新版本证据；权限问题未消除则维持试点暂停。证据交负责人确认恢复，不以一次刷新正常自行重开入口。

# 实际读取清单
包根目录：skills/zhxbai-fde
本轮新增读取：
- references/methods/operate.md
- references/guide/fde_15.md
此前同一对话累计已读取：
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


## 独立审阅

PASS。切回旧排班项目保留只读本人限制；只暂停获准入口，不猜根因；隔离复测与恢复批准分开。

边界：这是加载指定Skill的模型会话行为，不是宿主安装、真实接口或生产验收；宿主约束仍在，未隔离其贡献。
