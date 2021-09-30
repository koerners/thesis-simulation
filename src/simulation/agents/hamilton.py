
from simulation.agents.eating import EatingAgent


class HamiltonAgent(EatingAgent):
    def __init__(self, model, age=None):
        super().__init__(model=model, age=age)

    def bear_child(self):
        return HamiltonAgent(self.model, age=0)
