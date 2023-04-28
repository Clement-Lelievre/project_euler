"""https://projecteuler.net/problem=107
Using 'network.txt', a 6K text file containing a network
with forty vertices, and given in matrix form, find the maximum saving which can be achieved by
removing redundant edges whilst ensuring that the network remains connected.
"""
import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

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
        # check if this is a file path
        if os.path.isfile(matrix):
            with open(matrix, "r") as f:
                self.matrix = [
                    row.strip().split(",") for row in f.readlines() if row.strip()
                ]
        else:
            self.matrix = [
                row.strip().split(",") for row in matrix.splitlines() if row.strip()
            ]
        self.matrix = [
            [int(elem) if elem.isnumeric() else None for elem in row]
            for row in self.matrix
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
        self.graph = {i: {} for i in range(self.nb_vertices)}
        logging.info(
            f"Initial total weight: {self.total_weight_initial}, initial number of edges: {self.nb_edges_initial}, number of vertices: {self.nb_vertices}"
        )

    def _build_graph(self) -> None:
        logging.info("Building graph...")
        for i in range(self.nb_vertices):
            for j in range(self.nb_vertices):
                if i == j or self.matrix[i][j] is None:
                    continue
                self.graph[i][j] = self.matrix[i][j]
        assert len(self.graph) == self.nb_vertices
        assert sum(map(len, self.graph.values())) // 2 == self.nb_edges_initial
        logging.info("Graph built.")

    def make_minimal_graph(self) -> int:
        """Prunes the graph while retaining all initial connections

        Returns:
            int: the maximum weight saving possible
        """
        self._build_graph()
        max_saving = ...
        logging.info(f"Maximum saving: {max_saving}")
        return max_saving


if __name__ == "__main__":
    NO_test = NetworkOptimizer(TEST_MATRIX)
    assert NO_test.make_minimal_graph() == 150
    NO = NetworkOptimizer("minimal_network.txt")
    NO.make_minimal_graph()
