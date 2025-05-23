# Kazan Launcher

**Kazan Launcher** is a custom Minecraft launcher built with Python using `customtkinter` for the GUI and `minecraft-launcher-lib` for version management and launching. It supports vanilla Minecraft installations and Forge mod installations.

## 🚀 Features

- Launch installed Minecraft versions with a custom nickname
- Install vanilla and Forge versions
- Show snapshots toggle
- Simple modern GUI using `customtkinter`
- Version selector with custom dropdown
- Installed versions list with delete option

## 📁 Project Structure

project/
├── main.py # Entry point of the application
├── ui/
│ ├── launcher_ui.py # Main launcher GUI class
│ └── option_menu.py # Custom dropdown widget
├── logic/
│ ├── install_logic.py # Logic for installing versions
│ ├── launcher_utils.py # Launcher-related helpers
│ └── version_utils.py # Version filtering and sorting
└── assets/
├── profile.png
├── settings.png
└── version.png


## 🛠 Requirements

- Python 3.10+
- pip packages:
  - `customtkinter`
  - `minecraft-launcher-lib`
