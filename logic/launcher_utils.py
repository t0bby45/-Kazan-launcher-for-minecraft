import os
import subprocess
import minecraft_launcher_lib.utils
import minecraft_launcher_lib.command


def get_minecraft_directory():
    return minecraft_launcher_lib.utils.get_minecraft_directory().replace(".minecraft", ".minecraft")


def get_launch_command(version, directory, username):
    options = {
        "username": username,
        "uuid": "12345678-1234-1234-1234-123456789abc",
        "token": "offline_token"
    }
    return minecraft_launcher_lib.command.get_minecraft_command(version, directory, options)


def delete_version(version, directory):
    path = os.path.join(directory, "versions", version)
    if os.path.exists(path):
        subprocess.call(["rm", "-rf", path] if os.name != 'nt' else ["cmd", "/c", "rmdir", "/s", "/q", path])