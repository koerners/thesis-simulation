import pandas as pd

from analyze.models import plot_value_over_time_by_feature
from analyze.utils.files import get_run_data, get_saved_runs

ALL_RUNS = get_saved_runs()

all_run_data = pd.DataFrame()


if __name__ == '__main__':

    all_run_data = all_run_data.append(get_run_data(ALL_RUNS[-1]))

    print(all_run_data.head())

    plot_value_over_time_by_feature(
        all_run_data, "clustering", "foodlimit_multiplicator")

    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "finding_max")
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "genderless")
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "lifeexpectancy")
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "foodlimit_multiplicator")
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "child_bearing_cost")
