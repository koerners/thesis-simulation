from simulation.agents.group import GroupAgent
from simulation.helper.groups import Group
from simulation.models.altruism import AltruismModel


class GroupModel(AltruismModel):
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

        self.init_groups()

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

    def add_agent(self) -> None:
        GroupAgent(self, group=self.random.choice(self.groups).group_id)

    def get_group_of_agent(self, agent):
        return list(filter(lambda g: g.group_id == agent.group, self.groups))[0]

    def init_groups(self):
        self.groups = [Group("A"), Group("B")]
