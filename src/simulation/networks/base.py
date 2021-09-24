import networkx as nx


class BaseNetwork:
    def __init__(self, model):
        self.graph = nx.Graph()
        self.model = model

    def add_node(self, node):
        self.graph.add_node(node)

    def remove_node(self, node):
        self.graph.remove_node(node)
