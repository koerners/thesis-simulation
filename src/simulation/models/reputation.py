from simulation.agents.eating import EatingAgent
from simulation.agents.reputation import ReputationAgent
from simulation.agents.genuine import GenuineAgent
from simulation.models.altruism import AltruismModel


class ReputationModel(AltruismModel):
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

        self.average_reputation: float = 0

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
        )

    def step(self):
        self.average_reputation = self.__calculate_average_reputation()
        super().step()

    def add_agent(self):
        agent = self.random.choice([EatingAgent, GenuineAgent, ReputationAgent])
        agent(self)

    def __calculate_average_reputation(self) -> float:
        reputation_agents = list(
            filter(lambda x: isinstance(x, ReputationAgent), self.agents)
        )
        if len(reputation_agents) == 0:
            return 0
        return sum(agent.reputation for agent in reputation_agents) / len(
            reputation_agents
        )
