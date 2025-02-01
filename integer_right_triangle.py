"""https://projecteuler.net/problem=39"""

from math import sqrt
from tqdm import tqdm


def nb_solutions(perimeter: int) -> int:
    nb_sol = 0
    seen = set()
    for a in range(1, perimeter - 1):
        for b in range(1, perimeter - a):
            if (
                (hypoth := sqrt(a**2 + b**2)) == int(hypoth)
                and tuple(sorted([a, b, hypoth])) not in seen
                and a + b + hypoth == perimeter
            ):
                nb_sol += 1
                seen.add(tuple(sorted([a, b, hypoth])))
    return nb_sol


def solve() -> None:
    nb_sol = {perim: nb_solutions(perim) for perim in tqdm(range(4, 1001, 2))} # only even values of perimeter need checking
    print(max(nb_sol, key=nb_sol.get))


if __name__ == "__main__":
    assert nb_solutions(120) == 3
    solve()
