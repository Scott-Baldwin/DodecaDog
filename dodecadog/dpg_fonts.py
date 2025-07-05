import os
import dearpygui.dearpygui as dpg
import utils


def font_manager():
    dpg.create_context()

    font_reg = register_fonts(16)
    set_default()

    with dpg.window(label="Font Example", height=200, width=200):
        dpg.add_button(label="Default font")
        b2 = dpg.add_button(label="Secondary font")
        dpg.add_button(label="default")

        # set font of specific widgets
        set_default()
        dpg.bind_item_font(b2, font_reg[1])

    dpg.show_font_manager()

    dpg.create_viewport(
        # title="Font Manager",
        # width=800,
        # height=600,
    )
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def register_fonts(size):
    # paths to font files
    fonts = [
        "OpenSans-Regular.ttf",
        "SourceSansPro-Regular.otf",
        "Montserrat-Light.otf",
        "Montserrat-Regular.otf",
        "Montserrat-Black.otf",
        "Quicksand-Regular.otf",
    ]
    paths = [os.path.join(utils.AssetManager.font_folder, f) for f in fonts]

    # add fonts to registry
    with dpg.font_registry():
        font_reg = [dpg.add_font(p, size) for p in paths]

    return font_reg


def set_default(i=0, s=13):
    font_reg = register_fonts(s)
    dpg.bind_font(font_reg[i])


if __name__ == "__main__":
    font_manager()
