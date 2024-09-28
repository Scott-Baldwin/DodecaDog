from os.path import dirname, abspath, join
import tkinter as tk
from tkinter import filedialog, messagebox


class AssetManager:
    app_path = dirname(abspath(__file__))
    app_icon = join(app_path, "assets", "icons", "dog.ico")
    file_icon = join(app_path, "assets", "icons", "file.ico")
    font_folder = join(app_path, "assets", "fonts")


# basic tkinter windows
def file_browse(multiple=False, file_types=[]):
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


if __name__ == "__main__":
    # msg_box(str(file_browse(True)))
    msg_box(folder_browse())
    # msg_box()
