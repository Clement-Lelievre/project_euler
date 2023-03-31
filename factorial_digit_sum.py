def factorial(n):
    return 1 if n == 1 else factorial(n - 1) * n


print(sum(map(int, list(str(factorial(100))))))
