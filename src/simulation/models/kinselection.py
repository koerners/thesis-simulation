from simulation.agents.eating import EatingAgent
from simulation.agents.unconditional import UnconditionalAgent
from simulation.agents.kinselection import KinSelectionAgent
from simulation.models.altruism import AltruismModel


class KinSelectionModel(AltruismModel):
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
        mutation_chance,
        foodlimit_multiplicator=None,
        child_bearing_cost=0,
    ):
        self.min_relationship: int = min_relationship

        super().__init__(
            num_agents=num_agents,
            network_saving_steps=network_saving_steps,
            lifeexpectancy=lifeexpectancy,
            run_id=run_id,
            genderless=genderless,
            agent_limit=agent_limit,
            finding_max=finding_max,
            foodlimit_multiplicator=foodlimit_multiplicator,
            child_bearing_cost=child_bearing_cost,
            level_of_sacrifice=level_of_sacrifice,
            mutation_chance=mutation_chance,
        )

    def add_agent(self):
        agent = self.random.choice([EatingAgent, UnconditionalAgent, KinSelectionAgent])
        agent(self)
