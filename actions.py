
import subprocess


def ban_ip(ip: str) -> bool:
    try:
        process = subprocess.Popen(
            ["/usr/bin/sudo /usr/bin/env bash ./scripts/ban.sh", ip], shell=True)
        process.wait()
    except Exception as error:
        print("An error occurred while attempting to call ban script!")
        print(error)

        return False

    return process.returncode == 0


def unban_ip(ip: str) -> bool:
    try:
        process = subprocess.Popen(
            ["/usr/bin/sudo /usr/bin/env bash ./scripts/unban.sh", ip], shell=True)
        process.wait()
    except Exception as error:
        print("An error occurred while attempting to call ban script!")
        print(error)

        return False

    return process.returncode == 0


def is_ip_banned(ip: str) -> bool:
    try:
        process = subprocess.Popen(
            ["/usr/bin/sudo /usr/bin/env bash ./scripts/check.sh", ip], shell=True)
        process.wait()
    except Exception as error:
        print("An error ocurred while attempting to check ip!")
        print(error)

        return False
    # Check script will return 0 if ip is banned
    return process.returncode == 0
