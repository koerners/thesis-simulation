import unittest

from simulation.models.aging import AgingModel
from simulation.models.base import BaseModel
from simulation.models.eating import EatingModel
from simulation.models.reproduction import ReproductionModel


class ModelsTest(unittest.TestCase):
    def assert_step(self, model):
        self.assertEqual(model.schedule.steps, 0)
        model.step()
        self.assertEqual(model.schedule.steps, 1)

    def test_base(self):
        model = BaseModel(num_agents=0, network_saving_steps=None, run_id=None)
        self.assertIsInstance(model, BaseModel)
        self.assert_step(model)

    def test_aging(self):
        model = AgingModel(num_agents=0, network_saving_steps=None, run_id=None,
                           lifeexpectancy=(0, 0))
        self.assertIsInstance(model, AgingModel)
        self.assert_step(model)

    def test_reproducing(self):
        model = ReproductionModel(num_agents=0, network_saving_steps=None, run_id=None,
                                  lifeexpectancy=(0, 0), agent_limit=0,
                                  genderless=False)
        self.assertIsInstance(model, ReproductionModel)
        self.assert_step(model)

    def test_eating(self):
        model = EatingModel(num_agents=0, network_saving_steps=None, run_id=None,
                                  lifeexpectancy=(0, 0), agent_limit=0,
                                  genderless=False, foodlimit_multiplicator=None, finding_max=0)
        self.assertIsInstance(model, EatingModel)
        self.assert_step(model)


if __name__ == '__main__':
    unittest.main()
