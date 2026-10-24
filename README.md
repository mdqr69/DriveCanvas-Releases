# DriveCanvas Releases

Public update-delivery repository for DriveCanvas.

This repository contains only signed release APKs and update metadata published by the private DriveCanvas build pipeline. Source code and signing secrets are not stored here.

The publisher also accepts `DriveCanvas-<version>.apk.zip` containing exactly the signed APK named by `stable.json`. This keeps large APKs below Git's per-file limit. It checks the extracted APK's size, checksum and pinned existing signing certificate before publishing the normal `.apk` release download. Customers still download an APK, not a ZIP.
