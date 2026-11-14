#!/usr/bin/env python3
"""Check the bundle against SHA256SUMS.txt and write the release ZIP.

usage: zip_bundle.py BUNDLE_DIR ZIP_PATH

The bundle is exactly the files listed in SHA256SUMS.txt plus SHA256SUMS.txt itself (README.md, .nojekyll and .github/
of this repository are not part of it). The ZIP is the one pack_portable.py writes in the research repository:
entries presentation-map/<path> sorted by path, timestamps 2026-11-14 00:00, unix mode 0644, deflate level 9.
"""
import hashlib
import json
from pathlib import Path
import sys
import zipfile

STAMP = (2026, 11, 14, 0, 0, 0)


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def main():
    root, zpath = Path(sys.argv[1]), Path(sys.argv[2])
    listed = {}
    for line in (root / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        h, name = line.split('  ', 1)
        listed[name] = h
    bad = [n for n, h in listed.items() if not (root / n).is_file() or sha(root / n) != h]
    if bad:
        print('differs from SHA256SUMS.txt:', len(bad), bad[:5])
        sys.exit(1)
    files = sorted(list(listed) + ['SHA256SUMS.txt'])
    with zipfile.ZipFile(zpath, 'w') as z:
        for f in files:
            zi = zipfile.ZipInfo(f'presentation-map/{f}', date_time=STAMP)
            zi.create_system = 3
            zi.external_attr = 0o100644 << 16
            zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, (root / f).read_bytes(), compresslevel=9)
    sizes = {f: (root / f).stat().st_size for f in files}
    big = max(sizes, key=lambda f: (sizes[f], f))
    print(json.dumps({'files': len(files), 'bytes': sum(sizes.values()), 'largest': [big, sizes[big]],
                      'zip': zpath.name, 'zip_bytes': zpath.stat().st_size, 'zip_sha256': sha(zpath)}))


if __name__ == '__main__':
    main()
