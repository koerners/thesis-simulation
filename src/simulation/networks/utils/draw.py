import os

import networkx as nx
from matplotlib import pyplot as plt


def save_network_visualization(self, out) -> None:
    full_path = create_dir(out)
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(self.graph, k=0.8)
    nx.draw(self.graph, pos, with_labels=False, width=0.4,
            node_color='lightblue', node_size=400)
    plt.savefig(full_path)


def create_dir(out):
    file_name = out.split('/')[-1]
    path = os.path.join('./out', out.replace(file_name, ''))
    if not os.path.isdir(path):
        os.makedirs(path)
    return f"{path}/{file_name}"
