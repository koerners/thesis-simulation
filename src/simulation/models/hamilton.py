from simulation.agents.eating import EatingAgent
from simulation.agents.hamilton import HamiltonAgent
from simulation.models.eating import EatingModel


class HamiltonModel(EatingModel):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def add_agent(self) -> None:
        agent = self.random.choice([EatingAgent, HamiltonAgent])
        agent(self)
