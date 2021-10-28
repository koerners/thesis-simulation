from simulation.agents.eating import EatingAgent
from simulation.agents.hamilton import HamiltonAgent
from simulation.models.eating import EatingModel


class HamiltonModel(EatingModel):
    def __init__(
        self,
        num_agents,
        network_saving_steps,
        lifeexpectancy,
        genderless,
        agent_limit,
        run_id,
        finding_max,
        level_of_sacrifice,
        min_relationship,
        foodlimit_multiplicator=None,
        child_bearing_cost=0,
    ):
        self.level_of_sacrifice = level_of_sacrifice
        self.min_relationship = min_relationship

        super().__init__(
            num_agents=num_agents,
            network_saving_steps=network_saving_steps,
            lifeexpectancy=lifeexpectancy,
            run_id=run_id,
            genderless=genderless,
            agent_limit=agent_limit,
            finding_max=finding_max,
            foodlimit_multiplicator=foodlimit_multiplicator,
            child_bearing_cost=child_bearing_cost
        )

    def add_agent(self) -> None:
        agent = self.random.choice([EatingAgent, HamiltonAgent])
        agent(self)
