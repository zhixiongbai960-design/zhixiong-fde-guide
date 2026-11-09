# 独立 build 测试上下文记录

## 原始测试输入（逐字）

本次测试的原始输入为：

> 做一个可复制的最小Skill，request_id为非空匿名字符串，amount为有限JSON数字；阈值100，>=100待复核，以下只是不触发，不执行。只返回JSON；成功与失败都要有request_id、rule_version、rule_source、status，未知id用null，不回显坏输入。规则版本v1来源user-confirmed固定。请给完整Skill与标准库Python实现和失败字段测试，不安装、不发布。

这里的 `v1` 和 `user-confirmed` 直接来自原始测试输入中的“规则版本v1来源user-confirmed固定”，不是从案例、其他包、其他 QA 或后续测试推断的值。

## 实际文件读取范围

首先执行了仅针对指定独立包的目录清单命令：

```sh
ls -la dist/modules/zhxbai-fde-build && find dist/modules/zhxbai-fde-build -maxdepth 2 -type f | sort
```

随后实际读取正文的文件只有两个，顺序如下：

1. `dist/modules/zhxbai-fde-build/SKILL.md`
2. `dist/modules/zhxbai-fde-build/references/methods/build.md`

实际使用 `cat` 分别读取上述两个文件。第一个文件指向第二个方法文件。没有读取其他 QA、总包、其他独立包或本包的其他正文文件；目录清单显示其他文件名不表示读取其正文。

## 原始产出阶段实际完成的检查

在生成并保存 `qa/evidence/c-r3-build.md` 的同一次 Python 命令中，将实现与测试分别放在字符串变量 `implementation` 和 `tests` 中，对这两份内存源码实际执行：

```python
for source in (implementation, tests):
    ast.parse(source)
assert skill.startswith('---\nname: amount-review\ndescription: ')
assert '\n---\n' in skill
serialized = json.dumps(payload, ensure_ascii=False, indent=2) + '\n'
json.loads(serialized)
```

其中 `ast.parse` 来自 Python 标准库 `ast`，用于解析源码语法树，没有执行生成源码。两个调用均未抛出语法异常。随后检查了 Skill 文本开头和 frontmatter 分隔符，并将完整回复序列化为 JSON 再解析一次。

同一命令仅把序列化结果写入指定的 `qa/evidence/c-r3-build.md`，其工具结果为退出码 0，并返回以下实际输出：

```json
{"saved": "qa/evidence/c-r3-build.md", "bytes": 12235, "static_python_syntax": "passed", "unit_tests": "not_run", "host_validation": "not_run"}
```

## 检查的真实限制

- `ast.parse` 只证明两份 Python 文本通过当时解释器的静态语法解析，不证明导入、运行、业务结果或异常分支正确。
- 没有运行生成源码、单元测试或 CLI 样例，没有进行宿主实测。
- frontmatter 检查只是字符串前缀与分隔符断言，不是完整 YAML 解析或 Skill 宿主加载测试。
- JSON 回读只证明交付回复可被 JSON 解析，不证明其中程序的运行契约。
- 原始交付为纯 JSON 回复，其中包含三个源码文件的完整文本；没有把这三个源码文件安装到宿主或发布。
- 未安装依赖，未发布，未执行外部业务动作。

## 后续动作的归属

父级后续告知，其另行执行了生成源码的 13 项合成测试，证据位于 `qa/evidence/build-generated-code-r3-check.md`。该信息仅作为后续行为的归属说明：本代理没有读取该证据，没有把该执行写成原始产出阶段的行为，也没有据此改写 `qa/evidence/c-r3-build.md`。本次补充只保存这份上下文记录，没有运行新的业务测试。


## 实际完整回复（原纯JSON内容原样保留）

