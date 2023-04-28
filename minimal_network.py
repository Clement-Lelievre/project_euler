"""https://projecteuler.net/problem=107
Using 'network.txt', a 6K text file containing a network
with forty vertices, and given in matrix form, find the maximum saving which can be achieved by
removing redundant edges whilst ensuring that the network remains connected.
"""
import logging
import os
from collections import deque
from copy import deepcopy
from itertools import combinations

TEST_MATRIX = """
-,16,12,21,-,-,-
16,-,-,17,20,-,-
12,-,-,28,-,31,-
21,17,28,-,18,19,23
-,20,-,18,-,-,11
-,-,31,19,-,-,27
-,-,-,23,11,27,-
"""


class NetworkOptimizer:
    """Given the weights, vertices and edges of a graph in matrix form,
    'prunes' the graph and ouputs the graph that keeps all vertex connections
    while maximizing the saving on the weights"""

    def __init__(self, matrix: str) -> None:
        # check if `matrix` is a filepath
        if os.path.isfile(matrix):
            with open(matrix, "r") as f:
                self.data = [
                    row.strip().split(",") for row in f.readlines() if row.strip()
                ]
        else:
            self.data = [
                row.strip().split(",") for row in matrix.splitlines() if row.strip()
            ]
        self.matrix: list[int | None] = [
            [int(elem) if elem.isnumeric() else None for elem in row]
            for row in self.data
        ]
        # make sure the matrix is squared
        assert len(self.matrix[0]) == len(self.matrix)
        # compute initial total weight
        self.total_weight_initial = (
            sum(sum(filter(None, row)) for row in self.matrix) // 2
        )
        self.nb_edges_initial = (
            sum(len(list((filter(None, row)))) for row in self.matrix) // 2
        )
        self.nb_vertices = len(self.matrix)
        self.graph: dict[int, dict[int, int]] = {i: {} for i in range(self.nb_vertices)}
        logging.info(
            f"Initial total weight: {self.total_weight_initial}, initial number of edges: {self.nb_edges_initial}, number of vertices: {self.nb_vertices}"
        )

    def _build_graph(self) -> None:
        logging.info("Building graph...")
        self.edges_initial = set()
        for i, j in combinations(range(self.nb_vertices), 2):
            if self.matrix[i][j] is None:
                continue
            self.graph[i][j] = (dist := self.matrix[i][j])
            self.graph[j][i] = dist
            self.edges_initial.add((dist, frozenset((i, j))))
        assert len(self.graph) == self.nb_vertices
        assert sum(map(len, self.graph.values())) // 2 == self.nb_edges_initial
        self.edges_initial = sorted(self.edges_initial, reverse=True)
        logging.info("Graph built.")
        logging.debug(f"Initial edges: {self.edges_initial}")
        logging.debug(f"# of initial edges: {len(self.edges_initial)}")

    @staticmethod
    def _path_exists_between(
        edge1: int, edge2: int, graph: dict[int, dict[int, int]]
    ) -> bool:
        queue = deque([edge1])
        seen = set()
        while queue:
            current_edge = queue.pop()
            if current_edge in seen:
                continue
            if current_edge == edge2:
                return True
            seen.add(current_edge)
            queue.extend([neigh for neigh in graph[current_edge]])
        return False

    def make_minimal_graph(self) -> int:
        """Prunes the graph while retaining all initial connections
        Starts from the heaviest edges and drops them if the graph remains connected

        Returns:
            int: the maximum weight saving possible
        """
        self._build_graph()
        max_saving = 0
        temp_graph = deepcopy(self.graph)
        for dist, vertices in self.edges_initial:
            edge1, edge2 = vertices
            # drop the edge and check if the graph is still connected
            del temp_graph[edge1][edge2]
            del temp_graph[edge2][edge1]
            if NetworkOptimizer._path_exists_between(edge1, edge2, temp_graph):
                max_saving += dist
            else:  # re-add the edge
                temp_graph[edge1][edge2] = temp_graph[edge2][edge1] = dist
        logging.debug(f"Final graph: {temp_graph}")
        logging.info(f"Maximum saving: {max_saving}")
        return max_saving


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    NO_test = NetworkOptimizer(TEST_MATRIX)
    assert NO_test.make_minimal_graph() == 150

    NO = NetworkOptimizer("minimal_network.txt")
    NO.make_minimal_graph()
