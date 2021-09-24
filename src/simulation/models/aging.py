

from simulation.agents.aging import AgingAgent
from simulation.models.base import BaseModel


class AgingModel(BaseModel):
    def __init__(self, num_agents, network_visualization_steps,
                 min_lifeexpectancy, max_lifeexpectancy):
        self.min_lifeexpectancy = min_lifeexpectancy
        self.max_lifeexpectancy = max_lifeexpectancy
        super().__init__(num_agents=num_agents,
                         network_visualization_steps=network_visualization_steps)

    def add_agent(self) -> None:
        AgingAgent(self, min_lifeexpectancy=self.min_lifeexpectancy,
                   max_lifeexpectancy=self.max_lifeexpectancy)
