import unittest

from simulation.networks.base import BaseNetwork


class NetworksTest(unittest.TestCase):

    def test_base(self):
        network = BaseNetwork()
        self.assertIsInstance(network, BaseNetwork)


if __name__ == '__main__':
    unittest.main()
