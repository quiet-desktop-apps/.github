#!/usr/bin/env python3
"""Linux process-tree RSS/PSS sampler. Never outputs command lines or URLs."""
import argparse
import datetime
import json
import os
from pathlib import Path
import time


def sample(root_pids):
    processes = {}
    for path in Path('/proc').glob('[0-9]*'):
        try:
            fields = path.joinpath('stat').read_text().rsplit(')', 1)[1].split()
            processes[int(path.name)] = (int(fields[1]), int(fields[19]))
        except (OSError, ValueError, IndexError):
            continue
    selected = set(root_pids)
    while True:
        expanded = selected | {pid for pid, (parent, _) in processes.items() if parent in selected}
        if expanded == selected: break
        selected = expanded
    uptime = float(Path('/proc/uptime').read_text().split()[0])
    ticks = os.sysconf('SC_CLK_TCK')
    rows, missing = [], []
    for pid in sorted(selected):
        try:
            values = {}
            for line in Path(f'/proc/{pid}/smaps_rollup').read_text().splitlines():
                if ':' in line:
                    key, value = line.split(':', 1)
                    if key in ('Rss', 'Pss', 'Swap'): values[key] = int(value.split()[0]) / 1024
            parent, started = processes[pid]
            # Reject samples from an exited process whose PID was reused mid-read.
            fields = Path(f'/proc/{pid}/stat').read_text().rsplit(')', 1)[1].split()
            if int(fields[19]) != started: raise ValueError('process replaced')
            rows.append({'pid': pid, 'age_seconds': round(max(0, uptime-started/ticks), 1),
                         **{k.lower()+'_mib': round(v, 2) for k,v in values.items()}})
        except (OSError, KeyError, ValueError, IndexError):
            missing.append(pid)
    return {'utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'roots': root_pids, 'processes': rows, 'missing_or_unreadable': missing,
            'complete': not missing,
            'totals_mib': {metric: round(sum(r.get(metric+'_mib', 0) for r in rows), 2)
                           for metric in ('rss', 'pss', 'swap')}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pid', type=int, nargs='+', help='Root PID(s); descendants are included and deduplicated')
    parser.add_argument('--samples', type=int, default=1)
    parser.add_argument('--interval', type=float, default=1)
    args = parser.parse_args()
    if args.samples < 1 or args.interval < 0 or any(pid < 1 for pid in args.pid):
        parser.error('PIDs and sample count must be positive; interval must be nonnegative')
    for index in range(args.samples):
        print(json.dumps(sample(args.pid)), flush=True)
        if index+1 < args.samples: time.sleep(args.interval)


if __name__ == '__main__': main()
