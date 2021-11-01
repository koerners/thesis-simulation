from simulation.agents.altruism import AltruismAgent


class GreenBeardAgent(AltruismAgent):
    def __init__(self, model, age=None):
        super().__init__(model=model, age=age)

    def find_peer_in_need(self):
        for peer in self.model.agents:
            if (
                peer != self
                and peer.__class__.__name__ == self.__class__.__name__
                and peer.current_food < 1
            ):
                return peer
        return None
