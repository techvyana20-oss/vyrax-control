from core.commands import handle_command

def show_menu():
    print("""
[1] Check Device        [2] Connect Device        [3] Disconnect
[4] Screen Record       [5] Screen Mirror         [6] List Apps
[7] Screenshot          [8] Power Off             [9] Install APK
[10] Uninstall App      [11] Pull File            [12] Push File
[13] Open App           [14] Logs                 [15] Reboot
[16] WiFi ON            [17] WiFi OFF             [18] Storage Info
[19] Battery Info       [20] CPU Info             [21] Memory Info
[22] Volume Up          [23] Volume Down          [24] Lock Screen
[25] Unlock Swipe       [26] Open URL             [27] Clear Logs
[28] Processes          [29] Kill App             [30] Device Info
[31] Airplane ON        [32] Airplane OFF         [q] Quit
""")

def start_tool():
    while True:
        try:
            show_menu()
            choice = input("Select: ").strip()

            if choice.lower() == "q":
                print("Bye 😈")
                break

            handle_command(choice)

        except KeyboardInterrupt:
            print("\n⚠ Interrupted! Returning to menu...\n")
            continue
