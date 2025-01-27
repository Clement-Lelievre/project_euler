"""https://projecteuler.net/problem=50"""


def sieve_of_eratosthenes(n: int) -> list[int]:
    # I borrowed this implem from the Internet
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]

    return primes


def solve(n: int):
    primes = sieve_of_eratosthenes(n)
    primes_for_lookup = set(
        primes
    )  # set for O(1) lookup time. This REALLY makes a huge diff vs looking into a list here
    best = 0
    for start in range(len(primes) - 1):
        s = 0
        i = start
        ans = 0
        while s < n:
            s += primes[i]
            i += 1
            if s in primes_for_lookup:
                ans = i - start
                nb = s
        if ans > best:
            best = ans
            print(f"best so far: {nb} (sum of {best} consecutive primes)")

    return best


if __name__ == "__main__":
    assert solve(100) == 6
    assert solve(1000) == 21
    solve(10**6)
