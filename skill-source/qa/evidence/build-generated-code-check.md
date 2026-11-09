# 构建技能生成源码补充验证

从 c-r2-build.md 原样提取 scripts/gate.py 与 tests/test_gate.py 到一次性临时目录，执行 Python 标准库合成单元测试，未安装技能、未访问外部系统。

命令：python3 -m unittest discover -s tests -v

退出码：0

```text
test_above_threshold_requires_review (test_gate.GateTests.test_above_threshold_requires_review) ... ok
test_below_threshold_does_not_authorize_execution (test_gate.GateTests.test_below_threshold_does_not_authorize_execution) ... ok
test_decimal_boundary_is_exact (test_gate.GateTests.test_decimal_boundary_is_exact) ... ok
test_equal_threshold_requires_review (test_gate.GateTests.test_equal_threshold_requires_review) ... ok
test_input_cannot_supply_an_approval (test_gate.GateTests.test_input_cannot_supply_an_approval) ... ok
test_invalid_amount_blocks (test_gate.GateTests.test_invalid_amount_blocks) ... ok
test_missing_amount_blocks (test_gate.GateTests.test_missing_amount_blocks) ... ok
test_new_synthetic_rule_is_not_hardcoded (test_gate.GateTests.test_new_synthetic_rule_is_not_hardcoded) ... ok
test_unconfirmed_configuration_blocks (test_gate.GateTests.test_unconfirmed_configuration_blocks) ... ok
test_unit_mismatch_blocks (test_gate.GateTests.test_unit_mismatch_blocks) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.002s

OK
```

这仅支持上述生成代码的10项合成函数测试，不替代CLI解析、真实输入、接口、宿主加载、权限安全或课堂可靠性验证。原始测试者的“未执行”记录保留，不追溯修改。临时目录已自动清理。
