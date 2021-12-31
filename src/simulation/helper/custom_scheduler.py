from typing import List
from mesa.agent import Agent
from mesa.time import RandomActivation


class CustomScheduler(RandomActivation):
    def get_agent_by_id(self, agent_id: int) -> Agent:
        if agent_id not in self._agents.keys():
            return None
        return self._agents[agent_id]

    def get_agents_by_id(self, agent_ids: List[int]) -> List[Agent]:
        agents = []
        for agent_id in agent_ids:
            agent = self.get_agent_by_id(agent_id)
            if agent is not None:
                agents.append(agent)
        return agents
