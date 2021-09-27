from simulation.agents.reproducing import ReproducingAgent
from simulation.models.aging import AgingModel


class ReproductionModel(AgingModel):
    def __init__(self, num_agents, network_saving_steps,
                 min_lifeexpectancy, max_lifeexpectancy, genderless, agent_limit, run_id):
        self.genderless_agents = genderless
        self.agent_limit = agent_limit
        self.suitable_mates = []
        super().__init__(num_agents=num_agents,
                         network_saving_steps=network_saving_steps,
                         min_lifeexpectancy=min_lifeexpectancy,
                         max_lifeexpectancy=max_lifeexpectancy,
                         run_id=run_id)

    def add_agent(self) -> None:
        ReproducingAgent(self, gender_less=self.genderless_agents)

    def step(self) -> None:
        self.suitable_mates = list(filter(lambda agent: (agent.age > 14 and agent.age <
                                   40 and agent.partner is None), self.schedule.agents))


        super().step()
