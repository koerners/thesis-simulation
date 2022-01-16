from mesa.agent import Agent
from simulation.agents.group import GroupAgent


class CultureAgent(GroupAgent):
    def __init__(self, model, group, age=None):
        super().__init__(model=model, group=group, age=age)

    def find_peer_in_need(self) -> Agent:
        group = self.model.get_group_of_agent(self)
        if group is not None:
            willing_to_help = (
                self.random.uniform(0, 1)
                <= group.group_culture
            )
            if willing_to_help:
                for peer in self.model.agents:
                    if peer != self and peer.current_food < 1 and peer.group == self.group:
                        self.model.agent_acted_altruistic(self)
                        return peer
        else:
            self.model.agent_acted_non_altruistic(self)
        return None
