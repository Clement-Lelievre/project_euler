"""https://projecteuler.net/problem=24"""

from itertools import permutations

perms = permutations(range(10), 10)

for _ in range(1_000_000):
    perm = next(perms)

print("".join(map(str, perm)))
