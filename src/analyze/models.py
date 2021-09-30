
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.frame import DataFrame
import pandas as pd
from analyze.utils.arrays import pad_array


def get_steps_data(data, value_to_excert):
    return data['steps'].apply(
        lambda x:
        np.array(list(filter(lambda y:
                             y.get(value_to_excert) is not None, x))[0].get(value_to_excert)))


def plot_value_over_time_by_feature(data: DataFrame,
                                    value_to_excert: str,
                                    feature: str = None) -> None:
    plt.figure().clear()

    data[value_to_excert] = get_steps_data(data, value_to_excert)

    if feature is not None:
        unique_values = data[feature].unique()
        for value in unique_values:
            data_frame = data.loc[data[feature] == value]
            mean = np.mean(
                pad_array(np.array(data_frame[value_to_excert])), axis=0)
            plt.plot(mean, label=value)

    average = np.mean(
        pad_array(np.array(data[value_to_excert])), axis=0)

    plt.plot(average, "--", label="average")
    title = f"{value_to_excert} by {feature}" if feature is not None else plt.title(
        "f{value_to_excert}")
    plt.title(title)
    plt.xlabel("steps")
    plt.ylabel(value_to_excert)
    plt.legend()
    output = f'./out/{value_to_excert}_by_{feature}.png' \
        if feature is not None else f'./out/{value_to_excert}.png'
    plt.savefig(output)


def plot_distribution_over_time(data: DataFrame,
                                value_to_excert: str,
                                feature: str = None) -> None:
    # pylint: disable=cell-var-from-loop

    plt.figure().clear()

    extracted = get_steps_data(data, value_to_excert)
    data[value_to_excert] = extracted
    data_frame = pd.DataFrame()

    possible = list(extracted[0][0])

    for pos in possible:
        data[pos] = data[value_to_excert].apply(
            lambda x: np.array([y.get(pos, 0) for y in x]))
        data_frame[pos] = np.mean(np.array(data[pos]), axis=0)

    data_frame[possible].plot.area(stacked=True)
    title = f"distribution of{value_to_excert} by {feature}" if \
        feature is not None else f"distribution of {value_to_excert}"
    plt.title(title)
    plt.xlabel("steps")
    plt.legend()
    output = f'./out/distribution__{value_to_excert}_by_{feature}.png' \
        if feature is not None else f'./out/distribution__{value_to_excert}.png'
    plt.savefig(output)
