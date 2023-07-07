"""https://projecteuler.net/problem=57"""


def expand(n_times: int) -> dict[int, tuple[int, int]]:
    """Comptes and caches the first n_times expansions of the square root of 2.

    Args:
        n_times (int): Number of expansions to compute.

    Returns:
        dict[int, tuple[int, int]]: Dictionary of the form {i: (numerator, denominator)}.
    """
    assert isinstance(n_times, int) and n_times
    num, denom = 2, 1
    cache_dict = {}
    for i in range(1, n_times + 1):
        num, denom = denom, num  # invert fraction
        num, denom = 2 * denom + num, denom  # add 2 to fraction
        cache_dict[i] = (num + denom, num)  # cache fraction (expansion number i)
    return cache_dict


def solve() -> None:
    print(sum(len(str(num)) > len(str(denom)) for num, denom in expand(1_000).values()))


if __name__ == "__main__":
    solve()
