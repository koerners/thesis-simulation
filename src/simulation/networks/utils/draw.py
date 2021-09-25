import networkx as nx
from matplotlib import pyplot as plt

from simulation.utils.directory import create_dir


def save_network_visualization(self, out) -> None:
    full_path = create_dir(out)
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(self.graph, k=0.8)
    nx.draw(self.graph, pos, with_labels=False, width=0.4,
            node_color='lightblue', node_size=400)
    plt.savefig(full_path)
