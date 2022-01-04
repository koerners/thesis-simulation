import unittest

from simulation.agents.eating import EatingAgent
from simulation.agents.unconditional import UnconditionalAgent
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


class ModelsTest(unittest.TestCase):
    def assert_step(self, model):
        self.assertEqual(model.schedule.steps, 0)
        model.step()
        self.assertEqual(model.schedule.steps, 1)

    def assert_running(self, model, steps=500):
        for _ in range(0, steps):
            model.step()
            self.assertEqual(
                model.network.get_node_count(), model.schedule.get_agent_count()
            )

    def assert_test_group(self, model):
        """assert there are two types of agents present in the model: unconditional and eating"""
        existing_types_of_agents = set(
            agent.__class__ for agent in model.agents)
        self.assertIn(UnconditionalAgent, existing_types_of_agents)
        self.assertIn(EatingAgent, existing_types_of_agents)

    def test_base(self):
        model = BaseModel(
            num_agents=10, network_saving_steps=None, run_id=None)
        self.assertIsInstance(model, BaseModel)
        self.assertEqual(model.schedule.get_agent_count(), 10)
        self.assert_step(model)
        self.assert_running(model)

    def test_aging(self):
        model = AgingModel(
            num_agents=50,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
        )
        self.assertIsInstance(model, AgingModel)
        self.assertEqual(model.schedule.get_agent_count(), 50)

        self.assert_step(model)
        self.assert_running(model)

    def test_reproducing(self):
        model = ReproductionModel(
            num_agents=10,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            mutation_chance=0,
        )
        self.assertIsInstance(model, ReproductionModel)
        self.assertEqual(model.schedule.get_agent_count(), 10)
        self.assert_step(model)

        self.assert_running(model)

    def test_eating(self):
        model = EatingModel(
            num_agents=10,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=3,
            mutation_chance=0,
        )
        self.assertIsInstance(model, EatingModel)
        self.assertEqual(model.schedule.get_agent_count(), 10)
        self.assert_step(model)
        self.assert_running(model)

    def test_altruism(self):
        model = AltruismModel(
            num_agents=10,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=3,
            level_of_sacrifice=0.8,
            mutation_chance=0,
        )
        self.assertIsInstance(model, AltruismModel)
        self.assertEqual(model.schedule.get_agent_count(), 10)
        self.assert_step(model)
        self.assert_running(model)

    def test_group(self):
        model = GroupModel(
            num_agents=50,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=3,
            level_of_sacrifice=0.8,
            group_number=3,
            migration_rate=1.0,
            mutation_chance=0,
        )
        self.assertIsInstance(model, GroupModel)
        self.assertEqual(model.schedule.get_agent_count(), 50)
        self.assertEqual(len(model.groups), 3)
        self.assert_test_group(model)
        self.assert_step(model)
        self.assert_running(model, 10)

    def test_culture(self):
        model = CultureModel(
            num_agents=50,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=3,
            level_of_sacrifice=0.8,
            group_number=3,
            migration_rate=0.05,
            mutation_chance=0,
        )
        self.assertIsInstance(model, CultureModel)
        self.assertEqual(model.schedule.get_agent_count(), 50)
        self.assert_test_group(model)
        self.assertEqual(len(model.groups), 3)
        self.assert_step(model)
        self.assert_running(model)

    def test_kinselection(self):
        model = KinSelectionModel(
            num_agents=50,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            foodlimit_multiplicator=10,
            finding_max=3,
            level_of_sacrifice=0.8,
            min_relationship=2,
            mutation_chance=0,
        )
        self.assertIsInstance(model, KinSelectionModel)
        self.assertEqual(model.schedule.get_agent_count(), 50)
        self.assert_test_group(model)
        self.assert_step(model)
        self.assert_running(model)

    def test_greenbeard(self):
        model = GreenBeardModel(
            num_agents=50,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=100,
            genderless=False,
            foodlimit_multiplicator=10,
            finding_max=3,
            level_of_sacrifice=0.8,
            allow_fake_greenbeards=True,
            mutation_chance=0,
        )
        self.assertIsInstance(model, GreenBeardModel)
        self.assertEqual(model.schedule.get_agent_count(), 50)
        self.assert_test_group(model)
        self.assert_step(model)
        self.assert_running(model)

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
            mutation_chance=0,
        )
        self.assertIsInstance(model, ReputationModel)
        self.assertEqual(model.schedule.get_agent_count(), 50)
        self.assert_test_group(model)
        self.assert_step(model)
        self.assert_running(model)


if __name__ == "__main__":
    unittest.main()
