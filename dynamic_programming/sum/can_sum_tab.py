def can_sum(target, array):
    table = [False for _ in range(target + 1)]
    table[0] = True
    for i in range(target + 1):
        for n in [n for n in array if i + n <= target and table[i] is True]:
            table[i + n] = table[i]
    return table[target]


tests = [
    (7, [2, 3]),            # True
    (7, [5, 3, 4, 7]),      # True
    (7, [2, 4]),            # False
    (300, [7, 14]),         # False
    (8, [2, 3, 5]),         # True
    (8, [1, 4, 5]),         # True
    (100, [1, 2, 5, 25])    # True
]
for test in tests:
    can = can_sum(test[0], test[1])
    print(f'{test}: {can}')
