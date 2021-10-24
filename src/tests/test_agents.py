import unittest

from simulation.agents.aging import AgingAgent
from simulation.agents.base import BaseAgent
from simulation.agents.reproducing import ReproducingAgent
from simulation.agents.eating import EatingAgent
from simulation.models.aging import AgingModel
from simulation.models.base import BaseModel
from simulation.models.eating import EatingModel
from simulation.models.hamilton import HamiltonModel
from simulation.models.reproduction import ReproductionModel


class NetworksTest(unittest.TestCase):
    def test_base(self):
        model = BaseModel(num_agents=0, network_saving_steps=None, run_id=None)
        agent = BaseAgent(model)
        self.assertIsInstance(agent, BaseAgent)
        agent.step()

    def test_aging(self):
        model = AgingModel(
            num_agents=0, network_saving_steps=None, run_id=None, lifeexpectancy=(2, 2)
        )
        agent = AgingAgent(model, age=0)
        self.assertIsInstance(agent, AgingAgent)
        self.assertEqual(agent.age, 0)
        agent.step()
        self.assertEqual(agent.age, 1)
        self.assertEqual(model.schedule.get_agent_count(), 1)
        agent.step()
        agent.step()
        self.assertEqual(model.schedule.get_agent_count(), 0)


    def test_reproducing(self):
        model = ReproductionModel(
            num_agents=0,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(0, 0),
            agent_limit=5,
            genderless=True,
        )
        agent_1 = ReproducingAgent(model)
        agent_2 = ReproducingAgent(model)
        self.assertIsInstance(agent_1, ReproducingAgent)
        self.assertEqual(model.schedule.get_agent_count(), 2)
        agent_1.partner = agent_2
        agent_2.partner = agent_1
        agent_1.reproduce()
        self.assertEqual(model.schedule.get_agent_count(), 3)
        agent_1.step()

    def test_eating(self):
        model = EatingModel(
            num_agents=0,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(0, 0),
            agent_limit=0,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=0,
        )
        agent = EatingAgent(model)
        self.assertIsInstance(agent, EatingAgent)
        agent.step()

    def test_hamilton(self):
        model = HamiltonModel(
            num_agents=0,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(0, 0),
            agent_limit=0,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=0,
        )
        agent = EatingAgent(model)
        self.assertIsInstance(agent, EatingAgent)
        agent.step()


if __name__ == "__main__":
    unittest.main()
