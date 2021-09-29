import pandas as pd
import numpy as np

from analyze.models import plot_population_growth
from analyze.utils.files import get_run_data, get_saved_runs

ALL_RUNS = get_saved_runs()

all_run_data = pd.DataFrame()


if __name__ == '__main__':

    all_run_data = all_run_data.append(get_run_data(ALL_RUNS[-1]))

    all_run_data['agent_growth'] = all_run_data['steps'].apply(
        lambda x: np.array(x[0].get("total_agents")))

    print(all_run_data.head())

    plot_population_growth(all_run_data, "agent_growth", "genderless")
    plot_population_growth(all_run_data, "agent_growth", "lifeexpectancy")
    plot_population_growth(all_run_data, "agent_growth",
                           "foodlimit_multiplicator")
