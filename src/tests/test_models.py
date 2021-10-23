import unittest

from simulation.models.aging import AgingModel
from simulation.models.base import BaseModel
from simulation.models.eating import EatingModel
from simulation.models.hamilton import HamiltonModel
from simulation.models.reproduction import ReproductionModel


class ModelsTest(unittest.TestCase):
    def assert_step(self, model):
        self.assertEqual(model.schedule.steps, 0)
        model.step()
        self.assertEqual(model.schedule.steps, 1)

    def assert_running(self, model):
        for _ in range(0, 500):
            model.step()
            print(model.network.get_node_count(),
                  len(model.schedule.agents))
            self.assertEqual(model.network.get_node_count(),
                             len(model.schedule.agents))

    def test_base(self):
        model = BaseModel(
            num_agents=10, network_saving_steps=None, run_id=None)
        self.assertIsInstance(model, BaseModel)
        self.assert_step(model)
        self.assert_running(model)

    def test_aging(self):
        model = AgingModel(
            num_agents=50, network_saving_steps=None, run_id=None, lifeexpectancy=(50, 100)
        )
        self.assertIsInstance(model, AgingModel)
        self.assert_step(model)
        self.assert_running(model)

    def test_reproducing(self):
        model = ReproductionModel(
            num_agents=10,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=500,
            genderless=False,
        )
        self.assertIsInstance(model, ReproductionModel)
        self.assert_step(model)
        self.assert_running(model)

    def test_eating(self):
        model = EatingModel(
            num_agents=50,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=500,
            genderless=False,
            foodlimit_multiplicator=None,
            finding_max=3,
        )
        self.assertIsInstance(model, EatingModel)
        self.assert_step(model)

    def test_hamilton(self):
        model = HamiltonModel(
            num_agents=50,
            network_saving_steps=None,
            run_id=None,
            lifeexpectancy=(50, 100),
            agent_limit=500,
            genderless=False,
            foodlimit_multiplicator=10,
            finding_max=3,
        )
        self.assertIsInstance(model, HamiltonModel)
        self.assert_step(model)


if __name__ == "__main__":
    unittest.main()
