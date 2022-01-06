from mesa.batchrunner import BatchRunnerMP
from simulation.models.altruism import AltruismModel
from simulation.models.greenbeard import GreenBeardModel
from simulation.models.reputation import ReputationModel
from simulation.models.kinselection import KinSelectionModel
from simulation.models.group import GroupModel
from simulation.models.culture import CultureModel


from simulation.models.utils.datacollector import (
    get_experiment_id,
    get_seed,
    get_steps_data,
    get_total_agent_count,
)
from simulation.utils.commandline import Commandline
from simulation.utils.save_runs import pre_edit_run_data, save_to_pickle
from simulation.utils.time import get_current_timestring

RUN_ID = get_current_timestring()


# PARAMETERS
fixed_params = {"network_saving_steps": None, "run_id": RUN_ID}

variable_base_params = {"num_agents": [100]}

aging_model_params = {**variable_base_params, "lifeexpectancy": [(25, 35), (60, 70)]}

reproduction_model_params = {
    **aging_model_params,
    "genderless": [False],
    "agent_limit": [5000],
    "mutation_chance": [0, 0.05],
}

eating_model_params = {
    **reproduction_model_params,
    # will be multiplied by the amount of initial agents
    "foodlimit_multiplicator": [5],
    # maximum amount of food one agent can find per step
    "finding_max": [2, 3],
    # cost that has to be paid by BOTH parents
    "child_bearing_cost": [0, 2, 4, 6],  # float_range(0, 3, 0.5),
}

altruism_model_params = {
    **eating_model_params,
    # Percentage of food the agent is willing to sacrifice
    # 1.0 might leave the agent to starve without food
    # 0.x gives x percent to other agents but minimum 1 if the agent can afford it without starving
    "level_of_sacrifice": [0.2, 0.5, 0.8, 1.0],
}


greenbeard_model_params = {
    **altruism_model_params,
    "allow_fake_greenbeards": [True, False],
}

kin_selection_model_params = {
    **altruism_model_params,
    # minimmal relationship the agent has with the other agent to be willing to sacrifice for him
    "min_relationship": [1, 2, 3],
}

group_model_params = {
    **altruism_model_params,
    "group_number": [2, 4, 6],
    "migration_rate": [0.0, 0.05, 0.15],
}

# MODEL REPORTER
base_reporter = {
    "final_agents": get_total_agent_count,
    "experiment_id": get_experiment_id,
    "seed": get_seed,
}

extended_reporter = {"steps": get_steps_data}


MODELS = {
    "baseline": {
        "model": AltruismModel,
        "params": altruism_model_params,
    },
    "greenbeard": {
        "model": GreenBeardModel,
        "params": greenbeard_model_params,
    },
    "kinselection": {
        "model": KinSelectionModel,
        "params": kin_selection_model_params,
    },
    "group": {
        "model": GroupModel,
        "params": group_model_params,
    },
    "culture": {
        "model": CultureModel,
        "params": group_model_params,
    },
    "reputation": {
        "model": ReputationModel,
        "params": altruism_model_params,
    },
}


if __name__ == "__main__":
    commandline_args = Commandline()

    # BATCH RUNNER
    batch_run = BatchRunnerMP(
        model_cls=MODELS[commandline_args.model]["model"],
        nr_processes=commandline_args.nr_of_processes,
        variable_parameters=MODELS[commandline_args.model]["params"],
        fixed_parameters=fixed_params,
        iterations=commandline_args.iterations,
        max_steps=commandline_args.max_steps,
        model_reporters={
            **base_reporter,
            **extended_reporter,
        },
    )

    DONE = False
    while not DONE:
        try:
            batch_run.run_all()
            DONE = True
        # pylint: disable=broad-except
        except Exception as e:
            print(e)
            print("Retrying...")

    run_data = batch_run.get_model_vars_dataframe()
    run_data = pre_edit_run_data(run_data)

    print(run_data)
    save_to_pickle(run_data, f"{RUN_ID}-{batch_run.model_cls.__name__}/run_data.pkl")
