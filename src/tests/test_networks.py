import unittest

from simulation.networks.base import BaseNetwork


class TestNode:
    # pylint: disable=too-few-public-methods

    def __init__(self, unique_id):
        self.unique_id = unique_id
        self.group = None


class NetworksTest(unittest.TestCase):
    def test_base(self):
        network = BaseNetwork()
        self.assertIsInstance(network, BaseNetwork)

    def test_add(self):
        network = BaseNetwork()
        network.add_node(TestNode(1))
        self.assertEqual(network.get_node_count(), 1)

    def test_remove(self):
        network = BaseNetwork()
        network.add_node(TestNode(1))
        self.assertEqual(network.get_node_count(), 1)
        network.remove_node(TestNode(1))
        self.assertEqual(network.get_node_count(), 0)


if __name__ == "__main__":
    unittest.main()
