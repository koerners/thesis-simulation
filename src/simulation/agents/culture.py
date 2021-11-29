from simulation.agents.altruism import AltruismAgent


class CultureAgent(AltruismAgent):
    def __init__(self, model, group=None, age=None):
        super().__init__(model=model, group=group, age=age)

    def find_peer_in_need(self):
        if self.random.uniform(0, 1) < self.model.get_group_of_agent(self).group_culture:
            for peer in self.model.agents:
                if peer != self and peer.current_food < 1 and peer.group == self.group:
                    self.model.agent_acted_altruistic(self)
                    return peer
        self.model.agent_acted_non_altruistic(self)
        return None

    def bear_child(self):
        return CultureAgent(model=self.model, group=self.group, age=0)
