
import matplotlib.pyplot as plt
import numpy as np

from analyze.utils.arrays import pad_array


def plot_population_growth(data, path, feature: str = None):
    if feature is not None:
        unique_values = data[feature].unique()
        for value in unique_values:
            df = data.loc[data[feature] == value]
            growth = np.mean(
                pad_array(np.array(df['agent_growth'])), axis=0)
            plt.plot(growth, label=value)

    average_agent_growth = np.mean(
        pad_array(np.array(data['agent_growth'])), axis=0)

    plt.plot(average_agent_growth, "--", label="Average")
    plt.title(f"Agent growth by {feature}") if feature is not None else plt.title(
        "Agent growth")
    plt.xlabel("Steps")
    plt.ylabel("Population")
    plt.legend()
    output = f'./out/{path}_by_{feature}.png' if feature is not None else f'./out/{path}.png'
    plt.savefig(output)
