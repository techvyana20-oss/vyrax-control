import json
import os
import subprocess
from utils.runner import run

FILE = "data/device.json"

def save_device(ip):
    os.makedirs("data", exist_ok=True)
    with open(FILE, "w") as f:
        json.dump({"ip": ip}, f)

def load_device():
    if not os.path.exists(FILE):
        return None
    try:
        with open(FILE) as f:
            return json.load(f).get("ip")
    except:
        return None

def auto_connect():
    ip = load_device()

    if not ip:
        print("⚠ No saved device")
        return

    print(f"\n🔄 Connecting to {ip}...\n")

    run("adb disconnect")
    run(f"adb connect {ip}")

def check_and_fix():
    result = subprocess.run("adb devices", shell=True, capture_output=True, text=True)
    output = result.stdout

    if "offline" in output:
        print("⚠ Device offline → fixing...")
        run("adb disconnect")

        ip = load_device()
        if ip:
            run(f"adb connect {ip}")

    elif "device" in output:
        print("✔ Device ready")
    else:
        print("⚠ No device connected")
