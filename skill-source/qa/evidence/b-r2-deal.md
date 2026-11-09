# Standalone deal QA evidence

## Raw prompt

合同约定验收书面确认后付尾款，完整源码到账后移交；客户已能测试，昨天验收人书面确认版本v1通过，财务提供银行流水已收到5000元尾款。我想整理收尾清单和给客户说明草稿，不要发送，也别替我作法律结论。

## Actual output

按你提供的情况，目前可记录为：客户具备测试条件；v1 已由验收人书面确认通过；5000 元尾款已由财务提供银行流水确认到账。下一步是按合同整理并移交完整源码等约定成果，而不是继续催款。这是业务状态整理，不是法律效力或责任终结的判断。

### 收尾清单

- 归档同一版本依据：合同及附件、v1 范围、交付与测试记录、验收人的书面确认。将“昨天”替换成原始记录中的具体日期，保留确认人、版本和确认内容。
- 归档收款依据：记录尾款 5000 元、实际到账日期及财务确认，核对流水与本项目对应关系。账单、发票和到账分别登记；尚未提供的信息标为待核对，不把发票状态等同于到账状态。
- 准备完整源码移交包：对应已验收 v1，标明版本标签或提交号；按合同逐项核对源码、配置说明、依赖与构建部署说明、约定文档及其他文件，列明已有组件和第三方许可信息。包内不要夹带个人或其他项目凭据。
- 核对可用性与完整性：检查文件是否齐全、约定构建或部署步骤是否可复现，并如实记录已验证项、未验证项和已知限制，不以“源码已打包”代替核验。
- 安排移交：按约定核对接收人、渠道及时间；需要移交的凭据另走安全渠道。实际移交后记录交付清单、送达和接收确认。当前不要写成“已移交”。
- 收口未完事项：列出尚待交接的内容及负责人；原约定的修复、支持与维护责任按合同继续处理。新增需求另行确认，尾款与后续维护费、系统运行费分开，不因到账就宣布全部责任结束。

### 给客户的说明草稿（未发送）

您好，感谢贵方验收配合。我们已收到验收人于【书面确认日期】对 v1 版本验收通过的书面确认，财务也已根据银行流水确认本项目 5000 元尾款到账。

按合同关于完整源码在到账后移交的安排，下一步将整理并办理 v1 对应的完整源码及合同约定资料的移交。具体文件、版本标识与交接事项将列入移交清单，交接方式和时间按合同约定办理；未明确的部分再与贵方对接确认。

请贵方接收时按清单核对文件完整性，如有交接问题可及时反馈。合同约定的后续事项仍按约处理。

发送前请补齐具体日期，并核对收件人、实际移交准备情况及合同中的交接要求。这里没有发送消息或执行源码移交。

## Reads

- Listed only dist/modules/zhxbai-fde-deal and its files.
- Read SKILL.md.
- Read references/methods/commercial.md.
- Read references/guide-index.md.
- Read references/guide/fde_28.md.
- Read references/guide/fde_29.md.

All reads were under dist/modules/zhxbai-fde-deal. No total package, other QA, network, or business actions were used.

## Limits

- Contract, written acceptance, and bank statement were described by the user but not independently inspected. No assertion of legal enforceability or final discharge of obligations is made.
- Exact acceptance/payment dates, transfer recipient, transfer schedule, contractual file list, invoice status, and support terms remain unprovided.
- No client message was sent, no payment requested, no code transferred, and no project terms changed.
- This evidence file is the only write requested and performed.
