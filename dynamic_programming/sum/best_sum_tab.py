def best_sum(target, array):
    table = [None for _ in range(target + 1)]
    table[0] = []
    for i in range(target + 1):
        if table[i] is not None:
            for n in [n for n in array if i + n <= target]:
                new_value = table[i] + [n]
                if table[i + n] is None or len(new_value) < len(table[i + n]):
                    table[i + n] = new_value
    return table[target]
# O(nm^2) time
# O(m) space


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
    best = best_sum(test[0], test[1])
    print(f'{test[0]}: {best}')
