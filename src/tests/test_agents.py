import unittest

from simulation.agents.aging import AgingAgent
from simulation.agents.base import BaseAgent
from simulation.agents.reproducing import ReproducingAgent
from simulation.models.aging import AgingModel
from simulation.models.base import BaseModel
from simulation.models.reproduction import ReproductionModel


class NetworksTest(unittest.TestCase):

    def test_base(self):
        model = BaseModel(num_agents=0, network_saving_steps=None, run_id=None)
        agent = BaseAgent(model)
        self.assertIsInstance(agent, BaseAgent)

    def test_aging(self):
        model = AgingModel(num_agents=0, network_saving_steps=None, run_id=None,
                           lifeexpectancy=(0, 0))
        agent = AgingAgent(model)
        self.assertIsInstance(agent, AgingAgent)

    def test_reproducing(self):
        model = ReproductionModel(num_agents=0, network_saving_steps=None, run_id=None,
                                  lifeexpectancy=(0, 0), agent_limit=0,
                                  genderless=False)
        agent = ReproducingAgent(model)
        self.assertIsInstance(agent, ReproducingAgent)


if __name__ == '__main__':
    unittest.main()
