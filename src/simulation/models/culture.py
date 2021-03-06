from typing import List
import string
from simulation.agents.culture import CultureAgent
from simulation.agents.eating import EatingAgent
from simulation.agents.unconditional import UnconditionalAgent
from simulation.helper.groups import CultureGroup
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
        group_number,
        migration_rate,
        mutation_chance,
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
            group_number=group_number,
            migration_rate=migration_rate,
            mutation_chance=mutation_chance,
        )

    def init_groups(self, number_of_groups):
        letters = list(string.ascii_uppercase)
        step = float(1 / number_of_groups)
        counter = step
        self.groups: List[CultureModel] = []
        for i in range(number_of_groups):
            self.groups.append(CultureGroup(letters[i], round(counter, 2)))
            counter += step

    def add_agent(self):
        possible_agents = [EatingAgent, UnconditionalAgent, CultureAgent]
        agent = self.random.choice(possible_agents)
        if agent == CultureAgent:
            agent(self, group=self.random.choice(self.groups).group_id)
        else:
            agent(self)

    def agent_acted_altruistic(self, agent):
        group = self.get_group_of_agent(agent)
        group.agent_acted_altruistic()

    def agent_acted_non_altruistic(self, agent):
        group = self.get_group_of_agent(agent)
        group.agent_acted_non_altruistic()
