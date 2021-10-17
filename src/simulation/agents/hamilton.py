
from simulation.agents.eating import EatingAgent


class HamiltonAgent(EatingAgent):
    def __init__(self, model, age=None):
        super().__init__(model=model, age=age)

    def bear_child(self):
        self.current_food -= self.model.child_bearing_cost
        return HamiltonAgent(self.model, age=0)

    def __find_relative_in_need(self, agent):
        strongest_connection = 0
        strongest_connected_agent = None
        for neighbor in self.model.network.get_neighbors(agent):
            if neighbor.current_food > 0:
                continue
            connection = self.model.network.get_node_weight(agent, neighbor)
            if(connection > strongest_connection):
                strongest_connection = connection
                strongest_connected_agent = neighbor
        return strongest_connected_agent

    def end_of_step_action(self):
        if self.current_food > 1:
            in_need = self.__find_relative_in_need(self)
            if in_need is not None:
                self.give_food_to(in_need)
