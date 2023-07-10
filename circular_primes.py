"""https://projecteuler.net/problem=35"""

# I'll use the fact that a prime number ends with either 1, 3, 7 or 9 to
# optimize the algo

from typing import Generator


def prime_number_generator(target) -> Generator[int, None, None]:
    """Generate a sequence of prime numbers up to `target`"""
    D = {}
    # The running integer that's checked for primeness
    q = 2
    while q <= target:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def nb_circular_under(target: int) -> int:
    primes = set(prime_number_generator(target))
    nb_circulars = 0
    checked = set()
    for prime in primes:
        if prime in checked:
            continue
        #  generate rotations of the digits
        prime_str = str(prime)
        rotations = {int(prime_str[i:] + prime_str[:i]) for i in range(len(prime_str))}
        if rotations.issubset(primes):
            nb_circulars += len(rotations)
            print(rotations)
        checked |= rotations

    print(f"{nb_circulars=}")
    return nb_circulars


if __name__ == "__main__":
    assert nb_circular_under(100) == 13
    nb_circular_under(1_000_000)
