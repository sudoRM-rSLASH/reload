import os
import threading
import time

import requests
import zipfile
import json


tt = time.perf_counter()
programs = {
  "7zip": {"url": "https://www.7-zip.org/a/7z2201-x64.exe", "filename": "7z2201-x64.exe", "command":  "7z2201-x64.exe /S"},
  "MSIAfterburner": {"url": "https://download.msi.com/uti_exe/vga/MSIAfterburnerSetup.zip?__token__=exp=1665154892~acl=/*~hmac=6fefd1aee691541bbebe8ed09d1458906b9420a385f3a41914e9aac5c17e51a9", "filename": "MSIAfterburnerSetup.zip", "command": "MSIAfterburnerSetup.exe /S"},
  "Chrome": {"url": "https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B1E8E72F9-2198-DABE-12C0-DF798C329C98%7D%26lang%3Den%26browser%3D4%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe", "filename": "ChromeSetup.exe", "command":  "ChromeSetup.exe /silent /install"},
  "Steam": {"url": "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe", "filename": "SteamSetup.exe", "command":  "SteamSetup.exe /S"},
  "Telegram": {"url": "https://telegram.org/dl/desktop/win", "filename": "tsetup.exe", "command":  "tsetup.exe /VERYSILENT /NORESTART"},
  "Discord": {"url": "https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86", "filename": "DiscordSetup.exe", "command":  "DiscordSetup.exe -s"},
  "qBitTorrent" : {"url": "https://dl3.topfiles.net/files/2/860/51242/YW8vcWtTn71yVUw3OERCVlArb0MveXdpUVY1c0FzY0dpMjJ1bjhsOGx1S1lQaz06On6yavnQ2LlfEJdxda7jaNM/qbittorrent-64-bit_4.4.5.exe", "filename": "qbittorrent_4.4.5_x64.exe", "command":  "qbittorrent_4.4.5_x64.exe /S"},
  "Unlocker": {"url": "https://web.archive.org/web/20140724033856/http://www.emptyloop.com/unlocker/Unlocker1.9.2.exe", "filename": "Unlocker.exe", "command":  "Unlocker.exe /S"},
  "TotalCommander": {"url": "https://totalcommander.ch/win/tcmd1051x64.exe", "filename": "tmcd_setup.exe", "command":  "tmcd_setup.exe /AHMGDU"}
}
downloads = os.path.join(os.environ['USERPROFILE'], "Downloads")
os.chdir(downloads)

print(time.perf_counter() - tt)

def main(program: dict):
    r = requests.get(program['url'], allow_redirects=True, timeout=120)
    open(program['filename'], 'wb').write(r.content)
    if program['filename'].endswith(".zip"):
        with zipfile.ZipFile(f"{downloads}\\{program['filename']}", 'r') as zip_ref:
            zip_ref.extractall(f"{downloads}")
            for elem in zip_ref.namelist():
                if 'MSIAfterburnerSetup' in elem:
                    os.rename(elem.removeprefix(program['filename'].replace('.zip', '')+'/'), program['filename'].replace('.zip', '.exe'))
    print(program['filename'], program['command'])
    try:
        os.system(program['command'])
    except Exception as e:
        print(e, program['command'])
    return program['filename']

tt = time.perf_counter()

threads = [
    threading.Thread(target=main, args=(program,)) for program in programs.values()
]
for thread in threads:
    thread.start()
print(time.perf_counter() - tt)
for thread in threads:
    print(thread.join())
print(time.perf_counter() - tt)