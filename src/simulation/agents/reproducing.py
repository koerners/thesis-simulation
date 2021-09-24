
from simulation.agents.aging import AgingAgent


class ReproducingAgent(AgingAgent):
    def __init__(self, model, gender_less=False):
        super().__init__(model=model)
        self.gender = self.random.choice(
            ["m", "f"]) if not gender_less else "x"
        self.partner = None

    def step(self) -> None:
        super().step()
        if self.partner is None:
            self.partner = next(
                filter(lambda mate: (mate.partner is None and
                                     (mate.gender != self.gender or self.gender == "x")),
                       self.model.suitable_mates), None)
            if self.partner is not None:
                self.partner.partner = self
                self.model.network.add_node_connection(
                    self, self.partner, 1)

        elif self.partner is not None and (self.gender in ("f", "x")) \
                and self.age < 40:
            self.reproduce()

    def reproduce(self) -> None:
        ReproducingAgent(self.model)
