
from enum import Enum
from simulation.agents.aging import AgingAgent
from simulation.models.utils.datacollector import get_total_agent_count
from simulation.networks.constants_relationsships import Relationship


class Gender(Enum):
    MALE = "m"
    FEMALE = "f"
    GENDERLESS = "x"


class ReproducingAgent(AgingAgent):
    def __init__(self, model, age=None):
        super().__init__(model=model, age=age)
        self.gender = self.random.choice(
            [Gender.MALE, Gender.FEMALE]) if not model.genderless else Gender.GENDERLESS
        self.partner = None
        self.can_reproduce = True

    def step(self) -> None:
        super().step()
        agent_limit_reached = get_total_agent_count(
            self.model) >= self.model.agent_limit
        if self.partner is None:
            self.find_partner()
        if not agent_limit_reached and self.partner is not None \
            and (self.gender in (Gender.FEMALE, Gender.GENDERLESS)) \
                and self.age < 40 and self.can_reproduce:
            self.reproduce()

    def reproduce(self) -> None:
        child = self.bear_child()
        self.model.network.add_node_connection(
            self, child, Relationship.CHILD.value)
        self.model.network.add_node_connection(
            self.partner, child, Relationship.CHILD.value)

    def find_partner(self):
        self.partner = next(
            filter(lambda mate: (mate.partner is None and
                                 (mate.gender != self.gender or
                                     self.gender == Gender.GENDERLESS)),
                   self.model.suitable_mates), None)
        if self.partner is not None:
            self.partner.partner = self
            self.model.network.add_node_connection(
                self, self.partner, Relationship.PARTNER.value)

    def bear_child(self):
        return ReproducingAgent(self.model, age=0)
