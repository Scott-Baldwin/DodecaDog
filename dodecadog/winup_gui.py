import os
import random

import winup
from winup import ui, style, state
import matplotlib.pyplot as plt
import mplcyberpunk

import utils


# extras
def toggle_theme():
    # Access the theme manager via the 'themes' attribute on the style module
    current_theme = style.themes.get_active_theme_name()
    next_theme = "dark" if current_theme == "light" else "light"
    style.themes.set_theme(next_theme)


def show_mpl_plot():
    if plt.fignum_exists(1):
        # bring plot to front
        plt.show()

    else:
        print("Showing MPL figure")

        # line graph
        data = {
            "Series 1": [(random.uniform(20, 40)) for _ in range(10)],
            "Series 2": [(random.uniform(50, 70)) for _ in range(10)],
            "Series 3": [(random.uniform(35, 10)) for _ in range(10)],
        }

        for k, v in data.items():
            plt.plot(v, label=k)

        plt.legend()
        plt.tight_layout()

        # optional effect for cyberpunk theme
        # needs to be after legend creation
        # mplcyberpunk.make_lines_glow()

        plt.show()


# --- Main Application ---
# %%


@winup.component
def App():
    """The main app uses a TabView to organize the chart demos."""

    matrix_theme = {
        "primary-color": "#00FF41",
        "primary-text-color": "#000000",
        "background-color": "#0D0208",
        "text-color": "#00FF41",
        "border-color": "#008F11",
        "hover-color": "#00A62A",
        "secondary-color": "#1A1A1A",
        "secondary-text-color": "#00FF41",
        "disabled-color": "#333333",
        "error-color": "#FF4136",
    }

    sunset_theme = {
        "primary-color": "#FF6B35",
        "primary-text-color": "#FFFFFF",
        "background-color": "#2C1810",
        "text-color": "#FFE5D9",
        "border-color": "#8B4513",
        "hover-color": "#FF8C42",
        "secondary-color": "#4A2E20",
        "secondary-text-color": "#FFE5D9",
        "disabled-color": "#5A3D31",
        "error-color": "#FF4136",
    }
    custom_theme = {
        "primary-color": "#0EE761",
        "primary-text-color": "#0B0FF8",
        "background-color": "#2C1810",
        "text-color": "#F50606",
        "border-color": "#FF00F2",
        "hover-color": "#EEEA0D",
        "secondary-color": "#000000",
        "secondary-text-color": "#EC830A",
        "disabled-color": "#A410E9",
        "error-color": "#BFEE3D",
    }

    # Add the custom themes
    style.themes.add_theme("matrix", matrix_theme)
    style.themes.add_theme("sunset", sunset_theme)
    style.themes.add_theme("custom", custom_theme)

    # style.themes.set_theme("dark")
    style.themes.set_theme("matrix")
    # style.themes.set_theme("sunset")
    # style.themes.set_theme("custom")

    # plot styles
    # plt.style.use("dark_background")
    # plt.style.use("cyberpunk")

    file = state.create("file", "")

    def get_file():
        f = utils.file_browse()
        if f != "":
            file.set(f)

    def print_file():
        print(file.get())

    layout = ui.Column(
        props={"spacing": 10, "margin": "20px"},
        children=[
            # tabs,
            ui.Button("Toggle Theme", on_click=toggle_theme),
            ui.Button("Get File", on_click=get_file),
            ui.Button("Print File", on_click=print_file),
            ui.Button("MPL Plot", on_click=show_mpl_plot),
        ],
    )

    return layout


# %%


def run():
    this_module_name = f"{os.path.basename(__file__).split('.')[0]}"
    winup.run(
        main_component_path=f"{this_module_name}:App",
        title="WinUp Graphing Widgets Demo",
        width=200,
        height=100,
        icon=os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "assets",
            "icons",
            "dog.ico",
        ),
        dev=True,
    )


if __name__ == "__main__":
    run()
