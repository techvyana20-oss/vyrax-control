import subprocess
import time

def run(cmd, input_data=None):
    try:
        if "scrcpy" in cmd:
            subprocess.Popen(cmd, shell=True)
            print("✔ scrcpy launched")
            return

        # 🔥 special handling for adb pair
        if "adb pair" in cmd and input_data:
            proc = subprocess.Popen(
                cmd,
                shell=True,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            time.sleep(2)  # 🔥 wait for prompt

            proc.stdin.write(input_data)
            proc.stdin.flush()

            out, err = proc.communicate()

            print(out)
            if err:
                print(err)

            return

        # normal commands
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            print("✔ Success\n")
            print(result.stdout)
        else:
            print("❌ Failed\n")
            print(result.stderr)

    except Exception as e:
        print("⚠ Error:", e)
