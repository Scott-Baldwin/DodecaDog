from os.path import dirname, abspath, join
import tkinter as tk
from tkinter import filedialog, messagebox
from time import sleep
import threading
import sys, platform, logging


# 3rd party
from win11toast import notify, update_progress
import psutil

# custom
from core import VERSION


class progress_notification:
    is_running = False

    def push(self):
        if not self.is_running:
            notify(
                progress={
                    "title": "Progress Notification",
                    "status": "Testing...",
                    "value": "0",
                    "valueStringOverride": "0/5 items",
                }
            )
            thread = threading.Thread(target=self.long_process)
            thread.start()
            print("started thread...")

    def long_process(self):
        if not self.is_running:
            self.is_running = True

            for i in range(1, 5 + 1):
                sleep(1)
                update_progress(
                    {"value": i / 5, "valueStringOverride": f"{i}/15 videos"}
                )
            update_progress({"status": "Completed!"})
            self.is_running = False


class AssetManager:
    app_path = dirname(abspath(__file__))
    app_icon = join(app_path, "assets", "icons", "dog.ico")
    file_icon = join(app_path, "assets", "icons", "file.ico")
    font_folder = join(app_path, "assets", "fonts")
    mpl_style = join(app_path, "assets", "cyberpunk.mplstyle")


# basic tkinter windows
def file_browse(multiple: bool = False, file_types: list = []) -> str | tuple:
    file_types.append(("All Files", "*"))
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(AssetManager.file_icon)
    if multiple:
        file_path = filedialog.askopenfilenames(
            parent=root,
            title="Select file(s)",
            filetypes=file_types,
        )
    else:
        file_path = filedialog.askopenfilename(
            parent=root,
            title="Select a file",
            filetypes=file_types,
        )
    root.destroy()
    return file_path


def folder_browse():
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(AssetManager.file_icon)
    folder_path = filedialog.askdirectory(
        parent=root,
        title="Select folder",
    )
    root.destroy()
    return folder_path


def msg_box(msg="Good Dog!"):
    title = "INFO"
    app_path = dirname(abspath(__file__))
    icon_path = join(app_path, "assets", "icons", "dog.ico")
    root = tk.Tk()
    root.withdraw()
    root.iconbitmap(icon_path)
    messagebox.showinfo(title=title, message=msg, parent=root)
    root.destroy()


# %% custom logging function
def print_log(msg, log=logging.info):
    print(msg)
    log(msg)


# %% system info for logs
def print_system_info(p=print_log):
    p("=" * 40 + " SYS " + "=" * 40)
    p(f"File/Script: {__file__}")
    p(f"File version: {VERSION}")
    py_version = sys.version.split()[0]
    p(f"Python Version: {py_version}")
    uname = platform.uname()
    p(f"System: {uname.system}")
    p(f"Node Name: {uname.node}")
    p(f"Release: {uname.release}")
    p(f"Version: {uname.version}")
    p(f"Machine: {uname.machine}")
    p(f"Processor: {uname.processor}")

    p("=" * 40 + " CPU " + "=" * 40)
    p(f"Physical cores: {psutil.cpu_count(logical=False)}")
    p(f"Total cores: {psutil.cpu_count(logical=True)}")
    p(f"Max Frequency: {psutil.cpu_freq().max / 1000:.1f}Ghz")

    p("=" * 40 + " RAM " + "=" * 40)
    p(f"Total: {get_bytes_size(psutil.virtual_memory().total)}")
    p(f"Available: {get_bytes_size(psutil.virtual_memory().available)}")

    p("=" * 40 + " END " + "=" * 40)


def get_bytes_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


if __name__ == "__main__":
    # msg_box(str(file_browse(True)))
    # msg_box(folder_browse())
    # msg_box()
    pass
