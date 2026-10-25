# DriveCanvas 7.1.3-rc21-audit3 — parked tester correction

Install **DriveCanvas-7.1.3-rc21-audit3.apk** as an update without uninstalling or clearing storage. This uses the existing certificate and Android version code 257. It is a manual test prerelease; Check for update still follows the stable feed.

The tester previously classified an unknown/raw gear label as non-Park and could stop a parked run. audit3 distinguishes unknown readings from recognised gears. Unknown is never relabelled as P: your explicit parked confirmation remains required. Fresh movement or a recognised non-Park gear still stops the test.

The test page now shows current speed and gear evidence. Reports capture the exact speed, raw/decoded gear, freshness and reason at a stop, even if readings change before the log is saved. No global gear calibration is changed.

Verification: 548 Android tests with no failures/errors/skips, including eight new Android 13 regressions; 395 native screen checks; six browser checks. Physical completion on the head unit remains to be verified.

## Run the check

1. Park in P, open **More → Run app checks** and confirm the parked checkbox.
2. For the original load problem, enable the usual Passenger content and Cluster output first.
3. Untick **Continuous tester · repeat until I stop** for one cycle, or leave it ticked for repeated cycles.
4. Tap **Run app checks** and keep DriveCanvas visible.
5. When finished, or after Stop, save/share the ZIP report. If it stops unexpectedly, send the report; the triggering readings are now included.

Official BYD setup remains; private DriveCanvas phone remote is removed. Physical HUD/BYD/exterior-sound behavior and combined-screen performance still need car acceptance. Detailed Bao 5 model and full localization remain incomplete; native CarPlay/Android Auto receivers remain deferred.
