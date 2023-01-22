from itertools import repeat


def fib(n):
    table = list(repeat(0, n + 2))
    table[1] = 1
    for i in range(0, n):
        table[i + 1] += table[i]
        table[i + 2] += table[i]
    return table[n]


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(6))
print(fib(8))
print(fib(10))
print(fib(50))
