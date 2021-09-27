import networkx as nx
from matplotlib import pyplot as plt

from simulation.utils.directory import create_dir


def save_network_visualization(self, out: str) -> None:
    full_path = create_dir(out)
    plt.figure(figsize=(20, 12))
    pos = nx.planar_layout(self.graph, center=[0,0])
    nx.draw(self.graph, pos, with_labels=False, width=0.05,
            node_color='blue', node_size=2)
    plt.savefig(full_path)
