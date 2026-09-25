# DriveCanvas 7.1.3-rc14

- Checks replacement Maps/Waze notifications before clearing existing HUD guidance, including just before the 6.5-second removal grace period ends.
- Reduces duplicate SOME/IP sends and routine diagnostic writes while keeping the proven 200 ms HUD heartbeat.
- Reads slow vehicle data every 8 seconds and reduces idle telemetry to 2 Hz; a visible gauge retains its 25 Hz speed and power updates.
- Adds **Copy battery signal diagnostic** in Live Vehicle Data. If traction-battery SOC is unavailable, DriveCanvas reports the BYD read response or error without substituting the Android head unit's battery.

HUD continuity and performance still need in-car verification. A raw SOC result is needed to resolve the missing battery percentage on the Leopard 5. The owner may still have to approve Android's system installer.
