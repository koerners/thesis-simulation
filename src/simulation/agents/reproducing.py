from mesa.agent import Agent
from simulation.agents.aging import AgingAgent
from simulation.helper.gender import Gender
from simulation.models.utils.datacollector import get_total_agent_count
from simulation.networks.constants_relationsships import Relationship


def agent_can_reproduce(agent, agent_limit_reached):
    return (
        not agent_limit_reached
        and agent.partner is not None
        and (agent.gender in (Gender.FEMALE, Gender.GENDERLESS))
        and agent.age < 40
        and agent.can_reproduce
        and agent.partner.can_reproduce
    )


class ReproducingAgent(AgingAgent):
    def __init__(self, model, group=None, age=None, is_altruist=False):
        super().__init__(model=model, group=group, age=age, is_altruist=is_altruist)
        self.gender: Gender = (
            self.random.choice([Gender.MALE, Gender.FEMALE])
            if not model.genderless
            else Gender.GENDERLESS
        )
        self.partner: Agent = None
        self.can_reproduce: bool = True  # can be overwritten by parent classes

    def step(self):
        super().step()
        agent_limit_reached = (
            get_total_agent_count(self.model) >= self.model.agent_limit
        )
        if self.partner is None and self.age > 15:
            self.find_partner()
        if agent_can_reproduce(self, agent_limit_reached):
            self.reproduce()
        self.can_reproduce = True

    def reproduce(self):
        child = self.bear_child()
        self.model.network.add_node_connection(self, child, Relationship.CHILD.value)
        self.model.network.add_node_connection(
            self.partner, child, Relationship.CHILD.value
        )

        for parent_neighbor in self.model.get_neighbors(self):
            if (
                self.model.network.get_node_weight(self, parent_neighbor)
                == Relationship.CHILD.value
            ):
                self.model.network.add_node_connection(
                    parent_neighbor, child, Relationship.SIBLING.value
                )

    def find_partner(self):
        self.partner = next(
            filter(
                lambda mate: (
                    mate.partner is None
                    and (mate.gender != self.gender or self.gender == Gender.GENDERLESS)
                    and self.group == mate.group
                ),
                self.model.suitable_mates,
            ),
            None,
        )
        if self.partner is not None:
            self.partner.partner = self
            self.model.network.add_node_connection(
                self, self.partner, Relationship.PARTNER.value
            )

    def bear_child(self) -> Agent:
        agent = self.random.choice(
            [
                self.__class__,
                self.partner.__class__,
            ]
        )
        return agent(self.model, age=0, group=self.group)

    def die(self):
        if self.partner is not None:
            self.partner.partner = None
        super().die()
