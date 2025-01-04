"""https://projecteuler.net/problem=125"""


def is_palindrome(nb: int) -> bool:
    return str(nb) == str(nb)[::-1]


def solve(n: int) -> int:
    squares = []
    k = 1
    while k**2 + (k + 1) ** 2 < n:
        squares.append(k**2)
        k += 1
    valid_nbs = set()
    print(f"{len(squares)} squares")
    for seq_len in range(2, len(squares) + 1):
        for start in range(len(squares) - seq_len + 1):
            sq_sum = sum(squares[start : start + seq_len])
            if sq_sum >= n:
                break
            if is_palindrome(sq_sum):
                valid_nbs.add(
                    sq_sum
                )  # we want the sum of the UNIQUE numbers. Summing them all here instead would include duplicated numbers and thus be wrong.
                # the example provided (4164 with n=1000) does not have this gotcha
    print(ans := sum(valid_nbs))
    return ans


if __name__ == "__main__":
    assert solve(1000) == 4164
    solve(10**8)
