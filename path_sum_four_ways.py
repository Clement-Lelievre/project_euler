"""https://projecteuler.net/problem=81"""
from collections import deque

TEST_MATRIX = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]


def solve(matrix: list[list[int]]):
    queue = deque([(matrix[0][0], (0, 0))])
    nb_rows, nb_cols = len(matrix), len(matrix[0])
    assert nb_rows == nb_cols
    best = float("inf")
    dest = (nb_rows - 1, nb_cols - 1)
    seen = {}
    while queue:
        score, (x, y) = queue.popleft()
        if seen.get((x, y), float('inf')) < score:
            continue
        seen[(x, y)] = score
        if (x, y) == dest:
            best = min(best, score)
            continue
        for neigh in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
            if 0 <= neigh[0] < nb_rows and 0 <= neigh[1] < nb_cols:
                queue.append((score + matrix[neigh[0]][neigh[1]], neigh))
    print(best)
    return best


if __name__ == "__main__":
    assert solve(TEST_MATRIX) == 2297
    solve(
        [
            [int(nb) for nb in row.split(",")]
            for row in open("p081_matrix.txt").readlines()
            if row.strip()
        ]
    )
    