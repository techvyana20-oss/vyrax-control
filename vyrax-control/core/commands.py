from utils.runner import run
import shutil
from systems.connection_manager import save_device, auto_connect, check_and_fix
from systems.network_scanner import auto_find_adb

def handle_command(ch):

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

            run(f"adb pair {ip}:{pair_port}", input_data=code + "\n")

            connect_port = input("Connect Port: ").strip()

            run("adb disconnect")
            run(f"adb connect {ip}:{connect_port}")

            save_device(f"{ip}:{connect_port}")
            check_and_fix()

        elif mode == "2":
            ip = input("IP: ").strip()

            run("adb disconnect")
            run(f"adb connect {ip}:5555")

            save_device(f"{ip}:5555")
            check_and_fix()

    elif ch == "3":
        run("adb disconnect")

    elif ch == "36":
        auto_connect()

    elif ch == "37":
        auto_find_adb()

    elif ch == "4":
        run("adb shell screenrecord /sdcard/rec.mp4")

    elif ch == "5":
        if shutil.which("scrcpy") is None:
            print("❌ scrcpy not installed")
        else:
            run("scrcpy")

    elif ch == "7":
        run("adb shell screencap /sdcard/s.png && adb pull /sdcard/s.png")

    elif ch == "6":
        run("adb shell pm list packages")

    elif ch == "9":
        path = input("APK: ")
        run(f"adb install {path}")

    elif ch == "10":
        pkg = input("Package: ")
        run(f"adb uninstall {pkg}")

    elif ch == "13":
        pkg = input("Package: ")
        run(f"adb shell monkey -p {pkg} -c android.intent.category.LAUNCHER 1")

    elif ch == "29":
        pkg = input("Package: ")
        run(f"adb shell am force-stop {pkg}")

    elif ch == "33":
        pkg = input("Package: ")
        run(f"adb shell pm disable-user --user 0 {pkg}")

    elif ch == "34":
        pkg = input("Package: ")
        run(f"adb shell pm enable {pkg}")

    elif ch == "11":
        path = input("Phone path: ")
        run(f"adb pull {path}")

    elif ch == "12":
        path = input("Local file: ")
        run(f"adb push {path} /sdcard/")

    elif ch == "8":
        run("adb shell reboot -p")

    elif ch == "15":
        run("adb reboot")

    elif ch == "30":
        run("adb shell getprop")

    elif ch == "16":
        run("adb shell svc wifi enable")

    elif ch == "17":
        run("adb shell svc wifi disable")

    elif ch == "31":
        run("adb shell settings put global airplane_mode_on 1")

    elif ch == "32":
        run("adb shell settings put global airplane_mode_on 0")

    elif ch == "18":
        run("adb shell df -h")

    elif ch == "19":
        run("adb shell dumpsys battery")

    elif ch == "20":
        run("adb shell cat /proc/cpuinfo")

    elif ch == "21":
        run("adb shell cat /proc/meminfo")

    elif ch == "28":
        run("adb shell ps")

    elif ch == "22":
        run("adb shell input keyevent 24")

    elif ch == "23":
        run("adb shell input keyevent 25")

    elif ch == "24":
        run("adb shell input keyevent 26")

    elif ch == "25":
        run("adb shell input swipe 300 1000 300 300")

    elif ch == "26":
        url = input("URL: ")
        run(f'adb shell am start -a android.intent.action.VIEW -d "{url}"')

    elif ch == "14":
        run("adb logcat -d")

    elif ch == "27":
        run("adb logcat -c")

    elif ch == "35":
        if shutil.which("scrcpy") is None:
            print("❌ scrcpy not installed")
        else:
            print("✔ scrcpy installed")

    else:
        print("❌ Invalid option")
