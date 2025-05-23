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

markdown
Копировать
Редактировать

## 🛠 Requirements

- Python 3.10+
- pip packages:
  - `customtkinter`
  - `minecraft-launcher-lib`
  - `Pillow` *(for image support)*

Install them with:

```bash
pip install -r requirements.txt
Create requirements.txt:

text
Копировать
Редактировать
customtkinter
minecraft-launcher-lib
Pillow
🖼 Assets
All icons and images should be placed inside the assets/ folder. They are loaded using a helper function that supports both development and PyInstaller mode:

python
Копировать
Редактировать
def resource_path(relative_path):
    import sys, os
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
📦 Build to EXE
Use PyInstaller to build the launcher into a standalone .exe file:

bash
Копировать
Редактировать
pyinstaller --onefile --windowed --add-data "assets;assets" main.py
--onefile: packs everything into a single executable

--windowed: prevents console window on Windows

--add-data: includes assets/ directory

📥 Output
After building, you'll find your .exe inside the dist/ folder:

css
Копировать
Редактировать
dist/
└── main.exe
You can rename it to KazanLauncher.exe or anything you want.

✅ Compatibility
Tested on Windows 10/11

Should work on Linux/macOS with adjustments

📌 Notes
Make sure to launch Minecraft with valid version installations.

This launcher works in offline mode (no authentication).

Forge version installation relies on availability from minecraft-launcher-lib.


📜 License
MIT License – free to use and modify.

vbnet
Копировать
Редактировать

Let me know if you'd like to include installation GIFs, translation to Russian, or a `.spec` file t