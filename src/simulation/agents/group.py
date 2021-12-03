from mesa.agent import Agent
from simulation.agents.altruism import AltruismAgent


class GroupAgent(AltruismAgent):
    def __init__(self, model, group=None, age=None):
        super().__init__(model=model, group=group, age=age)

    def find_peer_in_need(self) -> Agent:
        for peer in self.model.agents:
            if peer != self and peer.current_food < 1 and peer.group == self.group:
                return peer
        return None

    def bear_child(self) -> Agent:
        return GroupAgent(model=self.model, group=self.group, age=0)
