# DriveCanvas Releases

Public update-delivery repository for DriveCanvas.

This repository contains only signed release APKs and update metadata published by the private DriveCanvas build pipeline. Source code and signing secrets are not stored here.

The publisher also accepts `DriveCanvas-<version>.apk.zip` containing exactly the signed APK named by `stable.json`. This keeps large APKs below Git's per-file limit. It checks the extracted APK's size, checksum and pinned existing signing certificate before publishing the normal `.apk` release download. Customers still download an APK, not a ZIP.

## Android test build

[Download DriveCanvas 7.1.3-rc21-audit2 APK](https://github.com/mdqr69/DriveCanvas-Releases/releases/download/v7.1.3-rc21-audit2/DriveCanvas-7.1.3-rc21-audit2.apk) · [Test release and instructions](https://github.com/mdqr69/DriveCanvas-Releases/releases/tag/v7.1.3-rc21-audit2)

This is a **manual test prerelease**. Install it as an update without uninstalling. The stable in-car update feed does not offer this test build. Find the tester under **More → Run app checks**. Vehicle acceptance and the limitations listed in the test notes remain pending.
