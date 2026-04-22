import subprocess
from utils.runner import run
from systems.connection_manager import save_device

def scan_network():
    print("\n🔍 Scanning network...\n")

    base_ip = "192.168.1."   # auto adjust if needed
    found = []

    for i in range(1, 255):
        ip = f"{base_ip}{i}"

        # quick ping check
        result = subprocess.run(
            f"ping -c 1 -W 1 {ip}",
            shell=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            print(f"🌐 Found device: {ip}")
            found.append(ip)

    return found


def auto_find_adb():
    devices = scan_network()

    print("\n⚡ Trying ADB connection...\n")

    for ip in devices:
        print(f"👉 Testing {ip}:5555")

        result = subprocess.run(
            f"adb connect {ip}:5555",
            shell=True,
            capture_output=True,
            text=True
        )

        output = result.stdout + result.stderr

        if "connected" in output or "device" in output:
            print(f"\n✅ ADB DEVICE FOUND: {ip}:5555\n")
            save_device(f"{ip}:5555")
            return

    print("\n❌ No ADB device found\n")