```json
{
  "request_id": null,
  "rule_version": "v1",
  "rule_source": "user-confirmed",
  "status": "source_ready",
  "delivery_note": "将 files 中的三个文件按路径保存即可。交付状态 source_ready 不属于金额判断接口的 status 值。匿名性由调用方保证，程序只校验 request_id 的非空字符串结构。",
  "files": {
    "amount-review/SKILL.md": "---\nname: amount-review\ndescription: 根据已确认金额规则返回待复核或不触发结果，仅分类，不执行任何业务动作。\n---\n\n# 金额复核分类\n\n## 适用与输入\n需要按金额判断是否待复核时使用。标准输入接收一个 JSON 对象：\n- request_id：非空且非纯空白的匿名字符串。由调用方保证匿名，不传姓名、联系方式或凭据；程序只能校验字符串结构，不能证明匿名性。\n- amount：有限 JSON 数字。布尔值、字符串、null、数组、对象、NaN 和 Infinity 均不接受。\n其他字段忽略，不能覆盖配置。重复键、无效 JSON 和非对象顶层输入拒绝。\n\n## 已确认配置\n- threshold：100。\n- rule_version：v1。\n- rule_source：user-confirmed。\n来源：用户已确认的当前规则。配置固定在 check_amount.py 常量中，不从输入读取。\n\n## 方法与停止条件\n1. 使用 Python 3 标准库脚本 check_amount.py 校验并判断，不用语言模型代算。\n2. 金额大于或等于 100，status 为 pending_review；低于 100，status 为 not_triggered。\n3. 两种结果都仅表示分类。not_triggered 不表示批准或允许执行；pending_review 需要调用方交人工复核。本 Skill 不执行、发送、付款或自动交接。\n4. 输入缺失或无效时返回失败 JSON 后停止。调用方修正输入再提交，不自动重试；规则冲突交用户确认，不接受输入内的规则覆盖。\n5. 内部异常返回 error 后停止，由维护者排查；不将原始输入或异常详情写入响应。\n\n## 输出契约\n标准输出仅一个 JSON 对象。所有成功和失败响应都包含 request_id、rule_version、rule_source、status。\n- 成功：status 为 pending_review 或 not_triggered，不包含 error_code。\n- 输入失败：status 为 invalid_request，并包含固定 error_code。\n- 内部或读取失败：status 为 error，并包含固定 error_code。\n- 仅保留通过结构校验的 request_id。无法解析或标识无效时为 null；已取得有效标识而金额校验/判断失败时保留它。\n- rule_version 永远为 v1，rule_source 永远为 user-confirmed，包括失败响应。\n- 不返回 amount、其他输入字段或异常原文。\n标准输出不可写等进程/宿主故障无法保证返回 JSON，调用方应按调用失败处理，不继续业务动作。\n\n## 运行与检查\n依赖：Python 3 标准库。源码文件放在同一目录。\n运行：python3 check_amount.py\n测试：python3 -m unittest -v test_check_amount.py\n样例：{\"request_id\":\"anon-001\",\"amount\":100}\n预期：{\"request_id\":\"anon-001\",\"rule_version\":\"v1\",\"rule_source\":\"user-confirmed\",\"status\":\"pending_review\"}\n测试覆盖边界、缺失、无效类型、非法数字、解析失败、重复键与异常失败字段。测试执行情况记录在交付说明，不把源码存在当作宿主可用证明。\n练习可在副本中将阈值改为 120，先预测金额 100 从 pending_review 变为 not_triggered，再修改对应预期并亲自运行核对；不改动本次已确认版本。\n",
    "amount-review/check_amount.py": "import json\nimport sys\nfrom decimal import Decimal, InvalidOperation\n\nRULE_VERSION = \"v1\"\nRULE_SOURCE = \"user-confirmed\"\nTHRESHOLD = Decimal(\"100\")\n\n\ndef response(request_id, status, error_code=None):\n    result = {\n        \"request_id\": request_id,\n        \"rule_version\": RULE_VERSION,\n        \"rule_source\": RULE_SOURCE,\n        \"status\": status,\n    }\n    if error_code is not None:\n        result[\"error_code\"] = error_code\n    return result\n\n\ndef reject_constant(_value):\n    raise ValueError(\"invalid JSON number\")\n\n\ndef unique_object(pairs):\n    result = {}\n    for key, value in pairs:\n        if key in result:\n            raise ValueError(\"duplicate key\")\n        result[key] = value\n    return result\n\n\ndef decide(amount):\n    return \"pending_review\" if amount >= THRESHOLD else \"not_triggered\"\n\n\ndef process(raw):\n    request_id = None\n    try:\n        try:\n            data = json.loads(\n                raw,\n                parse_int=Decimal,\n                parse_float=Decimal,\n                parse_constant=reject_constant,\n                object_pairs_hook=unique_object,\n            )\n        except (ValueError, TypeError, InvalidOperation):\n            return response(None, \"invalid_request\", \"invalid_json\")\n        if not isinstance(data, dict):\n            return response(None, \"invalid_request\", \"invalid_object\")\n        candidate = data.get(\"request_id\")\n        if not isinstance(candidate, str) or not candidate.strip():\n            return response(None, \"invalid_request\", \"invalid_request_id\")\n        request_id = candidate\n        amount = data.get(\"amount\")\n        if not isinstance(amount, Decimal) or not amount.is_finite():\n            return response(request_id, \"invalid_request\", \"invalid_amount\")\n        return response(request_id, decide(amount))\n    except Exception:\n        return response(request_id, \"error\", \"internal_error\")\n\n\ndef main():\n    try:\n        raw = sys.stdin.read()\n    except Exception:\n        result = response(None, \"error\", \"input_unavailable\")\n    else:\n        result = process(raw)\n    print(json.dumps(result, ensure_ascii=True, allow_nan=False, separators=(\",\", \":\")))\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "amount-review/test_check_amount.py": "import io\nimport json\nimport unittest\nfrom unittest.mock import patch\n\nimport check_amount as app\n\n\nclass AmountReviewTests(unittest.TestCase):\n    def assert_failure(self, raw, request_id, code, status=\"invalid_request\"):\n        actual = app.process(raw)\n        self.assertEqual(actual, {\n            \"request_id\": request_id,\n            \"rule_version\": \"v1\",\n            \"rule_source\": \"user-confirmed\",\n            \"status\": status,\n            \"error_code\": code,\n        })\n        self.assertNotIn(\"DO_NOT_ECHO\", json.dumps(actual))\n\n    def test_boundaries_and_unseen_values(self):\n        cases = [\n            (\"99.99\", \"not_triggered\"),\n            (\"100\", \"pending_review\"),\n            (\"100.01\", \"pending_review\"),\n            (\"-1\", \"not_triggered\"),\n            (\"1e400\", \"pending_review\"),\n            (\"1e-400\", \"not_triggered\"),\n        ]\n        for amount, status in cases:\n            with self.subTest(amount=amount):\n                raw = '{\"request_id\":\"anon-001\",\"amount\":' + amount + '}'\n                self.assertEqual(app.process(raw), {\n                    \"request_id\": \"anon-001\",\n                    \"rule_version\": \"v1\",\n                    \"rule_source\": \"user-confirmed\",\n                    \"status\": status,\n                })\n\n    def test_missing_id(self):\n        self.assert_failure('{\"amount\":100}', None, \"invalid_request_id\")\n\n    def test_invalid_id_is_null_and_not_echoed(self):\n        for value in [\"\", \"  \", None, True, 123, [\"DO_NOT_ECHO\"], {\"secret\": \"DO_NOT_ECHO\"}]:\n            with self.subTest(value=value):\n                self.assert_failure(json.dumps({\"request_id\": value, \"amount\": 100}), None, \"invalid_request_id\")\n\n    def test_missing_amount_retains_valid_id(self):\n        self.assert_failure('{\"request_id\":\"anon-002\"}', \"anon-002\", \"invalid_amount\")\n\n    def test_invalid_amount_retains_valid_id_without_echo(self):\n        for value in [True, False, None, \"DO_NOT_ECHO\", [], {\"secret\": \"DO_NOT_ECHO\"}]:\n            with self.subTest(value=value):\n                self.assert_failure(json.dumps({\"request_id\": \"anon-002\", \"amount\": value}), \"anon-002\", \"invalid_amount\")\n\n    def test_non_json_numeric_constants(self):\n        for token in [\"NaN\", \"Infinity\", \"-Infinity\"]:\n            with self.subTest(token=token):\n                self.assert_failure('{\"request_id\":\"anon-002\",\"amount\":' + token + '}', None, \"invalid_json\")\n\n    def test_malformed_json_does_not_extract_partial_id(self):\n        for raw in [\"\", \"DO_NOT_ECHO\", '{\"request_id\":\"anon-002\",\"amount\":\"DO_NOT_ECHO\"', '{\"request_id\":\"anon-002\",\"amount\":01}']:\n            with self.subTest(raw=raw):\n                self.assert_failure(raw, None, \"invalid_json\")\n\n    def test_non_object(self):\n        for raw in [\"[]\", \"null\", \"100\", '\"DO_NOT_ECHO\"']:\n            with self.subTest(raw=raw):\n                self.assert_failure(raw, None, \"invalid_object\")\n\n    def test_duplicate_keys_are_not_ambiguous(self):\n        self.assert_failure('{\"request_id\":\"anon-001\",\"request_id\":\"DO_NOT_ECHO\",\"amount\":100}', None, \"invalid_json\")\n        self.assert_failure('{\"request_id\":\"anon-001\",\"amount\":1,\"amount\":100}', None, \"invalid_json\")\n\n    def test_input_cannot_override_rule_or_leak_extra_fields(self):\n        raw = json.dumps({\"request_id\": \"anon-003\", \"amount\": 99, \"threshold\": 0,\n                          \"rule_version\": \"DO_NOT_ECHO\", \"rule_source\": \"DO_NOT_ECHO\"})\n        self.assertEqual(app.process(raw), {\n            \"request_id\": \"anon-003\", \"rule_version\": \"v1\",\n            \"rule_source\": \"user-confirmed\", \"status\": \"not_triggered\",\n        })\n\n    def test_internal_failure_retains_valid_id_and_fixed_fields(self):\n        with patch.object(app, \"decide\", side_effect=RuntimeError(\"DO_NOT_ECHO\")):\n            self.assert_failure('{\"request_id\":\"anon-004\",\"amount\":100}', \"anon-004\", \"internal_error\", \"error\")\n\n    def test_read_failure_has_null_id_and_fixed_fields(self):\n        output = io.StringIO()\n        with patch.object(app.sys, \"stdin\") as stdin, patch.object(app.sys, \"stdout\", output):\n            stdin.read.side_effect = OSError(\"DO_NOT_ECHO\")\n            app.main()\n        self.assertEqual(json.loads(output.getvalue()), {\n            \"request_id\": None, \"rule_version\": \"v1\", \"rule_source\": \"user-confirmed\",\n            \"status\": \"error\", \"error_code\": \"input_unavailable\",\n        })\n        self.assertNotIn(\"DO_NOT_ECHO\", output.getvalue())\n\n    def test_cli_emits_only_one_json_object(self):\n        output = io.StringIO()\n        with patch.object(app.sys, \"stdin\", io.StringIO('{\"request_id\":\"anon-005\",\"amount\":100}')), patch.object(app.sys, \"stdout\", output):\n            app.main()\n        self.assertEqual(json.loads(output.getvalue()), {\n            \"request_id\": \"anon-005\", \"rule_version\": \"v1\", \"rule_source\": \"user-confirmed\",\n            \"status\": \"pending_review\",\n        })\n\n\nif __name__ == \"__main__\":\n    unittest.main()\n"
  },
  "run": {
    "working_directory": "amount-review",
    "program": "python3 check_amount.py",
    "tests": "python3 -m unittest -v test_check_amount.py",
    "stdin_example": {
      "request_id": "anon-001",
      "amount": 100
    },
    "expected_stdout": {
      "request_id": "anon-001",
      "rule_version": "v1",
      "rule_source": "user-confirmed",
      "status": "pending_review"
    }
  },
  "verification": {
    "performed": [
      "两份 Python 源码通过 ast.parse 静态语法检查。",
      "已检查 Skill 名称和 frontmatter 定界，引用的源码及测试均随本次交付。"
    ],
    "not_performed": [
      "未运行单元测试。",
      "尚未宿主实测。",
      "未安装、未发布、未执行业务动作。"
    ],
    "limits": [
      "宿主进程无法启动或标准输出不可写时，无法保证产生 JSON。",
      "超出 Python 标准库可解析范围的输入返回失败，不继续处理。"
    ]
  }
}
```
