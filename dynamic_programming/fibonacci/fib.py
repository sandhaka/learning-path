def fib(n, memo=None):
    if memo is None:
        memo = {}
    elif n in memo.keys():
        return memo[n]
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    memo[n] = fib(n - 2, memo) + fib(n - 1, memo)
    return memo[n]


print(fib(0))
print(fib(1))
print(fib(2))
print(fib(6))
print(fib(8))
print(fib(10))
print(fib(50))
