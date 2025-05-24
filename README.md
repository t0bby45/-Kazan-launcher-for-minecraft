# Kazan Launcher
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Kazan+Launcher)](https://git.io/typing-svg)

**Kazan Launcher** is a custom Minecraft launcher built with Python using `customtkinter` for the GUI and `minecraft-launcher-lib` for version management and launching. It supports vanilla Minecraft installations and Forge mod installations.

## 🚀 Features

- Launch installed Minecraft versions with a custom nickname
- Install vanilla and Forge versions
- Show snapshots toggle
- Simple modern GUI using `customtkinter`
- Version selector with custom dropdown
- Installed versions list with delete option

![](https://komarev.com/ghpvc/?username=t0bby45)


## 🛠 Requirements

- Python 3.10+
- pip packages:
  - `customtkinter`
  - `minecraft-launcher-lib`

## 📁 Project Structure

project/
├── main.py                  # Entry point
├── ui/
│   ├── launcher_ui.py       # Main UI class
│   └── option_menu.py       # Custom dropdown widget
├── logic/
│   ├── install_logic.py     # Installation logic (vanilla & Forge)
│   ├── launcher_utils.py    # Helpers for launching versions
│   └── version_utils.py     # Version filtering & updates
└── assets/
    ├── profile.png
    ├── settings.png
    └── version.png
