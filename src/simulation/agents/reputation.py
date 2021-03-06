from mesa.agent import Agent
from simulation.agents.altruism import AltruismAgent


class ReputationAgent(AltruismAgent):
    def __init__(self, model, group=None, age=None):
        self.reputation = 0.0
        super().__init__(model=model, group=group, age=age)

    def find_peer_in_need(self) -> Agent:
        for peer in self.model.agents:
            if peer != self and peer.current_food < 1:
                if self.calculate_help_decision(peer):
                    self.reputation += 1
                    return peer
        return None

    def calculate_help_decision(self, peer) -> bool:
        peer_rep = 0
        if hasattr(peer, "reputation"):
            peer_rep = peer.reputation
        return peer_rep >= self.model.average_reputation
