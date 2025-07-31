import winup, os
from winup import ui, style


@winup.component
def RadioButtonExample():
    style.themes.set_theme("dark")

    def on_option_toggled(is_checked, option_name):
        if is_checked:
            print(f"Selected option: {option_name}")

    return ui.Column(
        children=[
            ui.Label(text="Choose a shipping method:"),
            ui.RadioButton(
                text="Standard (5-7 days)",
                on_toggle=lambda checked: on_option_toggled(checked, "Standard"),
            ).set_checked(True),  # Pre-select the first option
            ui.RadioButton(
                text="Express (2-3 days)",
                on_toggle=lambda checked: on_option_toggled(checked, "Express"),
            ),
            ui.RadioButton(
                text="Overnight (1 day)",
                on_toggle=lambda checked: on_option_toggled(checked, "Overnight"),
            ),
        ]
    )


def run():
    this_module_name = f"{os.path.basename(__file__).split('.')[0]}"
    winup.run(
        main_component_path=f"{this_module_name}:RadioButtonExample",
        title="Radio Button Demo",
        width=200,
        height=100,
        dev=True,
    )


if __name__ == "__main__":
    run()
