from simulation.agents.culture import CultureAgent
from simulation.models.group import Group, GroupModel


class CultureGroup(Group):
    def __init__(self, group_id, group_culture):
        self.group_culture = group_culture  # val between 0 and 1
        super().__init__(group_id=group_id)  # A, B, C ...

    def agent_acted_altruistic(self):
        self.group_culture = max(self.group_culture + 0.01, 1)

    def agent_acted_non_altruistic(self):
        self.group_culture = min(0, self.group_culture - 0.01)


class CultureModel(GroupModel):
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

    def init_groups(self):
        self.groups = [CultureGroup("A", 0), CultureGroup("B", 0.5)]

    def add_agent(self) -> None:
        CultureAgent(self, group=self.random.choice(self.groups).group_id)

    def get_group_of_agent(self, agent):
        return list(filter(lambda g: g.group_id == agent.group, self.groups))[0]

    def agent_acted_altruistic(self, agent):
        group = self.get_group_of_agent(agent)
        group.agent_acted_altruistic()

    def agent_acted_non_altruistic(self, agent):
        group = self.get_group_of_agent(agent)
        group.agent_acted_non_altruistic()
