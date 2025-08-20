# main script to use as the 'launcher' for app options

from utils import select_gui


def main():
    gui = select_gui()

    if gui == "WinUp":
        import winup_gui

        winup_gui.main()

    elif gui == "DearPyGUI":
        import dpg_gui

        dpg_gui.run()

    else:
        print(f"Invalid Selection: {gui}")


if __name__ == "__main__":
    try:
        main()
    except ModuleNotFoundError as e:
        print(f"An error occurred: {e}")
        print("Try running 'uv sync --all-groups' to install all dependencies")
