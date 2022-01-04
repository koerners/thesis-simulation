import pandas as pd

from analyze.models import (
    plot_correlations,
    plot_distribution_over_time,
    plot_distribution_over_time_by_feature,
    plot_value_over_time_by_feature,
    plot_values_over_time,
)
from analyze.utils.files import get_run_data, get_saved_runs
from simulation.utils.directory import create_dir


def analyze(all_run_data):

    # CORRELATIONS

    plot_correlations(
        all_run_data,
        drop_columns=[
            "agent_limit",
            "foodlimit_multiplicator",
            "num_agents",
            "genderless",
            "experiment_id",
        ],
    )

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
        all_run_data, "food_distribution_by_type", "level_of_sacrifice", line=True, zoom=200
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
    plot_distribution_over_time_by_feature(
        all_run_data, "food_distribution_by_type", "finding_max", line=True
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
        all_run_data, "agent_types", "child_bearing_cost", zoom=200
    )
    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "lifeexpectancy"
    )

    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "level_of_sacrifice"
    )

    plot_distribution_over_time_by_feature(
        all_run_data, "agent_types", "level_of_sacrifice", zoom=200
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
    plot_distribution_over_time_by_feature(all_run_data, "agent_types", "finding_max")
    plot_distribution_over_time_by_feature(all_run_data, "agent_types", "mutation_chance")
    plot_distribution_over_time(
        all_run_data, "agent_types", output_path=create_dir("agent_types_average.png"), line=True)

    # TOTAL AGENTS

    plot_value_over_time_by_feature(all_run_data, "total_agents", "finding_max")
    plot_value_over_time_by_feature(all_run_data, "total_agents", "genderless")
    plot_value_over_time_by_feature(all_run_data, "total_agents", "lifeexpectancy")
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "foodlimit_multiplicator"
    )
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "foodlimit_multiplicator", zoom=200
    )
    plot_value_over_time_by_feature(
        all_run_data, "total_agents", "allow_fake_greenbeards", zoom=200
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
    plot_distribution_over_time_by_feature(
        all_run_data, "trivers_values", "mutation_chance", line=True
    )


if __name__ == "__main__":

    ALL_RUNS = get_saved_runs()

    data = pd.DataFrame()

    data = data.append(get_run_data(ALL_RUNS[-1]))

    print(data)

    analyze(data)
