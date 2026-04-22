# Full updated `core/commands.py`

```python
from utils.runner import run
import shutil
import os
import time
from systems.connection_manager import save_device, auto_connect, check_and_fix
from systems.network_scanner import auto_find_adb

# -------- Auto folders --------
os.makedirs("captures/screenshots", exist_ok=True)
os.makedirs("captures/recordings", exist_ok=True)
os.makedirs("captures/files", exist_ok=True)


def handle_command(ch):

    # ---------------- BASIC ----------------
    if ch == "1":
        run("adb devices")
        check_and_fix()

    elif ch == "2":
        print("\n🔗 Wireless Setup\n")
        print("1) Pair (Android 11+)")
        print("2) Connect (Recommended - 5555)\n")

        mode = input("Select mode (1/2): ").strip()

        if mode == "1":
            ip = input("IP: ").strip()
            pair_port = input("Pairing Port: ").strip()
            code = input("Pairing Code: ").strip()

            run(
                f"adb pair {ip}:{pair_port}",
                input_data=code + "\n"
            )

            connect_port = input("Connect Port: ").strip()

            run("adb disconnect")
            run(
              f"adb connect {ip}:{connect_port}"
            )

            save_device(
              f"{ip}:{connect_port}"
            )

            check_and_fix()

        elif mode == "2":
            ip = input("IP: ").strip()

            run("adb disconnect")
            run(f"adb connect {ip}:5555")

            save_device(
               f"{ip}:5555"
            )

            check_and_fix()

    elif ch == "3":
        run("adb disconnect")

    # saved reconnect
    elif ch == "36":
        auto_connect()

    # auto scan network
    elif ch == "37":
        auto_find_adb()


    # ---------------- MEDIA ----------------

    # Screen Record (basic)
    elif ch == "4":
        secs = input("Seconds (default 30): ").strip()
        if not secs:
            secs = "30"

        name = f"record_{int(time.time())}.mp4"

        run(
          f"adb shell screenrecord --time-limit {secs} /sdcard/{name}"
        )

        run(
          f"adb pull /sdcard/{name} captures/recordings/"
        )

        print("✔ Saved in captures/recordings")


    # scrcpy mirror
    elif ch == "5":
        if shutil.which("scrcpy") is None:
            print("❌ scrcpy not installed")
        else:
            run("scrcpy")


    # list apps
    elif ch == "6":
        run("adb shell pm list packages")


    # screenshot
    elif ch == "7":
        name=f"shot_{int(time.time())}.png"

        run(
          f"adb shell screencap -p /sdcard/{name}"
        )

        run(
          f"adb pull /sdcard/{name} captures/screenshots/"
        )

        print("✔ Screenshot saved in captures/screenshots")


    elif ch == "8":
        run("adb shell reboot -p")


    elif ch == "9":
        path=input("APK: ")
        run(f"adb install {path}")


    elif ch == "10":
        pkg=input("Package: ")
        run(f"adb uninstall {pkg}")


    elif ch == "11":
        path=input("Phone path: ")
        run(
           f"adb pull {path} captures/files/"
        )
        print("✔ Saved in captures/files")


    elif ch == "12":
        path=input("Local file: ")
        run(
           f"adb push {path} /sdcard/"
        )


    elif ch == "13":
        pkg=input("Package: ")
        run(
          f"adb shell monkey -p {pkg} -c android.intent.category.LAUNCHER 1"
        )


    elif ch == "14":
        run("adb logcat -d")


    elif ch == "15":
        run("adb reboot")


    elif ch == "16":
        run("adb shell svc wifi enable")


    elif ch == "17":
        run("adb shell svc wifi disable")


    elif ch == "18":
        run("adb shell df -h")


    elif ch == "19":
        run("adb shell dumpsys battery")


    elif ch == "20":
        run("adb shell cat /proc/cpuinfo")


    elif ch == "21":
        run("adb shell cat /proc/meminfo")


    elif ch == "22":
        run("adb shell input keyevent 24")


    elif ch == "23":
        run("adb shell input keyevent 25")


    elif ch == "24":
        run("adb shell input keyevent 26")


    elif ch == "25":
        run(
          "adb shell input swipe 300 1000 300 300"
        )


    elif ch == "26":
        url=input("URL: ")
        run(
         f'adb shell am start -a android.intent.action.VIEW -d "{url}"'
        )


    elif ch == "27":
        run("adb logcat -c")


    elif ch == "28":
        run("adb shell ps")


    elif ch == "29":
        print("Example: com.instagram.android")
        pkg=input("Package: ")
        run(
          f"adb shell am force-stop {pkg}"
        )


    elif ch == "30":
        run("adb shell getprop")


    elif ch == "31":
        run(
          "adb shell settings put global airplane_mode_on 1"
        )


    elif ch == "32":
        run(
          "adb shell settings put global airplane_mode_on 0"
        )


    # hide app
    elif ch == "33":
        pkg=input("Package: ")
        run(
          f"adb shell pm disable-user --user 0 {pkg}"
        )


    # unhide app
    elif ch == "34":
        pkg=input("Package: ")
        run(
          f"adb shell pm enable {pkg}"
        )


    elif ch == "35":
        if shutil.which("scrcpy"):
            print("✔ scrcpy installed")
        else:
            print("❌ scrcpy not installed")


    # auto reconnect saved device
    elif ch == "36":
        auto_connect()


    # scan network for adb device
    elif ch == "37":
        auto_find_adb()


    # -------- Added Features --------

    # Advanced screen recording
    elif ch == "38":
        secs=input("Record seconds: ").strip()
        if not secs:
            secs="20"

        name=f"media_{int(time.time())}.mp4"

        run(
         f"adb shell screenrecord --time-limit {secs} /sdcard/{name}"
        )

        run(
         f"adb pull /sdcard/{name} captures/recordings/"
        )

        print("✔ Recording saved")


    # Open Camera app
    elif ch == "39":
        print("📷 Opening camera...")
        run(
          "adb shell am start -a android.media.action.IMAGE_CAPTURE"
        )


    # Open voice recorder app
    elif ch == "40":
        print("🎙 Opening recorder...")
        run(
          "adb shell monkey -p com.transsion.soundrecorder -c android.intent.category.LAUNCHER 1"
        )


    # Pull recordings from phone
    elif ch == "41":
        run(
          "adb pull /sdcard/Recordings captures/files/"
        )
        print("✔ Audio recordings pulled")


    # Flashlight on
    elif ch == "42":
        run(
          "adb shell cmd flashlight set on"
        )


    # Flashlight off
    elif ch == "43":
        run(
          "adb shell cmd flashlight set off"
        )


    else:
        print("❌ Invalid option")
```

## Add these to your menu too

```text
[33] Hide App
[34] Unhide App
[35] Check scrcpy
[36] Auto Connect
[37] Auto Scan
[38] Screen Record+
[39] Open Camera
[40] Open Voice Recorder
[41] Pull Audio Recordings
[42] Flashlight ON
[43] Flashlight OFF
```

## Example package names for kill/open:

```bash
com.instagram.android
com.whatsapp
com.android.chrome
```

## If recorder package fails find yours:

```bash
adb shell pm list packages | grep record
```
