# DriveCanvas 7.1.3-rc21-audit2 — Android test build

Download **DriveCanvas-7.1.3-rc21-audit2.apk** from the release assets and install it as an update. Do not uninstall or clear app storage first. It uses the existing signing certificate and Android version code 257.

This test build is a manual download. The in-car **Check for update** button still follows the stable feed and will not offer this prerelease.

Improvements include bounded wallpaper/gauge image memory, reduced drawing allocations, corrected HUD navigation values and stale-message handling, touch/accessibility fixes, and more accurate automatic test results. Private DriveCanvas phone remote services are removed; official BYD setup remains. Removed private pairing data will not be restored by reinstalling an old APK.

Verification: 540 Android tests with zero failures/errors/skips; 395 native layout checks; six browser checks; zero lint errors and 577 reviewed warnings. The exact APK hash and original signing identity were independently verified. These checks do not establish physical car performance or correct OEM/server behavior.

## Find and run the tester

1. Park the car and open **More → Run app checks**. Scroll the navigation menu to find More.
2. For the reported lag, first enable the usual Passenger wallpaper and Cluster output.
3. Tick **I confirm the car is parked**.
4. For one cycle, untick **Continuous tester · repeat until I stop**. Leave it ticked for repeating tests.
5. Tap **Run app checks** and keep DriveCanvas open. One cycle takes approximately 4–6 minutes.
6. When finished, or after pressing **Stop checks**, choose **Save test report** or **Share test report** and send the ZIP report.

Physical HUD accuracy, official BYD operation, exterior speaker routing and combined-screen load still require vehicle testing. Full Arabic localization and the detailed Bao 5 model remain incomplete. Native CarPlay/Android Auto receivers remain deferred.
