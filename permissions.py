import logging
import os
import stat
import subprocess
from pathlib import Path


def manage_permissions(file_path) -> bool:
    if not Path(file_path).exists():
        raise FileNotFoundError

    if os.access(file_path, os.W_OK):
        return True

    subprocess.check_call(["pkexec", "chown", os.getlogin(), file_path])
    logging.info("Upgraded chown")

    Path(file_path).chmod(stat.S_IWUSR | stat.S_IRUSR)
    logging.info("Upgraded chmod")

    return True


def update_fan_value(file_path, value="level auto"):
    if manage_permissions(file_path):
        Path(file_path).write_text(value)
        logging.info(value)


if __name__ == "__main__":
    file_path = "/proc/acpi/ibm/fan"
    import time

    try:
        update_fan_value(file_path, "level 5")
        time.sleep(5)
        update_fan_value(file_path)
    except PermissionError:
        logging.error("Permission error occurred. Please check the file permissions.")
    except FileNotFoundError:
        logging.error("File not found. Please check the file path.")
    except subprocess.CalledProcessError:
        logging.error("Failed to execute the command. Please check the command.")
