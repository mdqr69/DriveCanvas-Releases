#!/usr/bin/env python3
"""Verify exactly what the in-car Update Center will download, without credentials."""
import hashlib
import json
import os
import time
import urllib.request

feed = "https://github.com/mdqr69/DriveCanvas-Releases/releases/latest/download/stable.json"
for attempt in range(8):
    try:
        with urllib.request.urlopen(feed, timeout=30) as response:
            manifest = json.load(response)
        assert manifest["versionName"] == os.environ["VERSION_NAME"], "Latest feed points to another version"
        assert manifest["versionCode"] == int(os.environ["VERSION_CODE"])
        expected = "https://github.com/mdqr69/DriveCanvas-Releases/releases/download/v" + os.environ["VERSION_NAME"] + "/DriveCanvas-" + os.environ["VERSION_NAME"] + ".apk"
        assert manifest["apkUrl"] == expected, "Unexpected APK URL"
        digest, size = hashlib.sha256(), 0
        with urllib.request.urlopen(expected, timeout=60) as response:
            while chunk := response.read(1024 * 1024):
                digest.update(chunk)
                size += len(chunk)
        assert size == manifest["apkSizeBytes"], "Public APK size mismatch"
        assert digest.hexdigest() == manifest["sha256"], "Public APK checksum mismatch"
        print("PUBLIC_UPDATE_VERIFIED version=" + manifest["versionName"] +
              " bytes=" + str(size) + " sha256=" + digest.hexdigest())
        break
    except Exception as error:
        if attempt == 7:
            raise
        print("Waiting for public release availability:", type(error).__name__, str(error))
        time.sleep(5)
