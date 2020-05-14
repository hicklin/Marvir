# MIUI global

This ROM comes preinstalled with a lot of unnecissary apps. To removed them you
can use `adb`:

`sudo ./adb shell pm uninstall --user 0 com.android.chrome`

It might be usefill to see what packages are installed with

`sudo ./adb shell pm list packages -f`


You can use the `miui_remove_apps.py` to remove these unwanted apps.
