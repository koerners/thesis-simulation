import pandas as pd
import numpy as np

from analyze.models import plot_population_growth
from analyze.utils.files import get_run_data, get_saved_runs

ALL_RUNS = get_saved_runs()

all_run_data = pd.DataFrame()


if __name__ == '__main__':

    for run in ALL_RUNS:
        run_data = get_run_data(run)
        all_run_data = all_run_data.append(run_data)

    all_run_data['agent_growth'] = all_run_data['steps'].apply(
        lambda x: np.array(x[0].get("total_agents")))

    print(all_run_data.head())

    plot_population_growth(all_run_data, "agent_growth", "genderless")
