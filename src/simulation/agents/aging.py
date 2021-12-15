from simulation.agents.base import BaseAgent


class AgingAgent(BaseAgent):
    def __init__(self, model, group=None, age=None, is_altruist=False):
        super().__init__(model=model, group=group, is_altruist=is_altruist)
        if age is None:
            self.age: int = self.random.randint(0, 69)
        else:
            self.age: int = age
        min_lifeexpectancy, max_lifeexpectancy = model.lifeexpectancy
        self.life_expectancy: int = self.random.randint(
            min_lifeexpectancy, max_lifeexpectancy
        )

    def step(self):
        super().step()
        self.age += 1
