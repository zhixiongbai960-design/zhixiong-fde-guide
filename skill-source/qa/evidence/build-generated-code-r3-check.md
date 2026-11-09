# 修正后构建输出补充执行检查

将c-r3-build.md的纯JSON解析成功，将其中三个公开源码文件原样写入一次性临时目录。仅运行自编标准库合成测试，未安装、发布或访问业务系统。

命令：python3 -m unittest -v test_check_amount.py

退出码：0

```text
test_boundaries_and_unseen_values (test_check_amount.AmountReviewTests.test_boundaries_and_unseen_values) ... ok
test_cli_emits_only_one_json_object (test_check_amount.AmountReviewTests.test_cli_emits_only_one_json_object) ... ok
test_duplicate_keys_are_not_ambiguous (test_check_amount.AmountReviewTests.test_duplicate_keys_are_not_ambiguous) ... ok
test_input_cannot_override_rule_or_leak_extra_fields (test_check_amount.AmountReviewTests.test_input_cannot_override_rule_or_leak_extra_fields) ... ok
test_internal_failure_retains_valid_id_and_fixed_fields (test_check_amount.AmountReviewTests.test_internal_failure_retains_valid_id_and_fixed_fields) ... ok
test_invalid_amount_retains_valid_id_without_echo (test_check_amount.AmountReviewTests.test_invalid_amount_retains_valid_id_without_echo) ... ok
test_invalid_id_is_null_and_not_echoed (test_check_amount.AmountReviewTests.test_invalid_id_is_null_and_not_echoed) ... ok
test_malformed_json_does_not_extract_partial_id (test_check_amount.AmountReviewTests.test_malformed_json_does_not_extract_partial_id) ... ok
test_missing_amount_retains_valid_id (test_check_amount.AmountReviewTests.test_missing_amount_retains_valid_id) ... ok
test_missing_id (test_check_amount.AmountReviewTests.test_missing_id) ... ok
test_non_json_numeric_constants (test_check_amount.AmountReviewTests.test_non_json_numeric_constants) ... ok
test_non_object (test_check_amount.AmountReviewTests.test_non_object) ... ok
test_read_failure_has_null_id_and_fixed_fields (test_check_amount.AmountReviewTests.test_read_failure_has_null_id_and_fixed_fields) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.002s

OK
```

此检查覆盖13项合成函数/模拟标准输入输出测试，包含失败关联字段和不回显非法输入。不是目标宿主安装、真实业务、接口或生产可用性验证。原始答复的未执行声明保持原样，此为后续执行记录。
