from mesa.batchrunner import BatchRunnerMP

from simulation.models.eating import EatingModel
from simulation.models.utils.datacollector import (get_experiment_id,
                                                   get_steps_data,
                                                   get_total_agent_count)
from simulation.utils.commandline import Commandline
from simulation.utils.save_runs import pre_edit_run_data, save_to_pickle
from simulation.utils.time import get_current_timestring

RUN_ID = get_current_timestring()


# PARAMETERS
fixed_params = {"network_saving_steps": None,
                'run_id': RUN_ID}

variable_base_params = {"num_agents": [50]}

aging_model_params = {**variable_base_params,
                      'lifeexpectancy': [(30, 40)]}

reproduction_model_params = {**aging_model_params,
                             'genderless': [False],
                             'agent_limit': [500]}

eating_mode_params = {**reproduction_model_params,
                      # will be multiplied by the amount of initial agents
                      'foodlimit_multiplicator': [10],
                      # maximum amount of food one agent can find per step
                      'finding_max': range(2, 4),
                      'child_bearing_cost': range(0, 4)
                      }


# MODEL REPORTER
base_reporter = {'final_agents': get_total_agent_count,
                 'experiment_id': get_experiment_id}

extended_reporter = {'steps': get_steps_data}


if __name__ == "__main__":
    commandline_args = Commandline()

    # BATCH RUNNER
    batch_run = BatchRunnerMP(model_cls=EatingModel,
                              nr_processes=commandline_args.nr_of_processes,
                              variable_parameters=eating_mode_params,
                              fixed_parameters=fixed_params,
                              iterations=commandline_args.iterations,
                              max_steps=commandline_args.max_steps,
                              model_reporters={
                                  **base_reporter,
                                  **extended_reporter,
                              }
                              )

    batch_run.run_all()

    run_data = batch_run.get_model_vars_dataframe()
    run_data = pre_edit_run_data(run_data)

    print(run_data)
    save_to_pickle(run_data, f"{RUN_ID}/run_data.pkl")
