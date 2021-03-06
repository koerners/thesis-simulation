import math

from simulation.agents.eating import EatingAgent
from simulation.models.reproduction import ReproductionModel


class EatingModel(ReproductionModel):
    def __init__(
        self,
        num_agents,
        network_saving_steps,
        lifeexpectancy,
        genderless,
        agent_limit,
        run_id,
        finding_max,
        mutation_chance,
        foodlimit_multiplicator=None,
        child_bearing_cost=0,
    ):
        self.foodlimit: float = (
            (foodlimit_multiplicator * num_agents)
            if foodlimit_multiplicator is not None
            else math.inf
        )
        self.current_food: float = self.foodlimit
        self.finding_max: int = finding_max
        self.child_bearing_cost: float = child_bearing_cost

        super().__init__(
            num_agents=num_agents,
            network_saving_steps=network_saving_steps,
            lifeexpectancy=lifeexpectancy,
            run_id=run_id,
            genderless=genderless,
            agent_limit=agent_limit,
            mutation_chance=mutation_chance,
        )

    def add_agent(self):
        EatingAgent(self)

    def step(self):
        self.current_food = self.foodlimit
        super().step()
        for agent in self.schedule.agents:
            if agent.current_food < 1:
                agent.die()
