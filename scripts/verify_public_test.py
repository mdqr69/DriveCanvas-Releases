#!/usr/bin/env python3
"""Verify public APK bytes without authentication and confirm the stable feed is unchanged."""
import hashlib,json,time,urllib.request
from pathlib import Path

def main():
    data=json.loads(Path('test-release.json').read_text());stable=json.loads(Path('stable.json').read_text())
    for attempt in range(8):
        try:
            digest=hashlib.sha256();size=0
            with urllib.request.urlopen(data['apkUrl'],timeout=60) as response:
                while chunk:=response.read(1024*1024):digest.update(chunk);size+=len(chunk)
            assert size==data['apkSizeBytes'] and digest.hexdigest()==data['sha256'],'Public test APK differs'
            with urllib.request.urlopen('https://github.com/mdqr69/DriveCanvas-Releases/releases/latest/download/stable.json',timeout=30) as response:current=json.load(response)
            assert all(current[k]==stable[k] for k in ('versionName','versionCode','sha256','apkUrl')),'Stable feed unexpectedly changed'
            print('PUBLIC_TEST_VERIFIED',data['versionName'],size,digest.hexdigest(),'stable feed unchanged')
            return
        except Exception as error:
            if attempt==7:raise
            print('Waiting for public test download:',type(error).__name__,str(error));time.sleep(5)

if __name__=='__main__':main()
