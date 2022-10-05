import os

import httpx
import zipfile
import json

programs = json.load(open('programs.json'))
print(programs)

for name, program in programs.items():
    r = httpx.get(program['url'], follow_redirects=True)
    open(program['filename'], 'wb').write(r.content)
    if program['filename'].endswith(".zip"):
        with zipfile.ZipFile(f"C:\\Users\\KremenTech01\\PycharmProjects\\Project_reload\\{program['filename']}", 'r') as zip_ref:
            zip_ref.extractall("C:\\Users\KremenTech01\\PycharmProjects\\Project_reload\\")


    # os.system(program['command'])