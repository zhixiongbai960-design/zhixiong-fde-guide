#!/usr/bin/env python3
"""Build the renamed expert distribution without changing historical module identity.

This thin packaging layer reuses package.Packager and its existing QA gate.
Methods, article text, permissions, and license bytes have one source only.
"""
import argparse
import json
from pathlib import Path
import re

from package import Packager, ROOT, Invalid, encode, digest, require, safe


class ExpertPackager(Packager):
    def expected(self, target):
        require(target == 'expert', 'This builder only supports the expert distribution')
        config_path = safe(self.root, 'packaging/expert.json')
        config_bytes = config_path.read_bytes()
        config = json.loads(config_bytes)
        require(set(config) == {'name', 'display_name', 'version', 'method_baseline_version', 'legacy_name'},
                'Unexpected expert identity fields')
        name = config['name']
        require(isinstance(name, str) and len(name) < 64 and
                re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name), 'Invalid expert name')
        require(config['legacy_name'] == 'zhxbai-fde' and name != config['legacy_name'],
                'Expert and legacy identities must be distinct')
        require(config['method_baseline_version'] == self.version, 'Expert baseline differs from source registry')
        require(isinstance(config['version'], str) and re.fullmatch(r'\d+\.\d+\.\d+', config['version']),
                'Invalid expert version')
        require(isinstance(config['display_name'], str) and config['display_name'].strip() and
                not any(ord(c) < 32 for c in config['display_name']), 'Invalid expert display name')
        manual_path = safe(self.root, 'docs/专家技能使用说明.md')
        manual = manual_path.read_bytes()
        require(manual.strip(), 'Missing expert user manual')

        # Use the unchanged historical builder, including its QA source/evidence checks.
        legacy = super().expected('total')
        prefix = config['legacy_name'] + '/'
        require(all(k.startswith(prefix) for k in legacy), 'Unexpected legacy output layout')
        output = {name + '/' + k[len(prefix):]: value for k, value in legacy.items()}
        entry_key = name + '/SKILL.md'
        entry = output[entry_key].decode('utf-8')
        front = re.match(r'\A---\n(.*?)\n---\n', entry, re.S)
        require(front is not None, 'Missing total entry frontmatter')
        header = front.group(1)
        header, count = re.subn(r'^name: zhxbai-fde$', 'name: ' + name, header, flags=re.M)
        require(count == 1, 'Unexpected source entry name')
        expected_version = '  version: ' + json.dumps(self.version)
        require(header.splitlines().count(expected_version) == 1, 'Source entry/registry version mismatch')
        header = header.replace(expected_version, '  version: ' + json.dumps(config['version']))
        body = entry[front.end():]
        title = '# 志雄 · FDE 项目实战 AI 助手'
        require(body.count(title) == 1, 'Unexpected source entry heading')
        body = body.replace(title, '# ' + config['display_name'] + ' · 志雄 FDE 专家技能', 1)
        output[entry_key] = ('---\n' + header + '\n---\n' + body).encode('utf-8')
        provenance_key = name + '/PROVENANCE.json'
        provenance = json.loads(output[provenance_key])
        provenance.update(skill_name=name, version=config['version'])
        output[provenance_key] = encode(provenance)
        output[name + '/README.md'] = manual
        output[name + '/agents/openai.yaml'] = (
            'interface:\n  display_name: ' + json.dumps(config['display_name']) + '\n'
            '  short_description: "从客户需求到验证交付，基于志雄公开方法推进当前 FDE 项目"\n'
            '  default_prompt: "请使用 $' + name + '，根据我提供的项目现状，判断当前卡点和下一步。"\n'
        ).encode('utf-8')
        output[name + '/RELEASE.json'] = encode({
            'schema_version': 1,
            **config,
            'legacy_compatibility': 'Existing zhxbai-fde 0.4.2 remains a separate frozen package, not an alias.',
            'method_source': 'skill-source/src/',
            'method_source_fingerprint': digest(encode({k: digest(v) for k, v in sorted(self.data.items())})),
            'inputs_sha256': {
                'packaging/expert.json': digest(config_bytes),
                'tools/package_expert.py': digest(Path(__file__).read_bytes()),
                'docs/专家技能使用说明.md': digest(manual),
            },
        })
        return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['build', 'verify', 'rollback'])
    args = parser.parse_args()
    try:
        if args.command == 'rollback':
            p = object.__new__(ExpertPackager)
            p.root = ROOT
        else:
            p = ExpertPackager()
        print(getattr(p, args.command)('expert'))
    except (Invalid, OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(1, 'ERROR: ' + str(exc) + '\n')


if __name__ == '__main__':
    main()
