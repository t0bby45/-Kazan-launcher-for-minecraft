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



## 🛠 Requirements

- Python 3.10+
- pip packages:
  - `customtkinter`
  - `minecraft-launcher-lib`


## 📁 Project Structure

project/
├── main.py # Entry point of the application
│
├── ui/ # UI-related components
│ ├── launcher_ui.py # Main launcher window and layout
│ └── option_menu.py # Custom dropdown widget (version selector)
│
├── logic/ # Logic separated from UI
│ ├── install_logic.py # Functions for installing Minecraft & Forge
│ ├── launcher_utils.py # Helper methods for launching the game
│ └── version_utils.py # Version filtering and formatting
│
├── assets/ # Icons and image files used in the launcher
│ ├── profile.png
│ ├── settings.png
│ └── version.png
