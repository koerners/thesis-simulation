import string
from typing import List

from simulation.agents.eating import EatingAgent
from simulation.agents.unconditional import UnconditionalAgent
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
        group_number,
        migration_rate,
        mutation_chance,
        foodlimit_multiplicator=None,
        child_bearing_cost=0,
    ):

        self.init_groups(group_number)
        self.migration_rate = migration_rate

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
        possible_agents = [EatingAgent, UnconditionalAgent, GroupAgent]
        agent = self.random.choice(possible_agents)
        if agent == GroupAgent:
            agent(self, group=self.random.choice(self.groups).group_id)
        else:
            agent(self)

    def step(self):
        super().step()
        for agent in self.agents:
            if agent.group is not None and agent.partner is None and agent.age > 15:
                if self.random.random() < self.migration_rate:
                    agent.migrate()

    def get_group_of_agent(self, agent) -> Group:
        agent_group = list(filter(lambda g: g.group_id == agent.group, self.groups))
        return None if len(agent_group) == 0 else agent_group[0]

    def init_groups(self, number_of_groups):
        self.groups: List[Group] = []
        letters = list(string.ascii_uppercase)
        for i in range(number_of_groups):
            self.groups.append(Group(letters[i]))
