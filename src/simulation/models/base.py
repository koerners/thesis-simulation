from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from agents.base import BaseAgent
from networks.base import BaseNetwork


class BaseModel(Model):
    def __init__(self, N):
        super().__init__()
        self.num_agents = N
        self.schedule = self.init_scheduler()
        self.running = True
        self.network = self.init_social_network()
        self.datacollector = DataCollector()

        # Create agents
        for i in range(self.num_agents):
            a = self.add_agent(i)
            self.schedule.add(a)

    def step(self):
        self.custom_step()
        self.datacollector.collect(self)
        self.schedule.step()

    def add_agent(self, i):
        return BaseAgent(self, i)

    def init_social_network(self):
        return BaseNetwork(self)

    def init_scheduler(self):
        return RandomActivation(self)

    def custom_step(self):
        pass
