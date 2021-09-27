from typing import Dict


def get_total_agent_count(self) -> int:
    return self.schedule.get_agent_count()


def get_experiment_id(self) -> int:
    return self.experiment_id


def get_steps_data(self) -> Dict:
    keep = ['total_agents']
    return [{key: value} for (key, value) in self.datacollector.model_vars.items() if key in keep]


def get_current_network(self, step=10):
    """Returns the current network every 10 steps"""
    if self.schedule.steps % step == 0:
        return self.network
    return None
