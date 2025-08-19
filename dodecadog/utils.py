# standard
from os.path import dirname, abspath, join
import tkinter as tk
from tkinter import filedialog, messagebox
from time import sleep
import threading
import sys, platform, logging

# 3rd party
from win11toast import notify, update_progress
import psutil
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt

# custom
from core import VERSION


# %% misc
class AssetManager:
    app_path = dirname(abspath(__file__))
    app_icon = join(app_path, "assets", "icons", "dog.ico")
    file_icon = join(app_path, "assets", "icons", "file.ico")
    font_folder = join(app_path, "assets", "fonts")
    mpl_style = join(app_path, "assets", "cyberpunk.mplstyle")


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


def get_image_coords():
    # Replace this URL with the direct link to the image you want to download
    # image_url = "https://imgs.xkcd.com/comics/curve_fitting.png"
    image_url = "https://imgs.xkcd.com/comics/escalators.png"

    try:
        # Step 1: Download the image data from the URL
        response = requests.get(image_url)
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)

        # Step 2: Read the image data from the response content
        image_data = BytesIO(response.content)

        # Step 3: Open the image using Pillow (PIL)
        image = Image.open(image_data)

        # image = plt.imread(image_url)

        # Step 4: Display the image
        # This will open a new window showing the image
        print("Displaying the image...")
        plt.imshow(image)
        title = "Left-Click on the image to add a point\nRight-Click to undo the last point\nMiddle-Click to finish"
        plt.title(title)
        # print(title)
        plt.tight_layout()

        coordinates = plt.ginput(n=-1, timeout=0)
        plt.close()

        # print output
        [
            print(f"Point {index}: ({value[0]:.2f}, {value[1]:.2f})")
            for index, value in enumerate(coordinates)
        ]

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the image: {e}")
    except IOError as e:
        print(f"Error processing the image file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# %%basic tkinter windows
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


# %% system info
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
