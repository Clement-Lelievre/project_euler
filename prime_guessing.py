"""https://projecteuler.net/problem=869"""

import time


def sieve_of_eratosthenes(n: int) -> list[str]:
    # I borrowed this implem from the Internet
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [bin(p)[2:] for p in range(2, n + 1) if is_prime[p]]
    print(f"There are {len(primes)} primes <= {n}")
    return primes


def solve(n: int) -> float:
    """Will play all games recursively and finally average the number of points over the number of games

    Args:
        n (int): N as described in the text

    Returns:
        float: the expected number of points
    """
    start_time = time.time()
    total_points = 0
    print("Computing the primes...")
    primes = sieve_of_eratosthenes(n)

    def play(nb: str, points: int, primes: list[str]) -> None:
        """Recursively play, starting from the binary number `nb` and list of primes `primes`

        Args:
            nb (str): _description_
            points (int): _description_
            primes (list[str]): _description_
        """
        nonlocal total_points
        total_points += points
        if not primes:  # base case, stop recursing
            return
        ind = len(nb) + 1
        ones = [
            nb for nb in primes if len(nb) >= ind and nb[-ind] == "1"
        ]  # discard numbers of len ind, as those games are over
        zeros = [nb for nb in primes if len(nb) >= ind and nb[-ind] == "0"]
        guess_one = len(ones) > len(zeros)  # what if the lens are equal?
        play("1" + nb, len(ones) if guess_one else 0, ones)
        play("0" + nb, 0 if guess_one else len(zeros), zeros)

    print("Start recursing...")
    play("", 0, primes)
    avg = round(total_points / len(primes), 8)
    print(f"{avg=} in {round(time.time()-start_time,2)} sec")
    return avg


if __name__ == "__main__":
    assert (s := solve(10)) == 2.0, s
    assert (s := solve(30)) == 2.9, s
    solve(10**8)
