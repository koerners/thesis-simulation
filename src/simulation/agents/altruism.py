from simulation.agents.eating import EatingAgent


class AltruismAgent(EatingAgent):
    def __init__(self, model, group=None, age=None, is_altruist=True):
        super().__init__(model=model, group=group, age=age, is_altruist=is_altruist)

    def step(self):
        super().step()
        still_needy_peers_left: bool = True
        for _ in range(self.__determine_max_sacrifice()):
            if still_needy_peers_left:
                # pylint: disable=assignment-from-none
                peer_in_need = self.find_peer_in_need()
                if peer_in_need is not None:
                    self.give_food_to(peer_in_need)
                else:
                    still_needy_peers_left = False

    def give_food_to(self, receiver):
        if self.current_food > 0:
            self.current_food -= 1
            receiver.current_food += 1
            self.model.altruistic_action(receiver)
            #self.model.network.node_helped_node(self, receiver)

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
