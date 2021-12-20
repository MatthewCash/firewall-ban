
import subprocess


def ban_ip(ip: str) -> bool:
    try:
        process = subprocess.Popen(
            ["./scripts/ban.sh", ip], shell=True)
        process.wait()
    except Exception as error:
        print("An error ocurred while attempting to call ban script!")
        print(error)

        return False

    return process.returncode == 0


def unban_ip(ip: str) -> bool:
    try:
        process = subprocess.Popen(
            ["./scripts/unban.sh", ip], shell=True)
        process.wait()
    except Exception as error:
        print("An error ocurred while attempting to call ban script!")
        print(error)

        return False

    return process.returncode == 0
