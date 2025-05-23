import minecraft_launcher_lib.install
import minecraft_launcher_lib.forge


def install_minecraft(version, directory):
    minecraft_launcher_lib.install.install_minecraft_version(version, directory)


def install_forge(version, directory):
    forge_version = minecraft_launcher_lib.forge.find_forge_version(version)
    if forge_version:
        minecraft_launcher_lib.forge.install_forge_version(forge_version, directory)
        return forge_version
    return None