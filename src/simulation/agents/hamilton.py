from simulation.agents.eating import EatingAgent


class HamiltonAgent(EatingAgent):
    def __init__(self, model, age=None):
        super().__init__(model=model, age=age)

    def step(self) -> None:
        super().step()
        if self.current_food > 1:
            relative_in_need = self.__find_relative_in_need()
            if relative_in_need is not None:
                self.give_food_to(relative_in_need)

    def __find_relative_in_need(self):
        strongest_connection = 0
        strongest_connected_agent = None
        for neighbor in self.model.network.get_neighbors(self):
            if neighbor.current_food > 0:
                continue
            connection = self.model.network.get_node_weight(self, neighbor)
            if connection > strongest_connection:
                strongest_connection = connection
                strongest_connected_agent = neighbor
        return strongest_connected_agent
