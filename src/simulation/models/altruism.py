from simulation.agents.eating import EatingAgent
from simulation.models.eating import EatingModel
from simulation.agents.unconditional import UnconditionalAgent


class AltruismModel(EatingModel):
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
        foodlimit_multiplicator=None,
        child_bearing_cost=0,
    ):
        self.level_of_sacrifice: float = level_of_sacrifice
        self._altruists_benefits: int = 0  # For statistics
        self._non_altruists_benefits: int = 0  # For statistics
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
        )

    def add_agent(self):
        agent = self.random.choice([EatingAgent, UnconditionalAgent])
        agent(self)

    def altruistic_action_happend(self, receiver):
        if receiver.is_altruist:
            self._altruists_benefits += 1
        else:
            self._non_altruists_benefits += 1

    def reset_benefits(self):
        self._altruists_benefits = 0
        self._non_altruists_benefits = 0

    @property
    def benefits(self):
        return (self._altruists_benefits, self._non_altruists_benefits)
