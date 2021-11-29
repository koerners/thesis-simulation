import unittest

from simulation.agents.aging import AgingAgent
from simulation.agents.base import BaseAgent
from simulation.agents.culture import CultureAgent
from simulation.agents.genuine import GenuineAgent
from simulation.agents.greenbeard import GreenBeardAgent
from simulation.agents.reproducing import ReproducingAgent
from simulation.agents.eating import EatingAgent
from simulation.agents.hamilton import HamiltonAgent
from simulation.models.aging import AgingModel
from simulation.models.altruism import AltruismModel
from simulation.models.base import BaseModel
from simulation.models.culture import CultureGroup, CultureModel
from simulation.models.eating import EatingModel
from simulation.models.greenbeard import GreenBeardModel
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
        model.step()
        self.assertEqual(agent.age, 1)
        self.assertEqual(model.schedule.get_agent_count(), 1)
        model.step()
        model.step()
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

    def test_genuine(self):
        model = AltruismModel(
            num_agents=0,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(0, 0),
            agent_limit=0,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=0,
            level_of_sacrifice=0.8,
        )
        agent = GenuineAgent(model)
        self.assertIsInstance(agent, GenuineAgent)
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
            level_of_sacrifice=0.8,
            min_relationship=2,
        )
        agent = HamiltonAgent(model)
        self.assertIsInstance(agent, HamiltonAgent)
        agent.step()

    def test_greenbeard(self):
        model = GreenBeardModel(
            num_agents=0,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(0, 0),
            agent_limit=0,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=0,
            level_of_sacrifice=0.8,
        )
        agent = GreenBeardAgent(model)
        self.assertIsInstance(agent, GreenBeardAgent)
        agent.step()

    def test_culture(self):
        model = CultureModel(
            num_agents=10,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=3,
            level_of_sacrifice=0.8,
        )
        agent = CultureAgent(model, group=CultureGroup('A', 0))
        self.assertIsInstance(agent, CultureAgent)
        agent.step()


if __name__ == "__main__":
    unittest.main()
