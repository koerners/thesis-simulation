from simulation.agents.reproducing import ReproducingAgent
from simulation.models.aging import AgingModel


class ReproductionModel(AgingModel):
    def __init__(self, num_agents, network_visualization_steps,
                 min_lifeexpectancy, max_lifeexpectancy):
        super().__init__(num_agents=num_agents,
                         network_visualization_steps=network_visualization_steps,
                         min_lifeexpectancy=min_lifeexpectancy,
                         max_lifeexpectancy=max_lifeexpectancy)
        self.suitable_mates = []

    def add_agent(self) -> None:
        ReproducingAgent(self)

    def step(self) -> None:
        self.suitable_mates = list(filter(lambda agent: (agent.age > 14 and agent.age <
                                   40 and agent.partner is None), self.schedule.agents))
        super().step()
