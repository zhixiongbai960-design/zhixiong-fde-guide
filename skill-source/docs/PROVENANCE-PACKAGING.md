# 来源元数据与打包指纹

## 0.5.0发行工作树

专家名 `zhixiong-fde-expert`、展示名 `zhixiong-fde-Expert`；专家配置、总入口、registry 顶层及全部18模块版本统一为0.5.0。作者、来源、33篇文章、许可和两个构建器字节不变。

18精确受测模块共36条选定实际回答与独审已正确绑定当前哈希；原review另两答及未决链保留，不改判为通过。完整公共合成题面与业务答复、公开审查说明在qa/evidence/v050-advisory，旧qa/modules.json原字节另存qa/history/modules-before-v050.json。总包仍通过原门禁组装，不靠包装单测替代行为QA。

18包从dist/modules同步至skills同名目录，旧模块清单保存到skills/history。专家正式组装后以RELEASE和BUILD-MANIFEST记录精确源/产物指纹，最终包另做跨路由回归；发布与宿主安装独立验证。指纹不是签名或能力保证。当前状态见[v0.5.0验证记录](v0.5.0-validation.md)。

旧总包0.4.2、8旧入口、旧报告及0.4.0 manifest/release-manifest保留原字节。旧专家/独立包的历史记录不冒充新范围通过依据。

## 原构建器与方法指纹

每个独立包与总包只在包根生成一份 `PROVENANCE.json`，不另复制 `references/provenance.json`。作者、发布者、`zhxbai` 来源标识、仓库、固定来源提交和许可位置均来自 `src/provenance.json`；构建器加入稳定的 `module_id`、`skill_name` 和版本。独立包使用 `src/registry.json` 中本模块的 `modules[].version`；总包使用顶层 `version`。总包使用 `all` / `zhxbai-fde`，并公开角色 `志雄` / `ai-assistant`，不代表或冒充真人作者。

这是非执行 JSON 元数据，不是系统提示、访问控制、输出要求或新的许可。构建器不会读取其中的 URL 发起网络请求，不采集用户数据，不包含遥测或外部命令执行路径。根 `LICENSE` 与 `licenses/` 中的历史来源许可仍按原字节复制。

模块指纹同时包含 `src/provenance.json` 原始字节和该模块实际生成的 `PROVENANCE.json` 字节。共享来源改变会使所有模块的旧 QA 指纹失效；模块版本只使本模块及真正依赖它的包失效。单独更改总包版本不改变独立包字节或 QA 指纹。生成元数据不包含自身或模块的哈希，也不调用模块哈希函数；`SOURCE-HASH.json` 在元数据之后计算，因此没有循环依赖。总入口和无关模块的变更仍不会单独改变其他模块指纹。

缺失或不完整的 `src/provenance.json`、缺失 `registry.version` 或模块自身版本会明确失败，不静默制造作者或来源。合成测试 fixture 已显式补齐这些输入；测试记录不构成真实模块行为 QA。

修改来源或构建器后，先计算影响范围和指纹，生成仅测试暂存包，再交独立审查重新绑定证据。本次只同步全部真实受测的18模块与正式专家新包，保留旧总包和旧入口；同步前保存历史清单。不得为了构建总包伪造或自动刷新 `qa/modules.json` 的 PASS；总包仍必须通过原有 QA 检查。发布和目标宿主安装不属于离线打包验证。

若独立审查记录了 `qa/modules.json` 顶层 `metadata_only_migration.review_path`，构建器要求该报告位于 `qa/` 内、非空且无符号链接，并把报告随总包带入。该可选记录不替代现有两轮行为记录、当前指纹匹配或独立审查门禁。

## 来源基线与逐文件更新

PROVENANCE中的guide_source_commit、requirement_source_commit记录整套作品的固定来源基线，不代表每次构建已在线核实最新提交，也不替代references/source-manifest.json及需求来源清单的逐文件记录。仅更新一个方法或一篇材料时更新其实际引用记录与受影响模块，不为普通增量更新改共享起源标识。若确实变更整套来源基线、作者或许可等共享信息，则全部相关包失效是有意行为，应整体复核。
