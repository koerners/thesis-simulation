import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from analyze.utils.arrays import pad_array
from analyze.utils.files import get_run_data, get_saved_runs

ALL_RUNS = get_saved_runs()

all_run_data = pd.DataFrame()


def plot_population_growth(data, path):
    average_agent_growth = np.mean(
        pad_array(np.array(data['agent_growth'])), axis=0)

    plt.plot(average_agent_growth, label="Average")
    plt.title("Agent growth")
    plt.xlabel("Steps")
    plt.ylabel("Population")
    plt.legend()
    plt.savefig(f'./out/{path}.png')


if __name__ == '__main__':

    for run in ALL_RUNS:
        run_data = get_run_data(run)
        all_run_data = all_run_data.append(run_data)

    all_run_data['agent_growth'] = all_run_data['steps'].apply(
        lambda x: np.array(x[0].get("total_agents")))

    print(all_run_data.head())

    plot_population_growth(all_run_data, "average_agent_growth")
