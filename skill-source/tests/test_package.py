"""Infrastructure fixtures are synthetic, not module behavior QA evidence."""
import ast
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('pack', Path(__file__).parents[1] / 'tools/package.py')
pack = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pack)

class PackagingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.modules = [dict(id='base', name='fde-base', title='Base', description='Base task', method_file='base.md', articles=['one.md'], dependencies=[]), dict(id='child', name='fde-child', title='Child', description='Child task', method_file='child.md', articles=['two.md'], dependencies=['base'])]
        self.put('src/methods/base.md', '# Base\n[Template](../templates/spec.md)')
        self.put('src/methods/child.md', '# Child')
        self.put('src/guide/one.md', '# One')
        self.put('src/guide/two.md', '# Two')
        self.put('src/guide/unrelated.md', '# Unrelated')
        for f in ['legal/LICENSE', 'legal/licenses/notice', 'templates/spec.md', 'total-SKILL.md', 'project-navigation.md', 'guide-index.md']:
            self.put('src/' + f, 'Fixture: ' + f)
        self.version = '0.4.1'
        self.total_role = {'name': '志雄', 'type': 'ai-assistant'}
        self.total_entry()
        for module in self.modules:
            module['version'] = '0.4.1'
        self.provenance = {
            'schema_version': 1, 'origin_id': 'zhxbai', 'work_id': 'zhxbai-fde',
            'author': '白志雄', 'publisher': '志亚科技',
            'source_repository': 'https://example.invalid/fixture-source',
            'guide_source_commit': 'synthetic-guide-commit',
            'requirement_source_commit': 'synthetic-requirement-commit',
            'purpose': 'Non-executable attribution; no telemetry or license change.',
            'license_file': 'LICENSE', 'historical_license_directory': 'licenses/'
        }
        self.put('src/provenance.json', json.dumps(self.provenance, ensure_ascii=False))
        self.registry()
    def tearDown(self):
        self.tmp.cleanup()
    def put(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    def total_entry(self):
        self.put('src/total-SKILL.md', '---\nname: zhxbai-fde\nmetadata:\n  role_name: ' +
                 json.dumps(self.total_role['name'], ensure_ascii=False) + '\n  role_type: ' +
                 json.dumps(self.total_role['type']) + '\n---\n# Synthetic total entry\n')
    def registry(self):
        self.put('src/registry.json', json.dumps({'version': self.version, 'total_role': self.total_role, 'modules': self.modules}))
    def p(self):
        return pack.Packager(self.root)
    def test_closure_and_subset(self):
        output = self.p().module('child')
        self.assertIn('references/methods/base.md', output)
        self.assertIn('references/guide/one.md', output)
        self.assertNotIn('references/guide/unrelated.md', output)
        self.assertNotIn(b'Unrelated', output['references/guide-index.md'])
        self.assertIn(b'references/methods/child.md', output['SKILL.md'])
    def test_total_layout_without_assembly(self):
        output = self.p().total_files()
        self.assertIn('zhxbai-fde/LICENSE', output)
        self.assertIn('zhxbai-fde/licenses/notice', output)
        self.assertIn('zhxbai-fde/references/templates/spec.md', output)
        self.assertNotIn('zhxbai-fde/references/legal/LICENSE', output)
        self.assertIn('zhxbai-fde/SKILL.md', output)
    def test_standalone_provenance_links(self):
        self.put('src/requirement-source.md', '[license](../licenses/notice)')
        self.modules[0]['method_file'] = 'requirements.md'
        self.put('src/methods/requirements.md', '# Requirements')
        self.registry()
        output = self.p().module('base')
        self.assertEqual(output['references/requirement-source.md'], b'[license](../licenses/notice)')
        self.assertIn('licenses/notice', output)
        self.assertIn('LICENSE', output)
        self.assertNotIn('references/registry.json', output)
    def test_unrelated_metadata_and_global_navigation_do_not_invalidate(self):
        first = self.p().module_hash('base')
        self.version = '0.5.0'  # Global total version must not invalidate independent modules.
        self.modules[1]['title'] = 'Unrelated title change'
        self.modules[1]['description'] = 'Unrelated metadata change'
        self.registry()
        self.put('src/methods/child.md', 'Unrelated method change')
        self.put('src/project-navigation.md', 'Global navigation change')
        self.put('src/guide-index.md', 'Global guide index change')
        self.put('src/total-SKILL.md', 'Global total version change')
        self.assertEqual(first, self.p().module_hash('base'))
    def test_dependency_change_invalidates_dependents(self):
        before = self.p().module_hash('child')
        self.put('src/methods/base.md', 'Changed dependency')
        self.assertNotEqual(before, self.p().module_hash('child'))
        self.assertEqual(self.p().affected({'base'}), ['base', 'child'])
        self.assertEqual(self.p().affected({'child'}), ['child'])
    def test_provenance_subset_hash(self):
        manifest = {'source_commit': 'global-version', 'articles': [{'article': n, 'source_url': 'https://example.invalid/pinned/' + n, 'packaged_sha256': n} for n in ['one.md', 'two.md', 'unrelated.md']]}
        self.put('src/source-manifest.json', json.dumps(manifest))
        before = self.p().module_hash('base')
        manifest['source_commit'] = 'new-global-version'
        manifest['articles'][1]['packaged_sha256'] = 'unrelated change'
        self.put('src/source-manifest.json', json.dumps(manifest))
        self.assertEqual(before, self.p().module_hash('base'))
        selected = json.loads(self.p().selected('base')['source-manifest.json'])
        self.assertEqual([x['article'] for x in selected['articles']], ['one.md'])
        manifest['articles'][0]['packaged_sha256'] = 'relevant change'
        self.put('src/source-manifest.json', json.dumps(manifest))
        self.assertNotEqual(before, self.p().module_hash('base'))
    def test_shared_license_invalidates_all(self):
        before = {mid: self.p().module_hash(mid) for mid in ['base', 'child']}
        self.put('src/legal/LICENSE', 'Updated license')
        for mid in before: self.assertNotEqual(before[mid], self.p().module_hash(mid))
    def test_unused_template_does_not_invalidate(self):
        self.put('src/templates/unused.md', 'Unused')
        before = self.p().module_hash('child')
        self.put('src/templates/unused.md', 'Unused changed')
        self.assertEqual(before, self.p().module_hash('child'))
        self.assertNotIn('templates/unused.md', self.p().selected('child'))
    def test_tooling_change_invalidates_all(self):
        p = self.p()
        before = {mid: p.module_hash(mid) for mid in ['base', 'child']}
        real = Path.read_bytes
        tool = Path(pack.__file__)
        def changed(path):
            value = real(path)
            return value + b'\n# simulated tool change\n' if path == tool else value
        with patch.object(Path, 'read_bytes', changed):
            for mid in before: self.assertNotEqual(before[mid], p.module_hash(mid))
    def test_traversal_and_names(self):
        for bad in ['../evil', '/absolute', 'foo/../evil', 'a\\b', './evil', 'a//b']:
            with self.subTest(path=bad), self.assertRaises(pack.Invalid):
                pack.safe(self.root, bad)
        self.modules[0]['name'] = '../outside'
        self.registry()
        with self.assertRaises(pack.Invalid): self.p()
    def test_dependency_cycle_and_missing(self):
        self.modules[0]['dependencies'] = ['child']
        self.registry()
        with self.assertRaises(pack.Invalid): self.p()
        self.modules[0]['dependencies'] = ['missing']
        self.registry()
        with self.assertRaises(pack.Invalid): self.p()
    def test_symlink_rejected(self):
        (self.root / 'src/guide/link').symlink_to('/etc/passwd')
        with self.assertRaises(pack.Invalid): self.p()
    def test_output_symlink_rejected(self):
        (self.root / 'dist').symlink_to(self.root / 'src', target_is_directory=True)
        with self.assertRaises(pack.Invalid): self.p().build('modules')
    def test_determinism_and_hash_invalidation(self):
        first = self.p().module_hash('child')
        self.assertEqual(first, self.p().module_hash('child'))
        self.put('src/guide/unrelated.md', 'Unrelated change')
        self.assertEqual(first, self.p().module_hash('child'))
        self.put('src/templates/spec.md', 'Changed template')
        self.assertNotEqual(first, self.p().module_hash('child'))
    def test_old_output_preserved_on_bad_inputs(self):
        self.p().build('modules')
        before = pack.files(self.root / 'dist/modules')
        self.modules[0]['articles'] = ['missing.md']
        self.registry()
        with self.assertRaises(pack.Invalid): self.p().build('modules')
        self.assertEqual(before, pack.files(self.root / 'dist/modules'))
    def test_promotion_failure_restores_old(self):
        self.p().build('modules')
        before = pack.files(self.root / 'dist/modules')
        self.put('src/methods/base.md', 'Changed')
        real = pack.os.replace
        def replace(src, dst):
            if Path(src).name == 'release': raise OSError('simulated promotion failure')
            return real(src, dst)
        with patch.object(pack.os, 'replace', side_effect=replace), self.assertRaises(OSError):
            self.p().build('modules')
        self.assertEqual(before, pack.files(self.root / 'dist/modules'))
    def test_verify_and_rollback(self):
        self.p().build('modules')
        before = pack.files(self.root / 'dist/modules')
        self.put('src/methods/base.md', 'Changed')
        self.p().build('modules')
        self.p().verify('modules')
        self.p().rollback('modules')
        self.assertEqual(before, pack.files(self.root / 'dist/modules'))
        with self.assertRaises(pack.Invalid): self.p().verify('modules')
    def test_tampered_release(self):
        self.p().build('modules')
        self.put('dist/modules/fde-base/SKILL.md', 'tamper')
        with self.assertRaises(pack.Invalid): self.p().verify('modules')
    def test_total_requires_real_report_files(self):
        p = self.p()
        with self.assertRaises(pack.Invalid): p.expected('total')
        records = []
        for mid in p.modules:
            records.append({'id': mid, 'source_hash': p.module_hash(mid), 'rounds': [{'id': str(i), 'transcript_path': 'qa/' + mid + str(i) + '.md', 'reviewer_verdict': 'pass', 'notes': 'Synthetic infrastructure test; not actual QA'} for i in (1,2)], 'independent_review': {'path': 'qa/' + mid + '-review.md', 'verdict': 'pass'}})
        self.put('qa/modules.json', json.dumps({'modules': records}))
        with self.assertRaises(pack.Invalid): p.expected('total')
        for r in records:
            for x in r['rounds']: self.put(x['transcript_path'], '')
            self.put(r['independent_review']['path'], '')
        with self.assertRaises(pack.Invalid): p.expected('total')
    def test_module_provenance_is_complete_unique_and_non_executable(self):
        for mid, module in self.p().modules.items():
            with self.subTest(module=mid):
                output = self.p().module(mid)
                record = json.loads(output['PROVENANCE.json'])
                self.assertEqual(record, dict(self.provenance, module_id=mid,
                                              skill_name=module['name'], version='0.4.1'))
                self.assertEqual([k for k in output if k.lower().endswith('provenance.json')],
                                 ['PROVENANCE.json'])
                self.assertNotIn('role', record)
                self.assertNotIn('source_hash', record)
                self.assertNotIn('PROVENANCE.json', output['SKILL.md'].decode())
                self.assertEqual(output['PROVENANCE.json'], self.p().provenance(mid))

    def test_total_provenance_is_complete_unique_and_ai_identity(self):
        output = self.p().total_files()  # Inspect mapping, never assemble a real total.
        record = json.loads(output['zhxbai-fde/PROVENANCE.json'])
        self.assertEqual(record, dict(self.provenance, module_id='all',
                                      skill_name='zhxbai-fde', version='0.4.1',
                                      role={'name': '志雄', 'type': 'ai-assistant'}))
        self.assertEqual([k for k in output if k.lower().endswith('provenance.json')],
                         ['zhxbai-fde/PROVENANCE.json'])
        self.assertNotIn('source_hash', record)

    def test_source_provenance_changes_invalidate_every_module(self):
        before = {mid: self.p().module_hash(mid) for mid in ('base', 'child')}
        self.provenance['guide_source_commit'] = 'changed-source-commit'
        self.put('src/provenance.json', json.dumps(self.provenance))
        for mid in before:
            self.assertNotEqual(before[mid], self.p().module_hash(mid))
            self.assertEqual(self.p().selected(mid)['provenance.json'],
                             (self.root / 'src/provenance.json').read_bytes())
            self.assertEqual(json.loads(self.p().module(mid)['PROVENANCE.json'])['guide_source_commit'],
                             'changed-source-commit')

    def test_global_version_changes_only_total_metadata(self):
        before = {mid: self.p().module_hash(mid) for mid in ('base', 'child')}
        before_packages = {mid: self.p().module(mid) for mid in before}
        self.put('qa/modules.json', json.dumps(self.qa_fixture()))
        self.version = '0.4.2'
        self.registry()
        for mid in before:
            self.assertEqual(before[mid], self.p().module_hash(mid))
            self.assertEqual(before_packages[mid], self.p().module(mid))
            self.assertEqual(json.loads(self.p().module(mid)['PROVENANCE.json'])['version'], '0.4.1')
        self.assertEqual(json.loads(self.p().total_files()['zhxbai-fde/PROVENANCE.json'])['version'], '0.4.2')
        self.p().qa()  # A total-only version change does not stale independent module QA.
        self.assertFalse((self.root / 'dist/total').exists())

    def test_module_versions_change_only_self_and_dependents_and_stale_qa(self):
        before = {mid: self.p().module_hash(mid) for mid in ('base', 'child')}
        self.put('qa/modules.json', json.dumps(self.qa_fixture()))
        self.modules[1]['version'] = '0.4.2'
        self.registry()
        self.assertEqual(before['base'], self.p().module_hash('base'))
        self.assertNotEqual(before['child'], self.p().module_hash('child'))
        self.assertEqual(json.loads(self.p().module('base')['PROVENANCE.json'])['version'], '0.4.1')
        self.assertEqual(json.loads(self.p().module('child')['PROVENANCE.json'])['version'], '0.4.2')
        self.assertEqual(json.loads(self.p().total_files()['zhxbai-fde/PROVENANCE.json'])['version'], '0.4.1')
        with self.assertRaisesRegex(pack.Invalid, 'Stale QA source hash: child'):
            self.p().expected('total')
        child_version_hash = self.p().module_hash('child')
        self.modules[0]['version'] = '0.4.2'
        self.registry()
        self.assertNotEqual(before['base'], self.p().module_hash('base'))
        self.assertNotEqual(child_version_hash, self.p().module_hash('child'))
        self.assertEqual(json.loads(self.p().module('child')['PROVENANCE.json'])['version'], '0.4.2')
        self.assertFalse((self.root / 'dist/total').exists())

    def test_module_version_is_required(self):
        del self.modules[0]['version']
        self.registry()
        with self.assertRaisesRegex(pack.Invalid, 'Missing module field: version'):
            self.p()
        self.modules[0]['version'] = ' '
        self.registry()
        with self.assertRaisesRegex(pack.Invalid, 'Missing module version: base'):
            self.p()

    def test_exact_generated_provenance_participates_in_hash_without_cycle(self):
        p = self.p()
        selected = p.selected('base')
        selected['__generated_PROVENANCE.json'] = p.provenance('base')
        selected['__packager_version__'] = Path(pack.__file__).read_bytes()
        self.assertEqual(p.module_hash('base'), pack.fingerprint(selected))
        self.assertEqual(json.loads(p.module('base')['SOURCE-HASH.json'])['source_hash'],
                         p.module_hash('base'))
        before = p.module_hash('base')
        with patch.object(p, 'provenance', return_value=b'{"version": "changed-generated-output"}\n'):
            self.assertNotEqual(before, p.module_hash('base'))
        with patch.object(p, 'module_hash', side_effect=AssertionError('Circular source hash')):
            self.assertEqual(json.loads(p.provenance('base'))['module_id'], 'base')
            self.assertEqual(json.loads(p.provenance())['module_id'], 'all')

    def test_license_and_history_bytes_are_preserved_in_every_package(self):
        before = pack.files(self.root / 'src/legal')
        p = self.p()
        for mid in p.modules:
            output = p.module(mid)
            for name, value in before.items():
                self.assertEqual(output[name], value)
        total = p.total_files()
        for name, value in before.items():
            self.assertEqual(total['zhxbai-fde/' + name], value)
        self.assertEqual(before, pack.files(self.root / 'src/legal'))

    def test_missing_or_incomplete_provenance_and_version_fail_explicitly(self):
        (self.root / 'src/provenance.json').unlink()
        with self.assertRaisesRegex(pack.Invalid, 'Missing provenance.json'):
            self.p()
        self.put('src/provenance.json', '{}')
        with self.assertRaisesRegex(pack.Invalid, 'Unsupported provenance schema'):
            self.p()
        for key in self.provenance:
            with self.subTest(missing=key):
                incomplete = dict(self.provenance)
                del incomplete[key]
                self.put('src/provenance.json', json.dumps(incomplete))
                with self.assertRaises(pack.Invalid):
                    self.p()
        self.put('src/provenance.json', json.dumps(self.provenance))
        self.put('src/registry.json', json.dumps({'modules': self.modules}))
        with self.assertRaisesRegex(pack.Invalid, 'Missing registry version'):
            self.p()

    def test_provenance_license_paths_and_generated_fields_are_validated(self):
        for changes in ({'license_file': '../outside'},
                        {'license_file': 'missing'},
                        {'historical_license_directory': '../outside/'},
                        {'historical_license_directory': 'missing/'},
                        {'module_id': 'spoofed'}, {'skill_name': 'spoofed'},
                        {'version': 'spoofed'}, {'role': {'type': 'human'}}):
            with self.subTest(changes=changes):
                self.put('src/provenance.json', json.dumps(dict(self.provenance, **changes)))
                with self.assertRaises(pack.Invalid):
                    self.p()

    def test_provenance_is_data_only_without_network_or_execution_paths(self):
        # Static allow-list plus a live audit guard, not a production security proof.
        code = ast.parse(Path(pack.__file__).read_text())
        allowed = {'argparse', 'hashlib', 'json', 'os', 'pathlib', 're', 'shutil', 'tempfile'}
        imports = {n.module for n in ast.walk(code) if isinstance(n, ast.ImportFrom)}
        imports |= {alias.name for n in ast.walk(code) if isinstance(n, ast.Import) for alias in n.names}
        self.assertEqual(imports, allowed)
        dangerous = {'eval', 'exec', 'compile', '__import__', 'system', 'popen', 'spawn', 'execv',
                     'execve', 'fork', 'connect', 'urlopen', 'urlretrieve', 'getenv', 'environ'}
        references = {n.id for n in ast.walk(code) if isinstance(n, ast.Name)}
        references |= {n.attr for n in ast.walk(code) if isinstance(n, ast.Attribute)}
        self.assertFalse(dangerous.intersection(references))
        import sys
        def reject_external(event, args):
            if event.startswith(('socket.', 'subprocess.', 'urllib.', 'http.client.',
                                 'os.exec', 'os.posix_spawn', 'os.spawn')) or event == 'os.system':
                raise AssertionError('Unexpected external activity: ' + event)
        sys.addaudithook(reject_external)
        self.provenance['source_repository'] = 'https://example.invalid/never-fetch-this'
        self.put('src/provenance.json', json.dumps(self.provenance))
        p = self.p()
        p.build('modules')
        p.verify('modules')
        p.total_files()

    def qa_fixture(self):
        # Synthetic linkage data only; never use these records as real behavior QA.
        p = self.p()
        records = []
        for mid in p.modules:
            rounds = [{'id': str(i), 'transcript_path': 'qa/' + mid + str(i) + '.md',
                       'reviewer_verdict': 'pass', 'notes': 'Synthetic linkage fixture only'}
                      for i in (1, 2)]
            review = {'path': 'qa/' + mid + '-review.md', 'verdict': 'pass'}
            for item in rounds:
                self.put(item['transcript_path'], 'Synthetic fixture; not behavior evidence.')
            self.put(review['path'], 'Synthetic fixture; not independent behavior evidence.')
            records.append({'id': mid, 'source_hash': p.module_hash(mid),
                            'rounds': rounds, 'independent_review': review})
        return {'modules': records}

    def test_optional_migration_report_is_validated_and_packaged(self):
        attestation = self.qa_fixture()
        self.put('qa/modules.json', json.dumps(attestation))
        self.assertNotIn('zhxbai-fde/qa/migration.md', self.p().expected('total'))
        attestation['metadata_only_migration'] = {'review_path': 'qa/migration.md'}
        self.put('qa/migration.md', 'Synthetic metadata-only review fixture.')
        self.put('qa/modules.json', json.dumps(attestation))
        self.assertEqual(self.p().expected('total')['zhxbai-fde/qa/migration.md'],
                         b'Synthetic metadata-only review fixture.')
        self.assertFalse((self.root / 'dist/total').exists())

    def test_migration_reports_cannot_be_missing_empty_or_unsafe(self):
        attestation = self.qa_fixture()
        self.put('qa/empty.md', '')
        for migration in (None, {}, {'review_path': 'qa/missing.md'},
                          {'review_path': 'qa/empty.md'}, {'review_path': '../outside'},
                          {'review_path': '/absolute'}, {'review_path': 'src/total-SKILL.md'}):
            with self.subTest(migration=migration):
                attestation['metadata_only_migration'] = migration
                self.put('qa/modules.json', json.dumps(attestation))
                with self.assertRaises(pack.Invalid):
                    self.p().expected('total')
        (self.root / 'qa/linked.md').symlink_to(self.root / 'src/total-SKILL.md')
        attestation['metadata_only_migration'] = {'review_path': 'qa/linked.md'}
        self.put('qa/modules.json', json.dumps(attestation))
        with self.assertRaisesRegex(pack.Invalid, 'Symlink forbidden'):
            self.p().expected('total')

    def test_migration_report_does_not_bypass_existing_qa_gate(self):
        attestation = self.qa_fixture()
        self.put('qa/migration.md', 'Synthetic metadata-only review fixture.')
        attestation['metadata_only_migration'] = {'review_path': 'qa/migration.md'}
        attestation['modules'][0]['rounds'].pop()
        self.put('qa/modules.json', json.dumps(attestation))
        with self.assertRaisesRegex(pack.Invalid, 'Two behavior rounds required'):
            self.p().expected('total')
        attestation = self.qa_fixture()
        attestation['metadata_only_migration'] = {'review_path': 'qa/migration.md'}
        attestation['modules'][0]['source_hash'] = 'stale'
        self.put('qa/modules.json', json.dumps(attestation))
        with self.assertRaisesRegex(pack.Invalid, 'Stale QA source hash'):
            self.p().expected('total')

    def test_total_role_change_only_affects_total_not_independent_packages(self):
        before = self.p().expected('modules')
        hashes = {mid: self.p().module_hash(mid) for mid in ('base', 'child')}
        before_total = self.p().total_files()
        self.put('qa/modules.json', json.dumps(self.qa_fixture()))
        self.total_role['name'] = '新的总包助手'
        self.registry()
        self.total_entry()
        p = self.p()
        self.assertEqual(before, p.expected('modules'))
        self.assertEqual(hashes, {mid: p.module_hash(mid) for mid in hashes})
        after_total = p.total_files()
        self.assertEqual(json.loads(after_total['zhxbai-fde/PROVENANCE.json'])['role'], self.total_role)
        self.assertEqual({k for k in before_total if before_total[k] != after_total[k]},
                         {'zhxbai-fde/PROVENANCE.json', 'zhxbai-fde/SKILL.md',
                          'zhxbai-fde/references/registry.json'})
        p.qa()
        self.assertFalse((self.root / 'dist/total').exists())

    def test_total_role_mismatch_blocks_total_but_not_independent_modules(self):
        before = self.p().expected('modules')
        self.total_role['name'] = 'Changed registry name only'
        self.registry()
        self.assertEqual(before, self.p().expected('modules'))
        with self.assertRaisesRegex(pack.Invalid, 'Total role metadata mismatch: role_name'):
            self.p().total_files()
        self.total_entry()
        self.assertEqual(json.loads(self.p().provenance())['role'], self.total_role)

    def test_total_role_requires_unambiguous_quoted_metadata_and_ai_type(self):
        good_role = dict(self.total_role)
        for role in (None, {}, {'name': '', 'type': 'ai-assistant'},
                     {'name': '志雄', 'type': 'human'}, dict(good_role, extra='unexpected')):
            with self.subTest(role=role):
                self.total_role = role
                self.registry()
                with self.assertRaises(pack.Invalid):
                    self.p().total_files()
        self.total_role = good_role
        self.registry()
        self.total_entry()
        good_entry = (self.root / 'src/total-SKILL.md').read_text()
        variants = [
            good_entry.replace('  role_name: "志雄"', '  role_name: 志雄'),
            good_entry.replace('  role_name: "志雄"', '  role_name: "志雄"\n  role_name: "志雄"'),
            good_entry.replace('  role_name: "志雄"', '  role_name: "志雄"\n  role_name: unquoted'),
            good_entry.replace('  role_type: "ai-assistant"', '  role_type: "human"'),
            good_entry.replace('metadata:', 'metadata:\nmetadata:'),
            good_entry.replace('metadata:', 'other_metadata:'),
            '# No frontmatter',
        ]
        for entry in variants:
            with self.subTest(entry=entry):
                self.put('src/total-SKILL.md', entry)
                with self.assertRaises(pack.Invalid):
                    self.p().total_files()

    def test_unknown_and_duplicate_ids(self):
        self.modules.append(self.modules[0].copy())
        self.registry()
        with self.assertRaises(pack.Invalid): self.p()

if __name__ == '__main__': unittest.main()
