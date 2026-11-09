# 志雄 FDE Skills

志亚科技出品 · 作者：白志雄 · 专家包0.4.4（当前方法快照0.4.4；模块、入口及包装检查见发布前验证记录）

## 学员：一次安装完整流程

推荐安装完整的 [zhixiong-fde-Expert 专家技能目录](zhixiong-fde-expert/)，安装标识为 `zhixiong-fde-expert`。请先读[学员使用说明书](zhixiong-fde-expert/README.md)，保留目录中的全部文件。包内包含18个方法模块及33篇指南文字，不需要另外安装小技能。

指南、方法源码和可安装技能同仓维护；本目录是可独立安装的分发包，不是另一个仓库。当前发布方式为仓库目录，没有 GitHub Release 或第三方市场上架。发布不等于已安装到你的宿主或通过真实业务验收。

0.4.4只修订chat方法的追问粒度，并保留会议清单例外。旧总包0.4.2和18个独立发行包继续冻结，不随当前方法源码升级。模块两响应、专家入口/跨方法两响应均已独立审阅通过，包装检查已完成；本说明记录发布前验证事实，实际发布以仓库提交为准，见[0.4.4验证记录](../skill-source/docs/v0.4.4-validation.md)。0.4.3的重命名验证记录仅代表历史版本。

按当前问题使用：需求追问 → 需求准入 → MVP规格 → 设计文档评审；也可从客户、POC、代码、交付、维护等任意当前环节进入。已有材料直接复用，不强制全程问卷。

## 独立模块

每个包自带所需方法、模板、资料及许可，可单独安装，不要求互装依赖。总包已覆盖这些能力，不必重复安装。

- [zhxbai-fde-ready](zhxbai-fde-ready/)：课前就绪。
- [zhxbai-fde-knowledge](zhxbai-fde-knowledge/)：项目知识整理。
- [zhxbai-fde-review](zhxbai-fde-review/)：需求判断。
- [zhxbai-fde-scope](zhxbai-fde-scope/)：机会与范围。
- [zhxbai-fde-design](zhxbai-fde-design/)：最小方案设计。
- [zhxbai-fde-build](zhxbai-fde-build/)：业务Skill构建。
- [zhxbai-fde-deliver](zhxbai-fde-deliver/)：验证交付。
- [zhxbai-fde-case](zhxbai-fde-case/)：案例教学。
- [zhxbai-fde-need](zhxbai-fde-need/)：需求追问挖掘。
- [zhxbai-fde-client](zhxbai-fde-client/)：客户与机会。
- [zhxbai-fde-chat](zhxbai-fde-chat/)：客户聊天分析。
- [zhxbai-fde-poc](zhxbai-fde-poc/)：Demo与POC。
- [zhxbai-fde-team](zhxbai-fde-team/)：配合与授权。
- [zhxbai-fde-deal](zhxbai-fde-deal/)：项目商务。
- [zhxbai-fde-run](zhxbai-fde-run/)：运行与复用。
- [zhxbai-fde-next](zhxbai-fde-next/)：项目卡点推进。
- [zhxbai-fde-code](zhxbai-fde-code/)：应用工程检查。
- [zhxbai-fde-doc](zhxbai-fde-doc/)：MVP设计评审。

## 0.4.2 行为与可选资料

- 切换项目只复用方法，不继承其他项目的对象、授权或验收；报价就地分清已约定和待确认项目。
- 简单问题先给短而充分的回答；证据不足可以明确“不足以判断”，仍给能确定的部分和最小查证。评审建议不冒充有权人的批准。
- “志雄”角色以作者公开方法和本人确认的表达为蓝本，不冒充本人或补写经历。
- 可按用户指明的获准材料结合既有决策经验；本包不内置公司决策库，也不建立连接、自动同步或自动发布。缺少私有材料时仍可使用公开方法，并说明限制。
- 新经验先形成待确认修订，再按授权更新与回归。内部记录与公开方法分开；已安装版本不会静默变化。

本次更新knowledge、next、deal、poc、run、code六个独立包至0.4.2，其余12个包保持0.4.1及原有内容。方法只在下述权威源维护。

## 方法与维护

- [32张方法卡](01_方法卡片与Skill对照.md)
- [课程覆盖与衔接](03_课程覆盖与衔接.md)
- [33篇指南与模块覆盖](../skill-source/docs/课程与指南覆盖.md)
- [0.4.2验证记录](../skill-source/docs/v0.4.2-validation.md)及[历史检查记录](../skill-source/docs/检查与版本记录.md)
- [唯一权威源码与维护流程](../skill-source/README.md)

方法只在权威源码修改。小包和总包都是通过测试后生成的固定版本，源码更新不会静默修改已安装包；受影响模块回归通过后再重建总包。包内指纹用于校验来源与完整性，不代替真实行为判断。

旧 `skills/zhxbai-fde` 目录及内部 `name: zhxbai-fde` 保持0.4.2原样，旧安装继续使用旧名称；它不是新名称的自动别名，也不会自动升级。新安装使用 `zhixiong-fde-expert`。升级时先将旧包移到宿主技能扫描目录之外备份，再安装新包；不要同时安装新旧总包或重复的独立模块。旧 fde-* 入口和原 requirement-analysis 仓库也继续保留。历史0.1/0.2检查记录只描述当时版本，0.4.1来源迁移记录保持为历史依据，当前增量验证见0.4.2记录。

许可、作者与来源保持原样，见[LICENSE](../LICENSE)。公开不等于自由商业使用。正文资料随包提供，图卡和远端版本核对需要联网。
