from typing import Dict

from networkx.algorithms.approximation import average_clustering


def get_total_agent_count(self) -> int:
    return self.schedule.get_agent_count()


def get_experiment_id(self) -> int:
    return self.experiment_id


def get_steps_data(self) -> Dict:
    keep = ['total_agents', 'clustering', 'agent_types']
    return [{key: value}
            for (key, value) in self.datacollector.model_vars.items() if key in keep]


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
