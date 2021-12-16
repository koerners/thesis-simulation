from statistics import StatisticsError, median
from typing import Dict

from networkx.algorithms.approximation import average_clustering


def get_total_agent_count(self) -> int:
    return self.schedule.get_agent_count()


def get_experiment_id(self) -> int:
    return self.experiment_id


def get_seed(self) -> int:
    # pylint: disable=no-member protected-access
    return self._seed


def get_steps_data(self) -> Dict:
    keep = [
        "total_agents",
        "clustering",
        "agent_types",
        "food_distribution",
        "agent_groups",
        "average_reputation",
        "groups_culture",
        "agent_neighbors_by_type",
        "agent_neighbors_by_group",
        "trivers_values",
    ]
    return [
        {key: value}
        for (key, value) in self.datacollector.model_vars.items()
        if key in keep
    ]


def get_current_network(self, step=10):
    """Returns the current network every 10 steps"""
    if self.schedule.steps % step == 0:
        return self.network
    return None


def get_network_clustering(self):
    try:
        return average_clustering(self.network.graph)
    except IndexError:
        return 0


def get_current_agent_types(self):
    agents = {}
    for agent in self.schedule.agents:
        agent_type = type(agent).__name__
        if agent_type in agents:
            agents[agent_type] += 1
            continue
        agents[agent_type] = 1
    return agents


def get_trivers_values(self):
    left_hand_side, right_hand_side = 0, 0
    if hasattr(self, "benefits"):
        benefits_altruists, benefits_non_altruists = self.benefits
        self.reset_benefits()
        all_agents = len(self.agents)
        altruists = len(list(filter(lambda x: x.is_altruist, self.agents)))
        non_altruists = all_agents - altruists
        cum_benefits = benefits_non_altruists + benefits_altruists
        if altruists > 0:
            left_hand_side = (1 / ((altruists / all_agents) ** 2)) * (
                benefits_altruists
                - (cum_benefits * (1 / max(1, self.child_bearing_cost)))
            )
        if non_altruists > 0:
            right_hand_side = (
                1 / ((non_altruists / all_agents) ** 2)
            ) * benefits_non_altruists
    return {"avg_fitness_alt": left_hand_side, "avg_fitness_non_alt": right_hand_side}


def get_agent_neighbors_by_type(self):
    agents = {}
    agents_helper = {}
    for agent in self.schedule.agents:
        agent_type = type(agent).__name__
        if agent_type in agents:
            agents[agent_type] += self.network.get_nr_neighbors(agent)
            agents_helper[agent_type] += 1
            continue
        agents[agent_type] = self.network.get_nr_neighbors(agent)
        agents_helper[agent_type] = 1
    for agent_type in agents:
        agents[agent_type] = round(agents[agent_type] / agents_helper[agent_type], 2)
    return agents


def get_agent_neighbors_by_group(self):
    groups = {}
    groups_helper = {}
    if hasattr(self, "groups"):
        for agent in self.schedule.agents:
            agent_group = self.get_group_of_agent(agent).group_id
            if agent_group in groups:
                groups[agent_group] += self.network.get_nr_neighbors(agent)
                groups_helper[agent_group] += 1
                continue
            groups[agent_group] = self.network.get_nr_neighbors(agent)
            groups_helper[agent_group] = 1
        for group in groups:
            groups[group] = round(groups[group] / groups_helper[group], 2)
    return groups


def get_agent_groups(self):
    agents = {}
    for agent in self.schedule.agents:
        agent_group = agent.group
        if agent_group in agents:
            agents[agent_group] += 1
            continue
        agents[agent_group] = 1
    return agents


def get_groups_culture(self):
    groups = {}
    if hasattr(self, "groups"):
        for group in self.groups:
            if hasattr(group, "group_culture"):
                groups[group.group_id] = group.group_culture
    return groups


def get_average_reputation(self):
    if hasattr(self, "average_reputation"):
        return self.average_reputation
    return 0


def get_current_food_distribution(self):

    below_average = 0
    above_average = 0

    try:
        food_distribution = [x.current_food for x in self.schedule.agents]
        mean = median(food_distribution)
        below_average = len(list(filter(lambda x: x < mean, food_distribution)))
        above_average = len(list(filter(lambda x: x > mean, food_distribution)))
    except StatisticsError:
        # no agents
        pass
    except AttributeError:
        pass

    return {"below_mean": below_average, "above_mean": above_average}
