import math

from simulation.agents.eating import EatingAgent
from simulation.models.reproduction import ReproductionModel


class EatingModel(ReproductionModel):
    def __init__(self, num_agents, network_saving_steps,
                 lifeexpectancy, genderless, agent_limit, run_id, foodlimit_multiplicator=None):
        self.foodlimit = (foodlimit_multiplicator *
                          num_agents) if foodlimit_multiplicator is not None else math.inf
        self.current_food = self.foodlimit
        super().__init__(num_agents=num_agents,
                         network_saving_steps=network_saving_steps,
                         lifeexpectancy=lifeexpectancy,
                         run_id=run_id,
                         genderless=genderless,
                         agent_limit=agent_limit,
                         )

    def add_agent(self) -> None:
        EatingAgent(self)

    def step(self) -> None:
        self.current_food = self.foodlimit
        super().step()
