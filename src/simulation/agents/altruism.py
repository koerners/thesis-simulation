from simulation.agents.eating import EatingAgent


class AltruismAgent(EatingAgent):
    def __init__(self, model, age=None):
        super().__init__(model=model, age=age)

    def step(self) -> None:
        super().step()
        still_needy_peers_left = True
        for _ in range(self.__determine_max_sacrifice()):
            if still_needy_peers_left:
                # pylint: disable=assignment-from-none
                peer_in_need = self.find_peer_in_need()
                if peer_in_need is not None:
                    self.give_food_to(peer_in_need)
                else:
                    still_needy_peers_left = False

    def __determine_max_sacrifice(self) -> int:
        if self.current_food < 1:
            return 0
        if self.model.level_of_sacrifice == 1:
            return self.current_food

        to_sacrifice = int(self.model.level_of_sacrifice * self.current_food)
        return max(1, to_sacrifice)

    def find_peer_in_need(self):
        # pylint: disable=no-self-use
        return None
