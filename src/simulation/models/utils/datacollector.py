from statistics import StatisticsError, median
from typing import Dict

from networkx.algorithms.approximation import average_clustering


def get_total_agent_count(self) -> int:
    return self.schedule.get_agent_count()


def get_experiment_id(self) -> int:
    return self.experiment_id


def get_seed(self) -> int:
    # pylint: disable=no-member protected-access
    return self._seed


def get_steps_data(self) -> Dict:
    keep = [
        "total_agents",
        "clustering",
        "agent_types",
        "food_distribution",
        "agent_groups",
    ]
    return [
        {key: value}
        for (key, value) in self.datacollector.model_vars.items()
        if key in keep
    ]


def get_current_network(self, step=10):
    """Returns the current network every 10 steps"""
    if self.schedule.steps % step == 0:
        return self.network
    return None


def get_network_clustering(self):
    try:
        return average_clustering(self.network.graph)
    except IndexError:
        return 0


def get_current_agent_types(self):
    agents = {}
    for agent in self.schedule.agents:
        agent_type = type(agent).__name__
        if agent_type in agents:
            agents[agent_type] += 1
            continue
        agents[agent_type] = 1
    return agents


def get_agent_groups(self):
    agents = {}
    for agent in self.schedule.agents:
        agent_group = agent.group
        if agent_group in agents:
            agents[agent_group] += 1
            continue
        agents[agent_group] = 1
    return agents


def get_current_food_distribution(self):

    below_average = 0
    above_average = 0

    try:
        food_distribution = [x.current_food for x in self.schedule.agents]
        mean = median(food_distribution)
        below_average = len(list(filter(lambda x: x < mean, food_distribution)))
        above_average = len(list(filter(lambda x: x > mean, food_distribution)))
    except StatisticsError:
        # no agents
        pass
    except AttributeError:
        pass

    return {"below_mean": below_average, "above_mean": above_average}
