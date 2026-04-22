import shutil

def check_dep():
    print("\n[*] Checking dependencies...\n")

    if shutil.which("adb") is None:
        print("❌ adb not installed (install: android-tools)")
        exit()
    else:
        print("✔ adb found")

    if shutil.which("scrcpy") is None:
        print("⚠ scrcpy not installed (optional)")
    else:
        print("✔ scrcpy found")
