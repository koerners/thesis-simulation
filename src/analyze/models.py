import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

from pandas.core.frame import DataFrame
from analyze.colors import get_color_by_value
from simulation.utils.save_runs import create_dir

from analyze.utils.arrays import pad_array


def get_steps_data(data, value_to_excert):
    return data["steps"].apply(
        lambda x: np.array(
            list(filter(lambda y: y.get(value_to_excert) is not None, x))[0].get(
                value_to_excert
            )
        )
    )


def clear_figs():
    plt.figure().clear()
    plt.close("all")


def plot_value_over_time_by_feature(
    data: DataFrame, value_to_excert: str, feature: str = None, zoom: int = None
) -> None:
    plt.figure().clear()

    try:
        data[value_to_excert] = get_steps_data(data, value_to_excert)

        if feature is not None:
            unique_values = data[feature].unique()
            for value in unique_values:
                data_frame = data.loc[data[feature] == value]
                mean = np.mean(pad_array(np.array(data_frame[value_to_excert])), axis=0)
                if zoom is not None:
                    mean = mean[:zoom]
                plt.plot(mean, label=value, color=get_color_by_value(value))

        average = np.mean(pad_array(np.array(data[value_to_excert])), axis=0)

        if zoom is not None:
            average = average[:zoom]

        plt.plot(average, "--", label="average", color=get_color_by_value("average"))
        plt.xlabel("steps")
        plt.ylabel(value_to_excert)
        plt.legend()
        output = (
            f"{value_to_excert}/by_{feature}"
            if feature is not None
            else f"{value_to_excert}/average"
        )
        if zoom is not None:
            output = f"{output}_zoom_{zoom}"
        plt.savefig(create_dir(f"{output}.png"))

    except Exception as e:
        print(
            f'Error in plot_value_over_time_by_feature when processing "{value_to_excert}": {e}'
        )

    finally:
        clear_figs()


def _plot_distribution_over_time(
    data: DataFrame,
    value_to_excert: str,
    output_path: str = None,
    line=False,
    zoom=None,
) -> None:
    # pylint: disable=cell-var-from-loop

    plt.figure().clear()
    extracted = get_steps_data(data, value_to_excert)
    data[value_to_excert] = extracted
    data_frame = pd.DataFrame()

    possible = list(extracted[0][0])

    for pos in possible:
        data[pos] = data[value_to_excert].apply(
            lambda x: np.array([y.get(pos, 0) for y in x])
        )
        data_frame[pos] = np.mean(np.array(data[pos]), axis=0)

    if zoom is not None:
        data_frame = data_frame.head(n=zoom)
    if line is False:
        data_frame[possible].plot.area(
            stacked=True,
            color=[get_color_by_value(x) for x in data_frame[possible].columns],
        )

    else:
        data_frame[possible].plot.line(
            color=[get_color_by_value(x) for x in data_frame[possible].columns]
        )

    plt.xlabel("steps")
    plt.legend()
    plt.savefig(output_path)

    clear_figs()


def plot_distribution_over_time_by_feature(
    data: DataFrame,
    value_to_excert: str,
    feature: str = None,
    line=False,
    zoom: int = None,
) -> None:
    try:
        if feature not in data:
            return
        unique_values = data[feature].unique()
        for value in unique_values:
            data_frame = data.loc[data[feature] == value].copy(deep=True)
            path = (
                f"distribution_{value_to_excert}/{feature}_{value}"
                if line is False
                else f"{value_to_excert}/{feature}_{value}"
            )
            if zoom is not None:
                path += f"_zoom_{zoom}"
            _plot_distribution_over_time(
                data=data_frame.reset_index(),
                value_to_excert=value_to_excert,
                output_path=create_dir(f"{path}.png"),
                line=line,
                zoom=zoom,
            )
    except Exception as e:
        print(
            f'Error in plot_distribution_over_time_by_feature when processing "{value_to_excert}": {e}'
        )
    finally:
        clear_figs()


def plot_values_over_time(data: DataFrame, value_to_excert: str) -> None:
    plt.figure().clear()

    extracted = get_steps_data(data, value_to_excert)
    data[value_to_excert] = extracted
    data_frame = pd.DataFrame()
    try:
        possible = list(extracted[0][0])
        for pos in possible:
            # pylint: disable=cell-var-from-loop
            data[pos] = data[value_to_excert].apply(
                lambda x: np.array([y.get(pos, 0) for y in x])
            )
            data_frame[pos] = np.mean(np.array(data[pos]), axis=0)

        data_frame[possible].plot(
            color=[get_color_by_value(x) for x in data_frame[possible].columns]
        )

        plt.xlabel("steps")
        plt.legend()
        plt.savefig(create_dir(f"{value_to_excert}.png"))
    except Exception as exception:
        print(
            f'Error in plot_values_over_time when processing "{value_to_excert}": {exception}'
        )
    finally:
        clear_figs()


def plot_correlations(df: DataFrame) -> None:
    # plot correlation matrix for give pandas dataframe
    try:
        df["avg_food_distribution_factor"] = get_steps_data(df, "food_distribution").apply(
            lambda x: (
                (np.mean([y.get("below_median")
                 for y in x]) + 1) / (np.mean([y.get("above_median") for y in x]) + 1)
            )
        )
        df["avg_fitness_alt"] = get_steps_data(df, "trivers_values").apply(
            lambda x: np.mean([y.get("avg_fitness_alt") for y in x])
        )
        df["avg_fitness_non_alt"] = get_steps_data(df, "trivers_values").apply(
            lambda x: np.mean([y.get("avg_fitness_non_alt") for y in x])
        )
        df.drop(columns=["agent_limit"], inplace=True)
        corr = df.corr()

        fig = px.imshow(corr)
        fig.write_image(create_dir("correlations.png"))

    except Exception as e:
        print(f"Error in plot_correlations: {e}")
