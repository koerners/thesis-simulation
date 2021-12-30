from simulation.agents.eating import EatingAgent
from simulation.agents.greenbeard import GreenBeardAgent
from simulation.agents.greenbeard_fake import FakeGreenBeardAgent
from simulation.models.altruism import AltruismModel
from simulation.agents.unconditional import UnconditionalAgent


class GreenBeardModel(AltruismModel):
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
        allow_fake_greenbeards,
        foodlimit_multiplicator=None,
        child_bearing_cost=0,
    ):
        self.allow_fake_greenbeards: bool = allow_fake_greenbeards

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

    def add_agent(self):
        possible_agents = [EatingAgent, UnconditionalAgent, GreenBeardAgent]
        if self.allow_fake_greenbeards:
            possible_agents.append(FakeGreenBeardAgent)
        agent = self.random.choice(possible_agents)
        agent(self)
