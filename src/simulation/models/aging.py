from simulation.agents.aging import AgingAgent
from simulation.models.base import BaseModel


class AgingModel(BaseModel):
    def __init__(self, num_agents, network_saving_steps, lifeexpectancy, run_id):
        self.lifeexpectancy = lifeexpectancy
        super().__init__(
            num_agents=num_agents,
            network_saving_steps=network_saving_steps,
            run_id=run_id,
        )

    def step(self):
        super().step()
        for agent in self.schedule.agents:
            if agent.life_expectancy < agent.age:
                agent.die()

    def add_agent(self):
        AgingAgent(self)
