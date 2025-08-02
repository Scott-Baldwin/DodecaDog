import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


import winup
from winup import ui, style


@winup.component
def App():
    style.themes.set_theme("dark")
    return ui.Column(
        children=[
            ui.Label(text="Label!"),
            ui.Switch(
                text="Switch 1",
                on_toggle=lambda bool: print(f"Switch 1: {bool}"),
            ),
            ui.Switch(
                text="Switch 2",
                on_toggle=lambda bool: print(f"Switch 2: {bool}"),
                props={"color": "black"},
            ),
        ]
    )


if __name__ == "__main__":
    winup.run(
        main_component_path="switch:App",
        title="My Hot-Reloaded App",
        dev=True,
        width=100,
        height=50,
    )
