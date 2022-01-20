import unittest

from simulation.networks.base import BaseNetwork


class TestNode:
    # pylint: disable=too-few-public-methods

    def __init__(self, unique_id, group=None):
        self.unique_id = unique_id
        self.group = group


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

    def test_group_update(self):
        network = BaseNetwork()
        test_node = TestNode(1, "group_1")
        network.add_node(test_node)
        self.assertEqual(
            network.graph.nodes[test_node.unique_id]["agent_group"], "group_1"
        )
        test_node.group = "group_2"
        network.update_node_group(test_node)
        self.assertEqual(
            network.graph.nodes[test_node.unique_id]["agent_group"], "group_2"
        )

    def test_node_helped_node(self):
        network = BaseNetwork()
        donor = TestNode(1)
        receiver = TestNode(2)
        network.add_node(donor)
        network.add_node(receiver)
        network.node_helped_node(donor, receiver)
        network.node_helped_node(receiver, donor)
        self.assertEqual(network.graph[donor.unique_id][receiver.unique_id]["altruism"], 2)


if __name__ == "__main__":
    unittest.main()
