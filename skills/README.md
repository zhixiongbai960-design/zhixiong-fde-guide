# 志雄 FDE Skills

志亚科技出品 · 作者：白志雄 · 当前目录版本 0.5.0；公开发布以对应仓库提交为准。

## 一次安装完整参谋能力

[zhixiong-fde-Expert 专家技能](zhixiong-fde-expert/)内置 18 方法与 33 篇指南完整文字，无需再装独立模块；先读[使用说明](zhixiong-fde-expert/README.md)。本技能负责需求分析、具体产品/架构设计、项目推进、相关方协调、工程交接和证据评审，不直接或委派实现业务代码、应用/接口、测试脚本或业务 Skill。可以有条件推荐，最终决定由用户或有权方作出。

18 模块的精确当前字节已完成连续两阶段合成案例及独立审查，36 答进入新 QA；原 review 的另 2 答及未决原因保留，不改成通过。最终专家包的两条三阶段跨路由回归共6答已独立通过，不与模块回答或包装单测混计。本轮实际44答，最终接受集42答，原review旧链2答及未决结论保留。最新状态与限制见[0.5.0验证记录](../skill-source/docs/v0.5.0-validation.md)。本地包不是远端发布、宿主兼容或生产能力证明。

## 18 个独立模块

每个目录均为已受测的 0.5.0 固定包，自带方法闭包、实际引用模板、相关原文和许可，无需互装依赖。总包已覆盖这些能力，不必重复安装。

- [zhxbai-fde-ready](zhxbai-fde-ready/)：课前就绪。
- [zhxbai-fde-knowledge](zhxbai-fde-knowledge/)：项目知识整理。
- [zhxbai-fde-review](zhxbai-fde-review/)：需求判断。
- [zhxbai-fde-scope](zhxbai-fde-scope/)：机会与范围。
- [zhxbai-fde-design](zhxbai-fde-design/)：产品与最小架构设计。
- [zhxbai-fde-build](zhxbai-fde-build/)：业务Skill方法设计与交接。
- [zhxbai-fde-deliver](zhxbai-fde-deliver/)：验证策略与交付评审。
- [zhxbai-fde-case](zhxbai-fde-case/)：案例教学。
- [zhxbai-fde-need](zhxbai-fde-need/)：需求追问挖掘。
- [zhxbai-fde-client](zhxbai-fde-client/)：客户与机会。
- [zhxbai-fde-chat](zhxbai-fde-chat/)：客户聊天分析。
- [zhxbai-fde-poc](zhxbai-fde-poc/)：Demo与POC设计。
- [zhxbai-fde-team](zhxbai-fde-team/)：配合与授权。
- [zhxbai-fde-deal](zhxbai-fde-deal/)：项目商务。
- [zhxbai-fde-run](zhxbai-fde-run/)：运行评审与复用设计。
- [zhxbai-fde-next](zhxbai-fde-next/)：项目卡点推进。
- [zhxbai-fde-code](zhxbai-fde-code/)：工程方案与证据评审。
- [zhxbai-fde-doc](zhxbai-fde-doc/)：MVP设计评审。

## 历史与迁移

旧 `zhxbai-fde` 0.4.2 与 8 个 `fde-*` 入口继续保持原字节。它们不是新版别名，旧 fde-* 含方法正文而非纯跳转，也不自动获得新边界；尤其旧构建职责与新版不同，不应混用后声称采用新参谋范围。0.4.0 的 manifest/release-manifest 与旧验证报告保留为历史，不代表当前批次。

本次将 18 独立分发目录更新为精确受测的 0.5.0 包，旧模块构建清单已另存 `history/BUILD-MANIFEST-modules-before-v050.json`；新清单为 `BUILD-MANIFEST-modules.json`。旧专家清单同样保存在 history/。旧包完整字节可从历史版本取得；没有静默修改用户已安装目录。

升级时先把旧包整体移到宿主扫描目录之外备份，再安装所选版本；不要同时安装新旧总包或重复模块。原 requirement-analysis 继续兼容已有使用习惯，其需求能力已包含于新版，无需另装。

## 方法与维护

- [32 张方法卡](01_方法卡片与Skill对照.md)
- [课程覆盖与衔接](03_课程覆盖与衔接.md)
- [33 篇指南与模块覆盖](../skill-source/docs/课程与指南覆盖.md)
- [单一权威源码与维护流程](../skill-source/README.md)
- 历史：[0.4.2](../skill-source/docs/v0.4.2-validation.md)、[0.4.3](../skill-source/docs/v0.4.3-validation.md)、[0.4.4](../skill-source/docs/v0.4.4-validation.md)验证记录。

指纹用于完整性核对，不代替真实行为判断。许可、作者和来源保持原样，见[LICENSE](../LICENSE)；公开不等于自由商业使用。正文随包提供，图卡与远端版本核对需要联网。
