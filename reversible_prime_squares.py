"""https://projecteuler.net/problem=808

Find the sum of the first 50 reversible prime squares. """
from typing import Generator
import time

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/


def prime_number_generator() -> Generator[int, None, None]:
    """Generate an infinite sequence of prime numbers."""
    D = {}
    # The running integer that's checked for primeness
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def squared_primes() -> Generator[int, None, None]:
    """Generates an infinite sequence of squared primes that are not palindromes"""
    for prime in prime_number_generator():
        square_prime_str = str(prime**2)
        if square_prime_str != square_prime_str[::-1]:
            yield prime**2


def solve() -> None:
    starttime = time.time()
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
        if not reversed_current.endswith(
            ("1", "9")
        ):  # an optimization idea I found in the thread after a more naïve solve
            continue
        if reversed_current in candidate_rps:
            first_fifty_rps.add(current)
            first_fifty_rps.add(int(reversed_current))
            candidate_rps.remove(reversed_current)
        elif current < int(reversed_current):
            candidate_rps.add(str(current))
    answer = sum(first_fifty_rps)
    print(f"{answer=}; Time: {round(time.time() - starttime, 1)} seconds")


if __name__ == "__main__":
    solve()
