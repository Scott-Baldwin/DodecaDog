import os.path

import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

import core, fonts, utils


# %% main
def run():
    # create app instance
    app = core.AppClass()

    app_path = os.path.dirname(os.path.abspath(__file__))
    icon = os.path.join(app_path, "assets", "icons", "dog.ico")

    # boilerplate
    dpg.create_context()
    dpg.create_viewport(
        title="Custom Title", width=200, height=200, small_icon=icon, large_icon=icon
    )

    # add custom font
    fonts.set_default(i=1, s=16)

    # layout - does a lot of the heavy lifting
    _create_layout(app)

    # more boilerplate
    dpg.setup_dearpygui()
    dpg.show_viewport()

    # set main window
    dpg.set_primary_window("main", True)

    # more boilerplate
    dpg.start_dearpygui()
    dpg.destroy_context()


# %% layout
note = utils.progress_notification()


def _create_layout(app, name=core.NAME, version=core.VERSION):
    with dpg.window(tag="main"):
        dpg.add_text(f"{name} v{version}")

        _file_browse_group("file_path")
        _files_browse_group("files_path")
        _folder_browse_group("folder_path")

        dpg.add_button(label="test", callback=_callback_check)
        dpg.add_button(label="push", callback=note.push)

        dpg.add_slider_float(
            label="a",
            default_value=app.a,
            max_value=1,
            callback=_callback_a,
            user_data=app,
        )

        dpg.add_input_int(
            label="b", default_value=app.b, callback=_callback_b, user_data=app
        )
        with dpg.group(horizontal=True):
            dpg.add_text("a * b =")
            dpg.add_text("0.00", tag="display")


# %% callbacks
def _callback_a(sender, app_data, user_data):
    app = user_data
    app.set_a(app_data)
    _update_display(sender, app_data, app)


def _callback_b(sender, app_data, user_data):
    app = user_data
    app.set_b(app_data)
    _update_display(sender, app_data, app)


# %% window elements
# TODO: these might be able to combined into a single class
def _file_browse_callback(sender, value, user_data):
    tag = user_data
    path = utils.file_browse()
    if path not in ("", []):
        dpg.set_value(f"check_{tag}", True)
        dpg.set_value(f"tip_{tag}", path)


def _file_browse_group(tag):
    with dpg.group(horizontal=True):
        dpg.add_button(label="...", callback=_file_browse_callback, user_data=tag)
        dpg.add_checkbox(tag=f"check_{tag}", enabled=False)
        dpg.add_text(f"{tag}", tag=f"text_{tag}")
    with dpg.tooltip(f"text_{tag}"):
        dpg.add_text(tag, tag=f"tip_{tag}", wrap=400)


def _files_browse_callback(sender, value, user_data):
    tag = user_data
    path = utils.file_browse(multiple=True)
    if path not in ("", []):
        dpg.set_value(f"check_{tag}", True)
        dpg.set_value(f"tip_{tag}", path)


def _files_browse_group(tag):
    with dpg.group(horizontal=True):
        dpg.add_button(label="...", callback=_files_browse_callback, user_data=tag)
        dpg.add_checkbox(tag=f"check_{tag}", enabled=False)
        dpg.add_text(f"{tag}", tag=f"text_{tag}")
    with dpg.tooltip(f"text_{tag}"):
        dpg.add_text(tag, tag=f"tip_{tag}", wrap=400)


def _folder_browse_callback(sender, value, user_data):
    tag = user_data
    path = utils.folder_browse()
    if path != "":
        dpg.set_value(f"check_{tag}", True)
        dpg.set_value(f"tip_{tag}", path)


def _folder_browse_group(tag):
    with dpg.group(horizontal=True):
        dpg.add_button(
            label="...",
            callback=_folder_browse_callback,
            user_data=tag,
        )
        dpg.add_checkbox(tag=f"check_{tag}", enabled=False)
        dpg.add_text(f"{tag}", tag=f"text_{tag}")
    with dpg.tooltip(f"text_{tag}"):
        dpg.add_text(tag, tag=f"tip_{tag}", wrap=400)


# %% helpers
def _update_display(sender, app_data, app):
    dpg.set_value("display", app.go())


def _callback_check(sender, app_data, user_data):
    print(f"sender: {sender}\napp_data: {app_data}\nuser_data: {user_data}")


# %% extras
def dpg_demo():
    dpg.create_context()
    dpg.create_viewport(title="Custom Title", width=600, height=600)

    demo.show_demo()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    # dpg_demo()
    run()
