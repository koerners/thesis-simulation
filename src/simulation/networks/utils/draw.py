import networkx as nx

from simulation.utils.directory import create_dir


def save_network(self, out: str):
    full_path = create_dir(out)
    nx.write_gpickle(self.graph, full_path)
