import networkx as nx

from simulation.networks.utils.draw import save_network


class BaseNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node) -> None:
        self.graph.add_node(node)

    def remove_node(self, node) -> None:
        self.graph.remove_node(node)

    def add_node_connection(self, node_1, node_2, relatedness: int) -> None:
        self.graph.add_edge(node_1, node_2, weight=relatedness)

    def save(self, file_name: str) -> None:
        save_network(self, file_name)
