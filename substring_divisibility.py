"""https://projecteuler.net/problem=43"""

from typing import Generator
from itertools import permutations

# there are 10! ways to write the digit, that's ~ 3.628 million. I suspect this can be bruteforced


def pandigital_nbs() -> Generator[str, None, None]:
    for perm in permutations(map(str, range(10)), 10):
        yield "".join(perm)


def meets_divisibility_criteria(nb: str) -> bool:
    return all(
        int(nb[slice_]) % divisor == 0
        for (slice_, divisor) in zip(
            [slice(start, start + 3) for start in range(1, 9)],
            [2, 3, 5, 7, 11, 13, 17],
        )
    )


def solve() -> None:
    ans = sum(int(nb) for nb in pandigital_nbs() if meets_divisibility_criteria(nb))
    print(ans)


if __name__ == "__main__":
    test_nb = "1406357289"
    assert sorted(test_nb) == list(map(str, range(10)))
    assert meets_divisibility_criteria(test_nb)
    solve()
