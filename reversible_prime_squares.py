"""https://projecteuler.net/problem=808

Find the sum of the first 50 reversible prime squares. """
from typing import Generator


def prime_number_generator() -> Generator[int, None, None]:
    """Generates squares of prime numbers that are not palindromes."""
    primes = [2]
    yield 2
    n = 3
    while True:
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
            yield n
        n += 2


def squared_primes() -> Generator[int, None, None]:
    for prime in prime_number_generator():
        square_prime_str = str(prime**2)
        if square_prime_str != square_prime_str[::-1]:
            yield prime**2


def solve() -> int:
    first_fifty_rps: set[
        int
    ] = set()  # wil get filled 2 by 2 whenever I find a new pair
    candidate_rps: set[
        str
    ] = set()  # an ordered data structure would be better than a set
    all_rps = squared_primes()

    while len(first_fifty_rps) < 50:
        current: int = next(all_rps)
        # is it worth storing it in the candidates list?
        reversed_current = str(current)[::-1]
        if reversed_current in candidate_rps:
            first_fifty_rps.add(current)
            first_fifty_rps.add(int(reversed_current))
            candidate_rps.remove(reversed_current)
            print(len(first_fifty_rps))
        elif current < int(reversed_current):
            candidate_rps.add(str(current))
    ans = sum(first_fifty_rps)
    print(ans, first_fifty_rps)
    return ans


if __name__ == "__main__":
    solve()
