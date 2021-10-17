from mesa import Model
from mesa.datacollection import DataCollector
from mesa.time import RandomActivation
from simulation.agents.base import BaseAgent
from simulation.models.utils.datacollector import (
    get_current_agent_types,
    get_experiment_id,
    get_network_clustering,
    get_steps_data,
    get_total_agent_count)
from simulation.networks.base import BaseNetwork


class BaseModel(Model):
    def __init__(self, num_agents, network_saving_steps, run_id):
        super().__init__()
        self.run_id = run_id
        self.num_agents = num_agents
        self.schedule = self.init_scheduler()
        self.running = True
        self.network = self.init_social_network()
        self.network_saving_steps = network_saving_steps
        self.experiment_id = hash(self)
        self.datacollector = DataCollector(
            {'total_agents': get_total_agent_count,
             'experiment_id': get_experiment_id,
             'steps': get_steps_data,
             'clustering': get_network_clustering,
             'agent_types': get_current_agent_types
             }
        )

        # Create agents
        for _ in range(self.num_agents):
            self.add_agent()

    def step(self) -> None:
        self.datacollector.collect(self)
        if self.network_saving_steps is not None and \
                self.schedule.steps % self.network_saving_steps == 0:
            self.network.save(
                f"{self.run_id}/{self.experiment_id}/Step_{self.schedule.steps}.pkl")
        self.schedule.step()

    def add_agent(self) -> None:
        BaseAgent(self)

    def init_scheduler(self) -> RandomActivation:
        return RandomActivation(self)

    @ staticmethod
    def init_social_network() -> BaseNetwork:
        return BaseNetwork()
