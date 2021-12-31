from mesa.agent import Agent
from simulation.agents.greenbeard import GreenBeardAgent


class FakeGreenBeardAgent(GreenBeardAgent):
    def __init__(self, model, group=None, age=None):
        super().__init__(model=model, group=group, age=age, is_altruist=False)

    def find_peer_in_need(self) -> Agent:
        return None
