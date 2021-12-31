from mesa.agent import Agent
from simulation.agents.altruism import AltruismAgent


class GreenBeardAgent(AltruismAgent):
    def __init__(self, model, group=None, age=None, is_altruist=True):
        self.is_greenbeard = True
        super().__init__(model=model, group=group, age=age, is_altruist=is_altruist)

    def find_peer_in_need(self) -> Agent:
        for peer in self.model.agents:
            if (
                peer != self
                and hasattr(peer, "is_greenbeard")
                and peer.current_food < 1
            ):
                return peer
        return None
