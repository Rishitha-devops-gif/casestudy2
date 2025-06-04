import os
import platform
import subprocess

def get_system_uptime():
    system = platform.system()
    try:
        if system == "Windows":
            # Use 'net stats srv' and parse the output
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System Uptime:", line.strip())
                    return
            print("Could not determine uptime on Windows.")
        elif system in ["Linux", "Darwin"]:
            # Use 'uptime' command for Unix-like systems
            output = subprocess.check_output("uptime -p", shell=True, text=True)
            print("System Uptime:", output.strip())
        else:
            print("Unsupported operating system:", system)
    except Exception as e:
        print("Error getting system uptime:", e)

if __name__ == "__main__":
    get_system_uptime()
