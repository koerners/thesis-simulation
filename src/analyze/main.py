import pandas as pd

from analyze.models import (
    plot_correlations,
    plot_distribution_over_time_by_feature,
    plot_value_over_time_by_feature,
    plot_values_over_time,
)
from analyze.utils.files import get_run_data, get_saved_runs

ALL_RUNS = get_saved_runs()

all_run_data = pd.DataFrame()


if __name__ == "__main__":

    all_run_data = all_run_data.append(get_run_data(ALL_RUNS[-1]))

    print(all_run_data)

    # CORRELATIONS

    plot_correlations(all_run_data)

    # FOODDISTRIBUTION

    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution", "child_bearing_cost"
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution", "lifeexpectancy"
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution", "foodlimit_multiplicator"
    )

    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution_by_type", "child_bearing_cost", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution_by_type", "level_of_sacrifice", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution_by_type", "lifeexpectancy", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution_by_type", "foodlimit_multiplicator", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution_by_type", "allow_fake_greenbeards", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution_by_type", "migration_rate", line=True
    )

    # NEIGHBORS

    plot_values_over_time(all_run_data, "agent_neighbors_by_group")

    plot_values_over_time(all_run_data, "agent_neighbors_by_type")
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_neighbors_by_type", "lifeexpectancy", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_neighbors_by_type", "level_of_sacrifice", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_neighbors_by_type", "allow_fake_greenbeards", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_neighbors_by_type", "migration_rate", line=True
    )

    # AGENT TYPES
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "child_bearing_cost"
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "child_bearing_cost", zoom=1000
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "lifeexpectancy"
    )

    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "level_of_sacrifice"
    )

    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "level_of_sacrifice", zoom=1000
    )

    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "min_relationship"
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "foodlimit_multiplicator"
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "allow_fake_greenbeards"
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "migration_rate"
    )

    # TOTAL AGENTS

    plot_value_over_time_by_feature(all_run_data, "total_agents", "finding_max")
    plot_value_over_time_by_feature(all_run_data, "total_agents", "genderless")
    plot_value_over_time_by_feature(all_run_data, "total_agents", "lifeexpectancy")
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "foodlimit_multiplicator"
    )
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "foodlimit_multiplicator", zoom=1000
    )
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "allow_fake_greenbeards", zoom=1000
    )
    plot_value_over_time_by_feature(all_run_data, "total_agents", "child_bearing_cost")
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "allow_fake_greenbeards"
    )
    plot_value_over_time_by_feature(all_run_data, "total_agents", "migration_rate")

    # GROUPS AND CULTURE

    plot_distribution_over_time_by_feature(all_run_data, "agent_groups", "finding_max")
    plot_distribution_over_time_by_feature(all_run_data, "agent_groups", "group_number")

    plot_distribution_over_time_by_feature(
        all_run_data, "groups_culture", "lifeexpectancy", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "groups_culture", "level_of_sacrifice", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "groups_culture", "group_number", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "groups_culture", "migration_rate", line=True
    )
    # REPUTATION

    plot_value_over_time_by_feature(all_run_data, "average_reputation")
    plot_value_over_time_by_feature(
        all_run_data, "average_reputation", "lifeexpectancy"
    )
    plot_value_over_time_by_feature(
        all_run_data, "average_reputation", "level_of_sacrifice"
    )

    # TRIVERS

    plot_distribution_over_time_by_feature(
        all_run_data, "trivers_values", "child_bearing_cost", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "trivers_values", "lifeexpectancy", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "trivers_values", "level_of_sacrifice", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "trivers_values", "allow_fake_greenbeards", line=True
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "trivers_values", "migration_rate", line=True
    )
