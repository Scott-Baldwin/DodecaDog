# %% imports
# standard lib
import os
import random

# 3rd party
import winup
from winup import ui, style, state
import matplotlib.pyplot as plt
import darkdetect

# this repo
import core, utils


# %% helper functions
def show_mpl_plot(selection):
    theme = utils.AssetManager.mpl_style if selection == "custom" else selection
    plt.style.use(theme)
    if plt.fignum_exists(1):
        # bring plot to front
        plt.show()

    else:
        # print("Showing MPL figure")
        data = {
            "Series 1": [(random.uniform(20, 40)) for _ in range(10)],
            "Series 2": [(random.uniform(50, 70)) for _ in range(10)],
            "Series 3": [(random.uniform(35, 10)) for _ in range(10)],
        }
        for k, v in data.items():
            plt.plot(v, label=k)

        plt.legend()
        plt.tight_layout()
        plt.show()


def add_file_browse():
    is_running = state.create("is_running", False)

    def get_file():
        if not is_running.get():
            is_running.set(True)
            file = utils.file_browse()
            if file != "":
                btn.setToolTip(file)
            is_running.set(False)
        else:
            print("File window already open")

    label = ui.Label("Select a File")
    btn = ui.Button("...", on_click=get_file)

    return ui.Row(props={"spacing": 10}, children=[btn, label])


def add_folder_browse():
    is_running = state.create("is_running", False)

    def get_folder():
        if not is_running.get():
            is_running.set(True)
            path = utils.folder_browse()
            if path != "":
                btn.setToolTip(path)
            is_running.set(False)
        else:
            print("File dialog window already open")

    label = ui.Label("Select a Folder")
    btn = ui.Button("...", on_click=get_folder)

    return ui.Row(props={"spacing": 10}, children=[btn, label])


def add_plot_controls(plot_theme_state):
    def on_selection_change(selected_text):
        plot_theme_state.set(selected_text)

    items = ["default", "custom"]
    [items.append(s) for s in plt.style.available]
    combo = ui.ComboBox(items=items, on_change=on_selection_change)

    return ui.Column(
        children=[
            ui.Label(text="Select plot theme:"),
            combo,
            ui.Button(
                "MPL Plot", on_click=lambda: show_mpl_plot(plot_theme_state.get())
            ),
        ]
    )


def add_text_area():
    text = ui.Textarea(placeholder="Long text will be displayed here...")
    text.setReadOnly(True)
    return text


def update_text_area(state):
    state.set(
        {
            "A": 1,
            "B": 2,
            "C": 2,
            "D": 2,
            "E": 10,
        }
    )


# --- Main Application ---
# %%

# prep
# needs to be called before GUI function
note = utils.progress_notification()
app = core.AppClass()


@winup.component
def run():
    # detect system theme and set app theme to match
    if darkdetect.isDark():
        style.themes.set_theme("dark")

    # set up states
    plot_theme_state = state.create("plot_theme", "default")

    text_area_state = state.create("text_area", {})
    text = add_text_area()
    text_area_state.bind_to(
        widget=text,
        property_name="text",
        formatter=lambda d: "\n".join([f"{key}: {value}" for key, value in d.items()]),
    )

    layout = ui.Column(
        props={"spacing": 10, "margin": "20px"},
        children=[
            ui.Column(
                children=[
                    add_file_browse(),
                    add_folder_browse(),
                ]
            ),
            add_plot_controls(plot_theme_state),
            ui.Button(
                "Get Image Coords",
                on_click=lambda: utils.get_image_coords(plot_theme_state.get()),
            ),
            ui.Button("Push Notification", on_click=note.push),
            text,
            ui.Button(
                "Update Text", on_click=lambda: update_text_area(text_area_state)
            ),
        ],
    )

    return layout


# %%


def main():
    this_module_name = f"{os.path.basename(__file__).split('.')[0]}"
    winup.run(
        main_component_path=f"{this_module_name}:run",
        title=core.NAME,
        width=200,
        height=100,
        icon=utils.AssetManager.app_icon,
        dev=True,
    )


if __name__ == "__main__":
    main()
