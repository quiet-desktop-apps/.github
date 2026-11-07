"""Validate the publication profile and strict default-branch ruleset."""
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
rules = json.loads((root/'docs/ruleset.json').read_text())
assert rules['enforcement'] == 'active'
assert rules['bypass_actors'] == []
assert {'~DEFAULT_BRANCH','refs/heads/master'} <= set(rules['conditions']['ref_name']['include'])
assert {r['type'] for r in rules['rules']} == {'deletion','non_fast_forward','pull_request','required_status_checks'}
checks = next(r['parameters'] for r in rules['rules'] if r['type']=='required_status_checks')
assert checks['strict_required_status_checks_policy']
assert checks['required_status_checks'] == [{'context':'checks','integration_id':15368}]
assert (root/'profile/README.md').is_file() and (root/'LICENSE').is_file()
from importlib.util import spec_from_file_location, module_from_spec
spec = spec_from_file_location('measure_memory', root/'scripts/measure-memory.py')
module = module_from_spec(spec); spec.loader.exec_module(module)
import os
report = module.sample([os.getpid(), os.getpid()])
assert len(report['processes']) == 1 and report['complete']
assert report['totals_mib']['rss'] > 0 and report['totals_mib']['pss'] > 0
assert 'cmdline' not in json.dumps(report)
print('Profile, ruleset, and privacy-preserving memory sampler: passed')
