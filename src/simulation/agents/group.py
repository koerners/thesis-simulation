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

    def migrate(self):
        for group in self.model.groups:
            if group.group_id != self.group:
                self.group = group.group_id
                self.model.network.update_node_group(self)
