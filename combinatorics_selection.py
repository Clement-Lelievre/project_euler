def factorial(n: int):
    return 1 if n in {0, 1} else n * factorial(n - 1)


factorial_cache = dict(enumerate(map(factorial, range(101))))


def bin(n, k):
    return factorial_cache[n] // (factorial_cache[k] * factorial_cache[n - k])


def solve():
    ans = 0
    for n in range(23, 101):
        for k in range(n // 2 + 1):
            if bin(n, k) > 1_000_000:
                ans += 1 if (n % 2 == 0) and (k == n // 2) else 2
    print(ans)
    return ans


if __name__ == "__main__":
    solve()
