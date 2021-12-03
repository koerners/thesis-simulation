from mesa.agent import Agent
from simulation.agents.altruism import AltruismAgent


class GreenBeardAgent(AltruismAgent):
    def __init__(self, model, group=None, age=None):
        super().__init__(model=model, group=group, age=age)

    def find_peer_in_need(self) -> Agent:
        for peer in self.model.agents:
            if (
                peer != self
                and peer.__class__.__name__ == self.__class__.__name__
                and peer.current_food < 1
            ):
                return peer
        return None
