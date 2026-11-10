# 志雄 FDE Skills：单一源码与独立模块

志亚科技出品 · 作者：白志雄。当前方法、专家配置、总入口和 18 独立分发包版本均为 0.5.0；当前为发行工作树，实际公开发布以对应仓库提交为准。实际验证状态见[0.5.0记录](docs/v0.5.0-validation.md)。

## 参谋职责与单一来源

角色“志雄”是依据作者公开方法提供指导的 FDE 参谋 AI，不冒充本人。负责需求分析、具体产品/架构设计、项目推进、相关方协调、工程交接与证据评审；不直接或委派承担业务代码、应用/接口或业务 Skill 实现，不代最终决定。技术规格、JSON 契约、设计伪代码、手测方案与已有代码/日志设计级评审均保留。

`src/methods/` 是唯一方法源，每个方法自带独立边界；名称/描述/依赖/版本在 `src/registry.json`。`src/guide/` 保留完整 33 原文，`src/total-SKILL.md` 是总入口源，导航与 MVP 模板仍按实际任务加载。来源与许可未改，不把作者原文的工程实践删窄为本技能职责。

## 本轮真实 QA 与构建

18 精确冻包完成 18 条连续两阶段合成案例，36 实际回答及独立审查被选作当前 QA。原 review 另两答完整保留为未决链历史；新 review-v2 是明确差值方向的新完整链，不改旧判。两个阶段相关，不是独立样本；没有无 Skill 对照，不证明因果增益、无提示泛化、宿主或生产能力。

`qa/evidence/v050-advisory/` 保存完全合成题面、完整精确业务答复与公开审查说明；不带私人资料或运行协调记录。旧 `qa/modules.json` 在 `qa/history/modules-before-v050.json` 逐字保留，旧 evidence 不改。新 `qa/modules.json` 只绑定当前哈希的真正通过两阶段与独审。

在本目录运行 `python3 tools/package.py verify --target modules` 核对 18 包；`python3 tools/package_expert.py build` / `verify` 沿用原 QA 门禁，不绕过、不制造通过。正式专家包组装后已对最终122文件完成两条三阶段回归，6答独立通过；本轮44实际答中选定42答通过，原review旧链2答保留，不称全部44答通过。`python3 -m unittest discover -s tests -v` 检查包装基础设施，与行为 QA 分开计数。当前专家测试仅把版本断言更新为真实 0.5.0，负向覆盖保留，原基线和旧运行结论不改。

## 分发与历史

18 模块由 `dist/modules/` 的精确受测树同步到 `skills/` 同名目录；正式专家输出在 `dist/expert/zhixiong-fde-expert/`，同步完整专家目录及清单。同步不改变受测模块哈希。旧模块/专家清单保存到 `skills/history/`，旧总包0.4.2、8旧入口、旧报告和旧0.4.0清单保持原字节。

当前源码的 `build-total` 会产生旧名加当前方法，不能复现旧0.4.2，也不得覆盖历史总包。`src/total-SKILL.md`保留打包器需要的旧name/标题；专家发行身份由 `packaging/expert.json` 和不变的 `package_expert.py` 转换。

维护时先定位依赖、算 `hashes` 和 `affected --module <id>`，受影响字节必须重测；共享构建器/许可变更会扩大范围。已安装包不会跟随源码静默变化。失败保留旧产物，构建/回滚为单写者操作，不并发安装正在切换的目录。

远端发布与宿主安装是独立步骤，须分别核验。完整远端仓库另有本地源副本未携带的图片，发布必须基于远端原树叠加受控 delta，不能用本地副本替换全树。历史 [0.4.2](docs/v0.4.2-validation.md)、[0.4.3](docs/v0.4.3-validation.md)、[0.4.4](docs/v0.4.4-validation.md)仅代表当时结果；旧 current-module-hashes.json 是历史辅助文件，当前哈希以实算及新清单为准。
