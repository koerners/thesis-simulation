from simulation.agents.eating import EatingAgent


class HamiltonAgent(EatingAgent):
    def __init__(self, model, age=None):
        super().__init__(model=model, age=age)

    def step(self) -> None:
        super().step()
        still_needy_relatives_left = True
        for _ in range(self.__determine_max_sacrifice()):
            if still_needy_relatives_left:
                relative_in_need = self.__find_relative_in_need()
                if relative_in_need is not None:
                    self.give_food_to(relative_in_need)
                else:
                    still_needy_relatives_left = False

    def __determine_max_sacrifice(self) -> int:
        if self.current_food < 1:
            return 0
        if self.model.level_of_sacrifice == 1:
            return self.current_food

        to_sacrifice = int(self.model.level_of_sacrifice * self.current_food)
        return max(1, to_sacrifice)

    def __find_relative_in_need(self):
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
