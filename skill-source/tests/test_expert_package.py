"""Rename/packaging invariants. These are not live-host or behavioral acceptance tests."""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
import package
import package_expert


class ExpertPackagingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for name in ('src', 'qa', 'packaging'):
            shutil.copytree(ROOT / name, self.root / name)
        (self.root / 'docs').mkdir()
        shutil.copyfile(ROOT / 'docs/专家技能使用说明.md', self.root / 'docs/专家技能使用说明.md')

    def tearDown(self):
        self.tmp.cleanup()

    def p(self):
        return package_expert.ExpertPackager(self.root)

    def edit_config(self, **kwargs):
        path = self.root / 'packaging/expert.json'
        data = json.loads(path.read_text())
        data.update(kwargs)
        path.write_text(json.dumps(data))

    def test_name_layout_version_and_provenance(self):
        output = self.p().expected('expert')
        self.assertTrue(all(k.startswith('zhixiong-fde-expert/') for k in output))
        entry = output['zhixiong-fde-expert/SKILL.md'].decode()
        self.assertRegex(entry, r'\A---\nname: zhixiong-fde-expert\n')
        provenance = json.loads(output['zhixiong-fde-expert/PROVENANCE.json'])
        release = json.loads(output['zhixiong-fde-expert/RELEASE.json'])
        self.assertEqual(provenance['skill_name'], release['name'])
        self.assertEqual(provenance['version'], release['version'])
        self.assertEqual(provenance['role'], {'name': '志雄', 'type': 'ai-assistant'})
        self.assertEqual(release['version'], '0.5.0')
        self.assertEqual(release['method_baseline_version'], '0.5.0')

    def test_legacy_modules_and_all_behavior_resources_unchanged(self):
        before = package.Packager(self.root)
        legacy = before.expected('total')
        modules = before.expected('modules')
        output = self.p().expected('expert')
        for path, value in legacy.items():
            relative = path.removeprefix('zhxbai-fde/')
            if relative not in ('SKILL.md', 'PROVENANCE.json'):
                self.assertEqual(value, output['zhixiong-fde-expert/' + relative], relative)
        self.assertEqual(legacy, package.Packager(self.root).expected('total'))
        self.assertEqual(modules, package.Packager(self.root).expected('modules'))
        self.assertEqual(len([k for k in output if '/references/guide/' in k]), 33)
        self.assertEqual(len([k for k in output if '/references/methods/' in k]), 18)

    def test_manual_and_ui_are_deterministic(self):
        output = self.p().expected('expert')
        self.assertEqual(output, self.p().expected('expert'))
        self.assertEqual(output['zhixiong-fde-expert/README.md'], (self.root / 'docs/专家技能使用说明.md').read_bytes())
        ui = output['zhixiong-fde-expert/agents/openai.yaml'].decode()
        self.assertIn('display_name: "zhixiong-fde-Expert"', ui)
        self.assertIn('$zhixiong-fde-expert', ui)

    def test_unsafe_or_conflicting_identity_rejected(self):
        for name in ('../outside', 'zhixiong-fde-Expert', 'zhxbai-fde', '/absolute'):
            with self.subTest(name=name):
                self.edit_config(name=name)
                with self.assertRaises(package.Invalid): self.p().expected('expert')

    def test_baseline_mismatch_rejected(self):
        self.edit_config(method_baseline_version='0.0.0')
        with self.assertRaises(package.Invalid): self.p().expected('expert')

    def test_stale_qa_prevents_release_and_preserves_previous(self):
        self.p().build('expert')
        before = package.files(self.root / 'dist/expert')
        (self.root / 'src/methods/knowledge.md').write_text('Changed method')
        with self.assertRaises(package.Invalid): self.p().build('expert')
        self.assertEqual(before, package.files(self.root / 'dist/expert'))

    def test_missing_manual_and_symlink_config_rejected(self):
        (self.root / 'docs/专家技能使用说明.md').unlink()
        with self.assertRaises(OSError): self.p().expected('expert')
        (self.root / 'packaging/expert.json').unlink()
        (self.root / 'packaging/expert.json').symlink_to(ROOT / 'packaging/expert.json')
        with self.assertRaises(package.Invalid): self.p().expected('expert')

    def test_verify_and_rollback(self):
        self.p().build('expert')
        first = package.files(self.root / 'dist/expert')
        path = self.root / 'docs/专家技能使用说明.md'
        path.write_text(path.read_text() + '\nSynthetic test update.\n')
        self.p().build('expert')
        self.p().verify('expert')
        self.p().rollback('expert')
        self.assertEqual(first, package.files(self.root / 'dist/expert'))
        with self.assertRaises(package.Invalid): self.p().verify('expert')


if __name__ == '__main__':
    unittest.main()
