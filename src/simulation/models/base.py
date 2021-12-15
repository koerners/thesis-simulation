from typing import List
from mesa import Model
from mesa.agent import Agent
from mesa.datacollection import DataCollector
from mesa.time import BaseScheduler, RandomActivation
from simulation.agents.base import BaseAgent
from simulation.models.utils.datacollector import (
    get_agent_groups,
    get_agent_neighbors_by_group,
    get_agent_neighbors_by_type,
    get_average_reputation,
    get_current_agent_types,
    get_current_food_distribution,
    get_experiment_id,
    get_groups_culture,
    get_seed,
    get_steps_data,
    get_total_agent_count,
    get_trivers_values,
)
from simulation.networks.base import BaseNetwork


class BaseModel(Model):
    def __init__(self, num_agents, network_saving_steps, run_id):
        super().__init__()
        self.run_id: str = run_id
        self.num_agents: int = num_agents
        self.schedule: BaseScheduler = self.init_scheduler()
        self.running: bool = True
        self.network: BaseNetwork = self.init_social_network()
        self.network_saving_steps: int = network_saving_steps
        self.experiment_id: str = hash(self)
        self.datacollector: DataCollector = DataCollector(
            {
                "total_agents": get_total_agent_count,
                "experiment_id": get_experiment_id,
                "steps": get_steps_data,
                # "clustering": get_network_clustering,
                "agent_types": get_current_agent_types,
                "agent_neighbors_by_type": get_agent_neighbors_by_type,
                "agent_neighbors_by_group": get_agent_neighbors_by_group,
                "food_distribution": get_current_food_distribution,
                "seed": get_seed,
                "agent_groups": get_agent_groups,
                "average_reputation": get_average_reputation,
                "groups_culture": get_groups_culture,
                "trivers_values": get_trivers_values,
            }
        )

        # Create agents
        for _ in range(self.num_agents):
            self.add_agent()

    def step(self):
        self.datacollector.collect(self)
        if (
            self.network_saving_steps is not None
            and self.schedule.steps % self.network_saving_steps == 0
        ):
            self.network.save(
                f"{self.run_id}/{self.experiment_id}/Step_{self.schedule.steps}.pkl"
            )

        self.schedule.step()

        agent_keys = [x.unique_id for x in self.schedule.agents]
        self.network.remove_duplicates(agent_keys)

    def add_agent(self):
        BaseAgent(self)

    def get_agent_by_id(self, agent_id) -> Agent:
        to_return = None
        agent = list(filter(lambda x: x.unique_id == agent_id, self.schedule.agents))
        try:
            to_return = agent[0]
        except IndexError:
            pass

        return to_return

    def get_agents_by_id(self, agent_ids: List[int]) -> List[Agent]:
        return list(filter(lambda x: x.unique_id in agent_ids, self.schedule.agents))

    def get_neighbors(self, agent) -> List[Agent]:
        agent_ids = self.network.get_neighbors_ids(agent)
        agents = self.get_agents_by_id(agent_ids)
        return agents

    def init_scheduler(self) -> BaseScheduler:
        return RandomActivation(self)

    @staticmethod
    def init_social_network() -> BaseNetwork:
        return BaseNetwork()

    @property
    def agents(self) -> List[Agent]:
        return self.schedule.agents
