from typing import List
import networkx as nx
from networkx.exception import NetworkXError

from simulation.networks.utils.draw import save_network


class BaseNetwork:
    def __init__(self):
        self.__graph = nx.Graph()

    def get_node_count(self) -> int:
        return self.__graph.number_of_nodes()

    def add_node(self, node) -> None:
        self.__graph.add_node(node.unique_id)

    def remove_node(self, node) -> None:
        self.__graph.remove_node(node.unique_id)

    def add_node_connection(self, node_1, node_2, relatedness: int) -> None:
        self.__graph.add_edge(node_1.unique_id, node_2.unique_id, weight=relatedness)

    def get_neighbors_ids(self, node) -> List[int]:
        try:
            return self.__graph.neighbors(node.unique_id)
        except NetworkXError:
            return []

    def get_node_weight(self, node_1, node_2) -> int:
        conn = self.__graph.get_edge_data(node_1.unique_id, node_2.unique_id)
        return 0 if conn is None else conn.get("weight", 0)

    def save(self, file_name: str) -> None:
        save_network(self, file_name)

    @property
    def graph(self) -> nx.Graph:
        return self.__graph

    def remove_duplicates(self, to_keep) -> None:
        to_delete_from_network = list(
            filter(lambda x: x not in to_keep, self.graph.nodes())
        )
        for to_delete in to_delete_from_network:
            self.__graph.remove_node(to_delete)
