from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from simulation.agents.base import BaseAgent
from simulation.models.utils.datacollector import \
    get_current_network, get_data_collector, get_experiment_id, get_total_agent_count
from simulation.networks.base import BaseNetwork


class BaseModel(Model):
    def __init__(self, num_agents, network_visualization_steps, run_id):
        super().__init__()
        self.run_id = run_id
        self.num_agents = num_agents
        self.schedule = self.init_scheduler()
        self.running = True
        self.network = self.init_social_network()
        self.network_visualization_steps = network_visualization_steps
        self.experiment_id = hash(self)
        self.datacollector = DataCollector(
            {'total_agents': get_total_agent_count,
             'experiment_id': get_experiment_id,
             'network': get_current_network,
             'datacollector': get_data_collector})

        # Create agents
        for _ in range(self.num_agents):
            self.add_agent()

    def step(self) -> None:
        self.datacollector.collect(self)
        if self.network_visualization_steps is not None and \
                self.schedule.steps % self.network_visualization_steps == 0:
            self.network.draw(
                f"{self.run_id}/{self.experiment_id}/Step_{self.schedule.steps}")
        self.schedule.step()
        if get_total_agent_count(self) < 1:
            self.running = False

    def add_agent(self) -> None:
        BaseAgent(self)

    def init_social_network(self) -> BaseNetwork:
        return BaseNetwork()

    def init_scheduler(self) -> RandomActivation:
        return RandomActivation(self)
