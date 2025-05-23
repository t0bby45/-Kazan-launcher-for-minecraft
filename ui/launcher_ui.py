import os
import threading
import subprocess
import customtkinter as ctk
import tkinter.messagebox
from ui.option_menu import CustomCTkOptionMenu
from logic import launcher_utils, version_utils, install_logic

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

minecraft_directory = launcher_utils.get_minecraft_directory()

class MinecraftLauncherUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kazan Launcher")
        self.geometry("900x600")
        self.resizable(False, False)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        self.left_panel = ctk.CTkFrame(self.main_frame, width=300)
        self.left_panel.pack(side="left", fill="y", padx=10, pady=10)

        self.installed_label = ctk.CTkLabel(self.left_panel, text="Установленные версии")
        self.installed_label.pack(pady=5)

        self.installed_versions_box = ctk.CTkScrollableFrame(self.left_panel, width=280, height=400)
        self.installed_versions_box.pack(pady=5)

        self.right_panel = ctk.CTkFrame(self.main_frame)
        self.right_panel.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.username_entry = ctk.CTkEntry(self.right_panel, placeholder_text="Введите никнейм")
        self.username_entry.pack(pady=10)

        self.launch_button = ctk.CTkButton(self.right_panel, text="Запустить выбранную версию", command=self.launch_selected_version)
        self.launch_button.pack(pady=10)

        self.bottom_panel = ctk.CTkFrame(self)
        self.bottom_panel.pack(side="bottom", fill="x", padx=20, pady=10)

        self.include_snapshots = ctk.CTkCheckBox(self.bottom_panel, text="Показать снапшоты", command=self.update_version_list)
        self.include_snapshots.pack(side="left", padx=10)

        self.version_combobox_widget = CustomCTkOptionMenu(self.bottom_panel, values=[])
        self.version_combobox_widget.pack(side="left", padx=10)

        self.forge_checkbox = ctk.CTkCheckBox(self.bottom_panel, text="Forge")
        self.forge_checkbox.pack(side="left", padx=10)

        self.install_button = ctk.CTkButton(self.bottom_panel, text="Установить версию", command=self.threaded_install)
        self.install_button.pack(side="left", padx=10)

        self.status_label = ctk.CTkLabel(self.bottom_panel, text="")
        self.status_label.pack(side="left", padx=10)

        self.progress_bar = ctk.CTkProgressBar(self.bottom_panel, width=200)
        self.progress_bar.set(0)
        self.progress_bar.pack_forget()

        self.selected_version = None
        self.update_version_list()
        self.update_installed_versions()

    def update_version_list(self):
        show_snapshots = self.include_snapshots.get()
        filtered_versions = version_utils.get_filtered_versions(minecraft_directory, show_snapshots)
        self.version_combobox_widget.configure_values(filtered_versions)
        if filtered_versions:
            self.version_combobox_widget.set(filtered_versions[0])

    def update_installed_versions(self):
        for widget in self.installed_versions_box.winfo_children():
            widget.destroy()

        versions_path = os.path.join(minecraft_directory, "versions")
        if os.path.exists(versions_path):
            row, column = 0, 0
            for version in os.listdir(versions_path):
                tile = ctk.CTkFrame(self.installed_versions_box, width=130, height=70)
                tile.grid(row=row, column=column, padx=5, pady=5)
                label = ctk.CTkLabel(tile, text=version)
                label.pack(pady=2)
                button_frame = ctk.CTkFrame(tile)
                button_frame.pack()
                select_button = ctk.CTkButton(button_frame, text="Выбрать", width=80, command=lambda v=version: self.select_version(v))
                select_button.pack(side="left", padx=2)
                delete_button = ctk.CTkButton(button_frame, text="🗑", width=30, command=lambda v=version: self.delete_version(v))
                delete_button.pack(side="left", padx=2)
                column += 1
                if column >= 2:
                    column = 0
                    row += 1

    def delete_version(self, version):
        try:
            launcher_utils.delete_version(version, minecraft_directory)
            self.status_label.configure(text=f"Удалена версия: {version}")
            self.update_installed_versions()
        except Exception as e:
            self.status_label.configure(text=f"Ошибка удаления: {e}")

    def select_version(self, version):
        self.selected_version = version
        self.status_label.configure(text=f"Выбрана версия: {version}")

    def launch_selected_version(self):
        if not self.selected_version:
            self.status_label.configure(text="Ошибка: не выбрана версия")
            return
        username = self.username_entry.get() or "Player"
        try:
            command = launcher_utils.get_launch_command(self.selected_version, minecraft_directory, username)
            self.status_label.configure(text=f"Запуск {self.selected_version}...")
            subprocess.run(command)
        except Exception as e:
            self.status_label.configure(text=f"Ошибка запуска: {e}")

    def threaded_install(self):
        thread = threading.Thread(target=self.install_selected_version)
        thread.start()

    def simulate_progress(self):
        for i in range(1, 11):
            self.progress_bar.set(i / 10)
            self.update_idletasks()
            self.after(100)

    def install_selected_version(self):
        version = self.version_combobox_widget.get()
        if not version:
            self.status_label.configure(text="Ошибка: не выбрана версия для установки")
            return

        self.set_controls_state("disabled")
        self.progress_bar.set(0)
        self.progress_bar.pack(side="left", padx=10)
        self.update_idletasks()

        try:
            if self.forge_checkbox.get():
                forge_version = install_logic.install_forge(version, minecraft_directory)
                if forge_version:
                    self.status_label.configure(text=f"Forge {forge_version} установлен")
                else:
                    self.status_label.configure(text=f"Forge не найден для {version}")
            else:
                install_logic.install_minecraft(version, minecraft_directory)
                self.status_label.configure(text=f"Minecraft {version} установлен")
            self.progress_bar.set(1.0)
            self.update_installed_versions()
        except Exception as e:
            self.status_label.configure(text=f"Ошибка установки: {e}")
        finally:
            self.set_controls_state("normal")
            self.progress_bar.set(0)
            self.progress_bar.pack_forget()

    def set_controls_state(self, state):
        self.install_button.configure(state=state)
        self.version_combobox_widget.button.configure(state=state)
        self.forge_checkbox.configure(state=state)
        self.launch_button.configure(state=state)
        self.username_entry.configure(state=state)
        self.include_snapshots.configure(state=state)