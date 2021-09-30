
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.frame import DataFrame

from analyze.utils.arrays import pad_array


def plot_value_over_time_by_feature(data: DataFrame,
                                    value_to_excert: str,
                                    feature: str = None) -> None:
    plt.figure().clear()

    data[value_to_excert] = data['steps'].apply(
        lambda x:
        np.array(list(filter(lambda y:
                             y.get(value_to_excert) is not None, x))[0].get(value_to_excert)))

    if feature is not None:
        unique_values = data[feature].unique()
        for value in unique_values:
            data_frame = data.loc[data[feature] == value]
            growth = np.mean(
                pad_array(np.array(data_frame[value_to_excert])), axis=0)
            plt.plot(growth, label=value)

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
