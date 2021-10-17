import networkx as nx
from networkx.exception import NetworkXError

from simulation.networks.utils.draw import save_network


class BaseNetwork:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node) -> None:
        self.graph.add_node(node)

    def remove_node(self, node) -> None:
        try:
            self.graph.remove_node(node)
        except NetworkXError:
            pass

    def add_node_connection(self, node_1, node_2, relatedness: int) -> None:
        self.graph.add_edge(node_1, node_2, weight=relatedness)

    def get_neighbors(self, node):
        try:
            return nx.algorithms.components.node_connected_component(self.graph, node)
        except KeyError:
            return None

    def get_node_weight(self, node_1, node_2) -> int:
        conn = self.graph.get_edge_data(node_1, node_2)
        return 0 if conn is None else conn.get("weight", 0)

    def save(self, file_name: str) -> None:
        save_network(self, file_name)
