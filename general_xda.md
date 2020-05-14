# Working with Andorid (XDA)

Before starting any work, make sure that the phone is rooted. Check online for
how to unlock a specific phone model.

To interact with an Android phone we require the [XDA dev tools](https://www.xda-developers.com/install-adb-windows-macos-linux/).
These tools provide us a way of flashing and generally interacting with the
phone's OS.


## Flash a custom recovery

1.  Download [TWRP](https://twrp.me/Devices/) for your device.
2.  Boot the phone into fastboot. This differs according to the device. Usually
 it requires **holding down power and vol- buttons**.
3.  Flash the TWRP image with `sudo ./fastboot flash recovery ~/path/to/twrp-version-model.img`

Entering the custom recovery may be different for different phones. Usually you
can enter the custom recovery by **holding down power and vol+ buttons**. You
can also enter the recovery from fastboot with `sudo ./fastboot reboot recovery`.


## Flashing a ROM

### 1. Download a ROM

Locate a ROM of that is compatible with you device. Some ROMs consider;
*  [LinageOS](https://lineageos.org/)
*  [AEX](https://www.aospextended.com/)
*  [MIUI](https://c.mi.com/oc/miuidownload/index)
*  [GrapheneOS](https://grapheneos.org/)

The ROM is downloaded as a .zip file. Do not extract it.

### 2. Move ROM zip file to phone

There are a number of ways in which this can be accomplished. If you have the
phone running and connected the the PC you can transfer the file by drag and
drop. If you have USB debugging enabled you can use adb with;

`sudo ./adb push ~/path/to/rom.zip /sdcard/Download`

This can also be used if you are already in TWRP recover.

### 3. Flash the ROM

1.  Go to the TWRP recovery. See previous instructions.
2.  Tap on `Install`.
3.  Find the .zip file you transferred earlier and flash.
