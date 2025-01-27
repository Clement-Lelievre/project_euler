"""https://projecteuler.net/problem=49"""

from collections import defaultdict
from itertools import combinations


def sieve_of_eratosthenes(n: int) -> list[str]:
    # I borrowed this implem from the Internet
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    print(f"There are {len(primes)} primes <= {n}")
    return primes


def solve():
    primes = sieve_of_eratosthenes(9999)
    grouped_primes = defaultdict(list)  # stores permutations of primes
    for prime in primes:
        grouped_primes["".join(sorted(str(prime)))].append(prime)
    grouped_primes = {
        k: v for k, v in grouped_primes.items() if len(k) == 4 and len(v) >= 3
    }
    for nbs in grouped_primes.values():
        d = defaultdict(list)
        for combi in combinations(nbs, 2):
            d[max(combi) - min(combi)].append(combi)

        for k, v in d.items():
            if len(v) < 2:
                continue
            s = set(nb for tup in v for nb in tup)
            if len(s) == 3:
                print(k, v)


if __name__ == "__main__":
    solve()
