"""https://projecteuler.net/problem=81"""
import logging
from collections import deque
from time import time

logging.basicConfig(level=logging.INFO)
TEST_MATRIX = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]


def solve(matrix: list[list[int]]) -> int:
    """Uses a mapping to store the best score for each cell, prunes the tree and uses a queue to
    traverse the graph

    Args:
        matrix (list[list[int]]): the matrix as a list of lists of integers

    Returns:
        int: the minimal path sum
    """
    starttime = time()
    best = float("inf")
    nb_rows, nb_cols = len(matrix), len(matrix[0])
    assert nb_rows == nb_cols
    seen: dict[tuple[int, int], int] = {}

    def solve_from(start_row: int) -> None:
        nonlocal best, seen
        queue = deque([(matrix[start_row][0], (start_row, 0))])
        while queue:
            score, (x, y) = queue.popleft()
            if seen.get((x, y), float("inf")) < score:
                continue
            seen[(x, y)] = score
            if y == nb_cols - 1:
                best = min(best, score)
                continue
            for neigh in ((x + 1, y), (x, y + 1), (x - 1, y)):
                if 0 <= neigh[0] < nb_rows and 0 <= neigh[1] < nb_cols:
                    queue.append((score + matrix[neigh[0]][neigh[1]], neigh))

    for start_row in range(len(matrix)):
        solve_from(start_row)
    logging.info(f"Answer: {best}, Time: {round(time() - starttime, 2)}s")
    return best


if __name__ == "__main__":
    assert solve(TEST_MATRIX) == 994
    with open("p081_matrix.txt", encoding="utf-8") as f:
        solve([[int(nb) for nb in row.split(",")] for row in f if row.strip()])
    # to do: code a function to read the matrix from the file
