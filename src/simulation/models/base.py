from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from agents.base import BaseAgent
import networkx as nx

class BaseModel(Model):
    def __init__(self, N):
        super().__init__()
        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.running = True
        self.network = nx.Graph()

        # Create agents
        for i in range(self.num_agents):
            a = BaseAgent(i, self)
            self.schedule.add(a)

        self.datacollector = DataCollector()

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()
