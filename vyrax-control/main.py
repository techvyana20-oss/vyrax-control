from core.menu import start_tool
from systems.license import license_check
from systems.dependency import check_dep
from utils.ui import banner

def main():
    banner()

    if not license_check():
        return

    check_dep()
    start_tool()

if __name__ == "__main__":
    main()
