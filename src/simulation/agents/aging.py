from simulation.agents.base import BaseAgent


class AgingAgent(BaseAgent):
    def __init__(self, model, group=None, age=None):
        super().__init__(model=model, group=group)
        if age is None:
            self.age = self.random.randint(0, 69)
        else:
            self.age = age
        min_lifeexpectancy, max_lifeexpectancy = model.lifeexpectancy
        self.life_expectancy = self.random.randint(
            min_lifeexpectancy, max_lifeexpectancy
        )

    def step(self) -> None:
        super().step()
        self.age += 1
