from simulation.agents.reproducing import ReproducingAgent
from simulation.models.aging import AgingModel


class ReproductionModel(AgingModel):
    def __init__(self, num_agents, network_saving_steps,
                 lifeexpectancy, genderless, agent_limit, run_id):
        self.genderless_agents = genderless
        self.agent_limit = agent_limit
        self.suitable_mates = []
        super().__init__(num_agents=num_agents,
                         network_saving_steps=network_saving_steps,
                         lifeexpectancy=lifeexpectancy,
                         run_id=run_id)

    def add_agent(self) -> None:
        ReproducingAgent(self, gender_less=self.genderless_agents,
                         lifeexpectancy=self.lifeexpectancy)

    def step(self) -> None:
        self.suitable_mates = list(filter(lambda agent: (agent.age > 14 and agent.age <
                                   40 and agent.partner is None), self.schedule.agents))


        super().step()
