import unittest

from simulation.agents.aging import AgingAgent
from simulation.agents.base import BaseAgent
from simulation.agents.culture import CultureAgent
from simulation.agents.unconditional import UnconditionalAgent
from simulation.agents.greenbeard import GreenBeardAgent
from simulation.agents.group import GroupAgent
from simulation.agents.reproducing import ReproducingAgent
from simulation.agents.eating import EatingAgent
from simulation.agents.kinselection import KinSelectionAgent
from simulation.agents.reputation import ReputationAgent
from simulation.models.aging import AgingModel
from simulation.models.altruism import AltruismModel
from simulation.models.base import BaseModel
from simulation.models.culture import CultureModel
from simulation.models.eating import EatingModel
from simulation.models.greenbeard import GreenBeardModel
from simulation.models.group import GroupModel
from simulation.models.kinselection import KinSelectionModel
from simulation.models.reproduction import ReproductionModel
from simulation.models.reputation import ReputationModel


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

    def test_unconditional(self):
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
        agent = UnconditionalAgent(model)
        self.assertIsInstance(agent, UnconditionalAgent)
        agent.step()

    def test_kinselection(self):
        model = KinSelectionModel(
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
        agent = KinSelectionAgent(model)
        self.assertIsInstance(agent, KinSelectionAgent)
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

    def test_group(self):
        model = GroupModel(
            num_agents=10,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=3,
            level_of_sacrifice=0.8,
            group_number=1,
        )
        agent = GroupAgent(model, group="A")
        self.assertIsInstance(agent, GroupAgent)
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
            group_number=1,
        )
        agent = CultureAgent(model, group="A")
        self.assertIsInstance(agent, CultureAgent)
        agent.step()

    def test_reputation(self):
        model = ReputationModel(
            num_agents=50,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            foodlimit_multiplicator=10,
            finding_max=3,
            level_of_sacrifice=0.8,
        )
        agent = ReputationAgent(model)
        self.assertIsInstance(agent, ReputationAgent)
        agent.step()


if __name__ == "__main__":
    unittest.main()
