

from simulation.agents.reproducing import ReproducingAgent


class EatingAgent(ReproducingAgent):
    def __init__(self, model, age=None):
        self.current_food = 1
        super().__init__(model=model, age=age)

    def step(self) -> None:
        self.current_food += self.find_food()
        self.current_food -= 1
        self.can_reproduce = self.current_food >= self.model.child_bearing_cost

        super().step()

    def find_food(self) -> int:
        food = 0
        if self.model.current_food > 0:
            food = min(self.random.choice(
                range(0, self.model.finding_max)), self.model.current_food)
            self.model.current_food -= food
        return food

    def bear_child(self):
        self.current_food -= self.model.child_bearing_cost
        return EatingAgent(self.model, age=0)

    def give_food_to(self, receiver):
        if self.current_food > 0:
            self.current_food -= 1
            receiver.current_food += 1
