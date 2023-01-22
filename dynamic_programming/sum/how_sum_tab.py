def how_sum(target, array):
    table = [None for _ in range(target + 1)]
    table[0] = []
    for i in range(target + 1):
        for n in [n for n in array if i + n <= target and table[i] is not None]:
            table[i + n] = table[i] + [n]
    return table[target]


tests = [
    (8, [2, 3, 5]),
    (8, [1, 4, 5]),
    (100, [1, 2, 5, 25]),
    (7, [2, 3]),
    (7, [5, 3, 4, 7]),
    (7, [2, 4]),
    (300, [7, 14])
]
for test in tests:
    how = how_sum(test[0], test[1])
    print(f'{test[0]}: {how}')
