"""https://projecteuler.net/problem=46"""


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


def solve() -> None:
    primes = sieve_of_eratosthenes(10**6)
    squares = {nb**2 for nb in range(1, 10**6)}
    nb = 9
    while True:
        if nb in primes:
            nb += 2
            continue
        for prime in primes:
            if (nb - prime) / 2 in squares:
                break
            if prime >= nb:
                print(f"{nb} cannot be expressed as the sum of a prime and a square")
                return
        nb += 2


if __name__ == "__main__":
    solve()
