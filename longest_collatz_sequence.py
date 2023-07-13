"""https://projecteuler.net/problem=14"""
import time


def chain_length_naive(n: int) -> int:
    counter = 1
    while n != 1:
        n = n / 2 if n % 2 == 0 else 3 * n + 1
        counter += 1
    return counter


def solve_naive() -> None:
    starttime = time.time()
    print(
        f"{max(range(2, 1_000_001), key=chain_length_naive)} in {time.time() - starttime} seconds."
    )


def solve_smarter() -> None:
    starttime = time.time()
    seq_lengths = {1: 1}
    for n in range(2, 1_000_001):
        counter = 0
        n_original = n
        while True:
            if n in seq_lengths:
                seq_lengths[n_original] = seq_lengths[n] + counter
                break
            n = n / 2 if n % 2 == 0 else 3 * n + 1
            counter += 1

    print(
        f"{max(seq_lengths, key=seq_lengths.get)} in {time.time() - starttime} seconds."
    )


if __name__ == "__main__":
    solve_naive()
    solve_smarter()
    
# there were more optimizations to find, see the PDF document for this problem
