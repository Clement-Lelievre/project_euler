"""https://projecteuler.net/problem=31
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""


def count_coin_combinations(total: int)->int:
    """Uses dynamic programming

    Args:
        total (int): total amount in pence

    Returns:
        int: the number of possible unique combinations
    """
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = [0] * (total + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] += dp[i - coin]

    return dp[total]


if __name__ == "__main__":
    total = 200  # Total amount in pence (£2 = 200p)
    combinations = count_coin_combinations(total)
    print(
        f"The number of different ways to make £2 using any number of coins is: {combinations}"
    )
