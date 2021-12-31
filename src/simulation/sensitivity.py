from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np

from simulation.models.altruism import AltruismModel

problem = {
    "num_vars": 4,
    "names": [
        "finding_max",
        "level_of_sacrifice",
        "foodlimit_multiplicator",
        "child_bearing_cost",
    ],
    "bounds": [[0, 10], [0, 1], [0, 10], [0, 10]],
}


def evaluate_model(params):
    model = AltruismModel(
        agent_limit=1000,
        network_saving_steps=None,
        run_id="",
        num_agents=100,
        lifeexpectancy=(25, 35),
        genderless=False,
        finding_max=int(params[0]),
        level_of_sacrifice=int(params[1]),
        foodlimit_multiplicator=int(params[2]),
        child_bearing_cost=int(params[3]),
    )

    for _ in range(10):
        model.step()
    data_frame = model.datacollector.get_model_vars_dataframe().iloc[-1]["total_agents"]
    return data_frame


param_values = saltelli.sample(problem, 1024, calc_second_order=False)
param_values[:, 0] = np.round(param_values[:, 0], 0)

param_values = np.unique(param_values, axis=0)

Y = np.zeros([param_values.shape[0]])
print(f"Running {param_values.shape[0]} simulations")
for i, X in enumerate(param_values):
    Y[i] = evaluate_model(X)

Si = sobol.analyze(problem, Y)


print(Si)
