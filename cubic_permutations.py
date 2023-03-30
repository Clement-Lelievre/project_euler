"""The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
https://projecteuler.net/problem=62"""
from collections import defaultdict


def solve(n_perm: int) -> int:
    cubes = defaultdict(list)
    n = 0
    while max(map(len, cubes.values()), default=0) < n_perm:
        cubes["".join(sorted(str(n**3)))].append(n)
        n += 1
    answer = min(max(cubes.values(), key=len)) ** 3
    print(answer)
    return answer


if __name__ == "__main__":
    assert solve(n_perm=3) == 41063625
    solve(n_perm=5)
