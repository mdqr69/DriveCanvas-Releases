# DriveCanvas 7.1.3-rc15

- Adds a realistic white and graphite three-screen cockpit visualization based on the supplied cabin photos. Home, Screens, wallpapers, projection, gauge controls, screen switching and the shared section header use it.
- Shows each saved wallpaper image on its corresponding illustrated screen; opening a role's wallpaper editor or activating the wallpaper plays a short directional preview.
- Shows a moving app tile from Main to Passenger or Cluster when you request a projection. The illustration reflects the request; actual screen status remains in the screen cards.
- Adds a reference-based steering wheel illustration; both button groups briefly highlight when capture begins and when a physical button is detected.
- Uses about 36 KB of compressed artwork and event-driven animations. No persistent animation loop, HUD transport change, or live gauge polling change.

Android release tests, signed APK build, version and signing-certificate checks passed. Display alignment, image visibility and system load still require a check on the Leopard 5. The Android package installer can still require system approval.
