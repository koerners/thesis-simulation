from mesa.batchrunner import BatchRunnerMP
from simulation.models.reproduction import ReproductionModel
from simulation.models.utils.datacollector import \
    get_data_collector, get_experiment_id, get_total_agent_count
from simulation.utils.save_runs import pre_edit_run_data, save_to_pickle
from simulation.utils.time import get_current_timestring

RUN_ID = get_current_timestring()


# PARAMETERS
fixed_params = {"network_visualization_steps": None,
                'run_id': RUN_ID}

variable_base_params = {"num_agents": [10]}

aging_model_params = {**variable_base_params,
                      'min_lifeexpectancy': [30],
                      'max_lifeexpectancy': [50]}

reproduction_model_params = {**aging_model_params,
                             'genderless': [True, False],
                             'agent_limit': [5000]}

# MODEL REPORTER
base_reporter = {'total_agents': get_total_agent_count,
                 'experiment_id': get_experiment_id}

extended_reporter = {'datacollector': get_data_collector}


# BATCH RUNNER
batch_run = BatchRunnerMP(model_cls=ReproductionModel,
                          nr_processes=None,
                          variable_parameters=reproduction_model_params,
                          fixed_parameters=fixed_params,
                          iterations=1,
                          max_steps=50,
                          model_reporters={
                              **base_reporter, **extended_reporter}
                          )

batch_run.run_all()

run_data = batch_run.get_model_vars_dataframe()
run_data = pre_edit_run_data(run_data)

print(run_data.head())
save_to_pickle(run_data, f"{RUN_ID}/run_data.pkl")
