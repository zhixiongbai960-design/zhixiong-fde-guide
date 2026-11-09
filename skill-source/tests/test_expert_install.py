"""Run the published Bash copy snippet in isolated homes, never in a real host."""
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from package_expert import ExpertPackager


def hashes(path):
    return {p.relative_to(path).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in path.rglob('*') if p.is_file()}


@unittest.skipUnless(shutil.which('bash'), 'Bash is required for the documented Unix copy snippet')
class DocumentedInstallationTests(unittest.TestCase):
    def test_documented_copy_and_refusal_cases(self):
        manual = (ROOT / 'docs/专家技能使用说明.md').read_text()
        blocks = re.findall(r'```bash\n(.*?)\n```', manual, re.S)
        self.assertEqual(len(blocks), 1)
        with tempfile.TemporaryDirectory(prefix='expert-install-test-') as temp:
            base = Path(temp)
            repo = base / 'repo'
            for name, content in ExpertPackager(ROOT).expected('expert').items():
                path = repo / 'skills' / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            source = repo / 'skills/zhixiong-fde-expert'
            for case in ('clean-explicit', 'clean-default', 'existing-new', 'existing-old',
                         'dangling-new', 'dangling-old', 'wrong-directory', 'space-in-home'):
                with self.subTest(case=case):
                    work = base / case
                    env = os.environ.copy()
                    env['HOME'] = str(work / 'home')
                    env.pop('CODEX_HOME', None)
                    codex = Path(env['HOME']) / '.codex'
                    if case != 'clean-default':
                        codex = work / ('code home' if case == 'space-in-home' else 'codex')
                        env['CODEX_HOME'] = str(codex)
                    target = codex / 'skills'
                    target.mkdir(parents=True)
                    named = target / ('zhxbai-fde' if case.endswith('old') else 'zhixiong-fde-expert')
                    if case.startswith('existing'):
                        named.mkdir()
                        (named / 'keep.txt').write_text('existing user data')
                    elif case.startswith('dangling'):
                        named.symlink_to(work / 'absent')
                    before = hashes(target)
                    cwd = work if case == 'wrong-directory' else repo
                    result = subprocess.run(['bash'], input=blocks[0], text=True, cwd=cwd,
                                            env=env, capture_output=True)
                    success = case.startswith('clean') or case == 'space-in-home'
                    self.assertEqual(result.returncode == 0, success, result.stderr)
                    if success:
                        self.assertEqual(hashes(target / 'zhixiong-fde-expert'), hashes(source))
                    else:
                        self.assertEqual(hashes(target), before)
                        if case.startswith('dangling'):
                            self.assertTrue(named.is_symlink())


if __name__ == '__main__':
    unittest.main()
