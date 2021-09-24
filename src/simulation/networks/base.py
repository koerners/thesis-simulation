import networkx as nx

from simulation.networks.utils.draw import save_network_visualization


class BaseNetwork:
    def __init__(self, model):
        self.graph = nx.Graph()
        self.model = model

    def add_node(self, node):
        self.graph.add_node(node)

    def remove_node(self, node):
        self.graph.remove_node(node)

    def add_node_connection(self, node_1, node_2, relatedness):
        self.graph.add_edge(node_1, node_2, weight=relatedness)

    def draw(self, file_name):
        save_network_visualization(self, file_name)
