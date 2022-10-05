import os

import httpx
import zipfile
import json

programs = json.load(open('programs.json'))
print(programs)
downloads = os.path.join(os.environ['USERPROFILE'], "Downloads")
os.chdir(downloads)
for name, program in programs.items():
    r = httpx.get(program['url'], follow_redirects=True)
    open(program['filename'], 'wb').write(r.content)
    if program['filename'].endswith(".zip"):
        with zipfile.ZipFile(f"{downloads}\\{program['filename']}", 'r') as zip_ref:
            zip_ref.extractall(f"{downloads}")


    # os.system(program['command'])