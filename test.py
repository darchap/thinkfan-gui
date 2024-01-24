import os
from pathlib import Path


def check_permissions(file_path):
    # Check if the file exists
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Check if the current user has read and write permissions
    if not os.access(file_path, os.R_OK | os.W_OK):
        raise PermissionError(f"User does not have read and write rights for file: {file_path}")

    # Check if the current user has execute permissions
    if not os.access(file_path, os.X_OK):
        raise PermissionError(f"User does not have execute rights for file: {file_path}")

    return True, "User has read, write and execute rights"


# Example usage
file_path = "/proc/acpi/ibm/fan"
try:
    result, message = check_permissions(file_path)
    print(f"Result: {result}")
    print(f"Message: {message}")
except Exception as e:
    print(f"An error occurred: {e}")
