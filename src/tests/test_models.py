import unittest

from simulation.models.aging import AgingModel
from simulation.models.base import BaseModel
from simulation.models.reproduction import ReproductionModel


class ModelsTest(unittest.TestCase):

    def test_base(self):
        model = BaseModel(num_agents=0, network_saving_steps=None, run_id=None)
        self.assertIsInstance(model, BaseModel)

    def test_aging(self):
        model = AgingModel(num_agents=0, network_saving_steps=None, run_id=None,
                           lifeexpectancy=(0,0))
        self.assertIsInstance(model, AgingModel)

    def test_reproducing(self):
        model = ReproductionModel(num_agents=0, network_saving_steps=None, run_id=None,
                                  lifeexpectancy=(0,0), agent_limit=0,
                                  genderless=False)
        self.assertIsInstance(model, ReproductionModel)


if __name__ == '__main__':
    unittest.main()
