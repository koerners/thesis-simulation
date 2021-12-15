import matplotlib.pyplot as plt
import numpy as np
from pandas.core.frame import DataFrame
import pandas as pd
from analyze.utils.arrays import pad_array
from simulation.utils.save_runs import create_dir

import plotly.express as px

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
                plt.plot(mean, label=value)

        average = np.mean(pad_array(np.array(data[value_to_excert])), axis=0)

        plt.plot(average, "--", label="average")
        title = (
            f"{value_to_excert} by {feature}"
            if feature is not None
            else plt.title("f{value_to_excert}")
        )
        plt.title(title)
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
    data: DataFrame, value_to_excert: str, name: str = None, output_path: str = None
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

    data_frame[possible].plot.area(stacked=True)
    title = (
        f"distribution of {value_to_excert} by {name}"
        if name is not None
        else f"distribution of {value_to_excert}"
    )
    plt.title(title)
    plt.xlabel("steps")
    plt.legend()
    plt.savefig(output_path)

    clear_figs()


def plot_distribution_over_time_by_feature(
    data: DataFrame, value_to_excert: str, feature: str = None
) -> None:
    if feature not in data:
        return
    unique_values = data[feature].unique()
    for value in unique_values:
        data_frame = data.loc[data[feature] == value].copy(deep=True)
        _plot_distribution_over_time(
            data=data_frame.reset_index(),
            value_to_excert=value_to_excert,
            name=f"{feature}_{value}",
            output_path=create_dir(
                f"distribution_{value_to_excert}/{feature}_{value}.png"
            ),
        )

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

        data_frame[possible].plot()
        title = f"{value_to_excert}"
        plt.title(title)
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
    df['total_agents'] = get_steps_data(
        df, "total_agents").apply(lambda x: x[-1])
    df['food_distribution_factor'] = get_steps_data(
        df, "food_distribution").apply(lambda x: ((x[-1].get("below_mean")+1)/(x[-1].get("above_mean")+1)))
    df['avg_fitness_alt'] = get_steps_data(
        df, "trivers_values").apply(lambda x: x[-1].get("avg_fitness_alt"))
    df['avg_fitness_non_alt'] = get_steps_data(
        df, "trivers_values").apply(lambda x: x[-1].get("avg_fitness_non_alt"))
    print(df)
    corr = df.corr()
    print(corr)

    fig = px.imshow(corr)
    fig.write_image(create_dir("correlations.png"))
