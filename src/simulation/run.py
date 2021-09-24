from mesa.batchrunner import BatchRunner
from simulation.models.reproduction import ReproductionModel
from simulation.models.utils.datacollector import get_experiment_id, get_total_agent_count

fixed_params = {"network_visualization_steps": None}


variable_params = {"num_agents": [100]}

aging_model_params = {**variable_params,
                      'min_lifeexpectancy': [60], 'max_lifeexpectancy': [100]}


batch_run = BatchRunner(ReproductionModel,
                        aging_model_params,
                        fixed_params,
                        iterations=1,
                        max_steps=500,
                        model_reporters={'total_agents': get_total_agent_count,
                                         'experiment_id': get_experiment_id})

batch_run.run_all()
run_data = batch_run.get_model_vars_dataframe()
print(run_data)
