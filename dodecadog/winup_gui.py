# %% prep
import os

this_module_name = f"{os.path.basename(__file__).split('.')[0]}"
# use with This in winup.run(
# ... main_component_path=f"{this_module_name}:App",

# %% main
import winup
from winup import ui, style
import random
import matplotlib.pyplot as plt
import pandas as pd
import mplcyberpunk


# --- Helper Functions for Data Generation ---
def generate_bar_data():
    """Generates random data for the bar chart."""
    categories = ["Alpha", "Bravo", "Charlie", "Delta", "Echo"]
    return {cat: random.randint(10, 100) for cat in categories}


def generate_line_data():
    """Generates random data for the line chart."""
    return {
        "Series 1": [(i, random.uniform(20, 40)) for i in range(10)],
        "Series 2": [(i, random.uniform(50, 70)) for i in range(10)],
    }


def generate_pie_data():
    """Generates random data for the pie chart."""
    return {
        "Product A": random.randint(5, 30),
        "Product B": random.randint(10, 40),
        "Product C": random.randint(20, 50),
    }


def generate_scatter_data():
    """Generates random data for the scatter plot."""
    return {
        "Cluster 1": [(random.uniform(0, 5), random.uniform(0, 5)) for _ in range(20)],
        "Cluster 2": [
            (random.uniform(5, 10), random.uniform(5, 10)) for _ in range(20)
        ],
    }


# --- Tab Creation Functions ---


def create_bar_chart_tab():
    """Creates the UI for the Bar Chart demo tab."""
    chart = ui.BarChart(data=generate_bar_data(), title="Sample Bar Chart")
    return ui.Column(
        props={"spacing": 10},
        children=[
            chart,
            ui.Button(
                "Randomize Data", on_click=lambda: chart.set_data(generate_bar_data())
            ),
        ],
    )


def create_line_chart_tab():
    """Creates the UI for the Line Chart demo tab."""
    chart = ui.LineChart(data=generate_line_data(), title="Sample Line Chart")
    return ui.Column(
        props={"spacing": 10},
        children=[
            chart,
            ui.Button(
                "Randomize Data", on_click=lambda: chart.set_data(generate_line_data())
            ),
        ],
    )


def create_pie_chart_tab():
    """Creates the UI for the Pie Chart demo tab."""
    chart = ui.PieChart(data=generate_pie_data(), title="Sample Pie Chart")
    return ui.Column(
        props={"spacing": 10},
        children=[
            chart,
            ui.Button(
                "Randomize Data", on_click=lambda: chart.set_data(generate_pie_data())
            ),
        ],
    )


def create_scatter_plot_tab():
    """Creates the UI for the Scatter Plot demo tab."""
    chart = ui.ScatterPlot(
        data=generate_scatter_data(),
        title="Sample Scatter Plot",
    )
    return ui.Column(
        props={
            "spacing": 10,
            # "background-color": "$secondary-color",
            # "color": "$secondary-text-color",
        },
        children=[
            chart,
            ui.Button(
                "Randomize Data",
                on_click=lambda: chart.set_data(generate_scatter_data()),
            ),
        ],
    )


# extras
def toggle_theme():
    # Access the theme manager via the 'themes' attribute on the style module
    current_theme = style.themes.get_active_theme_name()
    next_theme = "dark" if current_theme == "light" else "light"
    style.themes.set_theme(next_theme)


def show_mpl_plot():
    plt.style.use("cyberpunk")
    # mpl_style(dark=True)

    ### scatter plot
    # # get random data
    # data = generate_scatter_data()
    # # convert to dataframe
    # df = pd.DataFrame(data)

    # cluster_1 = pd.DataFrame(
    #     df["Cluster 1"].to_list(), columns=["X", "Y"], index=df.index
    # )
    # cluster_2 = pd.DataFrame(
    #     df["Cluster 2"].to_list(), columns=["X", "Y"], index=df.index
    # )
    # plt.scatter(x=cluster_1.X, y=cluster_1.Y)
    # plt.scatter(x=cluster_2.X, y=cluster_2.Y)

    # mplcyberpunk.make_scatter_glow()

    ### line graph
    plt.plot([1, 3, 9, 5, 2, 1, 1], marker="o")
    plt.plot([4, 5, 5, 7, 9, 8, 6], marker="o")
    plt.plot([8, 6, 7, 3], marker="o")
    plt.plot([9, 8, 6, 4, 5], marker="o")

    mplcyberpunk.make_lines_glow()
    # mplcyberpunk.add_glow_effects()

    plt.show()


# --- Main Application ---


# @winup.component
def App():
    """The main app uses a TabView to organize the chart demos."""

    style.themes.set_theme("dark")

    tabs = ui.TabView(
        tabs={
            "Bar Chart": create_bar_chart_tab(),
            "Line Chart": create_line_chart_tab(),
            "Pie Chart": create_pie_chart_tab(),
            "Scatter Plot": create_scatter_plot_tab(),
        }
    )

    layout = ui.Column(
        props={"spacing": 10, "margin": "20px"},
        children=[
            tabs,
            ui.Button("Toggle Theme", on_click=toggle_theme),
            ui.Button("MPL Plot", on_click=show_mpl_plot),
        ],
    )
    return layout


def run():
    winup.run(
        main_component_path=f"{this_module_name}:App",
        title="Graphing Widgets Demo",
        width=800,
        height=600,
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

# %%
