from simulation.agents.altruism import AltruismAgent


class HamiltonAgent(AltruismAgent):
    def __init__(self, model, group=None, age=None):
        super().__init__(model=model, group=group, age=age)

    def find_peer_in_need(self):
        strongest_connection = 0
        strongest_connected_agent = None
        for neighbor in self.model.get_neighbors(self):
            if neighbor.current_food > 0:
                continue
            connection = self.model.network.get_node_weight(self, neighbor)
            if connection > strongest_connection:
                strongest_connection = connection
                strongest_connected_agent = neighbor
        if strongest_connection < self.model.min_relationship:
            return None
        return strongest_connected_agent
