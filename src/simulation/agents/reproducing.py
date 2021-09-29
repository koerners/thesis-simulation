
from enum import Enum
from simulation.agents.aging import AgingAgent
from simulation.models.utils.datacollector import get_total_agent_count
from simulation.networks.constants_relationsships import Relationship


class Gender(Enum):
    MALE = "m"
    FEMALE = "f"
    GENDERLESS = "x"


class ReproducingAgent(AgingAgent):
    def __init__(self, model, lifeexpectancy, gender_less=False):
        super().__init__(model=model, lifeexpectancy=lifeexpectancy)
        self.gender = self.random.choice(
            [Gender.MALE, Gender.FEMALE]) if not gender_less else Gender.GENDERLESS
        self.partner = None

    def step(self) -> None:
        super().step()
        agent_limit_reached = get_total_agent_count(
            self.model) >= self.model.agent_limit
        if self.partner is None:
            self.partner = next(
                filter(lambda mate: (mate.partner is None and
                                     (mate.gender != self.gender or
                                         self.gender == Gender.GENDERLESS)),
                       self.model.suitable_mates), None)
            if self.partner is not None:
                self.partner.partner = self
                self.model.network.add_node_connection(
                    self, self.partner, Relationship.PARTNER.value)

        elif not agent_limit_reached and self.partner is not None \
            and (self.gender in (Gender.FEMALE, Gender.GENDERLESS)) \
                and self.age < 40:
            self.reproduce()

    def reproduce(self) -> None:
        child = ReproducingAgent(self.model, self.model.lifeexpectancy)
        self.model.network.add_node_connection(self, child, Relationship.CHILD.value)
        self.model.network.add_node_connection(self.partner, child, Relationship.CHILD.value)
