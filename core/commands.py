from utils.runner import run
import shutil
import os
import time
import subprocess
from systems.connection_manager import save_device, auto_connect, check_and_fix
from systems.network_scanner import auto_find_adb

os.makedirs("captures/screenshots", exist_ok=True)
os.makedirs("captures/recordings", exist_ok=True)
os.makedirs("captures/files", exist_ok=True)


def handle_command(ch):

    if ch == "1":
        run("adb devices")
        check_and_fix()

    elif ch == "2":
        print("\nWireless Setup\n")
        print("1) Pair Android 11+")
        print("2) Connect 5555\n")

        mode=input("Select mode: ").strip()

        if mode=="1":
            ip=input("IP: ").strip()
            pair_port=input("Pairing Port: ").strip()
            code=input("Pairing Code: ").strip()

            run(
                f"adb pair {ip}:{pair_port}",
                input_data=code+"\n"
            )

            connect_port=input("Connect Port: ").strip()

            run("adb disconnect")
            run(f"adb connect {ip}:{connect_port}")

            save_device(
                f"{ip}:{connect_port}"
            )

            check_and_fix()

        elif mode=="2":
            ip=input("IP: ").strip()

            run("adb disconnect")
            run(f"adb connect {ip}:5555")

            save_device(
                f"{ip}:5555"
            )

            check_and_fix()


    elif ch == "3":
        run("adb disconnect")


    elif ch == "4":
        secs=input("Seconds (30): ").strip() or "30"
        name=f"record_{int(time.time())}.mp4"

        run(
            f"adb shell screenrecord --time-limit {secs} /sdcard/{name}"
        )

        run(
            f"adb pull /sdcard/{name} captures/recordings/"
        )


    # MIRROR BACKGROUND MODE 🔥
       elif ch == "5":
        if shutil.which("scrcpy"):
            subprocess.Popen(
                ["scrcpy"],
                start_new_session=True
            )

            print("✔ Mirror opened")
            print("👉 Use menu while watching screen")

        else:
            print("❌ scrcpy not installed")


    elif ch == "6":
        run("adb shell pm list packages")


    elif ch == "7":
        name=f"shot_{int(time.time())}.png"

        run(
            f"adb shell screencap -p /sdcard/{name}"
        )

        run(
            f"adb pull /sdcard/{name} captures/screenshots/"
        )


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


    elif ch == "33":
        pkg=input("Package: ")
        run(
         f"adb shell pm disable-user --user 0 {pkg}"
        )


    elif ch == "34":
        pkg=input("Package: ")
        run(
         f"adb shell pm enable {pkg}"
        )


    elif ch == "35":
        if shutil.which("scrcpy"):
            print("scrcpy installed")
        else:
            print("scrcpy missing")


    elif ch == "36":
        auto_connect()


    elif ch == "37":
        auto_find_adb()


    elif ch == "38":
        secs=input("Record seconds: ").strip() or "20"
        name=f"media_{int(time.time())}.mp4"

        run(
         f"adb shell screenrecord --time-limit {secs} /sdcard/{name}"
        )

        run(
         f"adb pull /sdcard/{name} captures/recordings/"
        )


    elif ch == "39":
        run(
         "adb shell am start -a android.media.action.IMAGE_CAPTURE"
        )


    elif ch == "40":
        run(
         "adb shell monkey -p com.transsion.soundrecorder -c android.intent.category.LAUNCHER 1"
        )


    elif ch == "41":
        run(
         "adb pull /sdcard/Recordings captures/files/"
        )


    elif ch == "42":
        run(
         "adb shell cmd flashlight set on"
        )


    elif ch == "43":
        run(
         "adb shell cmd flashlight set off"
        )


    # STOP MIRROR
    elif ch == "44":
        run("pkill scrcpy")
        print("✔ Mirror stopped")


    else:
        print("Invalid option")

