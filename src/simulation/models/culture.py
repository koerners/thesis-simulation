from typing import List
from simulation.agents.culture import CultureAgent
from simulation.helper.groups import CultureGroup, Group
from simulation.models.group import GroupModel


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
        self.groups: List[CultureGroup] = [
            CultureGroup("A", 0.25),
            CultureGroup("B", 0.5),
            CultureGroup("C", 0.75),
            CultureGroup("D", 1),
        ]

    def add_agent(self):
        CultureAgent(self, group=self.random.choice(self.groups).group_id)

    def get_group_of_agent(self, agent) -> Group:
        return list(filter(lambda g: g.group_id == agent.group, self.groups))[0]

    def agent_acted_altruistic(self, agent):
        group = self.get_group_of_agent(agent)
        group.agent_acted_altruistic()

    def agent_acted_non_altruistic(self, agent):
        group = self.get_group_of_agent(agent)
        group.agent_acted_non_altruistic()
