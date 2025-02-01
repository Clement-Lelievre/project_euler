"""https://projecteuler.net/problem=47"""


def prime_factorization(n: int) -> list[int]:
    """Returns:
    list[int]: list of prime factors
    """
    factors = []
    d = 2
    while n:
        exp = 0
        while n % d == 0:
            exp += 1
            n //= d
        if exp:
            factors.append(d)
        d += 1
        if d**2 > n:
            if n > 1:
                factors.append(n)
            break
    return factors


def solve(streak_target: int) -> int:
    i = 1
    streak = 0
    while True:
        prime_factors = prime_factorization(i)
        if len(prime_factors) == streak_target:
            streak += 1
            if streak == streak_target:
                print(i - streak_target + 1)
                return i - streak_target + 1
        else:
            streak = 0
        i += 1


if __name__ == "__main__":
    assert (s := prime_factorization(644)) == [2, 7, 23], s
    assert solve(streak_target=2) == 14
    assert solve(streak_target=3) == 644
    solve(streak_target=4)
