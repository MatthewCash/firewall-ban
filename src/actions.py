import subprocess
from os import environ

jail_name = environ.get("JAIL_NAME") or "fw-ban"


def ban_ip(ip: str) -> bool:
    try:
        process = subprocess.run(
            ["fail2ban-client", "set", jail_name, "banip", ip], capture_output=True)
    except Exception as error:
        print("An error occurred while attempting to call ban command!")
        print(error)

        return False

    return process.stdout.decode("utf-8").strip() == "1"


def unban_ip(ip: str) -> bool:
    try:
        process = subprocess.run(
            ["fail2ban-client", "set", jail_name, "unbanip", ip], capture_output=True)
    except Exception as error:
        print("An error occurred while attempting to call unban command!")
        print(error)

        return False

    return process.stdout.decode("utf-8").strip() == "1"


def is_ip_banned(ip: str) -> bool:
    try:
        process = subprocess.run(
            ["fail2ban-client", "get", jail_name, "banned", ip], capture_output=True)
    except Exception as error:
        print("An error ocurred while attempting to call check command!")
        print(error)

        return False

    return process.stdout.decode("utf-8").strip() == "1"
