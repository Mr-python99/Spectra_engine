#!/bin/bash
python3 -c "
import base64, zlib, marshal
with open('main_backup.py', 'r') as f:
    code = f.read()
compiled = compile(code, '<string>', 'exec')
marshaled = marshal.dumps(compiled)
compressed = zlib.compress(marshaled)
encoded = base64.b64encode(compressed).decode()[::-1]
obfuscated = f'#!/usr/bin/env python3\nimport base64, zlib, marshal as m\n_ = \"{encoded}\"[::-1]\nexec(m.loads(zlib.decompress(base64.b64decode(_))))'
with open('main.py', 'w') as f:
    f.write(obfuscated)
print('✅ main.py updated!')
"
git add main.py
git commit -m "Update"
git push
echo "✅ Uploaded to GitHub!"
