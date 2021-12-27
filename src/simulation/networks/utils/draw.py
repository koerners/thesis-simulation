import networkx as nx

from simulation.utils.directory import create_dir


def save_network(self, out: str, pickle=False):
    full_path = create_dir(out)
    if pickle:
        full_path += ".pkl"
        nx.write_gpickle(self.graph, full_path)
    else:
        full_path += ".graphml"
        nx.write_graphml(self.graph, full_path)
