from mesa.batchrunner import BatchRunner
from models.base import BaseModel

fixed_params = {}
variable_params = {"N": [1000]}

batch_run = BatchRunner(BaseModel,
                        variable_params,
                        fixed_params,
                        iterations=1,
                        max_steps=100,
                        model_reporters={})

batch_run.run_all()
