import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from palettable.cartocolors.qualitative import Prism_10
from palettable.cartocolors.qualitative import Vivid_10
from pandas.core.frame import DataFrame
from simulation.utils.save_runs import create_dir

from analyze.utils.arrays import pad_array

# https://jiffyclub.github.io/palettable/
color_pallet = Prism_10.mpl_colors

COLOR_MAP = {
    # Agents
    "GroupAgent": color_pallet[1],
    "CultureAgent": color_pallet[2],
    "AltruismAgent": color_pallet[3],
    "UnconditionalAgent": color_pallet[4],
    "GreenbeardAgent": color_pallet[6],
    "ReputationAgent": color_pallet[7],
    "EatingAgent": color_pallet[8],
    "KinSelectionAgent": color_pallet[9],
    # Statistics
    "below_median": color_pallet[2],
    "above_median": color_pallet[-1],
    "average": color_pallet[5],
    "avg_fitness_alt": color_pallet[2],
    "avg_fitness_non_alt": color_pallet[-1],
    # Numbers
    "0": color_pallet[0],
    "1": color_pallet[1],
    "2": color_pallet[2],
    "3": color_pallet[3],
    "4": color_pallet[4],
    "5": color_pallet[6],
    "6": color_pallet[7],
    "7": color_pallet[8],
    "8": color_pallet[9],
    # Boolean
    "True": color_pallet[2],
    "False": color_pallet[-1],
}


def get_color_by_value(value):
    return COLOR_MAP.get(str(value), random.choice(Vivid_10.mpl_colors))


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
    data: DataFrame, value_to_excert: str, feature: str = None
) -> None:
    plt.figure().clear()

    try:
        data[value_to_excert] = get_steps_data(data, value_to_excert)

        if feature is not None:
            unique_values = data[feature].unique()
            for value in unique_values:
                data_frame = data.loc[data[feature] == value]
                mean = np.mean(pad_array(np.array(data_frame[value_to_excert])), axis=0)
                plt.plot(mean, label=value, color=get_color_by_value(value))

        average = np.mean(pad_array(np.array(data[value_to_excert])), axis=0)

        plt.plot(average, "--", label="average", color=get_color_by_value("average"))
        plt.xlabel("steps")
        plt.ylabel(value_to_excert)
        plt.legend()
        output = (
            f"{value_to_excert}/by_{feature}.png"
            if feature is not None
            else f"{value_to_excert}/average.png"
        )
        plt.savefig(create_dir(output))

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
    data: DataFrame, value_to_excert: str, feature: str = None, line=False
) -> None:
    try:
        if feature not in data:
            return
        unique_values = data[feature].unique()
        for value in unique_values:
            data_frame = data.loc[data[feature] == value].copy(deep=True)
            path = (
                f"distribution_{value_to_excert}/{feature}_{value}.png"
                if line is False
                else f"{value_to_excert}/{feature}_{value}.png"
            )
            _plot_distribution_over_time(
                data=data_frame.reset_index(),
                value_to_excert=value_to_excert,
                output_path=create_dir(path),
                line=line,
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
        df["total_agents"] = get_steps_data(df, "total_agents").apply(lambda x: x[-1])
        df["food_distribution_factor"] = get_steps_data(df, "food_distribution").apply(
            lambda x: (
                (x[-1].get("below_median") + 1) / (x[-1].get("above_median") + 1)
            )
        )
        df["avg_fitness_alt"] = get_steps_data(df, "trivers_values").apply(
            lambda x: x[-1].get("avg_fitness_alt")
        )
        df["avg_fitness_non_alt"] = get_steps_data(df, "trivers_values").apply(
            lambda x: x[-1].get("avg_fitness_non_alt")
        )

        corr = df.corr()

        fig = px.imshow(corr)
        fig.write_image(create_dir("correlations.png"))

    except Exception as e:
        print(f"Error in plot_correlations: {e}")
